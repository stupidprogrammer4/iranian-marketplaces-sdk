# تپسی‌شاپ

برای ساخت کلاینت، مقدار `token` لازم است. نام و نسخهٔ کلاینت را هم می‌توانید با پارامترهای
اختیاری `client_name` و `client_version` مشخص کنید.

## محصولات و سفارش‌ها

```python
import os

from iranian_marketplaces_sdk import TapsiSync
from iranian_marketplaces_sdk.marketplaces.tapsi.data import OrdersQuery

with TapsiSync(token=os.environ["TAPSI_TOKEN"]) as client:
    products = client.get_products(page=1, page_size=5)
    for product in products.data.items:
        print(product.sku, product.final_price, product.on_hand_quantity)

    orders = client.list_orders(query=OrdersQuery(page_number=0, page_size=5))
    print("Orders:", orders.data.total_items)
```

صفحهٔ اول محصولات **۱** و صفحهٔ اول سفارش‌ها **۰** است. تفاوت نام فیلدها را هم رعایت کنید:
متد محصول `page` می‌گیرد، اما مدل سفارش `page_number` دارد.

## نتیجهٔ تغییر گروهی

برای تغییر محصول، مدل `ProductUpdate` را از `marketplaces.tapsi.data` وارد کنید و فهرست تغییرات
را به `client.update_products(...)` بدهید. این عملیات اطلاعات فروشگاه را تغییر می‌دهد.
در پاسخ، علاوه بر `success` و `data.status`، وضعیت تک‌تک آیتم‌های `data.data` را بررسی کنید.

## تمرین

```bash
python -m examples.tapsi.sync_usage
python -m examples.tapsi.async_usage
```

[نمونه‌ها](../../examples/tapsi) · [کار با async](../guides/async.md)
