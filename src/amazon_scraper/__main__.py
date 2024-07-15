"""
    Main module for amazon_scraper.
"""

import logging

import click

from amazon_scraper.collector import AmazonDataCollector


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option(
    "--url",
    help="The url of the page for which to return Amazon product data for.",
    required=True,
)
def scrape_amazon(url: str) -> None:
    collector = AmazonDataCollector()
    collector.collect_amazon_product_data(url)


if __name__ == "__main__":
    scrape_amazon()
