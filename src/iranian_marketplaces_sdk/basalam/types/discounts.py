"""TypedDicts for the Basalam vendor-discount endpoints.

The create endpoint responds ``202`` with an unspecified (``any``) body,
so the engine return type is ``object``.

NOTE: this package must NOT use ``from __future__ import annotations``.
"""

from typing import NotRequired, TypedDict

from .common import RangeInput

__all__ = [
    "ProductFilterSchema",
    "CreateVendorDiscountRequest",
    "DeleteVendorDiscountRequest",
]


class ProductFilterSchema(TypedDict, total=False):
    """Product selector for a vendor discount."""

    variation_ids: list[int] | None
    product_ids: list[int] | None
    status: list[str] | None
    stock: RangeInput | None
    price: RangeInput | None
    exclude: list[int] | None
    category_id: list[int] | None
    title: str | None


class CreateVendorDiscountRequest(TypedDict):
    """Request body for ``POST /v1/vendors/{vendor_id}/discounts``.

    ``product_filter`` is required but nullable.
    """

    product_filter: ProductFilterSchema | None
    discount_percent: int
    active_days: int
    decimal_discount_percent: NotRequired[float | None]


class DeleteVendorDiscountRequest(TypedDict):
    """Request body for ``DELETE /v1/vendors/{vendor_id}/discounts``.

    ``product_filter`` is required but nullable.
    """

    product_filter: ProductFilterSchema | None
