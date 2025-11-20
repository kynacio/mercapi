"""Debug script to examine raw API responses"""
import asyncio
import json
import sys
from mercapi import Mercapi

async def main():
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    api = Mercapi()

    # Make a raw API call to see the actual response
    print("Fetching search results for 'saint laurent'...\n")

    # Use the internal method to get raw response
    response = await api._request(
        "GET",
        "https://api.mercari.jp/v2/entities:search",
        params={
            "keyword": "saint laurent",
            "limit": "5",
            "offset": "0",
            "order": "ORDER_DESC",
            "sort": "SORT_CREATED_TIME",
            "status": "STATUS_ON_SALE"
        }
    )

    print("=== RAW API RESPONSE (first 3 items) ===\n")

    if "items" in response and len(response["items"]) > 0:
        for i, item in enumerate(response["items"][:3], 1):
            print(f"\n--- Item {i}: {item.get('name', 'NO NAME')[:50]} ---")
            print(f"ID: {item.get('id')}")
            print(f"Price: ¥{item.get('price')}")

            # Check brand
            brand = item.get('itemBrand')
            if brand:
                print(f"✅ HAS itemBrand: {json.dumps(brand, ensure_ascii=False)}")
            else:
                print(f"❌ NO itemBrand (value: {brand})")

            # Check size
            size = item.get('itemSize')
            if size:
                print(f"✅ HAS itemSize: {json.dumps(size, ensure_ascii=False)}")
            else:
                print(f"❌ NO itemSize (value: {size})")

            # Check sizes list
            sizes = item.get('itemSizes')
            if sizes:
                print(f"✅ HAS itemSizes: {json.dumps(sizes, ensure_ascii=False)}")
            else:
                print(f"❌ NO itemSizes (value: {sizes})")

            # Check auction
            auction = item.get('auction')
            if auction:
                print(f"✅ HAS auction: {json.dumps(auction, ensure_ascii=False)}")
            else:
                print(f"❌ NO auction (value: {auction})")

            # Check shop
            shop = item.get('shop')
            if shop:
                print(f"✅ HAS shop: {json.dumps(shop, ensure_ascii=False)}")
            else:
                print(f"❌ NO shop (value: {shop})")

    print("\n\n=== NOW TESTING PARSED RESULTS ===\n")

    results = await api.search('saint laurent')
    for i, item in enumerate(results.items[:3], 1):
        print(f"\n--- Parsed Item {i} ---")
        print(f"Name: {item.name[:50]}")
        print(f"Brand object: {item.item_brand}")
        if item.item_brand:
            print(f"  Brand name: {item.item_brand.name}")
        print(f"Size object: {item.item_size}")
        if item.item_size:
            print(f"  Size name: {item.item_size.name}")
        print(f"Sizes list: {item.item_sizes}")
        print(f"Auction: {item.auction}")
        print(f"Shop: {item.shop}")

if __name__ == '__main__':
    asyncio.run(main())
