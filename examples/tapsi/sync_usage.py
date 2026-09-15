"""Run with: python -m examples.tapsi.sync_usage"""

from examples._credentials import required_env
from iranian_marketplaces_sdk import TapsiSync
from iranian_marketplaces_sdk.marketplaces.tapsi.data import OrdersQuery


def main() -> None:
    """Tapsi, sync: products and orders. Product paging is 1-based, order paging is not."""
    with TapsiSync(required_env("TAPSI_TOKEN")) as client:
        products = client.get_products(1, 10)
        print("[sync] tapsi total products:", products.data.total_count)

        orders = client.list_orders(query=OrdersQuery(page_number=0, page_size=20))
        print("[sync] tapsi total orders:", orders.data.total_items)
        for order in orders.data.items:
            print(f"    {order.order_number} {order.state_title} — {order.final_price}")


if __name__ == "__main__":
    main()
