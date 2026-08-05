"""Digikala — the pricing / smart-discount endpoints (scope: ``promotion``).

A *smart discount* is a promotional price on a variant, live for a window and capped at a quantity.
This scope is the one place in the Seller Open API that speaks camelCase, so its request models
carry aliases: Python stays snake_case, the wire stays exactly what Digikala documented.
"""

from typing import Any, Literal

from iranian_marketplaces_sdk.common.data import (
    CamelCaseQuerySchema,
    CamelCaseRequestSchema,
    RequestSchema,
    ResponseSchema,
)
from iranian_marketplaces_sdk.marketplaces.digikala.data.common import Pager, SortData

__all__ = [
    "AutoJoined",
    "BatchEditSmartDiscountVariantsRequest",
    "BatchEditSmartDiscountVariantsResponse",
    "CreateSmartDiscountVariantsData",
    "CreateSmartDiscountVariantsRequest",
    "CreateSmartDiscountVariantsResponse",
    "DeleteSmartDiscountVariantsRequest",
    "DeleteSmartDiscountVariantsResponse",
    "SmartDiscountActiveStatus",
    "SmartDiscountBatchEditItem",
    "SmartDiscountVariant",
    "SmartDiscountVariantInput",
    "SmartDiscountVariantSearch",
    "SmartDiscountVariantsData",
    "SmartDiscountVariantsResponse",
]

SmartDiscountActiveStatus = Literal["active", "inactive"]
"""The ``active_status`` path segment. It also decides which ``status`` filter values are valid:
``approved``/``active`` on the active tab, ``rejected``/``ended`` on the inactive one."""


class AutoJoined(ResponseSchema):
    """Auto-join flags of a smart-discount variant."""

    normal: bool
    mega_promotion: bool


class SmartDiscountVariant(ResponseSchema):
    """A single variant with periodic (smart-discount) pricing.

    ``max_allowable_price`` is the ceiling Digikala will accept for this variant's promotion, and
    ``min_discount`` the floor it must clear to qualify.
    """

    promotion_variant_id: int
    variant_id: int
    variant_price_id: int
    product_id: int
    product_link: str
    selling_price: int
    rrp_price: int
    cash_selling_price: int
    cash_rrp_price: int
    cash_discount: int
    credit_selling_price: int
    credit_rrp_price: int
    credit_discount: int
    credit_increase_percentage: int
    selling_stock: int
    promotion_price: int
    limit: int
    order_limit: int
    discount: int
    min_discount: int
    max_allowable_price: int
    title: str
    platform: str
    promotion_status: str
    started_at: str
    end_at: str
    image_link: str
    auto_joined: AutoJoined
    can_join_to_mega_promotion: bool
    incentive: bool


class SmartDiscountVariantsData(ResponseSchema):
    """The ``data`` payload of a smart-discount variants response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[SmartDiscountVariant]
    meta_data: dict[str, Any]


class SmartDiscountVariantsResponse(ResponseSchema):
    """Full response body of the smart-discount variants endpoint."""

    status: str
    data: SmartDiscountVariantsData


class SmartDiscountVariantSearch(CamelCaseQuerySchema):
    """The ``search[...]`` filters for the smart-discount endpoint.

    ``status`` is a list, sent comma-joined. Which values are valid depends on the ``active_status``
    in the path — see :data:`SmartDiscountActiveStatus`.
    """

    query: str | None = None
    status: list[str] | None = None
    started_at: str | None = None
    end_at: str | None = None


class SmartDiscountVariantInput(CamelCaseRequestSchema):
    """A single periodic-price entry in a smart-discount creation request."""

    variant_id: int
    promotion_price: int
    limit: int
    order_limit: int
    started_at: str
    end_at: str


class CreateSmartDiscountVariantsRequest(RequestSchema):
    """Request body for ``POST /pricing/smart-discount/variants``.

    Applied atomically: one rejected entry rejects the batch, so a partial promotion never goes
    live.
    """

    data: list[SmartDiscountVariantInput]


class CreateSmartDiscountVariantsData(ResponseSchema):
    """The generic mutation result the smart-discount write endpoints return."""

    id: int
    success: bool
    message: str


class CreateSmartDiscountVariantsResponse(ResponseSchema):
    """Full response body of ``POST /pricing/smart-discount/variants``."""

    status: str
    data: CreateSmartDiscountVariantsData


class DeleteSmartDiscountVariantsRequest(RequestSchema):
    """Request body for ``DELETE /pricing/smart-discount/variants``."""

    variant_ids: list[int]


class DeleteSmartDiscountVariantsResponse(ResponseSchema):
    """Full response body of ``DELETE /pricing/smart-discount/variants``."""

    status: str
    data: CreateSmartDiscountVariantsData


class SmartDiscountBatchEditItem(CamelCaseRequestSchema):
    """A single edit group in a smart-discount batch-edit request.

    One set of terms applied to many promotions at once — which is why it takes
    ``promotion_variant_ids`` (from the list response) rather than variant ids.
    """

    promotion_variant_ids: list[int]
    discount: int
    limit: int
    order_limit: int
    started_at: str
    end_at: str


class BatchEditSmartDiscountVariantsRequest(RequestSchema):
    """Request body for ``PUT /pricing/smart-discount/variants/batch``."""

    variants: list[SmartDiscountBatchEditItem]


class BatchEditSmartDiscountVariantsResponse(ResponseSchema):
    """Full response body of ``PUT /pricing/smart-discount/variants/batch``."""

    status: str
    data: CreateSmartDiscountVariantsData
