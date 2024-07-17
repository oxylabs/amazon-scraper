"""
    Module for scraping Amazon product pages.
"""

import logging
import time

from enum import Enum
from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from seleniumwire import webdriver
from seleniumwire.request import Request
from webdriver_manager.chrome import ChromeDriverManager

from amazon_scraper.models import Product


logging.getLogger("WDM").setLevel(logging.ERROR)
logging.getLogger("seleniumwire").setLevel(logging.ERROR)


class DriverInitializationError(BaseException):
    message = "Unable to initialize Chrome webdriver for scraping."


class DriverGetProductsError(BaseException):
    message = "Unable to get Amazon product data with Chrome webdriver."


class MissingProductDataError(BaseException):
    message = "Missing required data for product."


class ProductXPath(str, Enum):
    PRODUCTS = "//div[@data-component-type='s-search-result']"
    TITLE = ".//h2/a/span"
    URL = ".//h2/a"
    PRICE_WHOLE = ".//span[@class='a-price']//span[@class='a-price-whole']"
    PRICE_FRACTIONAL = ".//span[@class='a-price']//span[@class='a-price-fraction']"
    IMAGE_URL = ".//img"


class AmazonScraper:
    """Class for scraping Amazon"""

    def __init__(self, logger: logging.Logger | None = None) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "keep-alive",
            "Referer": "https://www.amazon.com/",
            "Host": "www.amazon.com",
            "TE": "Trailers",
        }

    def _add_headers_to_request(self, request: Request) -> None:
        """Intercepts selenium requests to add headers"""
        for key, value in self._headers.items():
            request.headers[key] = value

    def _init_chrome_driver(self) -> webdriver.Chrome:
        """Initializes Chrome webdriver"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.request_interceptor = self._add_headers_to_request
        return driver

    def _parse_price_for_product(self, product: WebElement) -> str | None:
        """Parses price for a product element"""
        try:
            price_whole_element = product.find_element(
                By.XPATH, ProductXPath.PRICE_WHOLE
            )
            price_whole = price_whole_element.text if price_whole_element else None

            price_fractional_element = product.find_element(
                By.XPATH, ProductXPath.PRICE_FRACTIONAL
            )
            price_fractional = (
                price_fractional_element.text if price_fractional_element else None
            )

            return (
                price_whole + "." + price_fractional
                if all((price_whole, price_fractional))
                else None
            )
        except NoSuchElementException:
            return None

    def _parse_product_data(self, product: WebElement) -> Product:
        """Parses product data from the given product element"""
        title_element = product.find_element(By.XPATH, ProductXPath.TITLE)
        title = title_element.text if title_element else None

        url_element = product.find_element(By.XPATH, ProductXPath.URL)
        url = url_element.get_attribute("href") if url_element else None

        asin_code = product.get_attribute("data-asin")

        image_element = product.find_element(By.XPATH, ProductXPath.IMAGE_URL)
        image_url = image_element.get_attribute("src") if image_element else None

        price = self._parse_price_for_product(product)
        if not price:
            self._logger.warning(
                f"Price not found for product {title}. Likely out of stock."
            )

        if not all((title, url, asin_code, image_url)):
            raise MissingProductDataError

        return Product(
            title=title,
            url=url,
            asin_code=asin_code,
            price=price,
            image_url=image_url,
        )

    def _get_products_from_page(
        self, url: str, driver: webdriver.Chrome
    ) -> List[Product]:
        """Scrapes the Amazon page for products"""
        driver.get(url)
        time.sleep(3)
        product_elements = driver.find_elements(By.XPATH, ProductXPath.PRODUCTS)
        parsed_products = []
        for product in product_elements:
            try:
                parsed_product = self._parse_product_data(product)
            except MissingProductDataError:
                self._logger.error(
                    "Couldn't get all required data for product. Skipping.."
                )
                continue
            except Exception:
                self._logger.error(
                    "Uexpected error when parsing data for product. Skipping.."
                )
                continue
            else:
                parsed_products.append(parsed_product)

        return parsed_products

    def scrape_amazon_page(self, url: str) -> List[Product]:
        """
        Retrieves a list of products from Amazon for a given Amazon page URL.

        Returns:
            List[Product]: A list of Product objects.
        Raises:
            DriverInitializationError: If the Chrome webdriver cannot be initialized.
            DriverGetProductsError: If the Amazon product data cannot be scraped from the Amazon site.
        """
        self._logger.info("Scraping Amazon product data..")

        try:
            driver = self._init_chrome_driver()
        except Exception as e:
            raise DriverInitializationError from e

        try:
            return self._get_products_from_page(url, driver)
        except Exception as e:
            raise DriverGetProductsError from e
        finally:
            driver.close()
