from dataclasses import dataclass
from datetime import datetime
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from mercapi.models import Item, Profile
from mercapi.models.base import ResponseModel


@dataclass
class ItemBrand(ResponseModel):
    """Brand information for an item"""
    id_: str
    name: str
    sub_name: str


@dataclass
class ItemSize(ResponseModel):
    """Size information for an item"""
    id_: str
    name: str


@dataclass
class Photo(ResponseModel):
    """Photo information for an item"""
    uri: str


@dataclass
class Auction(ResponseModel):
    """Auction information for an item"""
    id_: str
    bid_deadline: str
    total_bid: str
    highest_bid: str


@dataclass
class Shop(ResponseModel):
    """Shop information for an item"""
    id_: str


@dataclass
class SearchResultItem(ResponseModel):
    id_: str
    name: str
    price: int
    seller_id: str
    status: str
    created: datetime
    updated: datetime
    thumbnails: List[str]
    item_type: str
    item_condition_id: int
    shipping_payer_id: int
    shipping_method_id: int
    category_id: int
    is_no_price: bool  # price==9999999 if True
    buyer_id: Optional[str] = None
    item_sizes: Optional[List[ItemSize]] = None
    item_brand: Optional[ItemBrand] = None
    item_promotions: Optional[List] = None
    shop_name: Optional[str] = None
    item_size: Optional[ItemSize] = None
    title: Optional[str] = None
    is_liked: Optional[bool] = None
    photos: Optional[List[Photo]] = None
    auction: Optional[Auction] = None
    shop: Optional[Shop] = None

    async def full_item(self) -> "Item":
        return await self._mercapi.item(self.id_)

    async def seller(self) -> "Profile":
        return await self._mercapi.profile(self.seller_id)

    """
    Actual price of the item, properly handling the case when the item has no price.
    """

    @property
    def real_price(self) -> Optional[int]:
        return None if self.is_no_price else self.price
