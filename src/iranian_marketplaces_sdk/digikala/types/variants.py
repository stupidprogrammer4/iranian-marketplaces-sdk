"""TypedDicts for the Digikala variant endpoints."""

from typing import NotRequired, TypedDict

from .common import DigikalaDateTime, Pager, RateLimit, SortData

__all__ = [
    "SkuConfig",
    "B2BParams",
    "SellingChannel",
    "ShippingOptions",
    "SupplyCategory",
    "CategoryPriceConfigs",
    "GoldPriceParameters",
    "AutoPricing",
    "ThemeValueColor",
    "ThemeValueDetail",
    "ThemeValue",
    "Variant",
    "ReferencePrice",
    "VariantsMetaData",
    "VariantsData",
    "VariantsResponse",
    "VariantResponse",
    "UpdateVariantRequest",
    "UpdatedVariant",
    "UpdateVariantResponse",
    "UpdateVariantActivationRequest",
    "UpdateVariantActivationResponse",
    "VariantGoldData",
    "VariantGoldResponse",
    "VariantSellerStockData",
    "VariantSellerStockResponse",
    "UpdateVariantSellingPriceRequest",
    "UpdateVariantSellingPriceData",
    "UpdateVariantSellingPriceResponse",
    "UpdateVariantSellerStockRequest",
    "UpdateVariantSellerStockData",
    "UpdateVariantSellerStockResponse",
    "UpdateVariantGoldRequest",
    "UpdateVariantGoldData",
    "UpdateVariantGoldResponse",
    "VariantSearch",
]


class SkuConfig(TypedDict):
    """Color/size descriptor of a variant SKU (either may be ``null``)."""

    color: str | None
    size: str | None


class B2BParams(TypedDict):
    """Business-to-business flags of a variant."""

    seller_b2b_active: bool
    is_only_b2b: bool
    is_b2b_active: bool


class SellingChannel(TypedDict):
    """Per-channel activation flags (Digikala / Digistyle).

    Note: the API spells the key ``*_chanel`` (single 'n').
    """

    active_digikala: bool
    active_digistyle: bool


class ShippingOptions(TypedDict):
    """Fulfilment/shipping capability flags of a variant."""

    is_fbs_ability_enable: bool
    is_fbd_active: bool
    is_fbs_active: bool
    is_needed_fbs_setting: bool
    is_sbs_module_active: bool
    only_sbs: bool
    is_three_hour_delivery_active: bool
    # Absent from the variant-update (PUT) response.
    is_three_hour_checkbox_active: NotRequired[bool]


class SupplyCategory(TypedDict):
    """Supply category reference of a variant."""

    id: int
    title: str


class CategoryPriceConfigs(TypedDict):
    """Per-order quantity limits configured for the variant's category."""

    order_limit_minimum: int
    order_limit_maximum: int


class GoldPriceParameters(TypedDict):
    """Live gold-pricing parameters (present only for gold variants)."""

    goldProfit: float
    goldWage: float
    noneGoldWage: float
    noneGoldCost: float
    size: float
    tax: float
    isPure: bool
    liveGoldPrice: int
    isGold: bool


class AutoPricing(TypedDict):
    """Automatic pricing configuration of a variant."""

    category: str | None
    status: str


class ThemeValueColor(TypedDict):
    """Color representation inside a theme value."""

    hex: str
    rgb: str
    value: str


class ThemeValueDetail(TypedDict):
    """Resolved value of a single product theme/attribute."""

    id: int
    titleFa: str
    titleEn: str
    value: ThemeValueColor
    nature: str
    active: bool
    standardUnitID: int | None
    colorPallateIDs: object | None
    extraData: dict[str, object]


class ThemeValue(TypedDict):
    """A product theme/attribute attached to a variant."""

    themeId: int
    themeLabel: str
    active: bool
    themeType: str
    themeValue: ThemeValueDetail


class Variant(TypedDict):
    """A single seller variant.

    Fields marked :data:`~typing.NotRequired` are not returned consistently
    across products (e.g. gold-only or theme-only attributes).
    """

    id: int
    image_src: str
    seller_id: int
    main_category_title: str
    category_id: int
    product_id: int
    product_url: str
    product_variant_id: int
    supplier_code: str
    product_moderation_status: str
    title: str
    product_title: str
    active: bool
    lead_time: int
    price_list: int
    market_price_last_update: str
    price_type: str
    selling_channel_site: str
    price_sale: int
    cash_selling_price: int
    credit_selling_price: int
    credit_increase_percentage: float
    maximum_credit_increase_percentage: float
    marketplace_seller_stock: int
    warehouse_stock: int
    on_the_way_stock: int
    reservation: int
    left_consumer: int
    maximum_per_order: int
    allowed_count: int
    ovl_selling_active: bool
    # The list endpoint returns the object form; the documented schema example
    # uses an ISO-8601 string. Accept both.
    created_at: DigikalaDateTime | str
    pol_active: bool
    b2b_params: B2BParams
    max_lead_time: int
    buy_box_price: int | None
    buy_box_badge_label: str | None
    is_buy_box_winner: bool
    is_sku_winner: bool
    sku_config: SkuConfig
    is_seller_buy_box_winner: bool
    is_in_buy_box_challenge: bool
    suppressed_until: str | None
    suppression_reason: str | None
    product_selling_chanel: SellingChannel
    variant_selling_chanel: SellingChannel
    is_in_incredible_promotion: bool
    is_in_periodic_promotion: bool
    is_in_promotion: bool
    promotion_price: int | None
    shipping_nature_id: int
    default_selling_chanel_code: int
    rating: float | None
    is_promotion_management_visible_for_seller: bool
    is_archived: bool
    fulfilment_and_delivery_cost: int
    seller_reservation: int
    digikala_reservation: int
    seller_shipping_lead_time: int
    shipping_options: ShippingOptions
    supply_category: NotRequired[SupplyCategory]
    product_order_limit_minimum: NotRequired[int | None]
    category_price_configs: NotRequired[CategoryPriceConfigs]
    seller_product_tags: NotRequired[list[object]]
    min_selling_price_limit: NotRequired[int | None]
    gold_price_parameters: NotRequired[GoldPriceParameters | None]
    auto_pricing: NotRequired[AutoPricing]
    theme_values: NotRequired[list[ThemeValue]]


class ReferencePrice(TypedDict):
    """Reference price category ids inside variant list metadata."""

    printed: int
    recommended: int
    regulated: int


class VariantsMetaData(TypedDict, total=False):
    """Extra metadata of a variant list response (may be empty)."""

    leaf_categories: dict[str, str]
    reference_price: ReferencePrice
    rate_limit: RateLimit


class VariantsData(TypedDict):
    """The ``data`` payload of a variant list response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[Variant]
    meta_data: VariantsMetaData


class VariantsResponse(TypedDict):
    """Full response body returned by ``GET /variants``."""

    status: str
    data: VariantsData


class VariantResponse(TypedDict):
    """Full response body returned by ``GET /variants/{variant_id}``."""

    status: str
    data: Variant


class UpdateVariantRequest(TypedDict, total=False):
    """Request body for ``PUT /variants/{variant_id}`` (partial update)."""

    seller_stock: int
    maximum_per_order: int
    selling_price: int
    credit_increase_percentage: int
    shipping_type: str
    lead_time: int
    seller_lead_time: int
    activation: bool
    three_hour_delivery: bool


class UpdatedVariant(TypedDict):
    """Variant payload returned by ``PUT /variants/{variant_id}``.

    A narrower projection than :class:`Variant`: it omits fields like
    ``created_at`` / ``sku_config`` / ``cash_selling_price`` and adds
    ``min_selling_price_limit`` and ``credit_increase_percentage``.
    """

    id: int
    image_src: str
    seller_id: int
    main_category_title: str
    category_id: int
    product_id: int
    product_url: str
    product_variant_id: int
    supplier_code: str
    product_moderation_status: str
    title: str
    product_title: str
    active: bool
    lead_time: int
    price_list: int
    market_price_last_update: str
    price_type: str
    selling_channel_site: str
    price_sale: int
    marketplace_seller_stock: int
    warehouse_stock: int
    on_the_way_stock: int
    reservation: int
    left_consumer: int
    maximum_per_order: int
    allowed_count: int
    ovl_selling_active: bool
    b2b_params: B2BParams
    max_lead_time: int
    buy_box_price: int | None
    is_buy_box_winner: bool
    is_seller_buy_box_winner: bool
    is_in_buy_box_challenge: bool
    min_selling_price_limit: int | None
    # Present in the price-update response, absent from the activation one.
    credit_increase_percentage: NotRequired[float]
    product_selling_chanel: SellingChannel
    variant_selling_chanel: SellingChannel
    is_in_incredible_promotion: bool
    is_in_periodic_promotion: bool
    is_in_promotion: bool
    promotion_price: int | None
    shipping_nature_id: int
    default_selling_chanel_code: int
    rating: float | None
    is_promotion_management_visible_for_seller: bool
    is_archived: bool
    fulfilment_and_delivery_cost: int
    seller_reservation: int
    digikala_reservation: int
    seller_shipping_lead_time: int
    shipping_options: ShippingOptions


class UpdateVariantResponse(TypedDict):
    """Full response body returned by ``PUT /variants/{variant_id}``."""

    status: str
    data: UpdatedVariant


class UpdateVariantActivationRequest(TypedDict):
    """Request body for ``PUT /variants/{variant_id}/activation``."""

    activation: bool


class UpdateVariantActivationResponse(TypedDict):
    """Full response body returned by ``PUT /variants/{variant_id}/activation``.

    The ``data`` payload is the same projection as the variant-update
    response (:class:`UpdatedVariant`).
    """

    status: str
    data: UpdatedVariant


class VariantGoldData(TypedDict):
    """The ``data`` payload of ``GET /variants/{variant_id}/gold``."""

    gold_wage: float
    gold_profit: float
    none_gold_wage: float
    none_gold_cost: float
    is_pure: bool
    size: float
    tax: float
    live_gold_price: int


class VariantGoldResponse(TypedDict):
    """Full response body returned by ``GET /variants/{variant_id}/gold``."""

    status: str
    data: VariantGoldData


class VariantSellerStockData(TypedDict):
    """The ``data`` payload of ``GET /variants/{variant_id}/seller-stock``."""

    marketplace_seller_stock: int
    warehouse_stock: int
    on_the_way_stock: int
    reservation: int
    left_consumer: int
    seller_reservation: int
    digikala_reservation: int
    rate_limit: NotRequired[RateLimit]


class VariantSellerStockResponse(TypedDict):
    """Full response body of ``GET /variants/{variant_id}/seller-stock``."""

    status: str
    data: VariantSellerStockData


class UpdateVariantSellingPriceRequest(TypedDict):
    """Request body for ``PATCH /variants/selling-price``.

    ``credit_increase_percentage`` is optional; ``variant_id`` and
    ``selling_price`` are required by the API.
    """

    variant_id: int
    selling_price: int
    credit_increase_percentage: NotRequired[int]


class UpdateVariantSellingPriceData(TypedDict):
    """The ``data`` payload of a selling-price update response."""

    variant_id: int
    selling_price: int
    credit_increase_percentage: int


class UpdateVariantSellingPriceResponse(TypedDict):
    """Full response body returned by ``PATCH /variants/selling-price``."""

    status: str
    data: UpdateVariantSellingPriceData


class UpdateVariantSellerStockRequest(TypedDict):
    """Request body for ``PATCH /variants/{variant_id}/seller-stock``."""

    seller_stock: int


class UpdateVariantSellerStockData(TypedDict):
    """The ``data`` payload of a seller-stock update response."""

    selling_stock: int
    marketplace_seller_stock: int
    dk_warehouse_stock: int
    digikala_reservation: int
    seller_reservation: int


class UpdateVariantSellerStockResponse(TypedDict):
    """Full response body of ``PATCH /variants/{variant_id}/seller-stock``."""

    status: str
    data: UpdateVariantSellerStockData


class UpdateVariantGoldRequest(TypedDict):
    """Request body for ``PUT /variants/{variant_id}/gold``.

    ``none_gold_wage`` / ``none_gold_cost`` are optional; ``gold_wage``,
    ``gold_profit`` and ``order_limit`` are required by the API.
    """

    gold_wage: float
    gold_profit: float
    order_limit: int
    none_gold_wage: NotRequired[float]
    none_gold_cost: NotRequired[float]


class UpdateVariantGoldData(TypedDict):
    """The ``data`` payload of a variant gold-update response."""

    status: str
    did_b2b_deactivate: bool


class UpdateVariantGoldResponse(TypedDict):
    """Full response body returned by ``PUT /variants/{variant_id}/gold``."""

    status: str
    data: UpdateVariantGoldData


class VariantSearch(TypedDict, total=False):
    """Optional ``search[...]`` filters accepted by ``GET /variants``."""

    id: int
    # Sent underscore-joined (e.g. ``[1, 2] -> "1_2"``).
    ids: list[int]
    shipping_type: str
    active: bool
    moderation_status: str
    # Sent comma-joined.
    category_ids: list[int]
    buy_box_winner: str
    in_competition: bool
    search_term: str
    # Sent comma-joined.
    price_terms: list[str]
    out_of_stock: bool
    archived: bool
    selling_channel: str
    creation_time_from: str
    creation_time_to: str
    # Sent comma-joined.
    seller_product_tags: list[str]
    nearby_seller_shipment: bool
