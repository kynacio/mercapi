from dataclasses import dataclass
from typing import List, Optional

from mercapi.models.base import ResponseModel


@dataclass
class ShopStats(ResponseModel):
    """Statistics for a Mercari shop"""
    shop_id: str
    score: int
    review_count: str


@dataclass
class ShopItem(ResponseModel):
    """A product listing from a shop (lightweight version)"""
    product_id: str
    display_name: str
    product_tags: List[str]
    thumbnail: str
    price: str


@dataclass
class Shop(ResponseModel):
    """Mercari shop information"""
    name: str
    display_name: str
    thumbnail: str
    shop_stats: ShopStats
    allow_direct_message: bool
    shop_items: List[ShopItem]
    is_inbound_xb: bool
    badges: List[str]
    has_approved_brand_screening: bool


@dataclass
class ShopCategory(ResponseModel):
    """Category information for shop products"""
    category_id: str
    display_name: str
    parent_id: str
    root_id: str
    has_child: bool


@dataclass
class ShopBrand(ResponseModel):
    """Brand information for shop products"""
    brand_id: str
    display_name: str


@dataclass
class ShopCondition(ResponseModel):
    """Condition information for shop products"""
    display_name: str


@dataclass
class ShopShippingMethod(ResponseModel):
    """Shipping method for shop products"""
    shipping_method_id: str
    display_name: str
    is_anonymous: bool


@dataclass
class ShopShippingPayer(ResponseModel):
    """Shipping payer information for shop products"""
    shipping_payer_id: str
    display_name: str
    code: str


@dataclass
class ShopShippingDuration(ResponseModel):
    """Shipping duration for shop products"""
    shipping_duration_id: str
    display_name: str
    min_days: int
    max_days: int


@dataclass
class ShopShippingFromArea(ResponseModel):
    """Shipping origin area for shop products"""
    shipping_area_code: str
    display_name: str


@dataclass
class PromotionAction(ResponseModel):
    """Action details for a promotion"""
    action: str
    discount_type: str
    discount_value: str
    return_type: str
    coupon_type: str
    max_return_amount: str
    return_text: str
    discount_amount: str
    discounted_price: str


@dataclass
class Promotion(ResponseModel):
    """Promotion information for shop products"""
    display_name: str
    action: PromotionAction


@dataclass
class Variant(ResponseModel):
    """Product variant information"""
    variant_id: str
    display_name: str
    quantity: str
    size: str
    attributes: List[str]


@dataclass
class RealCardReward(ResponseModel):
    """Mercard (Mercari credit card) reward information"""
    reward_amount: str
    has_active_card: bool
    has_mvno: bool
    reward_rate: float
    lp_uri: str
    estimate_reward_text: str
    disclaimer_text: str
    show_component: bool


@dataclass
class MercardCampaign(ResponseModel):
    """Mercard campaign information"""
    id_: str
    title: str
    uri: str
    text: str
    discount_amount: int
    max_discount: int


@dataclass
class ProductDetail(ResponseModel):
    """Detailed information about a shop product"""
    shop: Shop
    photos: List[str]
    description: str
    categories: List[ShopCategory]
    brand: Optional[ShopBrand]
    condition: ShopCondition
    shipping_method: ShopShippingMethod
    shipping_payer: ShopShippingPayer
    shipping_duration: ShopShippingDuration
    shipping_from_area: ShopShippingFromArea
    promotions: List[Promotion]
    product_stats: Optional[dict]
    time_sale_details: Optional[dict]
    variants: List[Variant]
    shipping_fee_config: Optional[dict]
    variation_grouping: Optional[dict]
    buyer_promotion: Optional[dict]
    follow_promotion: Optional[Promotion]
    last_purchased_date_time: Optional[str]
    real_card_reward: RealCardReward
    mercard_campaign: MercardCampaign
    seo_metadata: Optional[dict]
    product_pre_order: Optional[dict]
