"""Usage examples / smoke tests for the Iranian Marketplaces SDK."""

from __future__ import annotations

import asyncio
import os

from iranian_marketplaces_sdk.digikala import AsyncDigikalaClient, DigikalaClient

DIGIKALA_ACCESS_TOKEN = os.environ.get("DIGIKALA_ACCESS_TOKEN", "your-access-token")
DIGIKALA_REFRESH_TOKEN = os.environ.get("DIGIKALA_REFRESH_TOKEN", "your-refresh-token")


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


if __name__ == "__main__":
    digikala_sync_demo()
    asyncio.run(digikala_async_demo())
