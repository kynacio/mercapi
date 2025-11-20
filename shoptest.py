import asyncio
import sys
from mercapi import Mercapi

async def main():
    # Set UTF-8 encoding for console output (Windows compatibility)
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')
    api = Mercapi()

    # 1. Enhanced Search
    print("=== SEARCH RESULTS ===")
    results = await api.search('saint laurent')

    for item in results.items[:5]:  # Show first 5
        print(f"\n{item.name} - ¥{item.price}")

        # Auction information
        if item.auction:
            print(f"  🔨 Auction ends: {item.auction.bid_deadline}")
            print(f"     Highest bid: ¥{item.auction.highest_bid}")

        # Shop information
        if item.shop:
            # Note: Search results only include shop ID, not display_name
            # To get shop details, you need to fetch the full shop product
            print(f"  🏪 Shop Item (ID: {item.shop.id_})")

        # Brand
        if item.item_brand:
            print(f"  Brand: {item.item_brand.name}")

    # 2. COMPREHENSIVE SHOP PRODUCT DETAILS
    print("\n" + "="*80)
    print("=== COMPREHENSIVE SHOP PRODUCT DETAILS ===")
    print("="*80)
    shop_product = await api.shop_product('NRi5h7fcvRxpRD6QoLDRZU')

    if shop_product:
        print(f"\n📦 PRODUCT INFORMATION")
        print(f"  Product ID: {shop_product.name}")
        print(f"  Display Name: {shop_product.display_name}")
        print(f"  Price: ¥{shop_product.price}")
        print(f"  Thumbnail: {shop_product.thumbnail}")
        print(f"  Created: {shop_product.create_time}")
        print(f"  Updated: {shop_product.update_time}")
        print(f"  Product Tags: {shop_product.product_tags if shop_product.product_tags else 'None'}")

        # Product Details
        detail = shop_product.product_detail

        # Shop information
        print(f"\n🏪 SHOP INFORMATION")
        shop = detail.shop
        print(f"  Shop ID: {shop.name}")
        print(f"  Display Name: {shop.display_name}")
        print(f"  Thumbnail: {shop.thumbnail}")
        print(f"  Allow Direct Message: {shop.allow_direct_message}")
        print(f"  Is Inbound XB: {shop.is_inbound_xb}")
        print(f"  Has Approved Brand Screening: {shop.has_approved_brand_screening}")

        # Shop Stats
        print(f"\n  📊 Shop Statistics:")
        stats = shop.shop_stats
        print(f"    Score: {stats.score}/5")
        print(f"    Review Count: {stats.review_count}")
        print(f"    Shop ID: {stats.shop_id}")

        # Shop Badges
        if shop.badges:
            print(f"\n  🏅 Badges: {shop.badges}")
        else:
            print(f"\n  🏅 Badges: None")

        # Photos
        print(f"\n📸 PHOTOS")
        print(f"  Total: {len(detail.photos)}")
        for idx, photo in enumerate(detail.photos[:3], 1):
            print(f"  [{idx}] {photo}")

        # Description
        print(f"\n📝 DESCRIPTION")
        desc_preview = detail.description[:200] + "..." if len(detail.description) > 200 else detail.description
        print(f"  {desc_preview}")

        # Categories
        print(f"\n📁 CATEGORIES")
        for cat in detail.categories:
            print(f"  - {cat.display_name} (ID: {cat.category_id}, Root: {cat.root_id})")

        # Brand
        if detail.brand:
            print(f"\n🏷️ BRAND")
            print(f"  Brand ID: {detail.brand.brand_id}")
            print(f"  Display Name: {detail.brand.display_name}")

        # Condition
        if detail.condition:
            print(f"\n✨ CONDITION")
            print(f"  {detail.condition.display_name}")

        # Shipping Information
        print(f"\n🚚 SHIPPING INFORMATION")
        if detail.shipping_method:
            print(f"  Method: {detail.shipping_method.display_name} (ID: {detail.shipping_method.shipping_method_id})")
            print(f"  Is Anonymous: {detail.shipping_method.is_anonymous}")

        if detail.shipping_payer:
            print(f"  Payer: {detail.shipping_payer.display_name} ({detail.shipping_payer.code})")
            print(f"  Payer ID: {detail.shipping_payer.shipping_payer_id}")

        if detail.shipping_duration:
            print(f"  Duration: {detail.shipping_duration.display_name}")
            print(f"  Days: {detail.shipping_duration.min_days}-{detail.shipping_duration.max_days}")
            print(f"  Duration ID: {detail.shipping_duration.shipping_duration_id}")

        if detail.shipping_from_area:
            print(f"  From: {detail.shipping_from_area.display_name} (Code: {detail.shipping_from_area.shipping_area_code})")

        # Promotions
        print(f"\n🎁 PROMOTIONS")
        if detail.promotions:
            for promo in detail.promotions:
                print(f"  - {promo.display_name}")
                print(f"    Action: {promo.action.action}")
                print(f"    Discount Type: {promo.action.discount_type}")
                print(f"    Discount Value: {promo.action.discount_value}%")
                print(f"    Discount Amount: ¥{promo.action.discount_amount}")
                print(f"    Discounted Price: ¥{promo.action.discounted_price}")
                print(f"    Max Return: ¥{promo.action.max_return_amount}")
                print(f"    Coupon Type: {promo.action.coupon_type}")
        else:
            print("  None")

        # Follow Promotion
        if detail.follow_promotion:
            print(f"\n👥 FOLLOW PROMOTION")
            print(f"  Display Name: {detail.follow_promotion.display_name}")
            print(f"  Action: {detail.follow_promotion.action.action}")
            print(f"  Discount: ¥{detail.follow_promotion.action.discount_amount}")
            print(f"  Final Price: ¥{detail.follow_promotion.action.discounted_price}")

        # Product Stats
        if detail.product_stats:
            print(f"\n📊 PRODUCT STATISTICS")
            if hasattr(detail.product_stats, 'view_count') and detail.product_stats.view_count:
                print(f"  View Count: {detail.product_stats.view_count}")
            if hasattr(detail.product_stats, 'like_count') and detail.product_stats.like_count:
                print(f"  Like Count: {detail.product_stats.like_count}")

        # Time Sale Details
        if detail.time_sale_details:
            print(f"\n⏰ TIME SALE")
            print(f"  Sale ID: {detail.time_sale_details.sale_id}")
            print(f"  Sale Price: ¥{detail.time_sale_details.sale_price}")
            print(f"  Original Price: ¥{detail.time_sale_details.original_price}")
            print(f"  Start: {detail.time_sale_details.start_time}")
            print(f"  End: {detail.time_sale_details.end_time}")

        # Variants
        print(f"\n📦 VARIANTS")
        for variant in detail.variants:
            print(f"  - Variant ID: {variant.variant_id}")
            print(f"    Display Name: {variant.display_name if variant.display_name else '(no name)'}")
            print(f"    Quantity: {variant.quantity}")
            print(f"    Size: {variant.size if variant.size else '(no size)'}")

        # Real Card Reward
        if detail.real_card_reward:
            print(f"\n💳 MERCARD REWARD")
            print(f"  Reward Amount: ¥{detail.real_card_reward.reward_amount}")
            print(f"  Has Active Card: {detail.real_card_reward.has_active_card}")
            print(f"  Reward Rate: {detail.real_card_reward.reward_rate}%")
            print(f"  Estimate Text: {detail.real_card_reward.estimate_reward_text}")
            print(f"  Show Component: {detail.real_card_reward.show_component}")

        # Mercard Campaign
        if detail.mercard_campaign:
            print(f"\n🎉 MERCARD CAMPAIGN")
            print(f"  ID: {detail.mercard_campaign.id_}")
            print(f"  Title: {detail.mercard_campaign.title}")
            print(f"  Text: {detail.mercard_campaign.text}")
            print(f"  Discount Amount: ¥{detail.mercard_campaign.discount_amount}")
            print(f"  Max Discount: ¥{detail.mercard_campaign.max_discount}")

        # Other shop items
        print(f"\n🛍️ OTHER ITEMS FROM {shop.display_name}")
        for item in shop.shop_items[:5]:
            tags = f" [{', '.join(item.product_tags)}]" if item.product_tags else ""
            print(f"  - {item.display_name}: ¥{item.price}{tags}")

    # 3. COMPREHENSIVE REGULAR MERCARI ITEM DETAILS
    print("\n" + "="*80)
    print("=== COMPREHENSIVE REGULAR MERCARI ITEM DETAILS ===")
    print("="*80)
    item = await api.item('m54905959893')

    if item:
        print(f"\n📦 ITEM INFORMATION")
        print(f"  Item ID: {item.id_}")
        print(f"  Name: {item.name}")
        print(f"  Price: ¥{item.price}")
        print(f"  Status: {item.status}")
        print(f"  Is Shop Item: {item.is_shop_item}")

        # Description
        print(f"\n📝 DESCRIPTION")
        desc_preview = item.description[:200] + "..." if len(item.description) > 200 else item.description
        print(f"  {desc_preview}")

        # Seller information
        if item.seller:
            print(f"\n👤 SELLER INFORMATION")
            print(f"  Name: {item.seller.name}")
            print(f"  Seller ID: {item.seller.id_}")
            print(f"  Photo URL: {item.seller.photo}")
            print(f"  Created: {item.seller.created}")
            print(f"  Items for sale: {item.seller.num_sell_items}")
            print(f"\n  📊 Seller Ratings:")
            print(f"    Good: {item.seller.ratings.good}")
            print(f"    Normal: {item.seller.ratings.normal}")
            print(f"    Bad: {item.seller.ratings.bad}")
            print(f"    Total ratings: {item.seller.num_ratings}")
            print(f"    Score: {item.seller.score}")
            print(f"    Star rating: {item.seller.star_rating_score}/5")
            print(f"\n  ✓ Quick shipper: {item.seller.quick_shipper}")
            print(f"  ✓ Is official: {item.seller.is_official}")
            print(f"  ✓ Is followable: {item.seller.is_followable}")
            print(f"  ✓ Is blocked: {item.seller.is_blocked}")
            print(f"  SMS confirmation: {item.seller.register_sms_confirmation}")
            print(f"  SMS confirmation at: {item.seller.register_sms_confirmation_at}")

        # Requester
        if item.requester:
            print(f"\n🔍 REQUESTER INFO")
            print(f"  Created: {item.requester.created}")

        # Brand and Size
        if item.item_brand:
            print(f"\n🏷️ BRAND")
            print(f"  Brand ID: {item.item_brand.id_}")
            print(f"  Name: {item.item_brand.name}")
            print(f"  Sub-name: {item.item_brand.sub_name}")

        if item.item_size:
            print(f"\n📏 SIZE")
            print(f"  Size ID: {item.item_size.id_}")
            print(f"  Name: {item.item_size.name}")

        # Condition
        if item.item_condition:
            print(f"\n✨ CONDITION")
            print(f"  ID: {item.item_condition.id_}")
            print(f"  Name: {item.item_condition.name}")
            print(f"  Description: {item.item_condition.subname}")

        # Categories
        if item.item_category:
            print(f"\n📁 ITEM CATEGORY")
            print(f"  ID: {item.item_category.id_}")
            print(f"  Name: {item.item_category.name}")
            print(f"  Display order: {item.item_category.display_order}")
            if hasattr(item.item_category, 'parent_category_id'):
                print(f"  Parent: {item.item_category.parent_category_name} (ID: {item.item_category.parent_category_id})")
                print(f"  Root: {item.item_category.root_category_name} (ID: {item.item_category.root_category_id})")

        if item.item_category_ntiers:
            print(f"\n📁 CATEGORY HIERARCHY (N-TIERS)")
            print(f"  ID: {item.item_category_ntiers.id_}")
            print(f"  Name: {item.item_category_ntiers.name}")
            if hasattr(item.item_category_ntiers, 'size_group_id'):
                print(f"  Size group ID: {item.item_category_ntiers.size_group_id}")
            if hasattr(item.item_category_ntiers, 'brand_group_id'):
                print(f"  Brand group ID: {item.item_category_ntiers.brand_group_id}")

        if item.parent_categories_ntiers:
            print(f"\n📁 PARENT CATEGORIES")
            for cat in item.parent_categories_ntiers:
                print(f"  - {cat.name} (ID: {cat.id_}, Order: {cat.display_order})")

        # Colors
        if item.colors:
            print(f"\n🎨 COLORS")
            for color in item.colors:
                print(f"  - {color.name} (ID: {color.id_}, RGB: {color.rgb_code})")
        else:
            print(f"\n🎨 COLORS: None specified")

        # Auction information (if present)
        if item.auction_info:
            print(f"\n🔨 AUCTION INFORMATION")
            print(f"  Auction ID: {item.auction_info.id_}")
            print(f"  State: {item.auction_info.state}")
            print(f"  Type: {item.auction_info.auction_type}")
            print(f"  Initial price: ¥{item.auction_info.initial_price}")
            print(f"  Highest bid: ¥{item.auction_info.highest_bid}")
            print(f"  Total bids: {item.auction_info.total_bids}")
            print(f"  Start time: {item.auction_info.start_time}")
            print(f"  Expected end time: {item.auction_info.expected_end_time}")

        # Shipping information
        print(f"\n🚚 SHIPPING INFORMATION")
        if item.shipping_payer:
            print(f"  Payer: {item.shipping_payer.name} (Code: {item.shipping_payer.code})")
        if item.shipping_method:
            print(f"  Method: {item.shipping_method.name} (ID: {item.shipping_method.id_})")
            print(f"  Deprecated: {item.shipping_method.is_deprecated}")
        if item.shipping_from_area:
            print(f"  From: {item.shipping_from_area.name} (ID: {item.shipping_from_area.id_})")
        if item.shipping_duration:
            print(f"  Duration: {item.shipping_duration.name}")
            print(f"  Days: {item.shipping_duration.min_days}-{item.shipping_duration.max_days}")
        if item.shipping_class:
            print(f"\n  Shipping Class:")
            print(f"    Fee: ¥{item.shipping_class.fee}")
            print(f"    Shipping fee: ¥{item.shipping_class.shipping_fee}")
            print(f"    Pickup fee: ¥{item.shipping_class.pickup_fee}")
            print(f"    Total fee: ¥{item.shipping_class.total_fee}")
            print(f"    Is pickup: {item.shipping_class.is_pickup}")
        print(f"  Is anonymous shipping: {item.is_anonymous_shipping}")
        print(f"  Is dynamic shipping fee: {item.is_dynamic_shipping_fee}")

        # Payment options
        if item.defpay:
            print(f"\n💳 INSTALLMENT PAYMENT (DEFPAY)")
            print(f"  Calculated price: ¥{item.defpay.calculated_price}")
            print(f"  Monthly amount: ¥{item.defpay.installment_monthly_amount}")
            print(f"  Number of times: {item.defpay.installment_times}")
            print(f"  Is heavy user: {item.defpay.is_easypay_heavy_user}")
            print(f"  Has used before: {item.defpay.has_ever_used_installment_payment}")
            if item.defpay.promotion_installment:
                print(f"\n  Promotion:")
                print(f"    Message: {item.defpay.promotion_installment.message}")
                if item.defpay.promotion_installment.campaign_message:
                    print(f"    Campaign: {item.defpay.promotion_installment.campaign_message}")

        # Price promotion
        if item.price_promotion_area_details:
            print(f"\n💰 PRICE PROMOTION")
            print(f"  Type: {item.price_promotion_area_details.promotion_type}")
            if item.price_promotion_area_details.promotion_info:
                for info in item.price_promotion_area_details.promotion_info:
                    if info.supplementary_text:
                        print(f"  Info: {info.supplementary_text}")

        # Rewards
        if item.estimate_info:
            print(f"\n🎁 REWARD ESTIMATE")
            print(f"  Total rate: {item.estimate_info.total_rate}%")
            print(f"  Mercard reward: ¥{item.estimate_info.mercard_estimate_reward}")
            print(f"  Estimate text: {item.estimate_info.estimate_reward_text}")
            print(f"  Disclaimer: {item.estimate_info.disclaimer_text}")

        # Engagement
        print(f"\n💬 ENGAGEMENT")
        print(f"  Likes: {item.num_likes}")
        print(f"  Comments: {item.num_comments}")
        print(f"  Liked by you: {item.liked}")
        print(f"  Registered prices: {item.registered_prices_count}")

        # Comments
        if item.comments:
            print(f"\n  💬 Comments:")
            for comment in item.comments[:3]:  # Show first 3
                print(f"    - {comment.user.name}: {comment.message[:50]}...")
                print(f"      Posted: {comment.created}")

        # Photos
        print(f"\n📸 PHOTOS")
        print(f"  Total: {len(item.photos)}")
        print(f"  Thumbnails: {len(item.thumbnails)}")
        for idx, photo in enumerate(item.photos[:3], 1):
            print(f"  [{idx}] {photo}")

        # Attributes
        if item.item_attributes:
            print(f"\n🏷️ ITEM ATTRIBUTES")
            for attr in item.item_attributes:
                if attr.show_on_ui:
                    values = [v.text for v in attr.values if v.text]
                    if values:
                        print(f"  {attr.text}: {', '.join(values)}")

        # Hash tags
        if item.hash_tags:
            print(f"\n#️⃣ HASH TAGS")
            print(f"  {', '.join(item.hash_tags)}")

        # Flags and settings
        print(f"\n⚙️ ITEM FLAGS & SETTINGS")
        print(f"  Is web visible: {item.is_web_visible}")
        print(f"  Is offerable: {item.is_offerable}")
        print(f"  Is offerable v2: {item.is_offerable_v2}")
        print(f"  Is cancelable: {item.is_cancelable}")
        print(f"  Is stock item: {item.is_stock_item}")
        print(f"  Is dismissed: {item.is_dismissed}")
        print(f"  Is organizational user: {item.is_organizational_user}")
        print(f"  Organizational status: {item.organizational_user_status}")
        print(f"  Shipped by worker: {item.shipped_by_worker}")
        print(f"  Has additional service: {item.has_additional_service}")
        print(f"  Has like list: {item.has_like_list}")
        print(f"  Has active mercard: {item.has_active_mercard}")

        # Promotion message
        if item.promotion_explanation_message:
            print(f"\n📢 PROMOTION MESSAGE")
            print(f"  {item.promotion_explanation_message}")

        # Meta information
        print(f"\n📋 META INFORMATION")
        print(f"  Title: {item.meta_title}")
        print(f"  Subtitle: {item.meta_subtitle}")
        print(f"  Checksum: {item.checksum}")
        print(f"  Pager ID: {item.pager_id}")

        # Timestamps
        print(f"\n⏰ TIMESTAMPS")
        print(f"  Created: {item.created}")
        print(f"  Updated: {item.updated}")

if __name__ == '__main__':
    asyncio.run(main())
