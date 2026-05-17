"""Base URL and endpoint paths for the Tapsi Shop Hub vendor API."""

from __future__ import annotations

BASE_URL = "https://vendorgw.tapsi.shop"

# Default client identification headers (from the documented API client).
DEFAULT_CLIENT_NAME = "Swagger on HIT.Hastim.Hub.Endpoints.WebApi"
DEFAULT_CLIENT_VERSION = "1.0.0.0"

# Vendor products.
PRODUCTS_ENDPOINT = "/web/hub/vendors/v1/products"


def products_list_endpoint(page: int, page_size: int) -> str:
    """Path for a paginated vendor product list."""
    return f"/Web/Hub/vendors/v1/products/{page}/{page_size}"


# Vendor orders.
ORDERS_ENDPOINT = "/Web/Hub/vendors/v1/orders"
