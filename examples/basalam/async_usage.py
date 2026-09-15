"""Run with: python -m examples.basalam.async_usage"""

import asyncio

from examples._credentials import required_env
from iranian_marketplaces_sdk import BasalamAsync
from iranian_marketplaces_sdk.marketplaces.basalam.data import (
    VendorProductsQuery as BasalamProductsQuery,
)


async def main() -> None:
    """Basalam, async: products, then the parcels waiting to be shipped."""
    async with BasalamAsync(
        int(required_env("BASALAM_VENDOR_ID")), required_env("BASALAM_ACCESS_TOKEN")
    ) as client:
        products = await client.list_vendor_products(query=BasalamProductsQuery(per_page=5))
        print("[async] basalam result_count:", products.result_count)

        parcels = await client.list_vendor_parcels()
        print("[async] basalam parcels:", len(parcels.data), "| next:", parcels.next_cursor)


if __name__ == "__main__":
    asyncio.run(main())
