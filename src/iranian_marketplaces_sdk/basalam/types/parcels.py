"""TypedDicts for the Basalam vendor-parcels endpoint.

Several nested objects have no published field schema and are typed as
``dict[str, object]`` deliberately (not invented, not ``Any``):
``vendor``, ``order``, ``status`` (EnumerationResponse), the shipping
``Method`` objects, parcel-item ``photos``, variation ``property``/
``value``, and the post-receipt ``attachment`` (FileResponse).

NOTE: this package must NOT use ``from __future__ import annotations``.
"""

from typing import NotRequired, TypedDict

__all__ = [
    "ParcelProductVariationProperty",
    "ParcelProductVariation",
    "ParcelProductSummary",
    "ParcelPostReceipt",
    "ParcelItem",
    "ParcelShippingMethod",
    "VendorParcel",
    "VendorParcelsResponse",
    "VendorParcelsQuery",
]


class ParcelProductVariationProperty(TypedDict):
    """A property/value pair of a parcel product variation.

    ``property`` and ``value`` have no published field schema.
    """

    property: dict[str, object]
    value: dict[str, object]


class ParcelProductVariation(TypedDict):
    """Variation info of a parcel item's product."""

    id: int
    properties: NotRequired[list[ParcelProductVariationProperty] | None]


class ParcelProductSummary(TypedDict):
    """Product summary of a parcel item.

    ``photos`` entries have no published field schema.
    """

    id: int
    category_id: int
    photos: list[dict[str, object]]
    name: NotRequired[str | None]
    variation: NotRequired[ParcelProductVariation | None]


class ParcelPostReceipt(TypedDict):
    """Post-receipt of a parcel item.

    ``attachment`` (Basalam ``FileResponse``) has no published field
    schema.
    """

    id: int
    created_at: str
    updated_at: str
    tracking_code: NotRequired[str | None]
    final_post_cost: NotRequired[int | None]
    tracking_link: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    attachment: NotRequired[dict[str, object] | None]


class ParcelItem(TypedDict):
    """A single item within a vendor parcel."""

    id: int
    title: str
    quantity: int
    weight: int
    price: int
    product: ParcelProductSummary
    editable: bool
    edited: bool
    net_weight: NotRequired[int | None]
    post_receipt: NotRequired[ParcelPostReceipt | None]


class ParcelShippingMethod(TypedDict):
    """Shipping method of a parcel.

    ``current`` / ``default`` (Basalam ``Method``) have no published
    field schema.
    """

    current: dict[str, object]
    default: dict[str, object]


class VendorParcel(TypedDict):
    """A single vendor parcel.

    ``vendor``, ``order`` and ``status`` have no published field schema.
    """

    id: int
    total_items_price: int
    created_at: str
    updated_at: str
    weight: int
    vendor: dict[str, object]
    order: dict[str, object]
    shipping_method: ParcelShippingMethod
    items: list[ParcelItem]
    is_freight_collect: NotRequired[bool]
    estimate_send_at: NotRequired[str | None]
    status: NotRequired[dict[str, object] | None]


class VendorParcelsResponse(TypedDict):
    """Full response body of ``GET /v1/vendor-parcels`` (cursor-paginated)."""

    data: list[VendorParcel]
    next_cursor: NotRequired[str | None]
    previous_cursor: NotRequired[str | None]


class VendorParcelsQuery(TypedDict, total=False):
    """Optional query filters for the vendor-parcels endpoint.

    Pythonic snake_case keys are mapped to Basalam's actual query keys by
    the engine (e.g. ``items_order_ids`` -> ``items.order_ids``,
    ``created_at_gte`` -> ``created_at[gte]``). All values are plain
    strings/ints as the API documents them.
    """

    ids: str
    items_customer_ids: str
    items_vendor_ids: str
    items_product_ids: str
    items_order_ids: str
    statuses: str
    estimate_send_at_gte: str
    estimate_send_at_lte: str
    created_at_gte: str
    created_at_lte: str
    sort: str
    per_page: int
    cursor: str
