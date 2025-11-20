from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from mercapi.models.base import ResponseModel
from mercapi.models.common import ItemCategorySummary
from mercapi.models.item.data import (
    ItemCondition,
    ShippingFromArea,
    ShippingMethod,
    ShippingDuration,
    ShippingClass,
    ShippingPayer,
    Color,
    Seller,
    Comment,
    Requester,
    ItemSize,
    ItemBrand,
    ParentCategoryNtier,
    ItemCategoryNtiers,
    ItemAttribute,
    Defpay,
    PricePromotionAreaDetails,
    EstimateInfo,
)


# actually a mapping for 'data' object in item response
#
# consider nesting all the properties in data submodel
# if the original response gets more verbose
@dataclass
class Item(ResponseModel):
    id_: str
    seller: Seller
    status: str
    name: str
    price: int
    description: str
    photos: List[str]
    photo_paths: List[str]
    thumbnails: List[str]
    item_category: ItemCategorySummary
    item_condition: ItemCondition
    colors: List[Color]
    shipping_payer: ShippingPayer
    shipping_method: ShippingMethod
    shipping_from_area: ShippingFromArea
    shipping_duration: ShippingDuration
    shipping_class: ShippingClass
    num_likes: int
    num_comments: int
    comments: List[Comment]
    updated: datetime
    created: datetime
    pager_id: int
    liked: bool
    checksum: str
    is_dynamic_shipping_fee: bool
    application_attributes: dict
    is_shop_item: str
    is_anonymous_shipping: bool
    is_web_visible: bool
    is_offerable: bool
    is_organizational_user: bool
    organizational_user_status: str
    is_stock_item: bool
    is_cancelable: bool
    shipped_by_worker: bool
    has_additional_service: bool
    has_like_list: bool
    is_offerable_v2: bool
    # New fields from updated API
    requester: Optional[Requester] = None
    item_category_ntiers: Optional[ItemCategoryNtiers] = None
    parent_categories_ntiers: Optional[List[ParentCategoryNtier]] = None
    item_size: Optional[ItemSize] = None
    item_brand: Optional[ItemBrand] = None
    registered_prices_count: Optional[int] = None
    promotion_explanation_message: Optional[str] = None
    hash_tags: Optional[List[str]] = None
    additional_services: Optional[List[dict]] = None
    item_attributes: Optional[List[ItemAttribute]] = None
    is_dismissed: Optional[bool] = None
    photo_descriptions: Optional[List[str]] = None
    has_active_mercard: Optional[str] = None
    defpay: Optional[Defpay] = None
    meta_title: Optional[str] = None
    meta_subtitle: Optional[str] = None
    price_promotion_area_details: Optional[PricePromotionAreaDetails] = None
    estimate_info: Optional[EstimateInfo] = None
