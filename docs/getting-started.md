# ۱. نصب و اولین درخواست

در این درس یک کلاینت دیجی‌کالا می‌سازید و وضعیت سرویس را می‌خوانید. برای مارکت‌پلیس‌های دیگر،
بعد از نصب به [راهنمای مخصوص آن‌ها](README.md) بروید.

## نصب

پایتون ۳.۱۳ یا جدیدتر لازم است. برای استفاده از نمونه‌ها و قابلیت‌های همین شاخه:

```bash
git clone https://github.com/stupidprogrammer4/iranian-marketplaces-sdk.git
cd iranian-marketplaces-sdk
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

در ویندوز محیط مجازی را با `.venv\Scripts\Activate.ps1` فعال کنید.
برای نصب نسخهٔ منتشرشده به‌جای نسخهٔ مخزن، دستور `pip install iranian-marketplaces-sdk`
را اجرا کنید؛ قابلیت‌ها باید با نسخه‌ای که نصب کرده‌اید مطابقت داشته باشند.

## تنظیم توکن

توکن فروشنده را در متغیر محیطی `DIGIKALA_ACCESS_TOKEN` قرار دهید. مثال Bash برای ورود تعاملی:

```bash
read -rsp 'Digikala access token: ' DIGIKALA_ACCESS_TOKEN
export DIGIKALA_ACCESS_TOKEN
```

در IDE می‌توانید همین نام را در قسمت Environment Variables تنظیمات اجرای برنامه وارد کنید.
SDK فایل `.env` را به‌صورت خودکار بارگذاری نمی‌کند.

## اولین برنامه

```python
import os

from iranian_marketplaces_sdk import DigikalaSync

with DigikalaSync(os.environ["DIGIKALA_ACCESS_TOKEN"]) as client:
    response = client.health_check()
    print(response.status)
    print(response.data.mode)
```

`client` اتصال شما به سرویس است. `with` اتصال را هنگام خروج از بلوک می‌بندد، حتی اگر درخواست
خطا بدهد. پاسخ یک مدل پایتونی است؛ با `response.data.mode` به فیلد آن دسترسی دارید.

اگر پاسخ موفق باشد، `status` مقدار `ok` دارد. health در دسترس‌بودن سرویس را نشان می‌دهد؛
برای اطمینان از مجوز خواندن داده‌های فروشگاه، در گام بعد یک متد مربوط به فروشنده را اجرا کنید.

## اجرای نمونهٔ کامل

```bash
python -m examples.digikala.sync_usage
```

این نمونه وضعیت سرویس، فهرست scopeها و اولین صفحهٔ تنوع‌ها را می‌خواند. اگر با `403` مواجه
شدید، [راهنمای مجوزها](digikala/authentication.md) را ببینید.

**تمرین:** فایل [نمونهٔ sync](../examples/digikala/sync_usage.py) را باز کنید و مقدار `size`
را به `1` تغییر دهید.

[بعدی: مدل‌ها و فیلترها ←](guides/models-and-queries.md)
