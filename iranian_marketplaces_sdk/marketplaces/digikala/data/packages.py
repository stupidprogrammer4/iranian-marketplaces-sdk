"""Digikala — the package endpoints (scope: ``package``).

A *package* is one physical delivery of stock from the seller to a Digikala warehouse. The list
gives its status and its printable labels; the detail gives what is inside, down to the serial.

A few nested objects come back as a localized ``{key: title}`` map whose key is not stable, so they
are typed ``dict[str, str]`` rather than as a :class:`KeyTitle` that would promise more than the
API delivers.
"""

from iranian_marketplaces_sdk.common.data import QuerySchema, ResponseSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.common import KeyTitle, Pager, SortData

__all__ = [
    "PackageDetailData",
    "PackageDetailItem",
    "PackageDetailMetaData",
    "PackageDetailResponse",
    "PackageDetailSearch",
    "PackageFilters",
    "PackageItem",
    "PackageMetaData",
    "PackageProduct",
    "PackageProductSerial",
    "PackageReceived",
    "PackageSearch",
    "PackageStatusCount",
    "PackageTimeCope",
    "PackageWarehouse",
    "PackagesData",
    "PackagesResponse",
]


class PackageWarehouse(ResponseSchema):
    """Warehouse reference of a package."""

    id: int
    title: str


class PackageTimeCope(ResponseSchema):
    """Delivery time window of a package, as start/end hours."""

    start: int
    end: int


class PackageItem(ResponseSchema):
    """A single seller package.

    ``package_label_*_uri`` are the shipping labels: they must be printed and attached before the
    package is accepted at the warehouse.
    """

    package_id: int
    package_number: str
    type: KeyTitle
    shipping_nature: KeyTitle
    status: KeyTitle
    delivery_type: KeyTitle
    created_at: str
    received_at_forecast: str
    received_at: str
    warehouse: PackageWarehouse
    is_shippable_by_dk: bool
    time_cope: PackageTimeCope
    can_delete: bool
    show_print_label_package: bool
    show_print_label_serials: bool
    show_print_receive_receipt: bool
    package_label_html_uri: str
    package_label_pdf_uri: str


class PackageFilters(ResponseSchema):
    """The filter options this seller's package list actually offers."""

    package_delivery_types: list[KeyTitle]
    package_types: list[KeyTitle]
    package_statuses: list[KeyTitle]


class PackageMetaData(ResponseSchema):
    """Extra metadata of a package list response."""

    filters: PackageFilters | None = None
    is_shipment_allowed: bool | None = None


class PackagesData(ResponseSchema):
    """The ``data`` payload of a package list response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[PackageItem]
    meta_data: PackageMetaData


class PackagesResponse(ResponseSchema):
    """Full response body returned by ``GET /packages``."""

    status: str
    data: PackagesData


class PackageSearch(QuerySchema):
    """The ``search[...]`` filters accepted by ``GET /packages``. Dates use JS ISO format."""

    multi_search: str | int | None = None
    type: str | None = None
    status: str | None = None
    delivery_type: str | None = None
    package_created_at_from: str | None = None
    package_created_at_to: str | None = None
    package_received_at_from: str | None = None
    package_received_at_to: str | None = None


class PackageProductSerial(ResponseSchema):
    """A single serial inside a package product — one physical unit.

    ``status`` is a localized ``{key: title}`` map with a non-stable key.
    """

    id: int
    serial: str
    expiration_date: str
    production_date: str
    status: dict[str, str]
    show_print_label_package: bool


class PackageProduct(ResponseSchema):
    """A single product line inside a package.

    ``ordered_count`` versus ``delivered_count`` is the discrepancy the warehouse recorded on
    receipt — the number to reconcile against when a package settles short.
    """

    package_item_id: int
    title: str
    dkp: int
    product_link: str
    dkpc: int
    delivered_count: int
    ordered_count: int
    supplier_code: str
    serials: list[PackageProductSerial]
    image: str
    status: dict[str, str]


class PackageDetailItem(ResponseSchema):
    """A package-detail list item, grouping the package's products."""

    package_products: list[PackageProduct]


class PackageReceived(ResponseSchema):
    """Receipt detail of a package in the detail metadata."""

    date: str
    warehouse: PackageWarehouse
    time_scope: PackageTimeCope


class PackageStatusCount(ResponseSchema):
    """Per-status item count inside ``status_count`` metadata."""

    count: int
    title: str


class PackageDetailMetaData(ResponseSchema):
    """Extra metadata of a package-detail response.

    ``package_status`` and ``shipping_nature`` are localized ``{key: title}`` maps with non-stable
    keys.
    """

    package_id: int | None = None
    package_number: str | None = None
    package_delivery_type: KeyTitle | None = None
    seller_created: bool | None = None
    package_status: dict[str, str] | None = None
    package_received: PackageReceived | None = None
    shipping_nature: dict[str, str] | None = None
    status_count: dict[str, PackageStatusCount] | None = None
    show_export_receipt: bool | None = None
    package_label_html_uri: str | None = None
    package_label_pdf_uri: str | None = None


class PackageDetailData(ResponseSchema):
    """The ``data`` payload of a package-detail response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[PackageDetailItem]
    meta_data: PackageDetailMetaData


class PackageDetailResponse(ResponseSchema):
    """Full response body returned by ``GET /packages/{package_id}``."""

    status: str
    data: PackageDetailData


class PackageDetailSearch(QuerySchema):
    """The ``search[...]`` filters accepted by ``GET /packages/{package_id}``.

    ``status`` is a list, sent comma-joined. Values: ``new``, ``received``, ``partially_received``,
    ``rejected``, ``deleted``.
    """

    multi_search: str | None = None
    status: list[str] | None = None
