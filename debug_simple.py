"""Simple debug to check if brands/sizes/auctions are being returned"""
import asyncio
import sys
from mercapi import Mercapi

async def main():
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    api = Mercapi()

    # Search for items that should have brands
    print("Searching for 'saint laurent' - should have brands\n")
    results = await api.search('saint laurent')

    brands_found = 0
    sizes_found = 0
    auctions_found = 0

    for i, item in enumerate(results.items, 1):
        if item.item_brand:
            brands_found += 1
            if brands_found <= 3:
                print(f"✅ Item {i} HAS BRAND: {item.item_brand.name}")
                print(f"   Name: {item.name[:50]}")

        if item.item_size:
            sizes_found += 1
            if sizes_found <= 3:
                print(f"✅ Item {i} HAS SIZE: {item.item_size.name}")

        if item.item_sizes and len(item.item_sizes) > 0:
            if brands_found <= 3:  # reuse counter for display limit
                print(f"✅ Item {i} HAS SIZES LIST: {[s.name for s in item.item_sizes]}")

        if item.auction:
            auctions_found += 1
            if auctions_found <= 3:
                print(f"✅ Item {i} HAS AUCTION:")
                print(f"   Highest bid: ¥{item.auction.highest_bid}")
                print(f"   Deadline: {item.auction.bid_deadline}")

    print(f"\n=== SUMMARY ===")
    print(f"Total items: {len(results.items)}")
    print(f"Items with brands: {brands_found}")
    print(f"Items with size: {sizes_found}")
    print(f"Items with auctions: {auctions_found}")

if __name__ == '__main__':
    asyncio.run(main())
