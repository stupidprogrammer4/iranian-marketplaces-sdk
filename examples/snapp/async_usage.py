"""Run with: python -m examples.snapp.async_usage"""

import asyncio

from examples._credentials import required_env
from iranian_marketplaces_sdk import SnappAsync
from iranian_marketplaces_sdk.marketplaces.snapp.data import VendorOrdersQuery


async def main() -> None:
    """Snapp, async: walking the order cursor — there is no page number to jump to."""
    async with SnappAsync(
        required_env("SNAPP_UNIQUE_CODE"),
        required_env("SNAPP_ACCESS_TOKEN"),
        required_env("SNAPP_SELLER_ID"),
    ) as client:
        query = VendorOrdersQuery(per_page=5)
        for page in range(1, 4):
            orders = await client.list_orders(query=query)
            print(f"[async] snapp page {page}: {len(orders.data)} orders")
            pagination = orders.meta.pagination
            if not pagination.has_more or pagination.next_cursor is None:
                break
            query = VendorOrdersQuery(per_page=5, cursor=pagination.next_cursor)


if __name__ == "__main__":
    asyncio.run(main())
