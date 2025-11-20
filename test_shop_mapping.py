#!/usr/bin/env python3
"""
Test script to verify ShopProduct mapping with actual JSON data
"""
from mercapi.mapping import map_to_class
from mercapi.models.shop import ShopProduct

# Sample JSON response from the user's curl command
sample_json = {
    "name": "2JHDxUxi3SsqAG5umbmWY2",
    "displayName": "ISAMU KATAYAMA BACKLASH (イサムカタヤマバックラッシュ) カシミヤ混 ウールニットスヌード ブラック 866-03",
    "productTags": [],
    "thumbnail": "https://assets.mercari-shops-static.com/-/small/plain/2JHDxUvs2PVAihFDtCgPnr.jpg@jpg",
    "price": "11990",
    "createTime": "2025-11-20T01:27:24Z",
    "updateTime": "2025-11-20T01:27:24Z",
    "attributes": [],
    "productDetail": {
        "shop": {
            "name": "aXQx7LKu3us59Yo7fQmwsk",
            "displayName": "BRINGメルカリ店",
            "thumbnail": "https://assets.mercari-shops-static.com/-/small/plain/Yu4PKJmtoEyju8ApCNQR2b.png@jpg",
            "shopStats": {
                "shopId": "aXQx7LKu3us59Yo7fQmwsk",
                "score": 5,
                "reviewCount": "22386"
            },
            "allowDirectMessage": True,
            "shopItems": [
                {
                    "productId": "2JHDy725DfebdAL69ctjdq",
                    "displayName": "GIVENCHY (ジバンシィ) ダメージ加工ロゴプリントフーデッドプルオーバースウェットパーカー ブラック BM70BS306C",
                    "productTags": [],
                    "thumbnail": "https://assets.mercari-shops-static.com/-/small/plain/2JHDy6xaoVezZ3YeWZh942.jpg@jpg",
                    "price": "28875"
                }
            ],
            "isInboundXb": False,
            "badges": [],
            "hasApprovedBrandScreening": False
        },
        "photos": [
            "https://assets.mercari-shops-static.com/-/large/plain/2JHDxUvs2PVAihFDtCgPnr.jpg@jpg",
            "https://assets.mercari-shops-static.com/-/large/plain/2JHDxUvmKhdZgarURffFSN.jpg@jpg"
        ],
        "description": "【ブランド】ISAMU KATAYAMA BACKLASH（イサムカタヤマバックラッシュ）",
        "categories": [
            {
                "categoryId": "413",
                "displayName": "Others",
                "parentId": "38",
                "rootId": "3088",
                "hasChild": False
            }
        ],
        "brand": {
            "brandId": "5808",
            "displayName": "ISAMUKATAYAMA BACKLASH"
        },
        "condition": {
            "displayName": "Scratches/marks"
        },
        "shippingMethod": {
            "shippingMethodId": "1",
            "displayName": "Unspecified",
            "isAnonymous": False
        },
        "shippingPayer": {
            "shippingPayerId": "1",
            "displayName": "Included in price (by seller)",
            "code": "SELLER"
        },
        "shippingDuration": {
            "shippingDurationId": "3",
            "displayName": "4 - 7 days",
            "minDays": 4,
            "maxDays": 7
        },
        "shippingFromArea": {
            "shippingAreaCode": "jp12",
            "displayName": "Chiba"
        },
        "promotions": [
            {
                "displayName": "Get a 10% discount coupon at Shop follow!",
                "action": {
                    "action": "Shop follow",
                    "discountType": "RATE",
                    "discountValue": "10",
                    "returnType": "RETURN_TYPE_DISCOUNT",
                    "couponType": "COUPON_TYPE_SHOPS_BUYER_COUPON",
                    "maxReturnAmount": "50000",
                    "returnText": "",
                    "discountAmount": "1199",
                    "discountedPrice": "10791"
                }
            }
        ],
        "productStats": None,
        "timeSaleDetails": None,
        "variants": [
            {
                "variantId": "2JHDxUxksqxxBms8KLK2Tg",
                "displayName": "",
                "quantity": "1",
                "size": "",
                "attributes": []
            }
        ],
        "shippingFeeConfig": None,
        "variationGrouping": None,
        "buyerPromotion": None,
        "followPromotion": {
            "displayName": "",
            "action": {
                "action": "Shop follow",
                "discountType": "RATE",
                "discountValue": "10",
                "returnType": "RETURN_TYPE_DISCOUNT",
                "couponType": "COUPON_TYPE_SHOPS_BUYER_COUPON",
                "maxReturnAmount": "50000",
                "returnText": "",
                "discountAmount": "1199",
                "discountedPrice": "10791"
            }
        },
        "lastPurchasedDateTime": None,
        "realCardReward": {
            "rewardAmount": "0",
            "hasActiveCard": False,
            "hasMvno": False,
            "rewardRate": 0,
            "lpUri": "https://campaign.jp.mercari.com/pages/ft_rc_issue_2510_estreturnrate_v1/index.html?referer=pb3_bt_nonm_nonrc&source_location=pb3_bt_nonm_nonrc",
            "estimateRewardText": "Use Mercard for <b>1.1% point return</b>",
            "disclaimerText": "Details",
            "showComponent": True
        },
        "mercardCampaign": {
            "id": "91435618",
            "title": "50%OFFクーポンがもらえる（条件あり）",
            "uri": "https://campaign.jp.mercari.com/pages/ft_rc_issue_2510_r_hangaku-8486/index.html?liketab=true&reduction_percentage=50%2F1000&referer=shopspb&source_location=shopspb",
            "text": "クーポンをもらってお買い物した場合",
            "discountAmount": 1000,
            "maxDiscount": 1000
        },
        "seoMetadata": None,
        "productPreOrder": None
    }
}


def test_mapping():
    """Test mapping the JSON to ShopProduct model"""
    try:
        print("Testing ShopProduct mapping...")
        product = map_to_class(sample_json, ShopProduct)

        print("\n✅ Mapping successful!")
        print("\n=== Basic Fields ===")
        print(f"Product ID: {product.name}")
        print(f"Display Name: {product.display_name}")
        print(f"Price: ¥{product.price_int:,}")
        print(f"Created: {product.create_time}")
        print(f"Updated: {product.update_time}")

        print("\n=== Shop Information ===")
        print(f"Shop ID: {product.product_detail.shop.name}")
        print(f"Shop Name: {product.product_detail.shop.display_name}")
        print(f"Shop Score: {product.product_detail.shop.shop_stats.score}/5")
        print(f"Shop Reviews: {product.product_detail.shop.shop_stats.review_count}")

        print("\n=== Product Details ===")
        print(f"Brand: {product.product_detail.brand.display_name}")
        print(f"Condition: {product.product_detail.condition.display_name}")
        print(f"Categories: {len(product.product_detail.categories)}")
        print(f"Photos: {len(product.product_detail.photos)}")

        print("\n=== Shipping ===")
        print(f"Method: {product.product_detail.shipping_method.display_name}")
        print(f"Payer: {product.product_detail.shipping_payer.display_name}")
        print(f"Duration: {product.product_detail.shipping_duration.display_name} ({product.product_detail.shipping_duration.min_days}-{product.product_detail.shipping_duration.max_days} days)")
        print(f"From: {product.product_detail.shipping_from_area.display_name}")

        print("\n=== Promotions ===")
        for promo in product.product_detail.promotions:
            print(f"- {promo.display_name}")
            if promo.action:
                print(f"  Action: {promo.action.action}")
                print(f"  Discount: {promo.action.discount_value}%")

        print("\n=== Variants ===")
        for variant in product.product_detail.variants:
            print(f"- Variant ID: {variant.variant_id}, Quantity: {variant.quantity}")

        print("\n=== Convenience Properties ===")
        print(f"product.product_id: {product.product_id}")
        print(f"product.shop_name: {product.shop_name}")
        print(f"product.shop_id: {product.shop_id}")
        print(f"product.price_int: {product.price_int}")

        print("\n✅ All tests passed!")
        return True

    except Exception as e:
        print(f"\n❌ Mapping failed with error:")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_mapping()
    exit(0 if success else 1)
