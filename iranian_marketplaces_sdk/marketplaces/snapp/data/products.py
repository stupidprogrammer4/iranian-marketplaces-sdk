"""Snapp Shop — the vendor-products endpoint.

``promotion`` and ``discount`` come back ``null`` in every documented sample and have no published
object schema, so they are typed as open dictionaries rather than invented.
"""

from typing import Any

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema, ResponseSchema
from iranian_marketplaces_sdk.marketplaces.snapp.data.common import Meta

__all__ = [
    "ProductAttribute",
    "ProductAttributeValue",
    "ProductUpdate",
    "ProductUpdateResult",
    "ProductVariationAttribute",
    "ProductWarranty",
    "VendorProduct",
    "VendorProductsQuery",
    "VendorProductsResponse",
]


class ProductWarranty(ResponseSchema):
    """Warranty info of a vendor product."""

    id: str
    title: str
    company_title: str
    duration: str
    description: str


class ProductAttribute(ResponseSchema):
    """The attribute side of a variation attribute — colour, size, and the like."""

    id: str
    title: str
    unit: str | None = None
    swatch_type: str


class ProductAttributeValue(ResponseSchema):
    """The value side of a variation attribute."""

    id: str
    title: str
    swatch_value: str | None = None


class ProductVariationAttribute(ResponseSchema):
    """A single variation attribute: the attribute and the value selected for it."""

    attribute: ProductAttribute
    value: ProductAttributeValue


class VendorProduct(ResponseSchema):
    """A single Snapp vendor product.

    ``stock`` is what the vendor holds; ``capacity`` caps what may be sold; ``warehouse_stock`` is
    what Snapp holds. ``buy_box`` and ``reference_price`` are the competitive position — what the
    winning offer costs, when this listing is not it.
    """

    id: str
    sku: str
    product_number: int
    parent_product_number: int
    active: bool
    capacity: int
    stock: int
    warehouse_stock: int
    title: str
    title_en: str | None = None
    thumbnail: str | None = None
    price: int
    warranty: ProductWarranty | None = None
    promotion: dict[str, Any] | None = None
    discount: dict[str, Any] | None = None
    variation_attributes: list[ProductVariationAttribute]
    created_at: str
    reference_price: int | None = None
    buy_box: int | None = None
    is_blacklist: bool


class VendorProductsResponse(ResponseSchema):
    """Full response body of ``GET /vendors/{seller_id}/products``."""

    status: bool
    data: list[VendorProduct]
    meta: Meta


class VendorProductsQuery(QuerySchema):
    """Query filters for the vendor-products endpoint."""

    category_id: str | None = None
    page: int | None = None
    per_page: int | None = None


class ProductUpdate(RequestSchema):
    """A single product change for the products PATCH (batch) endpoint.

    Both ``sku`` and ``id`` are required — Snapp matches on the pair. The special-price fields go
    together: a price with no window, or a window with no price, is rejected. Dates are
    ``%Y-%m-%d``.
    """

    sku: str
    id: str
    price: int
    stock: int
    special_price: str | None = None
    special_price_stock: int | None = None
    special_price_start_at: str | None = None
    special_price_end_at: str | None = None


class ProductUpdateResult(ResponseSchema):
    """Per-product result of the products PATCH (batch) endpoint.

    The batch is not atomic: each entry reports its own ``status``, so a partial success is normal
    and every element has to be checked. ``messages`` has no published element schema.
    """

    id: str
    sku: str
    status: bool
    messages: list[Any]
