"""Basalam — base URL and endpoint paths for the Open API."""

NAME = "basalam"

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
    """Path for creating and deleting a vendor discount."""
    return f"/v1/vendors/{vendor_id}/discounts"


# Parcels — the one resource that is not vendor-scoped in the path.
VENDOR_PARCELS_ENDPOINT = "/v1/vendor-parcels"


#: Pythonic filter names that map to a Basalam query key no Python identifier can express.
PRODUCTS_QUERY_KEY_MAP = {
    "stock_gte": "stock[gte]",
    "stock_lte": "stock[lte]",
    "preparation_day_gte": "preparation_day[gte]",
    "preparation_day_lte": "preparation_day[lte]",
    "price_gte": "price[gte]",
    "price_lte": "price[lte]",
}

#: The same, for the parcels endpoint — which uses dots as well as brackets.
PARCELS_QUERY_KEY_MAP = {
    "items_customer_ids": "items.customer_ids",
    "items_vendor_ids": "items.vendor_ids",
    "items_product_ids": "items.product_ids",
    "items_order_ids": "items.order_ids",
    "estimate_send_at_gte": "estimate_send_at[gte]",
    "estimate_send_at_lte": "estimate_send_at[lte]",
    "created_at_gte": "created_at[gte]",
    "created_at_lte": "created_at[lte]",
}
