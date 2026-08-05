"""Tapsi Shop, async engine."""

from types import TracebackType
from typing import Self

import httpx

from iranian_marketplaces_sdk.common.constants import DEFAULT_TIMEOUT
from iranian_marketplaces_sdk.common.data import parse
from iranian_marketplaces_sdk.common.http import AsyncTransport
from iranian_marketplaces_sdk.marketplaces.tapsi.constants import (
    BASE_URL,
    DEFAULT_CLIENT_NAME,
    DEFAULT_CLIENT_VERSION,
    NAME,
    ORDERS_ENDPOINT,
    PRODUCTS_ENDPOINT,
    products_list_endpoint,
)
from iranian_marketplaces_sdk.marketplaces.tapsi.data import (
    OrdersQuery,
    OrdersResponse,
    ProductsResponse,
    ProductUpdate,
    ProductUpdateResponse,
    TapsiConfig,
)
from iranian_marketplaces_sdk.marketplaces.tapsi.helpers import (
    auth_headers,
    orders_body,
    product_updates_body,
)


class TapsiAsync:
    """Tapsi Shop (Hub vendor gateway) over the async engine.

    Satisfies :class:`~iranian_marketplaces_sdk.common.interfaces.IAsyncMarketplaceClient`.
    """

    name = NAME

    def __init__(
        self,
        token: str,
        *,
        client_name: str = DEFAULT_CLIENT_NAME,
        client_version: str = DEFAULT_CLIENT_VERSION,
        timeout: float = DEFAULT_TIMEOUT,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        self.config = TapsiConfig(
            token=token, client_name=client_name, client_version=client_version
        )
        self._transport = AsyncTransport(
            BASE_URL, headers=auth_headers(self.config), timeout=timeout, client=client
        )

    @property
    def base_url(self) -> str:
        return self._transport.base_url

    async def aclose(self) -> None:
        await self._transport.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.aclose()

    async def get_products(self, page: int, page_size: int) -> ProductsResponse:
        """List the vendor's products.

        Paging travels in the path, so both arguments are required — there is no "just give me the
        first page" form.

        Args:
            page: 1-based page number. (The orders endpoint is zero-based; this one is not.)
            page_size: Items per page.
        """
        return parse(
            ProductsResponse, await self._transport.get(products_list_endpoint(page, page_size))
        )

    async def list_orders(self, *, query: OrdersQuery | None = None) -> OrdersResponse:
        """List the vendor's orders.

        A POST, because Tapsi takes the filters as a JSON body. ``query.page_number`` is
        **zero-based**.
        """
        return parse(
            OrdersResponse, await self._transport.post(ORDERS_ENDPOINT, json=orders_body(query))
        )

    async def update_products(self, body: list[ProductUpdate]) -> ProductUpdateResponse:
        """Batch-update the vendor's products.

        Three levels of outcome to check: the response's ``success``, the inner ``data.status``,
        and each item's own ``status``. A 200 alone does not mean every product was updated.
        """
        return parse(
            ProductUpdateResponse,
            await self._transport.put(PRODUCTS_ENDPOINT, json=product_updates_body(body)),
        )
