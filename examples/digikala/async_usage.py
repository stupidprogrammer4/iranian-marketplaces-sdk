"""Run with: python -m examples.digikala.async_usage"""

import asyncio
import os

from examples._credentials import required_env
from iranian_marketplaces_sdk import DigikalaAsync
from iranian_marketplaces_sdk.marketplaces.digikala.data.api import variants as digikala_variants


async def main() -> None:
    """The same calls on the async engine: identical models, identical field names."""
    async with DigikalaAsync(
        required_env("DIGIKALA_ACCESS_TOKEN"), os.environ.get("DIGIKALA_REFRESH_TOKEN", "")
    ) as client:
        health = await client.health_check()
        print("[async] digikala health:", health.status, "-", health.data.mode)

        scopes = await client.get_scopes()
        for scope in scopes.data.items:
            print("[async] digikala scope:", scope.key, "->", scope.access)

        variants = await client.variants.list(query=digikala_variants.ListQuery(size=5))
        for variant in variants.data.items or []:
            print(f"    {variant.id} {variant.title} - {variant.price_sale}")


if __name__ == "__main__":
    asyncio.run(main())
