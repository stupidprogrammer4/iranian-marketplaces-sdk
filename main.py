"""Usage examples / smoke tests for the Iranian Marketplaces SDK."""

from __future__ import annotations

import asyncio
import os

from iranian_marketplaces_sdk.basalam import AsyncBasalamClient, BasalamClient
from iranian_marketplaces_sdk.digikala import AsyncDigikalaClient, DigikalaClient
from iranian_marketplaces_sdk.snapp import AsyncSnappClient, SnappClient
from iranian_marketplaces_sdk.tapsi import AsyncTapsiClient, TapsiClient

DIGIKALA_ACCESS_TOKEN = os.environ.get("DIGIKALA_ACCESS_TOKEN", "your-access-token")
DIGIKALA_REFRESH_TOKEN = os.environ.get("DIGIKALA_REFRESH_TOKEN", "your-refresh-token")
BASALAM_ACCESS_TOKEN = os.environ.get("BASALAM_ACCESS_TOKEN", "your-access-token")
BASALAM_VENDOR_ID = int(os.environ.get("BASALAM_VENDOR_ID", "0"))
SNAPP_UNIQUE_CODE = os.environ.get("SNAPP_UNIQUE_CODE", "your-unique-code")
SNAPP_ACCESS_TOKEN = os.environ.get("SNAPP_ACCESS_TOKEN", "your-access-token")
SNAPP_SELLER_ID = os.environ.get("SNAPP_SELLER_ID", "your-seller-id")
TAPSI_TOKEN = os.environ.get("TAPSI_TOKEN", "your-token")


def digikala_sync_demo() -> None:
    """Demonstrate the synchronous Digikala client."""
    with DigikalaClient(DIGIKALA_ACCESS_TOKEN, DIGIKALA_REFRESH_TOKEN) as client:
        health = client.health_check()
        print("[sync] health:", health["status"], "-", health["data"]["mode"])

        scopes = client.get_scopes()
        for scope in scopes["data"]["items"]:
            print("[sync] scope:", scope["key"], "->", scope["access"])


async def digikala_async_demo() -> None:
    """Demonstrate the asynchronous Digikala client."""
    async with AsyncDigikalaClient(
        DIGIKALA_ACCESS_TOKEN, DIGIKALA_REFRESH_TOKEN
    ) as client:
        health = await client.health_check()
        print("[async] health:", health["status"], "-", health["data"]["mode"])

        scopes = await client.get_scopes()
        for scope in scopes["data"]["items"]:
            print("[async] scope:", scope["key"], "->", scope["access"])


def basalam_sync_demo() -> None:
    """Demonstrate the synchronous Basalam client."""
    with BasalamClient(BASALAM_VENDOR_ID, BASALAM_ACCESS_TOKEN) as client:
        products = client.list_vendor_products(query={"per_page": 5})
        print("[sync] basalam result_count:", products["result_count"])


async def basalam_async_demo() -> None:
    """Demonstrate the asynchronous Basalam client."""
    async with AsyncBasalamClient(
        BASALAM_VENDOR_ID, BASALAM_ACCESS_TOKEN
    ) as client:
        products = await client.list_vendor_products(query={"per_page": 5})
        print("[async] basalam result_count:", products["result_count"])


def snapp_sync_demo() -> None:
    """Demonstrate the synchronous Snapp client."""
    with SnappClient(
        SNAPP_UNIQUE_CODE, SNAPP_ACCESS_TOKEN, SNAPP_SELLER_ID
    ) as client:
        products = client.list_products(query={"per_page": 5})
        total = products["meta"]["pagination"]["total"]
        print("[sync] snapp total products:", total)

        orders = client.list_orders(query={"per_page": 5})
        print("[sync] snapp orders count:", orders["meta"]["pagination"]["count"])

        if orders["data"]:
            order_number = orders["data"][0]["order_number"]
            detail = client.get_order(order_number)
            print("[sync] snapp order detail:", detail["data"]["order_status"])


async def snapp_async_demo() -> None:
    """Demonstrate the asynchronous Snapp client."""
    async with AsyncSnappClient(
        SNAPP_UNIQUE_CODE, SNAPP_ACCESS_TOKEN, SNAPP_SELLER_ID
    ) as client:
        products = await client.list_products(query={"per_page": 5})
        total = products["meta"]["pagination"]["total"]
        print("[async] snapp total products:", total)

        orders = await client.list_orders(query={"per_page": 5})
        print(
            "[async] snapp orders count:",
            orders["meta"]["pagination"]["count"],
        )

        if orders["data"]:
            order_number = orders["data"][0]["order_number"]
            detail = await client.get_order(order_number)
            print("[async] snapp order detail:", detail["data"]["order_status"])


def tapsi_sync_demo() -> None:
    """Demonstrate the synchronous Tapsi client."""
    with TapsiClient(TAPSI_TOKEN) as client:
        products = client.get_products(1, 10)
        print("[sync] tapsi total products:", products["data"]["totalCount"])

        orders = client.list_orders(query={"pageNumber": 0, "pageSize": 20})
        print("[sync] tapsi total orders:", orders["data"]["totalItems"])

        result = client.update_products(
            [
                {
                    "id": "your-sku",
                    "stock": 10,
                    "price": 20000,
                    "specialPrice": 10000,
                    "referenceCode": "ref-001",
                }
            ]
        )
        print("[sync] tapsi update success:", result["success"])


async def tapsi_async_demo() -> None:
    """Demonstrate the asynchronous Tapsi client."""
    async with AsyncTapsiClient(TAPSI_TOKEN) as client:
        products = await client.get_products(1, 10)
        print("[async] tapsi total products:", products["data"]["totalCount"])

        orders = await client.list_orders(
            query={"pageNumber": 0, "pageSize": 20}
        )
        print("[async] tapsi total orders:", orders["data"]["totalItems"])

        result = await client.update_products(
            [
                {
                    "id": "your-sku",
                    "stock": 10,
                    "price": 20000,
                    "specialPrice": 10000,
                    "referenceCode": "ref-001",
                }
            ]
        )
        print("[async] tapsi update success:", result["success"])


if __name__ == "__main__":
    digikala_sync_demo()
    asyncio.run(digikala_async_demo())
    basalam_sync_demo()
    asyncio.run(basalam_async_demo())
    snapp_sync_demo()
    asyncio.run(snapp_async_demo())
    tapsi_sync_demo()
    asyncio.run(tapsi_async_demo())
