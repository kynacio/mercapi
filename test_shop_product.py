"""
Example script demonstrating the new shop product functionality.

This script shows how to fetch a Mercari Shop product listing using the new shop_product() method.
"""

import asyncio
from mercapi import Mercapi


async def main():
    api = Mercapi()

    # Example shop product ID from your curl request
    product_id = "2JHDxUxi3SsqAG5umbmWY2"

    print(f"Fetching shop product: {product_id}")
    product = await api.shop_product(product_id)

    if product:
        print(f"\nProduct Name: {product.display_name}")
        print(f"Price: ¥{product.price}")
        print(f"Created: {product.create_time}")
        print(f"Updated: {product.update_time}")

        # Shop information
        shop = product.product_detail.shop
        print(f"\nShop: {shop.display_name}")
        print(f"Shop Score: {shop.shop_stats.score}/5")
        print(f"Shop Reviews: {shop.shop_stats.review_count}")

        # Product details
        print(f"\nDescription: {product.product_detail.description[:200]}...")
        print(f"Photos: {len(product.product_detail.photos)} images")
        print(f"Categories: {[cat.display_name for cat in product.product_detail.categories]}")

        # Brand (if available)
        if product.product_detail.brand:
            print(f"Brand: {product.product_detail.brand.display_name}")

        # Condition
        print(f"Condition: {product.product_detail.condition.display_name}")

        # Shipping info
        print(f"\nShipping From: {product.product_detail.shipping_from_area.display_name}")
        print(f"Shipping Duration: {product.product_detail.shipping_duration.display_name}")
        print(f"Shipping Payer: {product.product_detail.shipping_payer.display_name}")

        # Promotions
        if product.product_detail.promotions:
            print(f"\nPromotions:")
            for promo in product.product_detail.promotions:
                print(f"  - {promo.display_name}")
                print(f"    Discount: ¥{promo.action.discount_amount} (New price: ¥{promo.action.discounted_price})")

        # Variants
        print(f"\nVariants: {len(product.product_detail.variants)}")
        for variant in product.product_detail.variants:
            print(f"  - {variant.display_name or 'Default'}: Quantity {variant.quantity}")

        # Shop items (other products from this shop)
        print(f"\nOther shop items: {len(shop.shop_items)}")
        for item in shop.shop_items[:3]:  # Show first 3
            print(f"  - {item.display_name}: ¥{item.price}")
    else:
        print("Product not found")


if __name__ == "__main__":
    asyncio.run(main())
