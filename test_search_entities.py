"""Test script to verify search:entities returns all expected data"""

import asyncio

import sys

from mercapi import Mercapi

 

 

async def main():

    if sys.platform == 'win32':

        sys.stdout.reconfigure(encoding='utf-8')

 

    api = Mercapi()

 

    print("="*80)

    print("Testing search:entities with query 'isamu katayama backlash'")

    print("="*80)

 

    results = await api.search('isamu katayama backlash')

 

    print(f"\n📊 Total found: {results.meta.num_found}")

    print(f"📦 Retrieved: {len(results.items)} items\n")

 

    # Statistics

    stats = {

        'total': 0,

        'mercari': 0,

        'beyond': 0,

        'with_auction': 0,

        'with_shop': 0,

        'with_brand': 0,

        'without_brand': 0,

        'with_promotion': 0,

    }

 

    # Show first 10 items in detail

    print("="*80)

    print("First 10 Items:")

    print("="*80)

 

    for idx, item in enumerate(results.items[:10], 1):

        stats['total'] += 1

 

        print(f"\n[{idx}] {item.name[:70]}")

        print(f"    ID: {item.id_}")

        print(f"    Price: ¥{item.price:,}")

        print(f"    Type: {item.item_type}")

 

        # Track item type

        if 'MERCARI' in item.item_type:

            stats['mercari'] += 1

            print(f"    📱 Regular Mercari item")

        elif 'BEYOND' in item.item_type:

            stats['beyond'] += 1

            print(f"    🏪 Mercari Shops (BEYOND) item")

 

        # Brand

        if item.item_brand:

            stats['with_brand'] += 1

            print(f"    🏷️  Brand: {item.item_brand.name} (ID: {item.item_brand.id_})")

        else:

            stats['without_brand'] += 1

            print(f"    🏷️  Brand: None")

 

        # Size

        if item.item_size:

            print(f"    📏 Size: {item.item_size.name}")

        elif item.item_sizes:

            sizes = ', '.join([s.name for s in item.item_sizes])

            print(f"    📏 Sizes: {sizes}")

        else:

            print(f"    📏 Size: None")

 

        # Auction

        if item.auction:

            stats['with_auction'] += 1

            print(f"    🔨 AUCTION!")

            print(f"       Deadline: {item.auction.bid_deadline}")

            print(f"       Highest Bid: ¥{item.auction.highest_bid}")

            print(f"       Total Bids: {item.auction.total_bid}")

 

        # Shop

        if item.shop:

            stats['with_shop'] += 1

            print(f"    🏪 SHOP!")

            print(f"       Shop ID: {item.shop.id_}")

            if item.shop.display_name:

                print(f"       Shop Name: {item.shop.display_name}")

 

        # Promotions

        if item.item_promotions:

            stats['with_promotion'] += 1

            print(f"    💰 Promotions: {len(item.item_promotions)}")

            for promo in item.item_promotions:

                print(f"       {promo}")

 

        # Photos

        if item.photos:

            print(f"    📸 Photos: {len(item.photos)}")

 

    # Check remaining items for statistics

    for item in results.items[10:]:

        stats['total'] += 1

        if 'MERCARI' in item.item_type:

            stats['mercari'] += 1

        elif 'BEYOND' in item.item_type:

            stats['beyond'] += 1

        if item.auction:

            stats['with_auction'] += 1

        if item.shop:

            stats['with_shop'] += 1

        if item.item_brand:

            stats['with_brand'] += 1

        else:

            stats['without_brand'] += 1

        if item.item_promotions:

            stats['with_promotion'] += 1

 

    # Print statistics

    print("\n" + "="*80)

    print("STATISTICS FOR ALL RETRIEVED ITEMS")

    print("="*80)

    print(f"\n📊 Total items: {stats['total']}")

    print(f"\n📱 Item Types:")

    print(f"   - Regular Mercari (ITEM_TYPE_MERCARI): {stats['mercari']}")

    print(f"   - Mercari Shops (ITEM_TYPE_BEYOND): {stats['beyond']}")

    print(f"\n🏷️  Brands:")

    print(f"   - Items with brand: {stats['with_brand']}")

    print(f"   - Items without brand: {stats['without_brand']}")

    print(f"\n🔨 Auctions:")

    print(f"   - Items with auction: {stats['with_auction']}")

    print(f"\n🏪 Shops:")

    print(f"   - Items from shops: {stats['with_shop']}")

    print(f"\n💰 Promotions:")

    print(f"   - Items with promotions: {stats['with_promotion']}")

 

    # Validation

    print("\n" + "="*80)

    print("VALIDATION")

    print("="*80)

 

    checks = [

        ("Regular Mercari items", stats['mercari'] > 0),

        ("Mercari Shops items", stats['beyond'] > 0),

        ("Items with auctions", stats['with_auction'] > 0),

        ("Items from shops", stats['with_shop'] > 0),

        ("Items with brands", stats['with_brand'] > 0),

        ("Items with promotions", stats['with_promotion'] > 0),

    ]

 

    all_passed = True

    for check_name, passed in checks:

        status = "✅" if passed else "❌"

        print(f"{status} {check_name}")

        if not passed:

            all_passed = False

 

    if all_passed:

        print("\n🎉 SUCCESS! All different listing types found!")

    else:

        print("\n⚠️  Some listing types not found in results")

 

    print("\n" + "="*80)

 

 

if __name__ == '__main__':

    asyncio.run(main())

 