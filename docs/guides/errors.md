# ۵. مدیریت خطاها

SDK خطاهای اتصال و HTTP مارکت‌پلیس‌ها را به یک خانوادهٔ مشترک تبدیل می‌کند.

| خطا | معنی | اقدام معمول |
| --- | --- | --- |
| `ConfigurationError` | تنظیمات ضروری کلاینت ناقص است | ورودی سازنده را اصلاح کنید. |
| `AuthenticationError` | پاسخ ۴۰۱ یا ۴۰۳ | اعتبار توکن و مجوز همان عملیات را بررسی کنید. |
| `NotFoundError` | پاسخ ۴۰۴ | شناسه و مسیر عملیات را بررسی کنید. |
| `RateLimitError` | پاسخ ۴۲۹ | نرخ درخواست را کاهش دهید و زمان تلاش بعدی را تنظیم کنید. |
| `ServerError` | پاسخ ۵xx | وضعیت سرویس را بررسی و دربارهٔ تلاش مجدد تصمیم بگیرید. |
| `NetworkError` | قطع ارتباط یا timeout | اتصال شبکه و timeout را بررسی کنید. |
| `ResponseValidationError` | پاسخ با مدل موردانتظار سازگار نیست | ساختار پاسخ را بررسی کنید. |

همهٔ این خطاها از `MarketplaceError` ارث می‌برند. `ValidationError` پایدنتیک برای ورودی نامعتبر
قبل از ارسال درخواست رخ می‌دهد و باید جداگانه مدیریت شود.

```python
import os

from iranian_marketplaces_sdk import (
    AuthenticationError,
    DigikalaSync,
    MarketplaceError,
    RateLimitError,
    ResponseValidationError,
)

with DigikalaSync(os.environ["DIGIKALA_ACCESS_TOKEN"], timeout=20) as client:
    try:
        response = client.orders.statistics()
        print(response.status)
    except AuthenticationError as exc:
        print("Check access token and order scope:", exc.status_code)
    except RateLimitError as exc:
        print("Try later; suggested delay in seconds:", exc.retry_after)
    except ResponseValidationError as exc:
        print("Unexpected response shape for:", exc.model)
    except MarketplaceError as exc:
        print("Request failed:", type(exc).__name__)
```

`retry_after` ممکن است `None` باشد. SDK به‌صورت خودکار درخواست را تکرار یا توکن را تمدید
نمی‌کند. برای یک عملیات تغییردهنده، timeout به‌تنهایی مشخص نمی‌کند که تغییر در سرور انجام
شده است یا نه؛ قبل از تکرار، نتیجهٔ عملیات را بررسی کنید.

در `ResponseValidationError`، ویژگی `raw` پاسخ اصلی و `errors` جزئیات ناسازگاری را نگه می‌دارد.
اگر آن‌ها را برای عیب‌یابی ذخیره می‌کنید، فقط دادهٔ لازم را ثبت کنید؛ پاسخ ممکن است اطلاعات فروشگاه داشته باشد.

**قدم بعد:** [راهنمای مارکت‌پلیس خود را انتخاب کنید](../README.md).
