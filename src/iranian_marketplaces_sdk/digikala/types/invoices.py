"""TypedDicts for the Digikala invoice endpoints."""

from typing import Literal, NotRequired, TypedDict

from .common import DigikalaDateTime, KeyTitle, Pager, RateLimit, SortData

__all__ = [
    "InvoiceItem",
    "InvoicesMetaData",
    "InvoicesData",
    "InvoicesResponse",
    "InvoiceSearch",
    "InvoicePaymentMethod",
    "InvoiceEarlySettlement",
    "InvoiceNotation",
    "InvoiceNotationGroup",
    "InvoicePaymentDeficit",
    "InvoiceDetailData",
    "InvoiceDetailResponse",
    "InvoiceCalculationType",
    "InvoicePayMethod",
    "InvoiceFinancialItem",
    "InvoiceItemsMetaData",
    "InvoiceItemsData",
    "InvoiceItemsResponse",
    "InvoiceItemsSearch",
]

# The ``calculation_type`` path segment / FinancialNotation calc model.
InvoiceCalculationType = Literal[
    "dimension_based",
    "fixed",
    "package_based",
    "category_based",
    "order_based",
]


class InvoiceItem(TypedDict):
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


class InvoicesMetaData(TypedDict, total=False):
    """Extra metadata of an invoice list response."""

    last_updated_at: str


class InvoicesData(TypedDict):
    """The ``data`` payload of an invoice list response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[InvoiceItem]
    meta_data: InvoicesMetaData


class InvoicesResponse(TypedDict):
    """Full response body returned by ``GET /invoices``."""

    status: str
    data: InvoicesData


class InvoiceSearch(TypedDict, total=False):
    """Optional ``search[...]`` filters accepted by ``GET /invoices``.

    Date fields use ISO format.
    """

    payout_order_status: int
    invoice_start_date: str
    invoice_end_date: str


class InvoicePaymentMethod(TypedDict):
    """Cash/credit payment summary inside an invoice detail."""

    maturity_date: str | None
    total_amount: int
    status: KeyTitle


class InvoiceEarlySettlement(TypedDict):
    """Early-settlement detail of an invoice.

    ``amount`` is returned by the API as a numeric string.
    """

    status: str
    amount: str
    created_at: str
    settlement_date: str


class InvoiceNotation(TypedDict):
    """A single notation line inside an invoice notation group."""

    id: int
    title: str
    item_count: int
    total_amount: int
    general_discount_credit: int | None
    general_discount_debit: int | None
    calculation_model_type: str
    is_vat_free: bool


class InvoiceNotationGroup(TypedDict):
    """A group of notations (sales / sales_return / others)."""

    notations: list[InvoiceNotation]
    total_amount: int


class InvoicePaymentDeficit(TypedDict):
    """Payment-deficit breakdown of an invoice detail."""

    sales_amount: int
    sales_return_amount: int
    others_amount: int
    total_amount: int


class InvoiceDetailData(TypedDict):
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


class InvoiceDetailResponse(TypedDict):
    """Full response body of ``GET /invoices/{invoice_id}/details``."""

    status: str
    data: InvoiceDetailData


class InvoicePayMethod(TypedDict):
    """Payment method of a financial item (both fields may be ``null``)."""

    key: str | None
    title: str | None


class InvoiceFinancialItem(TypedDict):
    """A single financial line of an invoice notation.

    The response shape is shared across calculation types; fields marked
    :data:`~typing.NotRequired` only appear for some of them (e.g.
    ``variant_*``/``item_serial`` are absent from ``package_based``,
    ``cancellation_description`` only appears for ``order_based``).
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
    variant_code: NotRequired[str]
    variant_title: NotRequired[str]
    order_id: NotRequired[int | None]
    item_serial: NotRequired[str]
    pay_method: NotRequired[InvoicePayMethod]
    cancellation_description: NotRequired[str]


class InvoiceItemsMetaData(TypedDict):
    """Extra metadata of an invoice financial-items response."""

    from_date: DigikalaDateTime
    to_date: DigikalaDateTime
    business_name: str
    financial_notation: str


class InvoiceItemsData(TypedDict):
    """The ``data`` payload of an invoice financial-items response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[InvoiceFinancialItem]
    meta_data: InvoiceItemsMetaData
    rate_limit: NotRequired[RateLimit]


class InvoiceItemsResponse(TypedDict):
    """Full response body of the invoice financial-items endpoint."""

    status: str
    data: InvoiceItemsData


class InvoiceItemsSearch(TypedDict, total=False):
    """Optional ``search[...]`` filters for the invoice items endpoint."""

    invoice_id: int
    financial_notation_id: int
    calculation_type: str
