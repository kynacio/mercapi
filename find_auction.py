import asyncio
import sys
from mercapi import Mercapi

async def main():
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    api = Mercapi()

    # Search for items
    results = await api.search('saint laurent')

    print(f"Searching for auction items in {len(results.items)} results...\n")

    auction_count = 0
    for item in results.items:
        if item.auction:
            auction_count += 1
            print(f"✅ Found auction item!")
            print(f"  ID: {item.id_}")
            print(f"  Name: {item.name[:60]}...")
            print(f"  Highest bid: ¥{item.auction.highest_bid}")
            print(f"  Deadline: {item.auction.bid_deadline}")
            print()

            # Try to fetch full details
            full_item = await api.item(item.id_)
            if full_item:
                print(f"  Full item has auction_info: {full_item.auction_info is not None}")
                if full_item.auction_info:
                    print(f"  Auction info: {full_item.auction_info}")
            print()

    print(f"\nTotal auction items found: {auction_count}/{len(results.items)}")

if __name__ == '__main__':
    asyncio.run(main())
