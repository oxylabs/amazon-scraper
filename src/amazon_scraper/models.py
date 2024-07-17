"""
    Pydantic models for Amazon scraper.
"""

from pydantic import BaseModel


class Product(BaseModel):
    title: str
    url: str
    asin_code: str
    image_url: str
    price: str | None
