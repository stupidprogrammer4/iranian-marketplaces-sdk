"""Digikala — the invoice endpoints (scope: ``invoice``).

Three levels, each one drilling into the last: the invoice list, one invoice's summary broken down
into notation groups, and the individual financial lines behind a single notation. The last needs
all three of ``invoice_id``, ``financial_notation_id`` and ``calculation_type`` in its path, and
the second is where you find the notation ids to pass.
"""

from typing import Literal

from iranian_marketplaces_sdk.common.data import QuerySchema, ResponseSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.common import (
    DigikalaDateTime,
    KeyTitle,
    Pager,
    RateLimit,
    SortData,
)

__all__ = [
    "InvoiceCalculationType",
    "InvoiceDetailData",
    "InvoiceDetailResponse",
    "InvoiceEarlySettlement",
    "InvoiceFinancialItem",
    "InvoiceItem",
    "InvoiceItemsData",
    "InvoiceItemsMetaData",
    "InvoiceItemsResponse",
    "InvoiceItemsSearch",
    "InvoiceNotation",
    "InvoiceNotationGroup",
    "InvoicePayMethod",
    "InvoicePaymentDeficit",
    "InvoicePaymentMethod",
    "InvoiceSearch",
    "InvoicesData",
    "InvoicesMetaData",
    "InvoicesResponse",
]

InvoiceCalculationType = Literal[
    "dimension_based",
    "fixed",
    "package_based",
    "category_based",
    "order_based",
]
"""How a notation's amount was computed. Also the last path segment of the items endpoint, and it
decides which optional fields :class:`InvoiceFinancialItem` comes back with."""


class InvoiceItem(ResponseSchema):
    """A single seller invoice."""

    id: int
    start_date: str
    end_date: str
    cash_sale_date: str
    credit_sale_date: str
    invoice_total_amount: int
    payout_order_status: KeyTitle
    settlement_status: KeyTitle
    show_early_settlement: bool
    can_print: bool
    is_new: bool


class InvoicesMetaData(ResponseSchema):
    """Extra metadata of an invoice list response."""

    last_updated_at: str | None = None


class InvoicesData(ResponseSchema):
    """The ``data`` payload of an invoice list response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[InvoiceItem]
    meta_data: InvoicesMetaData


class InvoicesResponse(ResponseSchema):
    """Full response body returned by ``GET /invoices``."""

    status: str
    data: InvoicesData


class InvoiceSearch(QuerySchema):
    """The ``search[...]`` filters accepted by ``GET /invoices``. Dates are ISO format."""

    payout_order_status: int | None = None
    invoice_start_date: str | None = None
    invoice_end_date: str | None = None


class InvoicePaymentMethod(ResponseSchema):
    """Cash or credit payment summary inside an invoice detail."""

    maturity_date: str | None = None
    total_amount: int
    status: KeyTitle


class InvoiceEarlySettlement(ResponseSchema):
    """Early-settlement detail of an invoice.

    ``amount`` arrives as a numeric *string* — Digikala sends it that way, and it is kept that way
    rather than silently coerced.
    """

    status: str
    amount: str
    created_at: str
    settlement_date: str


class InvoiceNotation(ResponseSchema):
    """A single notation line inside an invoice notation group.

    ``id`` is the ``financial_notation_id`` the items endpoint needs, and
    ``calculation_model_type`` its ``calculation_type``.
    """

    id: int
    title: str
    item_count: int
    total_amount: int
    general_discount_credit: int | None = None
    general_discount_debit: int | None = None
    calculation_model_type: str
    is_vat_free: bool


class InvoiceNotationGroup(ResponseSchema):
    """A group of notations: sales, sales returns, or everything else."""

    notations: list[InvoiceNotation]
    total_amount: int


class InvoicePaymentDeficit(ResponseSchema):
    """Payment-deficit breakdown of an invoice detail."""

    sales_amount: int
    sales_return_amount: int
    others_amount: int
    total_amount: int


class InvoiceDetailData(ResponseSchema):
    """The ``data`` payload of ``GET /invoices/{invoice_id}/details``."""

    start_date: str
    end_date: str
    show_early_settlement: bool
    vat_amount: int
    show_income_factor: bool
    can_print: bool
    cash: InvoicePaymentMethod
    credit: InvoicePaymentMethod
    total_income: int
    total_paid_amount: int
    payout_order_status: KeyTitle
    early_settlement: InvoiceEarlySettlement
    sales: InvoiceNotationGroup
    sales_return: InvoiceNotationGroup
    others: InvoiceNotationGroup
    payment_deficit: InvoicePaymentDeficit


class InvoiceDetailResponse(ResponseSchema):
    """Full response body of ``GET /invoices/{invoice_id}/details``."""

    status: str
    data: InvoiceDetailData


class InvoicePayMethod(ResponseSchema):
    """Payment method of a financial item. Both fields may be ``null``."""

    key: str | None = None
    title: str | None = None


class InvoiceFinancialItem(ResponseSchema):
    """A single financial line of an invoice notation.

    One response shape covers every calculation type, so the optional fields are the ones that
    only some types carry: ``variant_*`` and ``item_serial`` are absent from ``package_based``,
    and ``cancellation_description`` only appears for ``order_based``.
    """

    id: int
    event_datetime: DigikalaDateTime
    credit: int
    debit: int
    general_discount_credit: int
    general_discount_debit: int
    final_credit: int
    final_debit: int
    description: str
    calculation_model_type: str
    variant_code: str | None = None
    variant_title: str | None = None
    order_id: int | None = None
    item_serial: str | None = None
    pay_method: InvoicePayMethod | None = None
    cancellation_description: str | None = None


class InvoiceItemsMetaData(ResponseSchema):
    """Extra metadata of an invoice financial-items response."""

    from_date: DigikalaDateTime
    to_date: DigikalaDateTime
    business_name: str
    financial_notation: str


class InvoiceItemsData(ResponseSchema):
    """The ``data`` payload of an invoice financial-items response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[InvoiceFinancialItem]
    meta_data: InvoiceItemsMetaData
    rate_limit: RateLimit | None = None


class InvoiceItemsResponse(ResponseSchema):
    """Full response body of the invoice financial-items endpoint."""

    status: str
    data: InvoiceItemsData


class InvoiceItemsSearch(QuerySchema):
    """The ``search[...]`` filters accepted by the invoice items endpoint.

    These repeat the path segments; the API accepts them as filters as well.
    """

    invoice_id: int | None = None
    financial_notation_id: int | None = None
    calculation_type: str | None = None
