"""Snapp Shop, sync engine."""

from types import TracebackType
from typing import Self

import httpx

from iranian_marketplaces_sdk.common.constants import DEFAULT_TIMEOUT
from iranian_marketplaces_sdk.common.data import parse, parse_list
from iranian_marketplaces_sdk.common.http import SyncTransport
from iranian_marketplaces_sdk.marketplaces.snapp.constants import (
    BASE_URL,
    NAME,
    vendor_order_endpoint,
    vendor_orders_endpoint,
    vendor_products_endpoint,
)
from iranian_marketplaces_sdk.marketplaces.snapp.data import (
    ProductUpdate,
    ProductUpdateResult,
    SnappConfig,
    VendorOrderResponse,
    VendorOrdersQuery,
    VendorOrdersResponse,
    VendorProductsQuery,
    VendorProductsResponse,
)
from iranian_marketplaces_sdk.marketplaces.snapp.helpers import (
    auth_headers,
    product_updates_payload,
    query_params,
)


class SnappSync:
    """Snapp Shop over the sync engine.

    Satisfies :class:`~iranian_marketplaces_sdk.common.interfaces.ISyncMarketplaceClient`.
    """

    name = NAME

    def __init__(
        self,
        unique_code: str,
        access_token: str,
        seller_id: str,
        *,
        timeout: float = DEFAULT_TIMEOUT,
        client: httpx.Client | None = None,
    ) -> None:
        self.config = SnappConfig(
            unique_code=unique_code, access_token=access_token, seller_id=seller_id
        )
        self._transport = SyncTransport(
            BASE_URL, headers=auth_headers(self.config), timeout=timeout, client=client
        )

    @property
    def base_url(self) -> str:
        return self._transport.base_url

    @property
    def seller_id(self) -> str:
        return self.config.seller_id

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()

    def list_products(self, *, query: VendorProductsQuery | None = None) -> VendorProductsResponse:
        """List the vendor's products. Offset-paginated — see ``meta.pagination``."""
        return parse(
            VendorProductsResponse,
            self._transport.get(
                vendor_products_endpoint(self.config.seller_id), params=query_params(query)
            ),
        )

    def update_products(self, body: list[ProductUpdate]) -> list[ProductUpdateResult]:
        """Batch-update the vendor's products.

        Not atomic: the response is one result per product, and a failed entry does not stop the
        others. Check every element's ``status``.
        """
        return parse_list(
            ProductUpdateResult,
            self._transport.patch(
                vendor_products_endpoint(self.config.seller_id),
                json=product_updates_payload(body),
            ),
        )

    def list_orders(self, *, query: VendorOrdersQuery | None = None) -> VendorOrdersResponse:
        """List the vendor's orders. Cursor-paginated.

        Pass ``meta.pagination.next_cursor`` back as ``query.cursor`` while ``has_more`` is true.
        There is no total count and no page number to jump to.
        """
        return parse(
            VendorOrdersResponse,
            self._transport.get(
                vendor_orders_endpoint(self.config.seller_id), params=query_params(query)
            ),
        )

    def get_order(self, order_number: str | int) -> VendorOrderResponse:
        """One order's detail, by its ``order_number``."""
        return parse(
            VendorOrderResponse,
            self._transport.get(vendor_order_endpoint(self.config.seller_id, order_number)),
        )
