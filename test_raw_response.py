import asyncio
import sys
import json
from mercapi import Mercapi

async def main():
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    api = Mercapi()

    # Make raw request
    req = api._item('m67451288459')
    res = await api._client.send(req)
    response = res.json()

    # Check if auction_info exists in response
    if 'data' in response and 'auction_info' in response['data']:
        print("✅ auction_info EXISTS in response!")
        print(f"\nAuction info:")
        print(json.dumps(response['data']['auction_info'], indent=2))
    else:
        print("❌ auction_info NOT in response")
        print(f"\nAvailable keys in data:")
        if 'data' in response:
            for key in sorted(response['data'].keys()):
                print(f"  - {key}")

if __name__ == '__main__':
    asyncio.run(main())
