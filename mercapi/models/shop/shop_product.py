from dataclasses import dataclass
from datetime import datetime
from typing import List

from mercapi.models.base import ResponseModel
from mercapi.models.shop.data import ProductDetail


@dataclass
class ShopProduct(ResponseModel):
    """A complete Mercari Shop product listing

    This represents a product sold by an official Mercari Shop, which is different
    from regular user-to-user marketplace items. Shop products have additional
    features like promotions, variants, and official shop guarantees.
    """

    # Basic Information
    name: str  # Product ID (e.g., "2JHDxUxi3SsqAG5umbmWY2")
    display_name: str  # Human-readable product name
    product_tags: List[str]  # Product tags
    thumbnail: str  # Thumbnail image URL
    price: str  # Price as string (e.g., "11990")
    create_time: datetime  # When the product was created
    update_time: datetime  # When the product was last updated
    attributes: List[str]  # Additional attributes

    # Detailed Information
    product_detail: ProductDetail  # Full product details including shop info, photos, etc.

    @property
    def product_id(self) -> str:
        """Returns the product ID (same as name field)"""
        return self.name

    @property
    def price_int(self) -> int:
        """Returns the price as an integer"""
        return int(self.price)

    @property
    def shop_name(self) -> str:
        """Returns the shop's display name"""
        return self.product_detail.shop.display_name

    @property
    def shop_id(self) -> str:
        """Returns the shop's ID"""
        return self.product_detail.shop.name
