"""Tapsi Shop — base URL and endpoint paths for the Hub vendor API."""

NAME = "tapsi"

BASE_URL = "https://vendorgw.tapsi.shop"

#: Client identification headers, defaulted to the values the documented API client sends.
DEFAULT_CLIENT_NAME = "Swagger on HIT.Hastim.Hub.Endpoints.WebApi"
DEFAULT_CLIENT_VERSION = "1.0.0.0"

# Vendor products. Note the casing difference between the two paths — it is the API's, not a typo:
# the batch update is served at lowercase ``/web/…`` and the list at ``/Web/…``.
PRODUCTS_ENDPOINT = "/web/hub/vendors/v1/products"


def products_list_endpoint(page: int, page_size: int) -> str:
    """Path for a paginated vendor product list. Paging is in the path, not the query string."""
    return f"/Web/Hub/vendors/v1/products/{page}/{page_size}"


# Vendor orders. A POST, because the filters travel as a JSON body rather than a query string.
ORDERS_ENDPOINT = "/Web/Hub/vendors/v1/orders"
