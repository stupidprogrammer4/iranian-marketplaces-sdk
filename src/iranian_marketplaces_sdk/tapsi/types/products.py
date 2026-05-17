"""TypedDicts for the Tapsi vendor-products endpoint.

JSON keys mirror the API exactly (``specialPrice``, ``referenceCode``,
``currentOriginalPrice``, ...). ``specialPrice`` is optional per the API.

NOTE: this package must NOT use ``from __future__ import annotations``.
"""

from typing import NotRequired, TypedDict

from .common import ApiMessage

__all__ = [
    "ProductUpdate",
    "ProductUpdatePayload",
    "ProductUpdateResultItem",
    "ProductUpdateData",
    "ProductUpdateResponse",
    "Product",
    "ProductsPage",
    "ProductsResponse",
]


class ProductUpdate(TypedDict):
    """A single product change for ``PUT /web/hub/vendors/v1/products``.

    ``id`` is the product's SKU on Tapsi. ``specialPrice`` is optional.
    ``referenceCode`` is a caller-supplied tracking code echoed back in the
    per-product result.
    """

    id: str
    stock: int
    price: int
    specialPrice: NotRequired[int | None]
    referenceCode: str


class ProductUpdatePayload(TypedDict):
    """Request body wrapper for the products PUT (batch) endpoint."""

    products: list[ProductUpdate]


class ProductUpdateResultItem(TypedDict):
    """Per-product result of the products PUT (batch) endpoint."""

    id: str
    sku: str
    status: bool
    messages: list[str]
    currentOriginalPrice: int
    currentFinalPrice: int
    currentOnHandQuantity: int
    referenceCode: str


class ProductUpdateData(TypedDict):
    """Inner ``data`` envelope of the products PUT response."""

    status: bool
    data: list[ProductUpdateResultItem]


class ProductUpdateResponse(TypedDict):
    """Full response body of ``PUT /web/hub/vendors/v1/products``."""

    success: bool
    messages: list[ApiMessage]
    data: ProductUpdateData


class Product(TypedDict):
    """A single vendor product in the paginated product list."""

    id: str
    hsin: str
    sku: str
    originalPrice: int
    finalPrice: int
    minimalPerOrder: int
    maximalPerOrder: int
    onHandQuantity: int


class ProductsPage(TypedDict):
    """Inner ``data`` envelope of the paginated products response."""

    page: int
    pageSize: int
    totalCount: int
    items: list[Product]


class ProductsResponse(TypedDict):
    """Full response body of
    ``GET /Web/Hub/vendors/v1/products/{page}/{pageSize}``."""

    success: bool
    messages: list[ApiMessage]
    data: ProductsPage
