# mercapi

![PyPI](https://img.shields.io/pypi/v/mercapi)
[![Tests](https://github.com/take-kun/mercapi/actions/workflows/check.yaml/badge.svg?branch=main)](https://github.com/take-kun/mercapi/actions/workflows/check.yaml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mercapi)

[API Documentation](https://take-kun.github.io/mercapi/)

## What is Mercapi?

Mercapi is a Python wrapper for *mercari.jp* API.
It's capable of producing HTTP requests implementing security mechanisms employed in native *mercari.jp* web app.
Requests and responses are mapped to custom classes with type-hinting and documentation.

**Features:**
- Search and browse regular Mercari listings
- Fetch detailed information for individual items
- **Full support for Mercari Shop listings** (business/commercial sellers)
- Access seller profiles and their items
- Comprehensive type hints and documentation

## Quickstart

First, install the `mercapi` package using the package manager of your choice.

As an example, we want to run the search query `sharpnel`.

```python
from mercapi import Mercapi


m = Mercapi()
results = await m.search('sharpnel')

print(f'Found {results.meta.num_found} results')
for item in results.items:
    print(f'Name: {item.name}\\nPrice: {item.price}\\n')

```

We can use a single result object to retrieve full details of the listing.
```python
item = results.items[0]
full_item = await item.full_item()

print(full_item.description)
```

Or get it directly using an ID.
```python
item = await m.item('m90925725213')

print(item.description)
```

### Mercari Shop Products

Mercari Shop listings (business/commercial sellers) are supported through the `shop_product()` method:

```python
# Get a shop product by ID
shop_product = await m.shop_product('2JHDxUxi3SsqAG5umbmWY2')

print(f'Product: {shop_product.display_name}')
print(f'Price: ¥{shop_product.price}')
print(f'Shop: {shop_product.product_detail.shop.display_name}')
print(f'Shop Rating: {shop_product.product_detail.shop.shop_stats.score}/5')

# Access promotions
for promo in shop_product.product_detail.promotions:
    print(f'Promotion: {promo.display_name}')
    print(f'Discount: ¥{promo.action.discount_amount}')
```

Shop products include additional information not available in regular listings:
- Complete shop information with ratings and reviews
- Product variants (size, color, etc.)
- Multiple promotion types (follow promotions, buyer promotions, campaigns)
- Mercard reward information
- Other products from the same shop

See [CHANGELOG_RECENT.md](CHANGELOG_RECENT.md) for comprehensive documentation on all new features including shop products, enhanced item fields, and search improvements.

Refer to `mercapi.mercapi.Mercapi` documentation for all implemented features.

*Examples above are not executable. If you want to try them out, run `python example.py`.*