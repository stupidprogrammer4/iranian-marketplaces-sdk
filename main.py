"""Usage examples / smoke tests for the Iranian Marketplaces SDK."""

from __future__ import annotations

import asyncio
import os

from iranian_marketplaces_sdk.basalam import AsyncBasalamClient, BasalamClient
from iranian_marketplaces_sdk.digikala import AsyncDigikalaClient, DigikalaClient

DIGIKALA_ACCESS_TOKEN = os.environ.get("DIGIKALA_ACCESS_TOKEN", "your-access-token")
DIGIKALA_REFRESH_TOKEN = os.environ.get("DIGIKALA_REFRESH_TOKEN", "your-refresh-token")
BASALAM_ACCESS_TOKEN = os.environ.get("BASALAM_ACCESS_TOKEN", "your-access-token")
BASALAM_VENDOR_ID = int(os.environ.get("BASALAM_VENDOR_ID", "0"))


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


if __name__ == "__main__":
    digikala_sync_demo()
    asyncio.run(digikala_async_demo())
    basalam_sync_demo()
    asyncio.run(basalam_async_demo())
