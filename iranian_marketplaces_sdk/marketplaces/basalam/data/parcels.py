"""Basalam — the vendor-parcels endpoint.

A *parcel* is what the vendor actually ships: the items of one order that travel together, with
their shipping method and post receipt.

Several nested objects have no published field schema and are left as open dictionaries rather
than invented: ``vendor``, ``order``, ``status`` (Basalam's ``EnumerationResponse``), the shipping
``Method`` objects, a parcel item's ``photos``, a variation's ``property``/``value``, and the post
receipt's ``attachment`` (``FileResponse``).
"""

from typing import Any

from iranian_marketplaces_sdk.common.data import QuerySchema, ResponseSchema

__all__ = [
    "ParcelItem",
    "ParcelPostReceipt",
    "ParcelProductSummary",
    "ParcelProductVariation",
    "ParcelProductVariationProperty",
    "ParcelShippingMethod",
    "VendorParcel",
    "VendorParcelsQuery",
    "VendorParcelsResponse",
]


class ParcelProductVariationProperty(ResponseSchema):
    """A property/value pair of a parcel product variation."""

    property: dict[str, Any]
    value: dict[str, Any]


class ParcelProductVariation(ResponseSchema):
    """Variation info of a parcel item's product — which colour/size actually shipped."""

    id: int
    properties: list[ParcelProductVariationProperty] | None = None


class ParcelProductSummary(ResponseSchema):
    """Product summary of a parcel item."""

    id: int
    category_id: int
    photos: list[dict[str, Any]]
    name: str | None = None
    variation: ParcelProductVariation | None = None


class ParcelPostReceipt(ResponseSchema):
    """Post-receipt of a parcel item — the proof of postage.

    ``tracking_code`` is what the customer follows; ``final_post_cost`` is what the vendor is
    actually charged, which is settled after the parcel is weighed and may differ from the
    estimate.
    """

    id: int
    created_at: str
    updated_at: str
    tracking_code: str | None = None
    final_post_cost: int | None = None
    tracking_link: str | None = None
    phone_number: str | None = None
    attachment: dict[str, Any] | None = None


class ParcelItem(ResponseSchema):
    """A single item within a vendor parcel."""

    id: int
    title: str
    quantity: int
    weight: int
    price: int
    product: ParcelProductSummary
    editable: bool
    edited: bool
    net_weight: int | None = None
    post_receipt: ParcelPostReceipt | None = None


class ParcelShippingMethod(ResponseSchema):
    """Shipping method of a parcel: the one in force, and the vendor's default."""

    current: dict[str, Any]
    default: dict[str, Any]


class VendorParcel(ResponseSchema):
    """A single vendor parcel.

    ``is_freight_collect`` decides who pays the courier: when true, the customer pays on delivery
    rather than the vendor at postage.
    """

    id: int
    total_items_price: int
    created_at: str
    updated_at: str
    weight: int
    vendor: dict[str, Any]
    order: dict[str, Any]
    shipping_method: ParcelShippingMethod
    items: list[ParcelItem]
    is_freight_collect: bool | None = None
    estimate_send_at: str | None = None
    status: dict[str, Any] | None = None


class VendorParcelsResponse(ResponseSchema):
    """Full response body of ``GET /v1/vendor-parcels``. Cursor-paginated."""

    data: list[VendorParcel]
    next_cursor: str | None = None
    previous_cursor: str | None = None


class VendorParcelsQuery(QuerySchema):
    """Query filters for the vendor-parcels endpoint.

    The pythonic names here are mapped to Basalam's own by the engine — ``items_order_ids`` becomes
    ``items.order_ids`` and ``created_at_gte`` becomes ``created_at[gte]``. The id filters are
    documented as strings (comma-separated lists), not arrays, and are passed through as sent.
    """

    ids: str | None = None
    items_customer_ids: str | None = None
    items_vendor_ids: str | None = None
    items_product_ids: str | None = None
    items_order_ids: str | None = None
    statuses: str | None = None
    estimate_send_at_gte: str | None = None
    estimate_send_at_lte: str | None = None
    created_at_gte: str | None = None
    created_at_lte: str | None = None
    sort: str | None = None
    per_page: int | None = None
    cursor: str | None = None
