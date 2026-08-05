"""Usage examples for the Iranian Marketplaces SDK.

Every marketplace appears twice — once on the sync engine, once on the async one — running similar
calls so the two can be read side by side. Credentials come from the environment; with none set
the calls fail authentication, which is the point: this file is for pointing at a live account.

    DIGIKALA_ACCESS_TOKEN=… SNAPP_ACCESS_TOKEN=… python main.py

The offline behaviour of these calls — the URL, the query string, the body, the parsed model — is
covered in ``tests/``, which needs no credentials at all.
"""

import asyncio
import inspect
import os
from collections.abc import Callable, Coroutine
from typing import Any

from iranian_marketplaces_sdk import (
    BasalamAsync,
    BasalamSync,
    DigikalaAsync,
    DigikalaSync,
    MarketplaceError,
    SnappAsync,
    SnappSync,
    TapsiAsync,
    TapsiSync,
)
from iranian_marketplaces_sdk.marketplaces.basalam.data import (
    VendorProductsQuery as BasalamProductsQuery,
)
from iranian_marketplaces_sdk.marketplaces.digikala.data import VariantSearch
from iranian_marketplaces_sdk.marketplaces.snapp.data import VendorOrdersQuery
from iranian_marketplaces_sdk.marketplaces.snapp.data import (
    VendorProductsQuery as SnappProductsQuery,
)
from iranian_marketplaces_sdk.marketplaces.tapsi.data import OrdersQuery

DIGIKALA_ACCESS_TOKEN = os.environ.get("DIGIKALA_ACCESS_TOKEN", "your-access-token")
DIGIKALA_REFRESH_TOKEN = os.environ.get("DIGIKALA_REFRESH_TOKEN", "")
BASALAM_ACCESS_TOKEN = os.environ.get("BASALAM_ACCESS_TOKEN", "your-access-token")
BASALAM_VENDOR_ID = int(os.environ.get("BASALAM_VENDOR_ID", "0"))
SNAPP_UNIQUE_CODE = os.environ.get("SNAPP_UNIQUE_CODE", "your-unique-code")
SNAPP_ACCESS_TOKEN = os.environ.get("SNAPP_ACCESS_TOKEN", "your-access-token")
SNAPP_SELLER_ID = os.environ.get("SNAPP_SELLER_ID", "your-seller-id")
TAPSI_TOKEN = os.environ.get("TAPSI_TOKEN", "your-token")


def digikala_sync_demo() -> None:
    """Digikala, sync: health, granted scopes, and the first page of active variants."""
    with DigikalaSync(DIGIKALA_ACCESS_TOKEN, DIGIKALA_REFRESH_TOKEN) as client:
        health = client.health_check()
        limit = health.data.rate_limit
        print("[sync] digikala health:", health.status, "-", health.data.mode)
        print(f"[sync] digikala rate limit: {limit.current}/{limit.max}")

        for scope in client.get_scopes().data.items:
            print("[sync] digikala scope:", scope.key, "->", scope.access)

        variants = client.list_variants(page=1, size=5, search=VariantSearch(active=True))
        print("[sync] digikala variants:", variants.data.pager.total_rows)
        for variant in variants.data.items:
            print(f"    {variant.id} {variant.title} — {variant.price_sale}")


async def digikala_async_demo() -> None:
    """The same calls on the async engine: identical models, identical field names."""
    async with DigikalaAsync(DIGIKALA_ACCESS_TOKEN, DIGIKALA_REFRESH_TOKEN) as client:
        health = await client.health_check()
        print("[async] digikala health:", health.status, "-", health.data.mode)

        scopes = await client.get_scopes()
        for scope in scopes.data.items:
            print("[async] digikala scope:", scope.key, "->", scope.access)


def basalam_sync_demo() -> None:
    """Basalam, sync: the vendor's products, filtered to what is actually in stock."""
    with BasalamSync(BASALAM_VENDOR_ID, BASALAM_ACCESS_TOKEN) as client:
        products = client.list_vendor_products(query=BasalamProductsQuery(per_page=5, stock_gte=1))
        print("[sync] basalam result_count:", products.result_count)
        for product in products.data or []:
            print(f"    {product.id} {product.title} — {product.price} ({product.inventory})")


async def basalam_async_demo() -> None:
    """Basalam, async: products, then the parcels waiting to be shipped."""
    async with BasalamAsync(BASALAM_VENDOR_ID, BASALAM_ACCESS_TOKEN) as client:
        products = await client.list_vendor_products(query=BasalamProductsQuery(per_page=5))
        print("[async] basalam result_count:", products.result_count)

        parcels = await client.list_vendor_parcels()
        print("[async] basalam parcels:", len(parcels.data), "| next:", parcels.next_cursor)


def snapp_sync_demo() -> None:
    """Snapp, sync: products (offset-paginated) and orders (cursor-paginated)."""
    with SnappSync(SNAPP_UNIQUE_CODE, SNAPP_ACCESS_TOKEN, SNAPP_SELLER_ID) as client:
        products = client.list_products(query=SnappProductsQuery(per_page=5))
        print("[sync] snapp total products:", products.meta.pagination.total)

        orders = client.list_orders(query=VendorOrdersQuery(per_page=5))
        print("[sync] snapp orders on this page:", orders.meta.pagination.count)

        if orders.data:
            detail = client.get_order(orders.data[0].order_number)
            print("[sync] snapp order status:", detail.data.order_status)


async def snapp_async_demo() -> None:
    """Snapp, async: walking the order cursor — there is no page number to jump to."""
    async with SnappAsync(SNAPP_UNIQUE_CODE, SNAPP_ACCESS_TOKEN, SNAPP_SELLER_ID) as client:
        query = VendorOrdersQuery(per_page=5)
        for page in range(1, 4):
            orders = await client.list_orders(query=query)
            print(f"[async] snapp page {page}: {len(orders.data)} orders")
            pagination = orders.meta.pagination
            if not pagination.has_more or pagination.next_cursor is None:
                break
            query = VendorOrdersQuery(per_page=5, cursor=pagination.next_cursor)


def tapsi_sync_demo() -> None:
    """Tapsi, sync: products and orders. Product paging is 1-based, order paging is not."""
    with TapsiSync(TAPSI_TOKEN) as client:
        products = client.get_products(1, 10)
        print("[sync] tapsi total products:", products.data.total_count)

        orders = client.list_orders(query=OrdersQuery(page_number=0, page_size=20))
        print("[sync] tapsi total orders:", orders.data.total_items)
        for order in orders.data.items:
            print(f"    {order.order_number} {order.state_title} — {order.final_price}")


async def tapsi_async_demo() -> None:
    """Tapsi, async: reading products.

    The batch update is left commented out on purpose — it writes. When you do run it, check all
    three outcomes: ``success``, ``data.status``, and each item's own ``status``.

        result = await client.update_products(
            [ProductUpdate(id="your-sku", stock=10, price=20_000, reference_code="ref-1")]
        )
        for item in result.data.data:
            print(item.reference_code, item.status, item.current_final_price)
    """
    async with TapsiAsync(TAPSI_TOKEN) as client:
        products = await client.get_products(1, 10)
        print("[async] tapsi total products:", products.data.total_count)
        for product in products.data.items:
            print(f"    {product.sku} — {product.final_price} ({product.on_hand_quantity})")


def run(label: str, demo: Callable[[], None] | Callable[[], Coroutine[Any, Any, None]]) -> None:
    """Run one demo, reporting a marketplace error rather than ending the script on it."""
    try:
        if inspect.iscoroutinefunction(demo):
            asyncio.run(demo())
        else:
            demo()
    except MarketplaceError as exc:
        print(f"[{label}] failed: {type(exc).__name__}: {exc}")


if __name__ == "__main__":
    run("digikala sync", digikala_sync_demo)
    run("digikala async", digikala_async_demo)
    run("basalam sync", basalam_sync_demo)
    run("basalam async", basalam_async_demo)
    run("snapp sync", snapp_sync_demo)
    run("snapp async", snapp_async_demo)
    run("tapsi sync", tapsi_sync_demo)
    run("tapsi async", tapsi_async_demo)
