# اتصال و مجوزهای دیجی‌کالا

## ساخت کلاینت با توکن

```python
import os

from iranian_marketplaces_sdk import DigikalaSync

with DigikalaSync(
    access_token=os.environ["DIGIKALA_ACCESS_TOKEN"],
    refresh_token=os.environ.get("DIGIKALA_REFRESH_TOKEN", ""),
) as client:
    response = client.categories.tree()
    for category in response.data.items or []:
        print(category.id, category.title)
```

`access_token` برای ساخت کلاینت لازم است. `refresh_token` اختیاری است و فقط برای تمدید توکن
استفاده می‌شود. SDK هدر `Authorization: Bearer ...` را خودش تنظیم می‌کند.

## گرفتن توکن اولیه

اگر authorization code دریافت کرده‌اید، آن را به متد کلاسی بدهید:

```python
import os

from iranian_marketplaces_sdk import DigikalaSync

tokens = DigikalaSync.create_token(os.environ["DIGIKALA_AUTHORIZATION_CODE"])
# Store tokens.data.access_token and tokens.data.refresh_token in your credential store.
```

این فراخوانی برای مبادلهٔ کد با جفت توکن است؛ قبل از آن لازم نیست یک کلاینت احرازهویت‌شده بسازید.

## تفاوت scope و دسترسی واقعی

| متد | نتیجه |
| --- | --- |
| `client.auth.list_scopes()` | فهرست scopeهای تعریف‌شده در سرویس |
| `client.auth.get_client_scopes(client_code)` | scopeهای قابل‌استفاده برای اپلیکیشن |
| اجرای یک عملیات فروشنده | بررسی مجوز توکن برای همان عملیات |

دریافت فهرست scopeها به معنی داشتن همهٔ آن مجوزها نیست. مثلاً خواندن دسته‌بندی به scope
`product` و خواندن سفارش به scope `order` مربوط است. در صورت دریافت `403`، مجوز توکن
برای همان بخش را بررسی کنید.

## تمدید توکن

در یک کلاینت فعال که refresh token دارد:

```python
fresh = client.refresh_token()
# Store both fields from fresh.data before discarding this response.
```

پس از موفقیت، درخواست‌های بعدی همان کلاینت و resourceهایش با access token جدید ارسال می‌شوند.
جفت جدید را در محل نگهداری اعتبارنامهٔ برنامه ذخیره کنید. تمدید به‌صورت خودکار انجام نمی‌شود.

در حالت async، ایجاد و تمدید توکن هم `await` می‌خواهند:
`await DigikalaAsync.create_token(code)` و `await client.refresh_token()`.

[بعدی: کالا، تنوع و سفارش ←](catalog-and-orders.md)
