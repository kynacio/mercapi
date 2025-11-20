"""
Comprehensive test for Mercari search API responses.
Tests all possible field combinations including:
- Regular Mercari items (ITEM_TYPE_MERCARI)
- Shop items (ITEM_TYPE_BEYOND)
- Items with auctions
- Items with/without brands
- Items with/without sizes
- Null value handling
"""
import asyncio
import sys
from mercapi import Mercapi


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f" {title}")
    print('='*60)


def validate_item_fields(item, item_data):
    """Validate that all expected fields are correctly parsed."""
    errors = []

    # Required fields
    if item.id_ != item_data['id']:
        errors.append(f"ID mismatch: {item.id_} != {item_data['id']}")
    if item.name != item_data['name']:
        errors.append(f"Name mismatch")
    if str(item.price) != str(item_data['price']):
        errors.append(f"Price mismatch: {item.price} != {item_data['price']}")

    # Optional fields with null handling
    if item_data.get('itemBrand') is not None:
        if item.item_brand is None:
            errors.append(f"Brand should not be None")
        elif item.item_brand.id_ != item_data['itemBrand']['id']:
            errors.append(f"Brand ID mismatch")
    else:
        if item.item_brand is not None:
            errors.append(f"Brand should be None but got {item.item_brand}")

    # Item size handling
    if item_data.get('itemSize') is not None:
        if item.item_size is None:
            errors.append(f"Item size should not be None")
        elif item.item_size.id_ != item_data['itemSize']['id']:
            errors.append(f"Item size ID mismatch")
    else:
        if item.item_size is not None:
            errors.append(f"Item size should be None but got {item.item_size}")

    # Item sizes list handling
    if item_data.get('itemSizes'):
        if not item.item_sizes:
            errors.append(f"Item sizes should not be empty")
        elif len(item.item_sizes) != len(item_data['itemSizes']):
            errors.append(f"Item sizes count mismatch: {len(item.item_sizes)} != {len(item_data['itemSizes'])}")
    else:
        if item.item_sizes:
            errors.append(f"Item sizes should be empty/None")

    # Auction handling
    if item_data.get('auction') is not None:
        if item.auction is None:
            errors.append(f"Auction should not be None")
        else:
            # Validate auction fields
            auction_data = item_data['auction']
            if auction_data.get('bidDeadline') and item.auction.bid_deadline != auction_data['bidDeadline']:
                errors.append(f"Auction bid_deadline mismatch")
            if auction_data.get('highestBid') and item.auction.highest_bid != auction_data['highestBid']:
                errors.append(f"Auction highest_bid mismatch")
    else:
        if item.auction is not None:
            errors.append(f"Auction should be None but got {item.auction}")

    # Shop handling
    if item_data.get('shop') is not None:
        if item.shop is None:
            errors.append(f"Shop should not be None")
        elif item.shop.id_ != item_data['shop']['id']:
            errors.append(f"Shop ID mismatch: {item.shop.id_} != {item_data['shop']['id']}")
    else:
        if item.shop is not None:
            errors.append(f"Shop should be None but got {item.shop}")

    # Photos handling
    if item_data.get('photos'):
        if not item.photos:
            errors.append(f"Photos should not be empty")
        elif len(item.photos) != len(item_data['photos']):
            errors.append(f"Photos count mismatch")

    return errors


async def test_search_variations():
    """Test various search queries to cover different field combinations."""
    api = Mercapi()

    test_queries = [
        ('Adidas', 'BACKLASH items - tests brands, sizes, auctions, shops'),
    ]

    all_stats = {
        'total_items': 0,
        'items_with_brand': 0,
        'items_without_brand': 0,
        'items_with_size': 0,
        'items_without_size': 0,
        'items_with_sizes_list': 0,
        'items_with_auction': 0,
        'items_with_shop': 0,
        'mercari_type_items': 0,
        'beyond_type_items': 0,
        'validation_errors': []
    }

    for query, description in test_queries:
        print_section(f"Testing: {query}")
        print(f"Description: {description}\n")

        try:
            results = await api.search(query)

            print(f"Found: {results.meta.num_found} items")
            print(f"Retrieved: {len(results.items)} items")

            # Analyze first page of results
            for idx, item in enumerate(results.items[:120], 1):
                all_stats['total_items'] += 1

                # Item type
                if item.item_type and 'MERCARI' in str(item.item_type):
                    all_stats['mercari_type_items'] += 1
                elif item.item_type and 'BEYOND' in str(item.item_type):
                    all_stats['beyond_type_items'] += 1

                # Brand stats
                if item.item_brand:
                    all_stats['items_with_brand'] += 1
                else:
                    all_stats['items_without_brand'] += 1

                # Size stats
                if item.item_size:
                    all_stats['items_with_size'] += 1
                else:
                    all_stats['items_without_size'] += 1

                if item.item_sizes:
                    all_stats['items_with_sizes_list'] += 1

                # Auction stats
                if item.auction:
                    all_stats['items_with_auction'] += 1
                    print(f"  [{idx}] 🔨 AUCTION: {item.name[:50]}...")
                    print(f"      Deadline: {item.auction.bid_deadline}")
                    print(f"      Highest bid: ¥{item.auction.highest_bid}")

                # Shop stats
                if item.shop:
                    all_stats['items_with_shop'] += 1
                    print(f"  [{idx}] 🏪 SHOP: {item.name[:50]}...")
                    print(f"      Shop ID: {item.shop.id_}")

                # Print item details for first few items
                if idx <= 3:
                    print(f"  [{idx}] {item.name[:60]}")
                    print(f"      Price: ¥{item.price}")
                    print(f"      Brand: {item.item_brand.name if item.item_brand else 'None'}")
                    print(f"      Size: {item.item_size.name if item.item_size else 'None'}")
                    print(f"      Sizes: {[s.name for s in item.item_sizes] if item.item_sizes else '[]'}")
                    print(f"      Photos: {len(item.photos) if item.photos else 0}")
                    print(f"      Auction: {'Yes' if item.auction else 'No'}")
                    print(f"      Shop: {'Yes' if item.shop else 'No'}")

            print()

        except Exception as e:
            print(f"ERROR: {e}")
            import traceback
            traceback.print_exc()

    # Print summary statistics
    print_section("SUMMARY STATISTICS")
    print(f"Total items analyzed: {all_stats['total_items']}")
    print(f"\nItem Types:")
    print(f"  - Regular Mercari items: {all_stats['mercari_type_items']}")
    print(f"  - Beyond/Shop items: {all_stats['beyond_type_items']}")
    print(f"\nBrand Coverage:")
    print(f"  - Items WITH brand: {all_stats['items_with_brand']}")
    print(f"  - Items WITHOUT brand (null): {all_stats['items_without_brand']}")
    print(f"\nSize Coverage:")
    print(f"  - Items WITH itemSize: {all_stats['items_with_size']}")
    print(f"  - Items WITHOUT itemSize (null): {all_stats['items_without_size']}")
    print(f"  - Items WITH itemSizes list: {all_stats['items_with_sizes_list']}")
    print(f"\nSpecial Features:")
    print(f"  - Items WITH auction: {all_stats['items_with_auction']}")
    print(f"  - Items WITH shop: {all_stats['items_with_shop']}")

    if all_stats['validation_errors']:
        print_section("VALIDATION ERRORS")
        for error in all_stats['validation_errors']:
            print(f"  ❌ {error}")
    else:
        print_section("✅ ALL VALIDATIONS PASSED")

    # Coverage report
    print_section("COVERAGE REPORT")
    coverage_items = [
        ("Null brand handling", all_stats['items_without_brand'] > 0),
        ("Non-null brand handling", all_stats['items_with_brand'] > 0),
        ("Null itemSize handling", all_stats['items_without_size'] > 0),
        ("Non-null itemSize handling", all_stats['items_with_size'] > 0),
        ("Empty itemSizes list", all_stats['items_without_size'] > 0),
        ("Non-empty itemSizes list", all_stats['items_with_sizes_list'] > 0),
        ("Auction items", all_stats['items_with_auction'] > 0),
        ("Shop items", all_stats['items_with_shop'] > 0),
        ("Regular items (no auction/shop)", (all_stats['total_items'] - all_stats['items_with_auction'] - all_stats['items_with_shop']) > 0),
    ]

    for feature, covered in coverage_items:
        status = "✅" if covered else "⚠️"
        print(f"  {status} {feature}")

    print()


async def test_field_access():
    """Test accessing all possible fields without errors."""
    print_section("FIELD ACCESS TEST")

    api = Mercapi()
    results = await api.search('isamu katayama backlash')

    if not results.items:
        print("No items found for testing")
        return

    item = results.items[0]

    print("Testing field access (should not raise exceptions):\n")

    fields_to_test = [
        ('id_', lambda: item.id_),
        ('name', lambda: item.name),
        ('price', lambda: item.price),
        ('status', lambda: item.status),
        ('seller_id', lambda: item.seller_id),
        ('created', lambda: item.created),
        ('updated', lambda: item.updated),
        ('thumbnails', lambda: item.thumbnails),
        ('item_type', lambda: item.item_type),
        ('item_condition_id', lambda: item.item_condition_id),
        ('shipping_payer_id', lambda: item.shipping_payer_id),
        ('shipping_method_id', lambda: item.shipping_method_id),
        ('category_id', lambda: item.category_id),
        ('is_no_price', lambda: item.is_no_price),
        ('title', lambda: item.title),
        ('is_liked', lambda: item.is_liked),
        ('buyer_id', lambda: item.buyer_id),
        ('shop_name', lambda: item.shop_name),
        ('item_brand', lambda: item.item_brand),
        ('item_size', lambda: item.item_size),
        ('item_sizes', lambda: item.item_sizes),
        ('item_promotions', lambda: item.item_promotions),
        ('photos', lambda: item.photos),
        ('auction', lambda: item.auction),
        ('shop', lambda: item.shop),
    ]

    for field_name, accessor in fields_to_test:
        try:
            value = accessor()
            value_str = str(value)[:50] if value is not None else 'None'
            print(f"  ✅ {field_name:25} = {value_str}")
        except Exception as e:
            print(f"  ❌ {field_name:25} - ERROR: {e}")

    # Test nested fields
    print("\nTesting nested fields:")

    if item.item_brand:
        print(f"  ✅ item_brand.id_ = {item.item_brand.id_}")
        print(f"  ✅ item_brand.name = {item.item_brand.name}")
        print(f"  ✅ item_brand.sub_name = {item.item_brand.sub_name}")
    else:
        print(f"  ⚠️  item_brand is None (this is valid)")

    if item.item_size:
        print(f"  ✅ item_size.id_ = {item.item_size.id_}")
        print(f"  ✅ item_size.name = {item.item_size.name}")
    else:
        print(f"  ⚠️  item_size is None (this is valid)")

    if item.auction:
        print(f"  ✅ auction.id_ = {item.auction.id_}")
        print(f"  ✅ auction.bid_deadline = {item.auction.bid_deadline}")
        print(f"  ✅ auction.total_bid = {item.auction.total_bid}")
        print(f"  ✅ auction.highest_bid = {item.auction.highest_bid}")
    else:
        print(f"  ⚠️  auction is None (this is valid)")

    if item.shop:
        print(f"  ✅ shop.id_ = {item.shop.id_}")
        print(f"  ✅ shop.display_name = {item.shop.display_name}")
        print(f"  ✅ shop.thumbnail = {item.shop.thumbnail}")
    else:
        print(f"  ⚠️  shop is None (this is valid)")

    if item.photos:
        print(f"  ✅ photos[0].uri = {item.photos[0].uri[:50]}...")

    print()


async def main():
    """Run all tests."""
    # Set UTF-8 encoding for console output (Windows compatibility)
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    print_section("COMPREHENSIVE MERCARI SEARCH TEST")
    print("Testing all possible JSON field combinations")
    print("This validates proper handling of:")
    print("  - Required vs optional fields")
    print("  - Null value handling")
    print("  - Auction items")
    print("  - Shop items")
    print("  - Items with/without brands, sizes, etc.")

    await test_field_access()
    await test_search_variations()

    print_section("TEST COMPLETE")


if __name__ == '__main__':
    asyncio.run(main())
