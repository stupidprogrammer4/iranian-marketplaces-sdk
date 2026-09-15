"""Run with: python -m examples.snapp.sync_usage"""

from examples._credentials import required_env
from iranian_marketplaces_sdk import SnappSync
from iranian_marketplaces_sdk.marketplaces.snapp.data import VendorOrdersQuery
from iranian_marketplaces_sdk.marketplaces.snapp.data import (
    VendorProductsQuery as SnappProductsQuery,
)


def main() -> None:
    """Snapp, sync: products (offset-paginated) and orders (cursor-paginated)."""
    with SnappSync(
        required_env("SNAPP_UNIQUE_CODE"),
        required_env("SNAPP_ACCESS_TOKEN"),
        required_env("SNAPP_SELLER_ID"),
    ) as client:
        products = client.list_products(query=SnappProductsQuery(per_page=5))
        print("[sync] snapp total products:", products.meta.pagination.total)

        orders = client.list_orders(query=VendorOrdersQuery(per_page=5))
        print("[sync] snapp orders on this page:", orders.meta.pagination.count)

        if orders.data:
            detail = client.get_order(orders.data[0].order_number)
            print("[sync] snapp order status:", detail.data.order_status)


if __name__ == "__main__":
    main()
