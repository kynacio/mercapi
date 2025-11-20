import asyncio
import sys
import logging
from mercapi import Mercapi

# Enable DEBUG logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

async def main():
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    api = Mercapi()

    print("Fetching item m67451288459...\n")
    item = await api.item('m67451288459')

    print(f"\n{'='*60}")
    print(f"Item: {item.name}")
    print(f"Has auction_info: {hasattr(item, 'auction_info')}")
    print(f"auction_info value: {item.auction_info}")

if __name__ == '__main__':
    asyncio.run(main())
