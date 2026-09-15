# کالا، تنوع و سفارش

در دیجی‌کالا **کالا** اطلاعات محصول مانند عنوان و برند را دارد. **تنوع** نسخهٔ قابل‌فروش آن
برای فروشنده است که قیمت، موجودی یا ویژگی‌هایی مثل رنگ به آن مربوط می‌شوند. شناسهٔ کالا و
شناسهٔ تنوع را در متدهای مربوط به خودشان استفاده کنید.

## خواندن کالا و تنوع

```python
import os

from iranian_marketplaces_sdk import DigikalaSync
from iranian_marketplaces_sdk.marketplaces.digikala.data.api import products, variants

with DigikalaSync(os.environ["DIGIKALA_ACCESS_TOKEN"]) as client:
    catalog = client.products.list_seller(query=products.ListSellerQuery(size=5))
    for product in catalog.data.items or []:
        print("Product:", product.product_id, product.title)

    offers = client.variants.list(query=variants.ListQuery(size=5, search_active=True))
    for variant in offers.data.items or []:
        print("Variant:", variant.id, variant.title, variant.price_sale)
```

برای خواندن جزئیات یک تنوع از `client.variants.get(variant_id)` استفاده کنید.
موجودی فروشنده از `client.variants.get_seller_stock(variant_id)` و موجودی نزد دیجی‌کالا از
`client.inventories.list(...)` در دسترس است.

## خواندن سفارش‌های باز

```python
import os

from iranian_marketplaces_sdk import DigikalaSync
from iranian_marketplaces_sdk.marketplaces.digikala.data.api import orders

with DigikalaSync(os.environ["DIGIKALA_ACCESS_TOKEN"]) as client:
    response = client.orders.list(query=orders.ListQuery(page=1, size=5))
    for item in response.data.items or []:
        print(item.model_dump())
```

`orders.list()` آیتم‌های سفارش باز را برمی‌گرداند. برای سابقه از `orders.history()` و برای
آمار از `orders.statistics()` استفاده کنید. سفارش‌های ارسال مستقیم فروشنده در بخش جداگانهٔ
`seller_orders` قرار دارند.

برای مشاهدهٔ بسته‌های ارسالی به انبار از `packages.list()` استفاده کنید؛ شناسهٔ بسته با شناسهٔ
سفارش متفاوت است. مدل query هر متد، فیلترهای همان فهرست را نشان می‌دهد.

## پیدا کردن عملیات بعدی

1. بخش را انتخاب کنید: مثلاً `orders`.
2. نام متد را از [مرجع متدها](../reference/digikala-endpoints.md#orders) پیدا کنید.
3. مدل query یا body را از `data.api.orders` وارد کنید.
4. برای فهرست‌ها، اندازهٔ صفحه را مشخص و پاسخ را بررسی کنید.

**تمرین:** نمونهٔ کالاها را با `size=1` اجرا کنید، سپس با راهنمای [صفحه‌بندی](../guides/pagination.md)
صفحهٔ بعد را بخوانید.

[بعدی: ویرایش و فایل‌ها ←](updates-and-files.md)
