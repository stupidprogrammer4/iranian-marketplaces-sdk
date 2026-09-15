# ۳. خواندن چند صفحه

هر فراخوانی فقط همان صفحه‌ای را می‌خواند که خواسته‌اید. برای ادامه باید شمارهٔ صفحه، offset
یا cursor بعدی را خودتان به درخواست بعدی بدهید.

## دیجی‌کالا: page و size

```python
import os

from iranian_marketplaces_sdk import DigikalaSync
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.variants import ListQuery

with DigikalaSync(os.environ["DIGIKALA_ACCESS_TOKEN"]) as client:
    for page_number in range(1, 4):
        response = client.variants.list(query=ListQuery(page=page_number, size=5))
        items = response.data.items or []
        for variant in items:
            print(variant.id, variant.title)

        pager = response.data.pager
        if not items or pager is None or pager.total_pages is None:
            break
        if page_number >= pager.total_pages:
            break
```

این نمونه حداکثر سه صفحه می‌خواند و با تمام‌شدن داده زودتر متوقف می‌شود.
[فایل قابل‌اجرا](../../examples/digikala/pagination.py) همین روند را نشان می‌دهد.

## اسنپ‌شاپ: cursor سفارش‌ها

`meta.pagination.next_cursor` را بدون تغییر به مدل `VendorOrdersQuery` درخواست بعدی بدهید.
وقتی `has_more` نادرست است یا cursor بعدی وجود ندارد، حلقه تمام شده است.
نمونهٔ کامل در [اسنپ async](../../examples/snapp/async_usage.py) قرار دارد.

## تفاوت مارکت‌پلیس‌ها

| داده | ورودی صفحه‌بندی |
| --- | --- |
| دیجی‌کالا، فهرست‌ها | `page` و `size`، از صفحهٔ ۱ |
| اسنپ، محصولات | `offset` و `per_page` |
| اسنپ، سفارش‌ها | `cursor` و `per_page` |
| باسلام، محصولات | `page` و `per_page` |
| باسلام، مرسوله‌ها | `cursor` و `per_page` |
| تپسی، محصولات | آرگومان‌های `page` و `page_size`، صفحهٔ اول ۱ |
| تپسی، سفارش‌ها | `OrdersQuery(page_number=0, page_size=...)`، صفحهٔ اول ۰ |

**تمرین:** تعداد صفحه‌های نمونهٔ دیجی‌کالا را به دو محدود کنید. شرط توقف بر اساس `pager` را
نگه دارید تا فروشگاه کم‌داده درخواست اضافی دریافت نکند.

[بعدی: کار با async ←](async.md)
