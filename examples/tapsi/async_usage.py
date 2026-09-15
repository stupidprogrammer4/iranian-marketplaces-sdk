"""Run with: python -m examples.tapsi.async_usage"""

import asyncio

from examples._credentials import required_env
from iranian_marketplaces_sdk import TapsiAsync


async def main() -> None:
    """Tapsi, async: reading products.

    The batch update is left commented out on purpose — it writes. When you do run it, check all
    three outcomes: ``success``, ``data.status``, and each item's own ``status``.

        result = await client.update_products(
            [ProductUpdate(id="your-sku", stock=10, price=20_000, reference_code="ref-1")]
        )
        for item in result.data.data:
            print(item.reference_code, item.status, item.current_final_price)
    """
    async with TapsiAsync(required_env("TAPSI_TOKEN")) as client:
        products = await client.get_products(1, 10)
        print("[async] tapsi total products:", products.data.total_count)
        for product in products.data.items:
            print(f"    {product.sku} — {product.final_price} ({product.on_hand_quantity})")


if __name__ == "__main__":
    asyncio.run(main())
