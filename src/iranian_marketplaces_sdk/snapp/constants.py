"""Base URL and endpoint paths for the Snapp Shop Automation API."""

from __future__ import annotations

BASE_URL = "https://apix.snappshop.ir/automation/v1"


# Vendor products.
def vendor_products_endpoint(seller_id: str | int) -> str:
    """Path for a vendor's product list."""
    return f"/vendors/{seller_id}/products"


# Vendor orders.
def vendor_orders_endpoint(seller_id: str | int) -> str:
    """Path for a vendor's order list."""
    return f"/vendors/{seller_id}/orders"


def vendor_order_endpoint(seller_id: str | int, order_number: str | int) -> str:
    """Path for a single vendor order's detail."""
    return f"/vendors/{seller_id}/orders/{order_number}"