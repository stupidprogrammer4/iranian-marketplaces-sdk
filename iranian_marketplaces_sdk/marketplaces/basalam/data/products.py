"""Basalam — the vendor-products endpoints.

Several nested objects — ``photo``, ``status``, ``revision``, ``shipping_data``, ``unit_type``,
``discount``, and a variant's ``properties`` — are returned by Basalam with no published field
schema. They are typed as open dictionaries: inventing keys would be guessing, and this way the
data still arrives intact. Tighten them once the upstream schemas are documented.
"""

from typing import Any

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema, ResponseSchema

__all__ = [
    "BatchProductUpdateRequest",
    "BatchProductUpdateResult",
    "ProductBatchUpdateItem",
    "ProductBatchUpdateProductAttribute",
    "ProductBatchUpdateVariant",
    "ProductBatchUpdateVariantAttribute",
    "VendorProduct",
    "VendorProductVariant",
    "VendorProductsQuery",
    "VendorProductsResponse",
]


class VendorProductVariant(ResponseSchema):
    """A single variant of a vendor product.

    ``primary_price`` is the price before any discount; ``price`` is what the customer pays.
    """

    stock: int
    properties: list[dict[str, Any]]
    unit_quantity: float | None = None
    unit_type: dict[str, Any] | None = None
    id: int | None = None
    price: int | None = None
    primary_price: int | None = None
    order: int | None = None
    sku: str | None = None
    discount: dict[str, Any] | None = None


class VendorProduct(ResponseSchema):
    """A single vendor product.

    ``is_product_for_revision`` means an edit is pending Basalam's review — the live listing still
    shows the previous values until it clears.
    """

    id: int
    title: str
    price: int
    photo: dict[str, Any]
    status: dict[str, Any]
    inventory: int
    primary_price: int | None = None
    is_product_for_revision: bool
    preparation_day: int | None = None
    published: bool | None = None
    shipping_data: dict[str, Any] | None = None
    net_weight: int
    packaged_weight: int
    net_weight_decimal: float | None = None
    variant: list[VendorProductVariant] | None = None
    revision: dict[str, Any] | None = None
    sku: str | None = None
    discount: dict[str, Any] | None = None
    is_wholesale: bool | None = None


class VendorProductsResponse(ResponseSchema):
    """Full response body of ``GET /v1/vendors/{vendor_id}/products``.

    Basalam returns the paginated payload at the top level — there is no ``{status, data}``
    envelope here, unlike Digikala and Snapp.
    """

    data: list[VendorProduct] | None = None
    result_count: int
    total_count: int | None = None
    total_page: int | None = None
    page: int | None = None
    per_page: int | None = None


class ProductBatchUpdateVariantAttribute(RequestSchema):
    """A key/value attribute of a variant in a batch update."""

    key: str
    value: str


class ProductBatchUpdateVariant(RequestSchema):
    """A variant entry inside a batch product update."""

    id: int
    primary_price: int | None = None
    stock: int | None = None
    attributes: list[ProductBatchUpdateVariantAttribute] | None = None


class ProductBatchUpdateProductAttribute(RequestSchema):
    """A product attribute entry inside a batch product update.

    Free-text attributes use ``value``; list attributes use ``selected_values`` with the option ids.
    """

    attribute_id: int
    value: str | None = None
    selected_values: list[int] | None = None


class ProductBatchUpdateItem(RequestSchema):
    """A single product's changes in a batch update.

    ``illegal_for_iran`` and ``illegal_for_same_city`` are required by the API on every entry, not
    only when they change — they declare whether the product may ship at all.

    ``shipping_data`` (Basalam's ``ProductShippingData``) has no published field schema.
    """

    id: int
    illegal_for_iran: bool
    illegal_for_same_city: bool
    name: str | None = None
    primary_price: int | None = None
    order: int | None = None
    stock: int | None = None
    status: int | None = None
    preparation_days: int | None = None
    variants: list[ProductBatchUpdateVariant] | None = None
    product_attribute: list[ProductBatchUpdateProductAttribute] | None = None
    shipping_data: dict[str, Any] | None = None


class BatchProductUpdateRequest(RequestSchema):
    """Request body for the vendor products batch-update endpoint."""

    data: list[ProductBatchUpdateItem]


class BatchProductUpdateResult(ResponseSchema):
    """A single per-product result of a batch update.

    The endpoint answers with a bare JSON array of these. ``has_error`` is per product: with
    ``continue_on_error`` set, some entries can succeed while others fail in the same call.
    """

    id: int
    is_product_for_revision: bool
    has_error: bool
    error_message: str | None = None


class VendorProductsQuery(QuerySchema):
    """Query filters for the vendor-products endpoint.

    The pythonic names here are mapped to Basalam's own by the engine — ``stock_gte`` becomes
    ``stock[gte]``, which is not something a Python identifier can spell. List filters are sent as
    repeated query parameters (FastAPI style), never comma-joined.
    """

    title: str | None = None
    category: list[int] | None = None
    statuses: list[str] | None = None
    stock_gte: int | None = None
    stock_lte: int | None = None
    preparation_day_gte: int | None = None
    preparation_day_lte: int | None = None
    price_gte: int | None = None
    price_lte: int | None = None
    ids: list[int] | None = None
    without_tags: list[int] | None = None
    skus: list[str] | None = None
    illegal_free_shipping_for_iran: int | None = None
    illegal_free_shipping_for_same_city: int | None = None
    page: int | None = None
    per_page: int | None = None
    variants_flatting: bool | None = None
    is_wholesale: bool | None = None
    sort: str | None = None
