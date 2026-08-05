"""Digikala — the variant endpoints (scope: ``variant``).

A *variant* is one sellable listing: a product, in one colour/size, offered by one seller. It is
where price, stock, lead time and buy-box position live, so this is the busiest scope in the API
and the one whose payloads are widest.

Fields declared ``| None = None`` are not returned consistently across products — gold pricing
only exists on gold variants, theme values only on products with attributes, and the update
endpoints answer with a narrower projection than the list one (:class:`UpdatedVariant`).
"""

from typing import Any

from pydantic import Field

from iranian_marketplaces_sdk.common.data import (
    CamelCaseResponseSchema,
    QuerySchema,
    RequestSchema,
    ResponseSchema,
)
from iranian_marketplaces_sdk.marketplaces.digikala.data.common import (
    DigikalaDateTime,
    Pager,
    RateLimit,
    SortData,
)

__all__ = [
    "AutoPricing",
    "B2BParams",
    "CategoryPriceConfigs",
    "GoldPriceParameters",
    "ReferencePrice",
    "SellingChannel",
    "ShippingOptions",
    "SkuConfig",
    "SupplyCategory",
    "ThemeValue",
    "ThemeValueColor",
    "ThemeValueDetail",
    "UpdateVariantActivationRequest",
    "UpdateVariantActivationResponse",
    "UpdateVariantGoldData",
    "UpdateVariantGoldRequest",
    "UpdateVariantGoldResponse",
    "UpdateVariantRequest",
    "UpdateVariantResponse",
    "UpdateVariantSellerStockData",
    "UpdateVariantSellerStockRequest",
    "UpdateVariantSellerStockResponse",
    "UpdateVariantSellingPriceData",
    "UpdateVariantSellingPriceRequest",
    "UpdateVariantSellingPriceResponse",
    "UpdatedVariant",
    "Variant",
    "VariantGoldData",
    "VariantGoldResponse",
    "VariantResponse",
    "VariantSearch",
    "VariantSellerStockData",
    "VariantSellerStockResponse",
    "VariantsData",
    "VariantsMetaData",
    "VariantsResponse",
]


class SkuConfig(ResponseSchema):
    """Colour/size descriptor of a variant SKU.

    Either may be ``null`` — a product with neither is a single, unvaried listing.
    """

    color: str | None = None
    size: str | None = None


class B2BParams(ResponseSchema):
    """Business-to-business flags of a variant."""

    seller_b2b_active: bool
    is_only_b2b: bool
    is_b2b_active: bool


class SellingChannel(ResponseSchema):
    """Per-channel activation flags (Digikala / Digistyle).

    Note the API's own spelling of the *field* that carries this object: ``*_selling_chanel``,
    with one 'n'. It is kept as sent.
    """

    active_digikala: bool
    active_digistyle: bool


class ShippingOptions(ResponseSchema):
    """Fulfilment and shipping capability flags of a variant.

    FBS is "fulfilled by seller", FBD "fulfilled by Digikala", SBS "shipped by seller".
    """

    is_fbs_ability_enable: bool
    is_fbd_active: bool
    is_fbs_active: bool
    is_needed_fbs_setting: bool
    is_sbs_module_active: bool
    only_sbs: bool
    is_three_hour_delivery_active: bool
    #: Absent from the variant-update (PUT) response.
    is_three_hour_checkbox_active: bool | None = None


class SupplyCategory(ResponseSchema):
    """Supply category reference of a variant."""

    id: int
    title: str


class CategoryPriceConfigs(ResponseSchema):
    """Per-order quantity limits configured for the variant's category."""

    order_limit_minimum: int
    order_limit_maximum: int


class GoldPriceParameters(CamelCaseResponseSchema):
    """Live gold-pricing parameters. Present only on gold variants.

    Digikala prices gold from the live bullion rate plus wage and profit rather than from a fixed
    number, so a gold variant's selling price is computed rather than set.
    """

    gold_profit: float
    gold_wage: float
    none_gold_wage: float
    none_gold_cost: float
    size: float
    tax: float
    is_pure: bool
    live_gold_price: int
    is_gold: bool


class AutoPricing(ResponseSchema):
    """Automatic pricing configuration of a variant."""

    category: str | None = None
    status: str


class ThemeValueColor(ResponseSchema):
    """Colour representation inside a theme value."""

    hex: str
    rgb: str
    value: str


class ThemeValueDetail(CamelCaseResponseSchema):
    """Resolved value of a single product theme/attribute.

    Two fields spell their id suffix ``ID`` rather than ``Id``, which no camelCase generator will
    produce, so those two say their wire name outright.
    """

    id: int
    title_fa: str
    title_en: str
    value: ThemeValueColor
    nature: str
    active: bool
    standard_unit_id: int | None = Field(
        default=None, validation_alias="standardUnitID", serialization_alias="standardUnitID"
    )
    #: Element schema is not published upstream; left untyped rather than invented.
    color_pallate_ids: Any = Field(
        default=None, validation_alias="colorPallateIDs", serialization_alias="colorPallateIDs"
    )
    extra_data: dict[str, Any] = Field(default_factory=dict)


class ThemeValue(CamelCaseResponseSchema):
    """A product theme/attribute attached to a variant."""

    theme_id: int
    theme_label: str
    active: bool
    theme_type: str
    theme_value: ThemeValueDetail


class Variant(ResponseSchema):
    """A single seller variant, as returned by ``GET /variants`` and ``GET /variants/{id}``."""

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
    #: The list endpoint returns the object form; the documented example uses an ISO-8601 string.
    #: Both are accepted.
    created_at: DigikalaDateTime | str
    pol_active: bool
    b2b_params: B2BParams
    max_lead_time: int
    buy_box_price: int | None = None
    buy_box_badge_label: str | None = None
    is_buy_box_winner: bool
    is_sku_winner: bool
    sku_config: SkuConfig
    is_seller_buy_box_winner: bool
    is_in_buy_box_challenge: bool
    suppressed_until: str | None = None
    suppression_reason: str | None = None
    product_selling_chanel: SellingChannel
    variant_selling_chanel: SellingChannel
    is_in_incredible_promotion: bool
    is_in_periodic_promotion: bool
    is_in_promotion: bool
    promotion_price: int | None = None
    shipping_nature_id: int
    default_selling_chanel_code: int
    rating: float | None = None
    is_promotion_management_visible_for_seller: bool
    is_archived: bool
    fulfilment_and_delivery_cost: int
    seller_reservation: int
    digikala_reservation: int
    seller_shipping_lead_time: int
    shipping_options: ShippingOptions
    supply_category: SupplyCategory | None = None
    product_order_limit_minimum: int | None = None
    category_price_configs: CategoryPriceConfigs | None = None
    #: Element schema is not published upstream.
    seller_product_tags: list[Any] | None = None
    min_selling_price_limit: int | None = None
    gold_price_parameters: GoldPriceParameters | None = None
    auto_pricing: AutoPricing | None = None
    theme_values: list[ThemeValue] | None = None


class ReferencePrice(ResponseSchema):
    """Reference price category ids inside variant list metadata."""

    printed: int
    recommended: int
    regulated: int


class VariantsMetaData(ResponseSchema):
    """Extra metadata of a variant list response. Every field may be absent."""

    leaf_categories: dict[str, str] | None = None
    reference_price: ReferencePrice | None = None
    rate_limit: RateLimit | None = None


class VariantsData(ResponseSchema):
    """The ``data`` payload of a variant list response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[Variant]
    meta_data: VariantsMetaData


class VariantsResponse(ResponseSchema):
    """Full response body returned by ``GET /variants``."""

    status: str
    data: VariantsData


class VariantResponse(ResponseSchema):
    """Full response body returned by ``GET /variants/{variant_id}``."""

    status: str
    data: Variant


class UpdateVariantRequest(RequestSchema):
    """Request body for ``PUT /variants/{variant_id}``.

    A partial update: only the fields you set are sent, so changing stock alone cannot
    accidentally reset a price.
    """

    seller_stock: int | None = None
    maximum_per_order: int | None = None
    selling_price: int | None = None
    credit_increase_percentage: int | None = None
    shipping_type: str | None = None
    lead_time: int | None = None
    seller_lead_time: int | None = None
    activation: bool | None = None
    three_hour_delivery: bool | None = None


class UpdatedVariant(ResponseSchema):
    """Variant payload returned by the variant update and activation endpoints.

    A narrower projection than :class:`Variant`: it omits ``created_at``, ``sku_config`` and
    ``cash_selling_price``, and adds ``min_selling_price_limit``.
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
    buy_box_price: int | None = None
    is_buy_box_winner: bool
    is_seller_buy_box_winner: bool
    is_in_buy_box_challenge: bool
    min_selling_price_limit: int | None = None
    #: Present in the price-update response, absent from the activation one.
    credit_increase_percentage: float | None = None
    product_selling_chanel: SellingChannel
    variant_selling_chanel: SellingChannel
    is_in_incredible_promotion: bool
    is_in_periodic_promotion: bool
    is_in_promotion: bool
    promotion_price: int | None = None
    shipping_nature_id: int
    default_selling_chanel_code: int
    rating: float | None = None
    is_promotion_management_visible_for_seller: bool
    is_archived: bool
    fulfilment_and_delivery_cost: int
    seller_reservation: int
    digikala_reservation: int
    seller_shipping_lead_time: int
    shipping_options: ShippingOptions


class UpdateVariantResponse(ResponseSchema):
    """Full response body returned by ``PUT /variants/{variant_id}``."""

    status: str
    data: UpdatedVariant


class UpdateVariantActivationRequest(RequestSchema):
    """Request body for ``PUT /variants/{variant_id}/activation``."""

    activation: bool


class UpdateVariantActivationResponse(ResponseSchema):
    """Full response body returned by ``PUT /variants/{variant_id}/activation``."""

    status: str
    data: UpdatedVariant


class VariantGoldData(ResponseSchema):
    """The ``data`` payload of ``GET /variants/{variant_id}/gold``.

    The same numbers as :class:`GoldPriceParameters`, under snake_case keys — this endpoint and
    the variant list disagree on spelling, and both are kept as sent.
    """

    gold_wage: float
    gold_profit: float
    none_gold_wage: float
    none_gold_cost: float
    is_pure: bool
    size: float
    tax: float
    live_gold_price: int


class VariantGoldResponse(ResponseSchema):
    """Full response body returned by ``GET /variants/{variant_id}/gold``."""

    status: str
    data: VariantGoldData


class VariantSellerStockData(ResponseSchema):
    """The ``data`` payload of ``GET /variants/{variant_id}/seller-stock``.

    ``marketplace_seller_stock`` is what you set; the rest is what Digikala has done with it —
    what is reserved against open orders, what is already in a Digikala warehouse, what is in
    transit.
    """

    marketplace_seller_stock: int
    warehouse_stock: int
    on_the_way_stock: int
    reservation: int
    left_consumer: int
    seller_reservation: int
    digikala_reservation: int
    rate_limit: RateLimit | None = None


class VariantSellerStockResponse(ResponseSchema):
    """Full response body of ``GET /variants/{variant_id}/seller-stock``."""

    status: str
    data: VariantSellerStockData


class UpdateVariantSellingPriceRequest(RequestSchema):
    """Request body for ``PATCH /variants/selling-price``.

    ``variant_id`` travels in the body, not the path — this is the one variant endpoint that does.
    """

    variant_id: int
    selling_price: int
    credit_increase_percentage: int | None = None


class UpdateVariantSellingPriceData(ResponseSchema):
    """The ``data`` payload of a selling-price update response."""

    variant_id: int
    selling_price: int
    credit_increase_percentage: int


class UpdateVariantSellingPriceResponse(ResponseSchema):
    """Full response body returned by ``PATCH /variants/selling-price``."""

    status: str
    data: UpdateVariantSellingPriceData


class UpdateVariantSellerStockRequest(RequestSchema):
    """Request body for ``PATCH /variants/{variant_id}/seller-stock``."""

    seller_stock: int


class UpdateVariantSellerStockData(ResponseSchema):
    """The ``data`` payload of a seller-stock update response."""

    selling_stock: int
    marketplace_seller_stock: int
    dk_warehouse_stock: int
    digikala_reservation: int
    seller_reservation: int


class UpdateVariantSellerStockResponse(ResponseSchema):
    """Full response body of ``PATCH /variants/{variant_id}/seller-stock``."""

    status: str
    data: UpdateVariantSellerStockData


class UpdateVariantGoldRequest(RequestSchema):
    """Request body for ``PUT /variants/{variant_id}/gold``."""

    gold_wage: float
    gold_profit: float
    order_limit: int
    none_gold_wage: float | None = None
    none_gold_cost: float | None = None


class UpdateVariantGoldData(ResponseSchema):
    """The ``data`` payload of a variant gold-update response.

    ``did_b2b_deactivate`` reports a side effect: switching a variant to gold pricing can turn its
    B2B offer off, and this is the only place that is said out loud.
    """

    status: str
    did_b2b_deactivate: bool


class UpdateVariantGoldResponse(ResponseSchema):
    """Full response body returned by ``PUT /variants/{variant_id}/gold``."""

    status: str
    data: UpdateVariantGoldData


class VariantSearch(QuerySchema):
    """The ``search[...]`` filters accepted by ``GET /variants``.

    The list-valued filters go up as one separated parameter, not repeated ones: ``ids`` is
    underscore-joined (``search[ids]=1_2_3``) and the rest comma-joined. Pass Python lists — the
    engine does the joining.
    """

    id: int | None = None
    ids: list[int] | None = None
    shipping_type: str | None = None
    active: bool | None = None
    moderation_status: str | None = None
    category_ids: list[int] | None = None
    buy_box_winner: str | None = None
    in_competition: bool | None = None
    search_term: str | None = None
    price_terms: list[str] | None = None
    out_of_stock: bool | None = None
    archived: bool | None = None
    selling_channel: str | None = None
    creation_time_from: str | None = None
    creation_time_to: str | None = None
    seller_product_tags: list[str] | None = None
    nearby_seller_shipment: bool | None = None
