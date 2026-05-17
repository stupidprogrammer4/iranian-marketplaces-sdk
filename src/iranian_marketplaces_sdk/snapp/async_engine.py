"""Asynchronous client for the Snapp Shop Automation API."""

from __future__ import annotations

import httpx

from ..base_async_client import BaseAsyncClient
from ..exceptions import ConfigurationError
from .constants import (
    BASE_URL,
    vendor_order_endpoint,
    vendor_orders_endpoint,
    vendor_products_endpoint,
)
from .engine import _build_query
from .types import (
    ProductUpdate,
    ProductUpdateResult,
    VendorOrderResponse,
    VendorOrdersQuery,
    VendorOrdersResponse,
    VendorProductsQuery,
    VendorProductsResponse,
)


class AsyncSnappClient(BaseAsyncClient):
    """Asynchronous API client for Snapp Shop.

    Snapp authenticates with two headers: ``User-Agent`` carries the
    account ``unique_code`` and ``Authorization`` the bearer
    ``access_token``. ``seller_id`` is part of the vendor endpoints' path.
    """

    def __init__(
        self,
        unique_code: str,
        access_token: str,
        seller_id: str,
        *,
        timeout: float = 30.0,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        if not unique_code:
            raise ConfigurationError("unique_code is required")
        if not access_token:
            raise ConfigurationError("access_token is required")
        self._unique_code = unique_code
        self._access_token = access_token
        self._seller_id = seller_id
        super().__init__(
            BASE_URL,
            headers={
                "User-Agent": unique_code,
                "Authorization": f"Bearer {access_token}",
            },
            timeout=timeout,
            client=client,
        )

    @property
    def seller_id(self) -> str:
        return self._seller_id

    async def list_products(
        self, *, query: VendorProductsQuery | None = None
    ) -> VendorProductsResponse:
        """List the vendor's products.

        Args:
            query: Optional filters; see :class:`VendorProductsQuery`.
        """
        return await self._get(
            vendor_products_endpoint(self._seller_id),
            params=_build_query(query),
        )

    async def list_orders(
        self, *, query: VendorOrdersQuery | None = None
    ) -> VendorOrdersResponse:
        """List the vendor's orders.

        The endpoint is cursor-paginated: pass ``meta.pagination.
        next_cursor`` from the previous response back as ``query["cursor"]``
        to fetch the next page while ``meta.pagination.has_more`` is true.

        Args:
            query: Optional filters; see :class:`VendorOrdersQuery`.
        """
        return await self._get(
            vendor_orders_endpoint(self._seller_id),
            params=_build_query(query),
        )

    async def get_order(self, order_number: str | int) -> VendorOrderResponse:
        """Fetch a single vendor order's detail.

        Args:
            order_number: The order's ``order_number``.
        """
        return await self._get(
            vendor_order_endpoint(self._seller_id, order_number),
        )

    async def update_products(
        self, body: list[ProductUpdate]
    ) -> list[ProductUpdateResult]:
        """Batch-update the vendor's products.

        Args:
            body: The product changes; see :class:`ProductUpdate`. The
                endpoint returns a per-product result list.
        """
        return await self._patch(
            vendor_products_endpoint(self._seller_id),
            json=[dict(item) for item in body],
        )
