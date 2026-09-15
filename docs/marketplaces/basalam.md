# باسلام

برای ساخت کلاینت، `vendor_id` را به‌صورت عدد و `access_token` را به‌صورت رشته بدهید.

## محصولات و مرسوله‌ها

```python
import os

from iranian_marketplaces_sdk import BasalamSync
from iranian_marketplaces_sdk.marketplaces.basalam.data import VendorProductsQuery

with BasalamSync(
    vendor_id=int(os.environ["BASALAM_VENDOR_ID"]),
    access_token=os.environ["BASALAM_ACCESS_TOKEN"],
) as client:
    products = client.list_vendor_products(query=VendorProductsQuery(per_page=5, stock_gte=1))
    for product in products.data or []:
        print(product.id, product.title, product.inventory)

    parcels = client.list_vendor_parcels()
    print("Parcels:", len(parcels.data))
```

مرسوله مجموعهٔ آیتم‌هایی است که فروشنده ارسال می‌کند. برای صفحه‌های بعد از
`VendorParcelsQuery` و مقدار `next_cursor` پاسخ استفاده کنید.

## تغییرات و تخفیف

`batch_update_vendor_products()` برای تغییر گروهی محصول است. برای ایجاد یا حذف تخفیف، از
`create_vendor_discount()` و `delete_vendor_discount()` با مدل request متناظر استفاده کنید.

در درخواست تخفیف، `product_filter` مشخص می‌کند کدام محصولات انتخاب شوند. مقدار `None` به معنی
انتخاب تمام محصولات است. برای محدودکردن انتخاب، مثلاً شناسه‌های مشخص را در `ProductFilterSchema`
قرار دهید:

```python
from iranian_marketplaces_sdk.marketplaces.basalam.data import ProductFilterSchema

selection = ProductFilterSchema(product_ids=[101, 102])
```

ساخت فیلتر درخواست شبکه‌ای ارسال نمی‌کند؛ ارسال متد تخفیف، فروشگاه را تغییر می‌دهد.

## تمرین

```bash
python -m examples.basalam.sync_usage
python -m examples.basalam.async_usage
```

[نمونه‌ها](../../examples/basalam) · [مدل‌ها](../guides/models-and-queries.md)
