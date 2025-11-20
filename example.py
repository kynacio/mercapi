import asyncio
import logging

from mercapi import Mercapi


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


async def main():
    m = Mercapi()

    # Regular listing search
    results = await m.search('sharpnel')

    print(f'Found {results.meta.num_found} results')
    for item in results.items:
        print(f'Name: {item.name}\nPrice: {item.price}\n')

    item = results.items[0]
    full_item = await item.full_item()
    print(full_item.description)

    item = await m.item('m64017471338')
    print(item.description)

    # Shop product example
    print('\n--- Shop Product Example ---')
    shop_product = await m.shop_product('2JHDxUxi3SsqAG5umbmWY2')
    if shop_product:
        print(f'Product: {shop_product.display_name}')
        print(f'Price: ¥{shop_product.price}')
        print(f'Shop: {shop_product.product_detail.shop.display_name}')
        print(f'Shop Rating: {shop_product.product_detail.shop.shop_stats.score}/5')
        print(f'Reviews: {shop_product.product_detail.shop.shop_stats.review_count}')

        if shop_product.product_detail.promotions:
            print(f'\nPromotions:')
            for promo in shop_product.product_detail.promotions:
                print(f'  - {promo.display_name}')
    else:
        print('Shop product not found')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
