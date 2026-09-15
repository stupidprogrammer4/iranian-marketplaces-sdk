"""Run with: python -m examples.basalam.sync_usage"""

from examples._credentials import required_env
from iranian_marketplaces_sdk import BasalamSync
from iranian_marketplaces_sdk.marketplaces.basalam.data import (
    VendorProductsQuery as BasalamProductsQuery,
)


def main() -> None:
    """Basalam, sync: the vendor's products, filtered to what is actually in stock."""
    with BasalamSync(
        int(required_env("BASALAM_VENDOR_ID")), required_env("BASALAM_ACCESS_TOKEN")
    ) as client:
        products = client.list_vendor_products(query=BasalamProductsQuery(per_page=5, stock_gte=1))
        print("[sync] basalam result_count:", products.result_count)
        for product in products.data or []:
            print(f"    {product.id} {product.title} — {product.price} ({product.inventory})")


if __name__ == "__main__":
    main()
