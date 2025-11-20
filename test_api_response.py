"""Simple test with error handling to see API response"""

import asyncio

import sys

from mercapi import Mercapi

 

 

async def main():

    if sys.platform == 'win32':

        sys.stdout.reconfigure(encoding='utf-8')

 

    api = Mercapi()

 

    # Patch the _search_impl to see responses

    original_search_impl = api._search_impl

 

    async def patched_search_impl(request):

        res = await api._client.send(api._search(request))

        print(f"Status code: {res.status_code}")

        print(f"Response headers: {dict(res.headers)}")

        print(f"Response text (first 500 chars): {res.text[:500]}")

 

        if res.status_code != 200:

            print(f"ERROR: Got status {res.status_code}")

            return None

 

        return await original_search_impl(request)

 

    api._search_impl = patched_search_impl

 

    print("Testing search...")

    try:

        results = await api.search('isamu katayama backlash')

        if results:

            print(f"\n✅ Success! Found {len(results.items)} items")

            if results.items:

                item = results.items[0]

                print(f"First item: {item.name}")

                print(f"  Type: {item.item_type}")

                print(f"  Brand: {item.item_brand}")

                print(f"  Shop: {item.shop}")

                print(f"  Auction: {item.auction}")

    except Exception as e:

        print(f"\n❌ ERROR: {e}")

        import traceback

        traceback.print_exc()

 

 

if __name__ == '__main__':

    asyncio.run(main())