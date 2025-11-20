#!/usr/bin/env python3
"""Test JSON parsing for shop product with the provided JSON structure."""

import json
import sys
sys.path.insert(0, '/home/user/mercapi')

from mercapi.models.shop import ShopProduct
from mercapi.mapping import map_to_class

# The JSON structure from the user
test_json = {
    "name": "NRi5h7fcvRxpRD6QoLDRZU",
    "displayName": "ISAMU KATAYAMA BACKLASH (イサムカタヤマバックラッシュ) カウレザー 牛革 ダブルライダースジャケット ダークブラウン",
    "productTags": [],
    "thumbnail": "https://assets.mercari-shops-static.com/-/small/plain/Zff9FPZngkJ2L6KrJGcbR8.jpg@jpg",
    "price": "62700",
    "createTime": "2025-10-01T01:03:36Z",
    "updateTime": "2025-10-24T03:47:16Z",
    "attributes": [],
    "productDetail": {
        "shop": {
            "name": "aXQx7LKu3us59Yo7fQmwsk",
            "displayName": "BRINGメルカリ店",
            "thumbnail": "https://assets.mercari-shops-static.com/-/small/plain/Yu4PKJmtoEyju8ApCNQR2b.png@jpg",
            "shopStats": {
                "shopId": "aXQx7LKu3us59Yo7fQmwsk",
                "score": 5,
                "reviewCount": "22408"
            },
            "allowDirectMessage": True,
            "shopItems": [
                {
                    "productId": "2JHEqdQJjCLg3kqwUUzb5z",
                    "displayName": "BALENCIAGA (バレンシアガ) High Top Sneaker レザーハイカットスニーカー ブラック",
                    "productTags": [],
                    "thumbnail": "https://assets.mercari-shops-static.com/-/small/plain/2JHEqdMmAbwW4iQTtGo5x4.jpg@jpg",
                    "price": "12589"
                }
            ],
            "isInboundXb": False,
            "badges": [],
            "hasApprovedBrandScreening": False
        },
        "photos": [
            "https://assets.mercari-shops-static.com/-/large/plain/Zff9FPZngkJ2L6KrJGcbR8.jpg@jpg",
            "https://assets.mercari-shops-static.com/-/large/plain/RFJBdJqvkfXGSEgXu8UsVf.jpg@jpg"
        ],
        "description": "【ブランド】ISAMU KATAYAMA BACKLASH（イサムカタヤマバックラッシュ）",
        "categories": [
            {
                "categoryId": "132",
                "displayName": "Hoodie",
                "parentId": "11",
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
                    "discountAmount": "5956",
                    "discountedPrice": "53609"
                }
            }
        ],
        "productStats": {
            "productId": "NRi5h7fcvRxpRD6QoLDRZU",
            "score": 0,
            "reviewCount": 0,
            "likesCount": 7
        },
        "timeSaleDetails": {
            "name": "",
            "percentage": 5,
            "price": "59565",
            "startTime": "2025-10-24T08:00:00Z",
            "endTime": "2025-11-22T08:00:00Z",
            "base": "STABLE_PRICE",
            "calculationStartTime": "2025-08-29T02:48:08.191243Z",
            "calculationEndTime": "2025-10-24T02:48:08.191243Z"
        },
        "variants": [
            {
                "variantId": "ySJbokgwcVV47ZK7jLkbXb",
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
                "discountAmount": "5956",
                "discountedPrice": "53609"
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

print("Testing JSON parsing...")
print("=" * 80)

try:
    product = map_to_class(test_json, ShopProduct)

    print("✅ PARSING SUCCESS!")
    print("\n" + "=" * 80)
    print("PARSED DATA:")
    print("=" * 80)

    print(f"\n📦 PRODUCT INFORMATION")
    print(f"  Product ID: {product.name}")
    print(f"  Display Name: {product.display_name}")
    print(f"  Price: ¥{product.price}")
    print(f"  Product Tags: {product.product_tags}")

    detail = product.product_detail

    print(f"\n🎁 PROMOTIONS")
    if detail.promotions:
        for promo in detail.promotions:
            print(f"  - {promo.display_name}")
            print(f"    Discount: ¥{promo.action.discount_amount}")
    else:
        print("  None")

    print(f"\n📊 PRODUCT STATISTICS")
    if detail.product_stats:
        print(f"  Product ID: {detail.product_stats.product_id}")
        print(f"  Score: {detail.product_stats.score}")
        print(f"  Review Count: {detail.product_stats.review_count}")
        print(f"  Likes Count: {detail.product_stats.likes_count}")

    print(f"\n⏰ TIME SALE DETAILS")
    if detail.time_sale_details:
        print(f"  Name: {detail.time_sale_details.name if detail.time_sale_details.name else '(empty)'}")
        print(f"  Discount Percentage: {detail.time_sale_details.percentage}%")
        print(f"  Sale Price: ¥{detail.time_sale_details.price}")
        print(f"  Base: {detail.time_sale_details.base}")
        print(f"  Start: {detail.time_sale_details.start_time}")
        print(f"  End: {detail.time_sale_details.end_time}")

    print(f"\n🎉 MERCARD CAMPAIGN")
    if detail.mercard_campaign:
        print(f"  ID: {detail.mercard_campaign.id_}")
        print(f"  Title: {detail.mercard_campaign.title}")
        print(f"  Text: {detail.mercard_campaign.text}")
        print(f"  Discount Amount: ¥{detail.mercard_campaign.discount_amount}")
        print(f"  Max Discount: ¥{detail.mercard_campaign.max_discount}")

    print("\n" + "=" * 80)
    print("✅ ALL FIELDS PARSED SUCCESSFULLY!")
    print("=" * 80)

except Exception as e:
    print(f"❌ PARSING FAILED!")
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
