# اجرای مثال‌ها

هر فایل یک نمونهٔ مستقل است. از ریشهٔ مخزن، SDK را در محیط مجازی نصب کنید:

```bash
python -m pip install -e .
```

سپس متغیرهای محیطی همان مارکت‌پلیس را تنظیم و فقط نمونهٔ موردنظر را اجرا کنید.
برای توضیح قدم‌به‌قدم به [مسیر یادگیری](../docs/README.md) بروید.

## مثال‌های آماده

| مارکت‌پلیس | sync | async |
| --- | --- | --- |
| دیجی‌کالا | `python -m examples.digikala.sync_usage` | `python -m examples.digikala.async_usage` |
| اسنپ‌شاپ | `python -m examples.snapp.sync_usage` | `python -m examples.snapp.async_usage` |
| باسلام | `python -m examples.basalam.sync_usage` | `python -m examples.basalam.async_usage` |
| تپسی‌شاپ | `python -m examples.tapsi.sync_usage` | `python -m examples.tapsi.async_usage` |

این نمونه‌ها درخواست واقعی برای خواندن اطلاعات می‌فرستند. نمونهٔ async اسنپ‌شاپ حداکثر سه
صفحهٔ سفارش را می‌خواند. نمونه‌های تپسی شمارهٔ صفحهٔ متفاوت کالا و سفارش را نشان می‌دهند.
import کردن فایل‌ها هیچ درخواست شبکه‌ای ارسال نمی‌کند.

## متغیرهای محیطی

| مارکت‌پلیس | الزامی | اختیاری |
| --- | --- | --- |
| دیجی‌کالا | `DIGIKALA_ACCESS_TOKEN` | `DIGIKALA_REFRESH_TOKEN` |
| اسنپ‌شاپ | `SNAPP_UNIQUE_CODE`, `SNAPP_ACCESS_TOKEN`, `SNAPP_SELLER_ID` | — |
| باسلام | `BASALAM_VENDOR_ID` (عدد), `BASALAM_ACCESS_TOKEN` | — |
| تپسی‌شاپ | `TAPSI_TOKEN` | — |

اگر متغیر لازم تنظیم نشده باشد، نمونه پیش از اتصال با نام همان متغیر متوقف می‌شود.
فایل `.env` به‌صورت خودکار خوانده نمی‌شود؛ متغیرها را در shell یا تنظیمات اجرای IDE وارد کنید.

## مثال‌های تکمیلی دیجی‌کالا

```bash
# Read up to three pages of variants; requires credentials.
python -m examples.digikala.pagination

# Build and print an update payload; works offline without credentials.
python -m examples.digikala.prepare_update
```

خروجی نمونهٔ دوم:

```json
{"seller_stock": 7}
```

برای تبدیل این بدنه به درخواست واقعی، [راهنمای ویرایش](../docs/digikala/updates-and-files.md)
را بخوانید.
