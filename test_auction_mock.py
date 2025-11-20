"""Test auction_info parsing with mock data from user's JSON example"""
import sys
from mercapi.mapping.definitions import map_to_class, mapping_definitions
from mercapi.models import Item

# Mock auction_info data from user's JSON
mock_auction_info = {
    "id": "12216407",
    "start_time": 1761121435,
    "expected_end_time": 1763724878,
    "total_bids": 0,
    "initial_price": 57800,
    "highest_bid": 57800,
    "state": "STATE_NO_BID",
    "auction_type": "AUCTION_TYPE_NORMAL"
}

# Minimal item data with auction_info
mock_item_data = {
    "id": "m67451288459",
    "status": "on_sale",
    "name": "Test Auction Item",
    "price": 57800,
    "auction_info": mock_auction_info
}

def test_auction_parsing():
    print("Testing AuctionInfo parsing with mock data\n")
    print("="*60)

    item = map_to_class(mock_item_data, Item, mapping_definitions[Item])

    print(f"\n✅ Item parsed successfully")
    print(f"   Name: {item.name}")
    print(f"   Price: ¥{item.price}")
    print(f"   Has auction_info: {item.auction_info is not None}")

    if item.auction_info:
        print(f"\n🔨 AUCTION INFORMATION:")
        print(f"   Auction ID: {item.auction_info.id_}")
        print(f"   State: {item.auction_info.state}")
        print(f"   Type: {item.auction_info.auction_type}")
        print(f"   Initial price: ¥{item.auction_info.initial_price}")
        print(f"   Highest bid: ¥{item.auction_info.highest_bid}")
        print(f"   Total bids: {item.auction_info.total_bids}")
        print(f"   Start time: {item.auction_info.start_time}")
        print(f"   Expected end time: {item.auction_info.expected_end_time}")

        # Assertions
        assert item.auction_info.id_ == "12216407"
        assert item.auction_info.state == "STATE_NO_BID"
        assert item.auction_info.auction_type == "AUCTION_TYPE_NORMAL"
        assert item.auction_info.highest_bid == 57800
        assert item.auction_info.total_bids == 0

        print(f"\n✅ All assertions passed!")
    else:
        raise AssertionError("auction_info should not be None!")

    print("\n" + "="*60)
    print("✅ AUCTION INFO PARSING WORKS CORRECTLY!")
    print("\nNote: The live API is not currently returning auction_info")
    print("for item m67451288459, but the parsing logic is ready for")
    print("when auction items are available.")

if __name__ == '__main__':
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    try:
        test_auction_parsing()
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
