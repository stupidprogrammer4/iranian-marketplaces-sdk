"""Run with: python -m examples.digikala.sync_usage"""

import os

from examples._credentials import required_env
from iranian_marketplaces_sdk import DigikalaSync
from iranian_marketplaces_sdk.marketplaces.digikala.data.api import variants as digikala_variants


def main() -> None:
    """Digikala, sync: health, the scope catalog, and the first page of active variants."""
    with DigikalaSync(
        required_env("DIGIKALA_ACCESS_TOKEN"), os.environ.get("DIGIKALA_REFRESH_TOKEN", "")
    ) as client:
        health = client.health_check()
        limit = health.data.rate_limit
        print("[sync] digikala health:", health.status, "-", health.data.mode)
        print(f"[sync] digikala rate limit: {limit.current}/{limit.max}")

        for scope in client.get_scopes().data.items:
            print("[sync] digikala scope:", scope.key, "->", scope.access)

        variants = client.variants.list(
            query=digikala_variants.ListQuery(page=1, size=5, search_active=True)
        )
        for variant in variants.data.items or []:
            print(f"    {variant.id} {variant.title} — {variant.price_sale}")


if __name__ == "__main__":
    main()
