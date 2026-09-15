# اسنپ‌شاپ

پیش‌نیاز: [نصب SDK](../getting-started.md). سه مقدار برای ساخت کلاینت لازم است:
`unique_code`، `access_token` و `seller_id`.

## محصولات و سفارش‌ها

```python
import os

from iranian_marketplaces_sdk import SnappSync
from iranian_marketplaces_sdk.marketplaces.snapp.data import VendorOrdersQuery, VendorProductsQuery

with SnappSync(
    unique_code=os.environ["SNAPP_UNIQUE_CODE"],
    access_token=os.environ["SNAPP_ACCESS_TOKEN"],
    seller_id=os.environ["SNAPP_SELLER_ID"],
) as client:
    products = client.list_products(query=VendorProductsQuery(per_page=5))
    for product in products.data:
        print(product.sku, product.price, product.stock)

    orders = client.list_orders(query=VendorOrdersQuery(per_page=5))
    if orders.data:
        detail = client.get_order(orders.data[0].order_number)
        print(detail.data.order_status)
```

محصولات با `offset` و سفارش‌ها با `cursor` صفحه‌بندی می‌شوند. در سفارش‌ها از
`orders.meta.pagination.next_cursor` برای درخواست بعدی استفاده کنید.

## تغییر محصولات

مدل هر تغییر `ProductUpdate` است و متد `update_products()` یک فهرست از تغییرات می‌گیرد.
قبل از ارسال، فیلدها و خروجی `to_payload()` را بررسی کنید. این متد اطلاعات واقعی فروشگاه را تغییر می‌دهد.

## تمرین

```bash
python -m examples.snapp.sync_usage
python -m examples.snapp.async_usage
```

نمونهٔ async حداکثر سه صفحهٔ سفارش را با cursor می‌خواند. فایل‌ها در
[examples/snapp](../../examples/snapp) قرار دارند.

[صفحه‌بندی](../guides/pagination.md) · [مدیریت خطاها](../guides/errors.md)
