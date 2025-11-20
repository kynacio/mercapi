import asyncio
import sys
from mercapi import Mercapi

async def main():
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    api = Mercapi()
    item = await api.item('m67451288459')

    print(f"Item: {item.name}")
    print(f"Has auction_info: {hasattr(item, 'auction_info')}")
    print(f"auction_info value: {item.auction_info}")

    if item.auction_info:
        print(f"\nAuction details:")
        print(f"  ID: {item.auction_info.id_}")
        print(f"  State: {item.auction_info.state}")
        print(f"  Highest bid: ¥{item.auction_info.highest_bid}")

if __name__ == '__main__':
    asyncio.run(main())
