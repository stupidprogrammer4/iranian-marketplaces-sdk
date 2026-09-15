# ۴. کار با async

اگر برنامهٔ شما از `asyncio` یا یک فریم‌ورک async استفاده می‌کند، کلاینت `Async` همان
مارکت‌پلیس را انتخاب کنید. نام متدها و مدل‌ها با کلاینت sync یکسان است.

```python
import asyncio
import os

from iranian_marketplaces_sdk import DigikalaAsync
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.orders import ListQuery


async def main() -> None:
    async with DigikalaAsync(os.environ["DIGIKALA_ACCESS_TOKEN"]) as client:
        response = await client.orders.list(query=ListQuery(size=5))
        for order in response.data.items or []:
            print(order.model_dump())


if __name__ == "__main__":
    asyncio.run(main())
```

سه تغییر اصلی نسبت به sync:

1. `DigikalaAsync` به‌جای `DigikalaSync`.
2. `async with` برای مدیریت اتصال.
3. `await` پیش از متد شبکه‌ای.

اگر داخل تابع async برنامه یا notebook هستید، تابع را با `await main()` اجرا کنید؛
`asyncio.run()` برای نقطهٔ شروع یک اسکریپت مستقل است.

## طول عمر اتصال

کلاینت را برای مجموعه‌ای از درخواست‌های همان فروشنده باز نگه دارید و همهٔ فراخوانی‌های
resource را داخل context انجام دهید. به این ترتیب اتصال HTTP قابل استفادهٔ مجدد می‌ماند.
خروج از `async with`، اتصال را می‌بندد.

برای بستن دستی از `await client.aclose()` استفاده کنید. در کلاینت sync معادل آن `client.close()`
است. متدهای sync را در مسیر درخواست async فراخوانی نکنید؛ تا پایان شبکه اجرای آن مسیر را متوقف می‌کنند.

**تمرین:** [نمونهٔ async دیجی‌کالا](../../examples/digikala/async_usage.py) را با نسخهٔ sync
مقایسه کنید و همان query را در هر دو قرار دهید.

[بعدی: مدیریت خطاها ←](errors.md)
