# ۲. مدل‌ها و فیلترها

برای فراخوانی SDK با سه نوع داده سروکار دارید:

| نوع | کاربرد | نمونه |
| --- | --- | --- |
| Query | فیلتر و صفحه‌بندی | `ListQuery(size=5)` |
| Request | بدنهٔ تغییر یا ایجاد | `UpdateRequest(seller_stock=7)` |
| Response | نتیجهٔ برگشتی | `response.data.items` |

مدل‌ها بر پایهٔ Pydantic هستند. اشتباه در نام فیلد ورودی، قبل از ارسال درخواست مشخص می‌شود.

## خواندن با فیلتر

```python
import os

from iranian_marketplaces_sdk import DigikalaSync
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.variants import ListQuery

query = ListQuery(page=1, size=5, search_active=True)

with DigikalaSync(os.environ["DIGIKALA_ACCESS_TOKEN"]) as client:
    response = client.variants.list(query=query)
    for variant in response.data.items or []:
        print(variant.id, variant.title)
```

در دیجی‌کالا مدل‌ها را از `data.api.<resource>` وارد می‌کنید. مثلاً `products.ListSellerQuery`
برای `client.products.list_seller()` است. مدل‌های اسنپ، باسلام و تپسی از `data` همان مارکت‌پلیس
وارد می‌شوند.

## نام پایتونی و نام ارسالی

`search_active` در پایتون به `search[active]` در آدرس درخواست تبدیل می‌شود.
فهرست شناسه‌ها را به شکل `list` بدهید:

```python
query = ListQuery(search_ids=[11, 22], search_category_ids=[3, 4])
```

SDK جداکنندهٔ مناسب همان مسیر را اعمال می‌کند؛ برای این متد `ids` با `_` و `category_ids`
با `,` ارسال می‌شود.

## ساخت بدنهٔ تغییر

```python
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.variants import UpdateRequest

body = UpdateRequest(seller_stock=7)
print(body.to_payload())  # {'seller_stock': 7}
```

فقط فیلدهایی که تعیین کرده‌اید ارسال می‌شوند. دادن `None` در بدنه، آن فیلد را به‌صورت JSON null
ارسال می‌کند؛ بنابراین `None` با تعیین‌نکردن فیلد فرق دارد. در query، مقادیر `None` حذف می‌شوند.

## کار با پاسخ

بعضی فیلدهای پاسخ اختیاری‌اند. قبل از استفاده از `pager` یا فیلدهای تو‌در‌تو، مقدار `None` را
بررسی کنید. `items or []` در حلقهٔ بالا، پاسخ بدون فهرست را هم پوشش می‌دهد.

برای تبدیل پاسخ به دیکشنری از `response.model_dump()` استفاده کنید. فیلدهای جدیدی که سرویس
اضافه کند در `model_extra` حفظ می‌شوند. تاریخ‌ها در قالب رشته یا مدل تاریخ خود سرویس می‌مانند.

**تمرین:** نمونهٔ آفلاین `python -m examples.digikala.prepare_update` را اجرا کنید و یک فیلد
معتبر دیگر به بدنه اضافه کنید.

[بعدی: صفحه‌بندی ←](pagination.md)
