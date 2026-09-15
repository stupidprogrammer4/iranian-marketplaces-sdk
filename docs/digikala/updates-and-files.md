# ویرایش داده و کار با فایل‌ها

## ابتدا بدنهٔ تغییر را بسازید

```python
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.variants import UpdateRequest

body = UpdateRequest(seller_stock=7)
print(body.to_payload())
```

خروجی `{'seller_stock': 7}` است. ساخت این مدل به‌تنهایی درخواست شبکه‌ای ندارد.
[نمونهٔ prepare_update](../../examples/digikala/prepare_update.py) همین مرحله را اجرا می‌کند.

## ارسال تغییر موجودی

وقتی شناسهٔ تنوع و مقدار جدید را انتخاب کردید، می‌توانید آن را ارسال کنید. **اجرای این نمونه
موجودی واقعی تنوع انتخاب‌شده را تغییر می‌دهد:**

```python
import os

from iranian_marketplaces_sdk import DigikalaSync
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.variants import UpdateRequest

variant_id = int(os.environ["DIGIKALA_VARIANT_ID"])
new_stock = int(os.environ["DIGIKALA_NEW_STOCK"])

with DigikalaSync(os.environ["DIGIKALA_ACCESS_TOKEN"]) as client:
    response = client.variants.update(variant_id, body=UpdateRequest(seller_stock=new_stock))
    print(response.status)
```

فقط موجودی در بدنه قرار دارد. برای عملیات دیگر، مدل request همان متد را بسازید؛ مدل `UpdateRequest`
یک بخش را به متد بخش دیگری ندهید.

## آپلود تصویر

با یک کلاینت فعال، تصویر را به این شکل آپلود کنید:

```python
from iranian_marketplaces_sdk.marketplaces.digikala import Upload

with open("product.png", "rb") as image:
    response = client.products.upload_image(
        file=Upload(filename="product.png", content=image, content_type="image/png")
    )
```

`content` می‌تواند `bytes` یا فایل بازشده در حالت باینری باشد. SDK بدنهٔ multipart را می‌سازد.
فایل را خودتان با `with` ببندید. متدهای import دیگر ممکن است شناسهٔ فایل آپلودشده را در بدنهٔ JSON
بخواهند؛ نوع ورودی را از امضای همان متد بخوانید.

## دانلود یا پاسخ بدون مدل مشخص

بعضی عملیات به‌جای مدل Pydantic، `RawResponse` برمی‌گردانند. ویژگی‌های مهم آن `content`،
`headers` و `status_code` هستند. `content` بایت‌های اصلی را نگه می‌دارد:

```python
response = client.smart_discount.sample_excel()
if "json" in response.headers.get("content-type", ""):
    payload = response.json()
    print(payload)
else:
    with open("sample.xlsx", "wb") as output:
        output.write(response.content)
```

اگر سرویس به‌جای فایل، JSON حاوی شناسهٔ کار یا آدرس دانلود بدهد، ابتدا همان JSON را بررسی کنید.
SDK فایل را خودکار ذخیره و آدرس دانلود را خودکار دنبال نمی‌کند.

در async نام‌ها و مدل‌ها یکسان‌اند؛ مثلاً `await client.products.upload_image(...)`.

[بازگشت به راهنمای دیجی‌کالا](README.md) · [مرجع متدها](../reference/digikala-endpoints.md)
