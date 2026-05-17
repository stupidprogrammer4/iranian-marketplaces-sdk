"""Asynchronous client for the Tapsi Shop Hub vendor API."""

from __future__ import annotations

import httpx

from ..base_async_client import BaseAsyncClient
from ..exceptions import ConfigurationError
from .constants import (
    BASE_URL,
    DEFAULT_CLIENT_NAME,
    DEFAULT_CLIENT_VERSION,
    ORDERS_ENDPOINT,
    PRODUCTS_ENDPOINT,
    products_list_endpoint,
)
from .engine import _clean_body
from .types import (
    OrdersQuery,
    OrdersResponse,
    ProductsResponse,
    ProductUpdate,
    ProductUpdateResponse,
)


class AsyncTapsiClient(BaseAsyncClient):
    """Asynchronous API client for Tapsi Shop (Hub vendor gateway).

    Tapsi authenticates with the ``TapsiShop.Hub.Authorization`` header
    carrying the vendor ``token``. ``client-name`` / ``client-version``
    identify the calling client and default to the documented values.
    """

    def __init__(
        self,
        token: str,
        *,
        client_name: str = DEFAULT_CLIENT_NAME,
        client_version: str = DEFAULT_CLIENT_VERSION,
        timeout: float = 30.0,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        if not token:
            raise ConfigurationError("token is required")
        self._token = token
        super().__init__(
            BASE_URL,
            headers={
                "TapsiShop.Hub.Authorization": token,
                "client-name": client_name,
                "client-version": client_version,
                "accept": "text/plain",
            },
            timeout=timeout,
            client=client,
        )

    async def get_products(
        self, page: int, page_size: int
    ) -> ProductsResponse:
        """List the vendor's products (page-based pagination).

        Args:
            page: 1-based page number.
            page_size: Number of items per page.
        """
        return await self._get(products_list_endpoint(page, page_size))

    async def list_orders(
        self, *, query: OrdersQuery | None = None
    ) -> OrdersResponse:
        """List the vendor's orders (page-based pagination).

        Args:
            query: Optional JSON filter body; see :class:`OrdersQuery`.
                ``pageNumber`` is zero-based.
        """
        return await self._post(ORDERS_ENDPOINT, json=_clean_body(query))

    async def update_products(
        self, body: list[ProductUpdate]
    ) -> ProductUpdateResponse:
        """Batch-update the vendor's products.

        Args:
            body: The product changes; see :class:`ProductUpdate`. The
                endpoint returns a per-product result list.
        """
        return await self._put(
            PRODUCTS_ENDPOINT,
            json={"products": [dict(item) for item in body]},
        )
