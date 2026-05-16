"""TypedDicts for the Digikala package endpoints (list + detail)."""

from typing import TypedDict

from .common import KeyTitle, Pager, SortData

__all__ = [
    "PackageWarehouse",
    "PackageTimeCope",
    "PackageItem",
    "PackageFilters",
    "PackageMetaData",
    "PackagesData",
    "PackagesResponse",
    "PackageSearch",
    "PackageProductSerial",
    "PackageProduct",
    "PackageDetailItem",
    "PackageReceived",
    "PackageStatusCount",
    "PackageDetailMetaData",
    "PackageDetailData",
    "PackageDetailResponse",
    "PackageDetailSearch",
]


class PackageWarehouse(TypedDict):
    """Warehouse reference of a package."""

    id: int
    title: str


class PackageTimeCope(TypedDict):
    """Delivery time window of a package."""

    start: int
    end: int


class PackageItem(TypedDict):
    """A single seller package."""

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


class PackageFilters(TypedDict):
    """Available package filter options inside list metadata."""

    package_delivery_types: list[KeyTitle]
    package_types: list[KeyTitle]
    package_statuses: list[KeyTitle]


class PackageMetaData(TypedDict, total=False):
    """Extra metadata of a package list response."""

    filters: PackageFilters
    is_shipment_allowed: bool


class PackagesData(TypedDict):
    """The ``data`` payload of a package list response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[PackageItem]
    meta_data: PackageMetaData


class PackagesResponse(TypedDict):
    """Full response body returned by ``GET /packages``."""

    status: str
    data: PackagesData


class PackageSearch(TypedDict, total=False):
    """Optional ``search[...]`` filters accepted by ``GET /packages``.

    Date fields use JS ISO format.
    """

    multi_search: str | int
    type: str
    status: str
    delivery_type: str
    package_created_at_from: str
    package_created_at_to: str
    package_received_at_from: str
    package_received_at_to: str


class PackageProductSerial(TypedDict):
    """A single serial inside a package product.

    ``status`` is modelled as a free-form ``{str: str}`` map because the
    upstream schema returns a localized, non-stable key.
    """

    id: int
    serial: str
    expiration_date: str
    production_date: str
    status: dict[str, str]
    show_print_label_package: bool


class PackageProduct(TypedDict):
    """A single product line inside a package."""

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


class PackageDetailItem(TypedDict):
    """A package-detail list item (groups the package products)."""

    package_products: list[PackageProduct]


class PackageReceived(TypedDict):
    """Receipt detail of a package in the detail metadata."""

    date: str
    warehouse: PackageWarehouse
    time_scope: PackageTimeCope


class PackageStatusCount(TypedDict):
    """Per-status item count inside ``status_count`` metadata."""

    count: int
    title: str


class PackageDetailMetaData(TypedDict, total=False):
    """Extra metadata of a package-detail response.

    ``package_status`` / ``shipping_nature`` use free-form ``{str: str}``
    maps because the upstream schema keys are localized/non-stable.
    """

    package_id: int
    package_number: str
    package_delivery_type: KeyTitle
    seller_created: bool
    package_status: dict[str, str]
    package_received: PackageReceived
    shipping_nature: dict[str, str]
    status_count: dict[str, PackageStatusCount]
    show_export_receipt: bool
    package_label_html_uri: str
    package_label_pdf_uri: str


class PackageDetailData(TypedDict):
    """The ``data`` payload of a package-detail response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[PackageDetailItem]
    meta_data: PackageDetailMetaData


class PackageDetailResponse(TypedDict):
    """Full response body returned by ``GET /packages/{package_id}``."""

    status: str
    data: PackageDetailData


class PackageDetailSearch(TypedDict, total=False):
    """Optional ``search[...]`` filters accepted by ``GET /packages/{id}``.

    ``status`` is a comma-separated list of: ``new``, ``received``,
    ``partially_received``, ``rejected``, ``deleted``.
    """

    multi_search: str
    # Sent comma-joined.
    status: list[str]
