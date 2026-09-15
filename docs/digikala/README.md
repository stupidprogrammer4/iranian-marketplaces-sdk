# یادگیری دیجی‌کالا

در دیجی‌کالا هر بخش یک resource دارد؛ مثلاً `client.products` برای کالا و `client.orders`
برای سفارش. مدل ورودی همان بخش را از `data.api` وارد می‌کنید و پاسخ را به شکل مدل دریافت می‌کنید.

پیش‌نیاز: [اولین درخواست](../getting-started.md) و [مدل‌ها و فیلترها](../guides/models-and-queries.md).

## مسیر پیشنهادی

| مرحله | چه کاری انجام می‌دهید؟ |
| --- | --- |
| [۱. اتصال و مجوزها](authentication.md) | کلاینت می‌سازید و تفاوت توکن، scope و تمدید توکن را یاد می‌گیرید. |
| [۲. کالا، تنوع و سفارش](catalog-and-orders.md) | کالاها و موجودی قابل‌فروش را می‌خوانید و سفارش‌ها را دریافت می‌کنید. |
| [۳. ویرایش و فایل‌ها](updates-and-files.md) | درخواست تغییر می‌سازید، فایل آپلود می‌کنید و پاسخ دانلود را مدیریت می‌کنید. |

## انتخاب بخش مناسب

| نیاز | resource |
| --- | --- |
| ساخت و خواندن کالا | `products`, `categories`, `themes` |
| قیمت و موجودی تنوع | `variants`, `variant_creation`, `inventories` |
| سفارش و تعهد ارسال | `orders`, `commitments` |
| بسته و تحویل به دیجی‌کالا | `packages`, `shipments` |
| ارسال مستقیم فروشنده | `seller_orders`, `seller_shipping`, `shipping_services` |
| تخفیف و کمپین | `smart_discount`, `promotions`, `vouchers`, `plp` |
| صورتحساب و تسویه | `invoices`, `finance` |
| تبلیغات و گزارش | `search_ads`, `search_ads_v2`, `insight` |
| حساب و رویدادها | `profile`, `webhooks`, `questions` |

بعد از یادگیری روش فراخوانی، [مرجع متدها](../reference/digikala-endpoints.md) کمک می‌کند
عملیات دقیق هر بخش را پیدا کنید.

## اجرای نمونه‌ها

از ریشهٔ مخزن و بعد از تنظیم `DIGIKALA_ACCESS_TOKEN`:

```bash
python -m examples.digikala.sync_usage
python -m examples.digikala.async_usage
python -m examples.digikala.pagination
```

برای دیدن بدنهٔ تغییر موجودی، بدون اتصال به فروشگاه:

```bash
python -m examples.digikala.prepare_update
```

## استفاده‌کنندگان نسخهٔ قبلی

متدهای قبلی و مدل‌هایشان همچنان کار می‌کنند. برای مهاجرت، متد و مدل ورودی را با هم عوض کنید:

```python
from iranian_marketplaces_sdk.marketplaces.digikala.data import VariantSearch
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.variants import ListQuery

# Existing API, inside an active client context:
old_page = client.list_variants(search=VariantSearch(ids=[11, 22]))

# Resource API:
new_page = client.variants.list(query=ListQuery(search_ids=[11, 22]))
```

[شروع فصل اول: اتصال و مجوزها ←](authentication.md)
