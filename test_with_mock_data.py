"""Test parsing with mock data matching your JSON examples"""
import sys
from mercapi.mapping.definitions import map_to_class, mapping_definitions
from mercapi.models.search import SearchResultItem

# Mock data from your JSON examples
mock_item_with_brand_and_size = {
    "id": "m39209055620",
    "sellerId": "112690196",
    "buyerId": "",
    "status": "ITEM_STATUS_ON_SALE",
    "name": "SAINT LAURENT ロゴ Tシャツ",
    "price": "13500",
    "created": "1763529622",
    "updated": "1763617642",
    "thumbnails": ["https://static.mercdn.net/thumb/item/webp/m39209055620_1.jpg?1763529622"],
    "itemType": "ITEM_TYPE_MERCARI",
    "itemConditionId": "2",
    "shippingPayerId": "2",
    "itemSizes": [{"id": "3", "name": "M"}],
    "itemBrand": {"id": "606", "name": "Saint Laurent", "subName": "Saint Laurent"},
    "itemPromotions": [],
    "shopName": "",
    "itemSize": {"id": "3", "name": "M"},
    "shippingMethodId": "14",
    "categoryId": "302",
    "isNoPrice": False,
    "title": "",
    "isLiked": False,
    "photos": [{"uri": "https://static.mercdn.net/item/detail/webp/photos/m39209055620_1.jpg?1763529622"}],
    "auction": None,
    "shop": None
}

mock_item_with_auction = {
    "id": "m40081209342",
    "sellerId": "379270463",
    "buyerId": "",
    "status": "ITEM_STATUS_ON_SALE",
    "name": "ISAMU KATAYAMA BACKLASH×WHITE FLAGS コラボ",
    "price": "15555",
    "created": "1763567438",
    "updated": "1763570756",
    "thumbnails": ["https://static.mercdn.net/thumb/item/webp/m40081209342_1.jpg?1763568020"],
    "itemType": "ITEM_TYPE_MERCARI",
    "itemConditionId": "3",
    "shippingPayerId": "2",
    "itemSizes": [{"id": "10", "name": "26.5cm"}],
    "itemBrand": {"id": "5808", "name": "ISAMUKATAYAMA BACKLASH", "subName": "ISAMUKATAYAMA BACKLASH"},
    "itemPromotions": [],
    "shopName": "",
    "itemSize": {"id": "10", "name": "26.5cm"},
    "shippingMethodId": "14",
    "categoryId": "345",
    "isNoPrice": False,
    "title": "",
    "isLiked": False,
    "photos": [{"uri": "https://static.mercdn.net/item/detail/webp/photos/m40081209342_1.jpg?1763568020"}],
    "auction": {
        "id": "",
        "bidDeadline": "2025-11-21T11:33:30.602704221Z",
        "totalBid": "0",
        "highestBid": "15555"
    },
    "shop": None
}

mock_item_with_shop = {
    "id": "2JGtpGVLCmtyCah9YzffbX",
    "sellerId": "0",
    "buyerId": "",
    "status": "ITEM_STATUS_ON_SALE",
    "name": "ISAMU KATAYAMA BACKLASH (イサムカタヤマバックラッシュ) リネンキャスケット 帽子 ブラック 874-01",
    "price": "9790",
    "created": "1762996585",
    "updated": "1762996585",
    "thumbnails": ["https://assets.mercari-shops-static.com/-/small/plain/2JGtpGTFaCFwJUgXDkyVtB.jpg@webp"],
    "itemType": "ITEM_TYPE_BEYOND",
    "itemConditionId": "5",
    "shippingPayerId": "0",
    "itemSizes": [],
    "itemBrand": {"id": "5808", "name": "ISAMUKATAYAMA BACKLASH", "subName": "ISAMUKATAYAMA BACKLASH"},
    "itemPromotions": [],
    "shopName": "",
    "itemSize": None,
    "shippingMethodId": "0",
    "categoryId": "369",
    "isNoPrice": False,
    "title": "",
    "isLiked": False,
    "photos": [{"uri": "https://assets.mercari-shops-static.com/-/large/plain/2JGtpGTFaCFwJUgXDkyVtB.jpg@webp"}],
    "auction": None,
    "shop": {"id": "aXQx7LKu3us59Yo7fQmwsk"}
}

def test_parsing():
    print("Testing SearchResultItem parsing with mock data\n")
    print("="*60)

    # Test 1: Item with brand and size
    print("\n1. Testing item WITH brand and size:")
    item1 = map_to_class(mock_item_with_brand_and_size, SearchResultItem, mapping_definitions[SearchResultItem])
    print(f"   ✅ Parsed successfully")
    print(f"   Name: {item1.name}")
    print(f"   Brand: {item1.item_brand.name if item1.item_brand else 'None'}")
    print(f"   Size: {item1.item_size.name if item1.item_size else 'None'}")
    print(f"   Sizes list: {[s.name for s in item1.item_sizes] if item1.item_sizes else []}")
    assert item1.item_brand is not None, "Brand should not be None!"
    assert item1.item_brand.name == "Saint Laurent", f"Brand name mismatch: {item1.item_brand.name}"
    assert item1.item_size is not None, "Size should not be None!"
    assert item1.item_size.name == "M", f"Size mismatch: {item1.item_size.name}"
    assert len(item1.item_sizes) == 1, f"Sizes list length mismatch: {len(item1.item_sizes)}"

    # Test 2: Item with auction
    print("\n2. Testing item WITH auction:")
    item2 = map_to_class(mock_item_with_auction, SearchResultItem, mapping_definitions[SearchResultItem])
    print(f"   ✅ Parsed successfully")
    print(f"   Name: {item2.name}")
    print(f"   Auction: {item2.auction}")
    if item2.auction:
        print(f"   Highest bid: ¥{item2.auction.highest_bid}")
        print(f"   Deadline: {item2.auction.bid_deadline}")
    assert item2.auction is not None, "Auction should not be None!"
    assert item2.auction.highest_bid == "15555", f"Auction bid mismatch: {item2.auction.highest_bid}"

    # Test 3: Item with shop
    print("\n3. Testing item WITH shop:")
    item3 = map_to_class(mock_item_with_shop, SearchResultItem, mapping_definitions[SearchResultItem])
    print(f"   ✅ Parsed successfully")
    print(f"   Name: {item3.name}")
    print(f"   Shop: {item3.shop}")
    if item3.shop:
        print(f"   Shop ID: {item3.shop.id_}")
    assert item3.shop is not None, "Shop should not be None!"
    assert item3.shop.id_ == "aXQx7LKu3us59Yo7fQmwsk", f"Shop ID mismatch: {item3.shop.id_}"

    # Test 4: Brand with snake_case (item details endpoint format)
    print("\n4. Testing brand with snake_case (item details endpoint):")
    mock_brand_snake_case = {
        "id": "7664",
        "name": "blackmeans",
        "sub_name": "blackmeans"  # snake_case instead of camelCase
    }
    from mercapi.models.item.data import ItemBrand
    brand = map_to_class(mock_brand_snake_case, ItemBrand, mapping_definitions[ItemBrand])
    print(f"   ✅ Parsed successfully")
    print(f"   Name: {brand.name}")
    print(f"   Sub-name: {brand.sub_name}")
    assert brand.name == "blackmeans", f"Brand name mismatch: {brand.name}"
    assert brand.sub_name == "blackmeans", f"Brand sub_name mismatch: {brand.sub_name}"

    print("\n" + "="*60)
    print("✅ ALL TESTS PASSED!")
    print("\nThis confirms the parsing logic correctly handles:")
    print("  - camelCase format (search endpoint)")
    print("  - snake_case format (item details endpoint)")
    print("\nThe live API may be returning null for some fields currently.")

if __name__ == '__main__':
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    try:
        test_parsing()
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
