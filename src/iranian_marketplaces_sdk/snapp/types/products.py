"""TypedDicts for the Snapp vendor-products endpoint.

``promotion`` / ``discount`` are ``null`` in the sample with no published
object schema, so they are typed ``dict[str, object] | None`` deliberately
(not invented, not ``Any``).

NOTE: this package must NOT use ``from __future__ import annotations``.
"""

from typing import NotRequired, TypedDict

from .common import Meta

__all__ = [
    "ProductWarranty",
    "ProductAttribute",
    "ProductAttributeValue",
    "ProductVariationAttribute",
    "VendorProduct",
    "VendorProductsResponse",
    "VendorProductsQuery",
    "ProductUpdate",
    "ProductUpdateResult",
]


class ProductWarranty(TypedDict):
    """Warranty info of a vendor product."""

    id: str
    title: str
    company_title: str
    duration: str
    description: str


class ProductAttribute(TypedDict):
    """The attribute side of a variation attribute."""

    id: str
    title: str
    unit: str | None
    swatch_type: str


class ProductAttributeValue(TypedDict):
    """The value side of a variation attribute."""

    id: str
    title: str
    swatch_value: str | None


class ProductVariationAttribute(TypedDict):
    """A single variation attribute (attribute + selected value)."""

    attribute: ProductAttribute
    value: ProductAttributeValue


class VendorProduct(TypedDict):
    """A single Snapp vendor product."""

    id: str
    sku: str
    product_number: int
    parent_product_number: int
    active: bool
    capacity: int
    stock: int
    warehouse_stock: int
    title: str
    title_en: str | None
    thumbnail: str | None
    price: int
    warranty: ProductWarranty | None
    promotion: dict[str, object] | None
    discount: dict[str, object] | None
    variation_attributes: list[ProductVariationAttribute]
    created_at: str
    reference_price: int | None
    buy_box: int | None
    is_blacklist: bool


class VendorProductsResponse(TypedDict):
    """Full response body of ``GET /vendors/{seller_id}/products``."""

    status: bool
    data: list[VendorProduct]
    meta: Meta


class VendorProductsQuery(TypedDict, total=False):
    """Optional query filters for the vendor-products endpoint."""

    category_id: str
    page: int
    per_page: int


class ProductUpdate(TypedDict):
    """A single product change for the products PATCH (batch) endpoint.

    ``special_price_start_at`` / ``special_price_end_at`` use the
    ``%Y-%m-%d`` format.
    """

    sku: str
    id: str
    price: int
    stock: int
    special_price: NotRequired[str | None]
    special_price_stock: NotRequired[int | None]
    special_price_start_at: NotRequired[str | None]
    special_price_end_at: NotRequired[str | None]


class ProductUpdateResult(TypedDict):
    """Per-product result of the products PATCH (batch) endpoint.

    ``messages`` element schema is not documented; typed ``list[object]``.
    """

    id: str
    sku: str
    status: bool
    messages: list[object]
