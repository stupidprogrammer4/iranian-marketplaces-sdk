"""Base URL and endpoint paths for the Basalam Open API."""

from __future__ import annotations

BASE_URL = "https://openapi.basalam.com"


# Vendors (vendor products).
def vendor_products_endpoint(vendor_id: int) -> str:
    """Path for a vendor's product list."""
    return f"/v1/vendors/{vendor_id}/products"


def vendor_products_batch_updates_endpoint(vendor_id: int) -> str:
    """Path for batch-updating a vendor's products."""
    return f"/v1/vendors/{vendor_id}/products/batch-updates"


# Discounts.
def vendor_discounts_endpoint(vendor_id: int) -> str:
    """Path for creating a vendor discount."""
    return f"/v1/vendors/{vendor_id}/discounts"


# Parcels (not vendor-scoped in the path).
VENDOR_PARCELS_ENDPOINT = "/v1/vendor-parcels"
