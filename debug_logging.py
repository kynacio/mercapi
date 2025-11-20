"""Debug with logging enabled"""
import asyncio
import sys
import logging
from mercapi import Mercapi

# Enable DEBUG logging to see all warnings and debug messages
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

async def main():
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    api = Mercapi()

    print("Searching for 'saint laurent' with DEBUG logging enabled\n")
    print("="*60)
    results = await api.search('saint laurent')

    print("\n" + "="*60)
    print(f"\nGot {len(results.items)} items")

    # Check first item
    if results.items:
        item = results.items[0]
        print(f"\nFirst item: {item.name}")
        print(f"  Brand: {item.item_brand}")
        print(f"  Size: {item.item_size}")
        print(f"  Auction: {item.auction}")

if __name__ == '__main__':
    asyncio.run(main())
