"""Basalam — the vendor-discount endpoints.

Both endpoints select the products to act on with the same filter object rather than a list of
ids, so a discount can be applied to "everything in this category under this price" in one call.
That cuts both ways: a filter that matches more than intended discounts more than intended, and
``exclude`` is the only way to carve items back out.

Both respond ``202`` with a body Basalam documents as unspecified, so the engines return the
decoded body as-is.
"""

from iranian_marketplaces_sdk.common.data import RequestSchema
from iranian_marketplaces_sdk.marketplaces.basalam.data.common import RangeInput

__all__ = [
    "CreateVendorDiscountRequest",
    "DeleteVendorDiscountRequest",
    "ProductFilterSchema",
]


class ProductFilterSchema(RequestSchema):
    """Which of the vendor's products a discount applies to.

    Fields combine as an AND. ``exclude`` removes ids from whatever the rest selected.
    """

    variation_ids: list[int] | None = None
    product_ids: list[int] | None = None
    status: list[str] | None = None
    stock: RangeInput | None = None
    price: RangeInput | None = None
    exclude: list[int] | None = None
    category_id: list[int] | None = None
    title: str | None = None


class CreateVendorDiscountRequest(RequestSchema):
    """Request body for ``POST /v1/vendors/{vendor_id}/discounts``.

    ``product_filter`` is required *and* nullable: passing ``None`` explicitly means every product
    the vendor has. Set it to ``None`` deliberately or not at all — leaving it unset omits the key,
    which the API rejects.

    ``active_days`` is how long the discount runs from now; there is no end date to set.
    """

    product_filter: ProductFilterSchema | None
    discount_percent: int
    active_days: int
    decimal_discount_percent: float | None = None


class DeleteVendorDiscountRequest(RequestSchema):
    """Request body for ``DELETE /v1/vendors/{vendor_id}/discounts``.

    Same selector semantics as the create call, including ``product_filter`` being required and
    nullable — ``None`` clears the discount on every product.
    """

    product_filter: ProductFilterSchema | None
