"""Test to check what's being parsed"""

import asyncio

import sys

import json

from mercapi import Mercapi

 

 

async def main():

    if sys.platform == 'win32':

        sys.stdout.reconfigure(encoding='utf-8')

 

    api = Mercapi()

 

    # Patch to see raw data

    from mercapi.mapping import map_to_class

    from mercapi.models.search import SearchResults

    original_impl = api._search_impl

 

    async def patched_impl(request):

        res = await api._client.send(api._search(request))

        body = res.json()

 

        # Print first item raw data

        if 'items' in body and len(body['items']) > 0:

            first_item = body['items'][0]

            print("="*80)

            print("RAW FIRST ITEM DATA:")

            print("="*80)

            print(json.dumps(first_item, indent=2, ensure_ascii=False)[:1000])

 

        # Continue with normal mapping

        result = map_to_class(body, SearchResults)

        result._request = request

        return result

 

    api._search_impl = patched_impl

 

    print("\nFetching search results...\n")

    results = await api.search('isamu katayama backlash')

 

    print("\n" + "="*80)

    print("PARSED FIRST ITEM:")

    print("="*80)

    if results.items:

        item = results.items[0]

        print(f"id_: {item.id_}")

        print(f"name: {item.name}")

        print(f"price: {item.price}")

        print(f"item_type: {item.item_type}")

        print(f"seller_id: {item.seller_id}")

        print(f"status: {item.status}")

        print(f"item_brand: {item.item_brand}")

        print(f"item_size: {item.item_size}")

        print(f"item_sizes: {item.item_sizes}")

        print(f"shop: {item.shop}")

        print(f"auction: {item.auction}")

        print(f"photos: {len(item.photos) if item.photos else 0}")

 

 

if __name__ == '__main__':

    asyncio.run(main())