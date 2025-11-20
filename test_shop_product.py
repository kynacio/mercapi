#!/usr/bin/env python3
"""
Test script for ShopProduct functionality
"""
import asyncio
from mercapi import Mercapi


async def test_shop_product():
    """Test fetching a shop product"""
    # Initialize Mercapi client
    m = Mercapi()

    # Test product ID from the example
    product_id = "2JHDxUxi3SsqAG5umbmWY2"

    print(f"Fetching shop product: {product_id}")
    product = await m.shop_product(product_id)

    if product is None:
        print("Product not found (404) or network error")
        return

    print("\n=== Shop Product Details ===")
    print(f"Product ID: {product.product_id}")
    print(f"Display Name: {product.display_name}")
    print(f"Price: ¥{product.price_int:,}")
    print(f"Thumbnail: {product.thumbnail}")
    print(f"Created: {product.create_time}")
    print(f"Updated: {product.update_time}")

    if product.product_detail:
        detail = product.product_detail
        print(f"\n=== Shop Information ===")
        print(f"Shop Name: {product.shop_name}")
        print(f"Shop ID: {product.shop_id}")

        if detail.shop.shop_stats:
            stats = detail.shop.shop_stats
            print(f"Shop Score: {stats.score}/5")
            print(f"Review Count: {stats.review_count}")

        print(f"\n=== Product Details ===")
        print(f"Description: {detail.description[:100]}...")
        print(f"Number of Photos: {len(detail.photos)}")

        if detail.brand:
            print(f"Brand: {detail.brand.display_name}")

        if detail.condition:
            print(f"Condition: {detail.condition.display_name}")

        if detail.categories:
            print(f"Categories: {' > '.join([c.display_name for c in detail.categories])}")

        print(f"\n=== Shipping Information ===")
        if detail.shipping_method:
            print(f"Method: {detail.shipping_method.display_name}")
        if detail.shipping_payer:
            print(f"Payer: {detail.shipping_payer.display_name}")
        if detail.shipping_duration:
            print(f"Duration: {detail.shipping_duration.display_name} ({detail.shipping_duration.min_days}-{detail.shipping_duration.max_days} days)")
        if detail.shipping_from_area:
            print(f"From: {detail.shipping_from_area.display_name}")

        if detail.variants:
            print(f"\n=== Variants ===")
            for variant in detail.variants:
                print(f"  - {variant.variant_id}: Quantity {variant.quantity}")

        if detail.promotions:
            print(f"\n=== Promotions ===")
            for promo in detail.promotions:
                print(f"  - {promo.display_name}")
                if promo.action:
                    print(f"    Action: {promo.action.action}")
                    if promo.action.discount_value:
                        print(f"    Discount: {promo.action.discount_value}% off")

    print("\n✅ Test completed successfully!")


if __name__ == "__main__":
    asyncio.run(test_shop_product())
