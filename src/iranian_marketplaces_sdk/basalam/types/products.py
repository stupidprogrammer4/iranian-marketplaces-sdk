"""TypedDicts for the Basalam vendor-products endpoint.

Several nested objects (``photo``, ``status``, ``revision``,
``shipping_data``, ``unit_type``, ``discount``, variant ``properties``)
are returned by Basalam without a published field schema. They are typed
as ``dict[str, object]`` deliberately: inventing keys would be guessing,
and ``object`` (not ``Any``) keeps callers honest. Tighten these once the
upstream schemas are documented.

NOTE: this package must NOT use ``from __future__ import annotations`` —
stringized annotations break ``TypedDict`` ``NotRequired`` resolution at
runtime.
"""

from typing import NotRequired, TypedDict

__all__ = [
    "VendorProductVariant",
    "VendorProduct",
    "VendorProductsResponse",
    "VendorProductsQuery",
    "ProductBatchUpdateVariantAttribute",
    "ProductBatchUpdateVariant",
    "ProductBatchUpdateProductAttribute",
    "ProductBatchUpdateItem",
    "BatchProductUpdateRequest",
    "BatchProductUpdateResult",
]


class VendorProductVariant(TypedDict):
    """A single variant of a vendor product."""

    stock: int
    properties: list[dict[str, object]]
    unit_quantity: float | None
    unit_type: dict[str, object] | None
    id: NotRequired[int | None]
    price: NotRequired[int | None]
    primary_price: NotRequired[int | None]
    order: NotRequired[int | None]
    sku: NotRequired[str | None]
    discount: NotRequired[dict[str, object] | None]


class VendorProduct(TypedDict):
    """A single vendor product."""

    id: int
    title: str
    price: int
    photo: dict[str, object]
    status: dict[str, object]
    inventory: int
    primary_price: int | None
    is_product_for_revision: bool
    preparation_day: int | None
    published: bool | None
    shipping_data: dict[str, object] | None
    net_weight: int
    packaged_weight: int
    net_weight_decimal: float | None
    variant: list[VendorProductVariant] | None
    revision: NotRequired[dict[str, object] | None]
    sku: NotRequired[str | None]
    discount: NotRequired[dict[str, object] | None]
    is_wholesale: NotRequired[bool | None]


class VendorProductsResponse(TypedDict):
    """Full response body of ``GET /v1/vendors/{vendor_id}/products``.

    Basalam returns the paginated payload at the top level (no
    ``{status, data}`` envelope).
    """

    data: list[VendorProduct] | None
    result_count: int
    total_count: NotRequired[int | None]
    total_page: NotRequired[int | None]
    page: NotRequired[int | None]
    per_page: NotRequired[int | None]


class ProductBatchUpdateVariantAttribute(TypedDict):
    """A key/value attribute of a variant in a batch update."""

    key: str
    value: str


class ProductBatchUpdateVariant(TypedDict):
    """A variant entry inside a batch product update."""

    id: int
    primary_price: NotRequired[int | None]
    stock: NotRequired[int | None]
    attributes: NotRequired[list[ProductBatchUpdateVariantAttribute] | None]


class ProductBatchUpdateProductAttribute(TypedDict):
    """A product attribute entry inside a batch product update."""

    attribute_id: int
    value: NotRequired[str | None]
    selected_values: NotRequired[list[int] | None]


class ProductBatchUpdateItem(TypedDict):
    """A single product's changes in a batch update.

    ``shipping_data`` (Basalam ``ProductShippingData``) has no published
    field schema, so it is typed as ``dict[str, object]``.
    """

    id: int
    illegal_for_iran: bool
    illegal_for_same_city: bool
    name: NotRequired[str | None]
    primary_price: NotRequired[int | None]
    order: NotRequired[int | None]
    stock: NotRequired[int | None]
    status: NotRequired[int | None]
    preparation_days: NotRequired[int | None]
    variants: NotRequired[list[ProductBatchUpdateVariant] | None]
    product_attribute: NotRequired[
        list[ProductBatchUpdateProductAttribute] | None
    ]
    shipping_data: NotRequired[dict[str, object] | None]


class BatchProductUpdateRequest(TypedDict):
    """Request body for the vendor products batch-update endpoint."""

    data: list[ProductBatchUpdateItem]


class BatchProductUpdateResult(TypedDict):
    """A single per-product result of a batch update.

    The endpoint responds with a JSON array of these (no envelope), so the
    engine returns ``list[BatchProductUpdateResult]``.
    """

    id: int
    is_product_for_revision: bool
    has_error: bool
    error_message: str | None


class VendorProductsQuery(TypedDict, total=False):
    """Optional query filters for the vendor-products endpoint.

    Pythonic snake_case keys are mapped to Basalam's actual query keys by
    the engine (e.g. ``stock_gte`` -> ``stock[gte]``). Array filters are
    sent as repeated query params (FastAPI style), not comma-joined.
    """

    title: str
    category: list[int]
    statuses: list[str]
    stock_gte: int
    stock_lte: int
    preparation_day_gte: int
    preparation_day_lte: int
    price_gte: int
    price_lte: int
    ids: list[int]
    without_tags: list[int]
    skus: list[str]
    illegal_free_shipping_for_iran: int
    illegal_free_shipping_for_same_city: int
    page: int
    per_page: int
    variants_flatting: bool
    is_wholesale: bool
    sort: str
