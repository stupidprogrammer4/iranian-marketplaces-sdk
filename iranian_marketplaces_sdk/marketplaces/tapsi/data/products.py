"""Tapsi Shop — the vendor-products endpoints.

Tapsi speaks camelCase on the wire, so every field here that is not already snake_case carries an
alias. Python code reads ``special_price``; the request body still says ``specialPrice``.
"""

from iranian_marketplaces_sdk.common.data import (
    CamelCaseRequestSchema,
    CamelCaseResponseSchema,
)
from iranian_marketplaces_sdk.marketplaces.tapsi.data.common import ApiMessage

__all__ = [
    "Product",
    "ProductUpdate",
    "ProductUpdateData",
    "ProductUpdatePayload",
    "ProductUpdateResponse",
    "ProductUpdateResultItem",
    "ProductsPage",
    "ProductsResponse",
]


class ProductUpdate(CamelCaseRequestSchema):
    """A single product change for ``PUT /web/hub/vendors/v1/products``.

    ``id`` is the product's SKU on Tapsi. ``reference_code`` is yours: whatever you put there comes
    back on the matching result, which is how a per-product outcome is tied to the row it came
    from when a batch partly fails.
    """

    id: str
    stock: int
    price: int
    special_price: int | None = None
    reference_code: str


class ProductUpdatePayload(CamelCaseRequestSchema):
    """Request body wrapper for the products PUT (batch) endpoint."""

    products: list[ProductUpdate]


class ProductUpdateResultItem(CamelCaseResponseSchema):
    """Per-product result of the products PUT (batch) endpoint.

    The ``current_*`` fields are the state *after* the update, straight from Tapsi — the value to
    reconcile against rather than assuming the request went through as sent.
    """

    id: str
    sku: str
    status: bool
    messages: list[str]
    current_original_price: int
    current_final_price: int
    current_on_hand_quantity: int
    reference_code: str


class ProductUpdateData(CamelCaseResponseSchema):
    """Inner ``data`` envelope of the products PUT response.

    Tapsi nests a second ``status``/``data`` pair inside the outer ``success``/``data`` one; both
    have to be checked, along with each item's own ``status``.
    """

    status: bool
    data: list[ProductUpdateResultItem]


class ProductUpdateResponse(CamelCaseResponseSchema):
    """Full response body of ``PUT /web/hub/vendors/v1/products``."""

    success: bool
    messages: list[ApiMessage]
    data: ProductUpdateData


class Product(CamelCaseResponseSchema):
    """A single vendor product in the paginated product list.

    ``original_price`` is before discount, ``final_price`` after. ``hsin`` is Tapsi's own catalogue
    identifier for the underlying product, as opposed to ``sku``, which is the vendor's.
    """

    id: str
    hsin: str
    sku: str
    original_price: int
    final_price: int
    minimal_per_order: int
    maximal_per_order: int
    on_hand_quantity: int


class ProductsPage(CamelCaseResponseSchema):
    """Inner ``data`` envelope of the paginated products response."""

    page: int
    page_size: int
    total_count: int
    items: list[Product]


class ProductsResponse(CamelCaseResponseSchema):
    """Full response body of ``GET /Web/Hub/vendors/v1/products/{page}/{pageSize}``."""

    success: bool
    messages: list[ApiMessage]
    data: ProductsPage
