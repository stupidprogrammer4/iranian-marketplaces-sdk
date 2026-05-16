"""TypedDicts for the Digikala pricing / smart-discount endpoints."""

from typing import Literal, TypedDict

from .common import Pager, SortData

__all__ = [
    "SmartDiscountActiveStatus",
    "AutoJoined",
    "SmartDiscountVariant",
    "SmartDiscountVariantsData",
    "SmartDiscountVariantsResponse",
    "SmartDiscountVariantSearch",
    "SmartDiscountVariantInput",
    "CreateSmartDiscountVariantsRequest",
    "CreateSmartDiscountVariantsData",
    "CreateSmartDiscountVariantsResponse",
    "DeleteSmartDiscountVariantsRequest",
    "DeleteSmartDiscountVariantsResponse",
    "SmartDiscountBatchEditItem",
    "BatchEditSmartDiscountVariantsRequest",
    "BatchEditSmartDiscountVariantsResponse",
]

# The ``active_status`` path segment of the smart-discount endpoint.
SmartDiscountActiveStatus = Literal["active", "inactive"]


class AutoJoined(TypedDict):
    """Auto-join flags of a smart-discount variant."""

    normal: bool
    mega_promotion: bool


class SmartDiscountVariant(TypedDict):
    """A single variant with periodic (smart-discount) pricing."""

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


class SmartDiscountVariantsData(TypedDict):
    """The ``data`` payload of a smart-discount variants response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[SmartDiscountVariant]
    meta_data: dict[str, object]


class SmartDiscountVariantsResponse(TypedDict):
    """Full response body of the smart-discount variants endpoint."""

    status: str
    data: SmartDiscountVariantsData


class SmartDiscountVariantSearch(TypedDict, total=False):
    """Optional ``search[...]`` filters for the smart-discount endpoint.

    ``status`` is sent comma-joined. Valid values depend on the tab:
    ``["approved", "active"]`` for the active tab,
    ``["rejected", "ended"]`` for the inactive tab.
    """

    query: str
    # Sent comma-joined.
    status: list[str]
    startedAt: str
    endAt: str


class SmartDiscountVariantInput(TypedDict):
    """A single periodic-price entry in a smart-discount creation request."""

    variantId: int
    promotionPrice: int
    limit: int
    orderLimit: int
    startedAt: str
    endAt: str


class CreateSmartDiscountVariantsRequest(TypedDict):
    """Request body for ``POST /pricing/smart-discount/variants``."""

    data: list[SmartDiscountVariantInput]


class CreateSmartDiscountVariantsData(TypedDict):
    """The ``data`` payload of a smart-discount creation response."""

    id: int
    success: bool
    message: str


class CreateSmartDiscountVariantsResponse(TypedDict):
    """Full response body of ``POST /pricing/smart-discount/variants``."""

    status: str
    data: CreateSmartDiscountVariantsData


class DeleteSmartDiscountVariantsRequest(TypedDict):
    """Request body for ``DELETE /pricing/smart-discount/variants``."""

    variant_ids: list[int]


class DeleteSmartDiscountVariantsResponse(TypedDict):
    """Full response body of ``DELETE /pricing/smart-discount/variants``.

    The ``data`` payload is the same generic mutation result as the
    creation endpoint (:class:`CreateSmartDiscountVariantsData`).
    """

    status: str
    data: CreateSmartDiscountVariantsData


class SmartDiscountBatchEditItem(TypedDict):
    """A single edit group in a smart-discount batch-edit request."""

    promotionVariantIds: list[int]
    discount: int
    limit: int
    orderLimit: int
    startedAt: str
    endAt: str


class BatchEditSmartDiscountVariantsRequest(TypedDict):
    """Request body for ``PUT /pricing/smart-discount/variants/batch``."""

    variants: list[SmartDiscountBatchEditItem]


class BatchEditSmartDiscountVariantsResponse(TypedDict):
    """Full response body of ``PUT /pricing/smart-discount/variants/batch``.

    The ``data`` payload is the same generic mutation result as the
    creation endpoint (:class:`CreateSmartDiscountVariantsData`).
    """

    status: str
    data: CreateSmartDiscountVariantsData
