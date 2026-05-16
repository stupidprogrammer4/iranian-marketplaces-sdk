"""Base URL and endpoint paths for the Digikala Seller Open API."""

from __future__ import annotations

BASE_URL = "https://seller.digikala.com/open-api/v1"

# The health-check endpoint is served at the API root itself.
HEALTH_CHECK_ENDPOINT = ""

# Token generation (unauthenticated: exchanges an authorization_code).
AUTH_TOKEN_ENDPOINT = "/auth/token"

# Token refresh (unauthenticated: exchanges an expired access + refresh token).
AUTH_REFRESH_TOKEN_ENDPOINT = "/auth/refresh-token"

# Authenticated endpoints.
AUTH_SCOPES_ENDPOINT = "/auth/scopes"


def auth_client_scopes_endpoint(client_code: str) -> str:
    """Path for the available scopes of a given application (``client_code``)."""
    return f"/auth/scopes/{client_code}"


# Variants (scope: variant).
VARIANTS_ENDPOINT = "/variants"
VARIANTS_SELLING_PRICE_ENDPOINT = "/variants/selling-price"


def variant_endpoint(variant_id: int) -> str:
    """Path for a single variant by id."""
    return f"/variants/{variant_id}"


def variant_gold_endpoint(variant_id: int) -> str:
    """Path for the gold data of a single variant by id."""
    return f"/variants/{variant_id}/gold"


def variant_activation_endpoint(variant_id: int) -> str:
    """Path for the activation status of a single variant by id."""
    return f"/variants/{variant_id}/activation"


def variant_seller_stock_endpoint(variant_id: int) -> str:
    """Path for the seller stock detail of a single variant by id."""
    return f"/variants/{variant_id}/seller-stock"


# Orders (scope: order).
ORDERS_ENDPOINT = "/orders"
ORDERS_HISTORY_ENDPOINT = "/orders/history"


# Inventories (scope: inventory).
INVENTORIES_ENDPOINT = "/inventories"


def inventory_dead_stock_endpoint(product_variant_id: int) -> str:
    """Path for the dead-stock detail of a single product variant."""
    return f"/inventories/{product_variant_id}"


# Packages (scope: package).
PACKAGES_ENDPOINT = "/packages"


def package_endpoint(package_id: int) -> str:
    """Path for a single package detail by id."""
    return f"/packages/{package_id}"


# Smart discount / pricing (scope: promotion).
SMART_DISCOUNT_VARIANTS_ENDPOINT = "/pricing/smart-discount/variants"
SMART_DISCOUNT_VARIANTS_BATCH_ENDPOINT = (
    f"{SMART_DISCOUNT_VARIANTS_ENDPOINT}/batch"
)


def smart_discount_variants_endpoint(active_status: str) -> str:
    """Path for smart-discount variants. ``active_status``: active|inactive."""
    return f"{SMART_DISCOUNT_VARIANTS_ENDPOINT}/{active_status}"


# Invoices (scope: invoice).
INVOICES_ENDPOINT = "/invoices"


def invoice_details_endpoint(invoice_id: int) -> str:
    """Path for a single invoice's detail view."""
    return f"/invoices/{invoice_id}/details"


def invoice_items_endpoint(
    invoice_id: int, financial_notation_id: int, calculation_type: str
) -> str:
    """Path for an invoice's financial items of a given notation/calc type."""
    return (
        f"/invoices/{invoice_id}/items/"
        f"{financial_notation_id}/{calculation_type}"
    )
