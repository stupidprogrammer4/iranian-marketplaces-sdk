"""Synchronous client for the Snapp Shop Automation API."""

from __future__ import annotations

from typing import Mapping

import httpx

from ..base_client import BaseClient
from ..exceptions import ConfigurationError
from .constants import (
    BASE_URL,
    vendor_order_endpoint,
    vendor_orders_endpoint,
    vendor_products_endpoint,
)
from .types import (
    ProductUpdate,
    ProductUpdateResult,
    VendorOrderResponse,
    VendorOrdersQuery,
    VendorOrdersResponse,
    VendorProductsQuery,
    VendorProductsResponse,
)


def _build_query(query: Mapping[str, object] | None) -> dict[str, object] | None:
    """Drop ``None`` values from a query mapping."""
    if not query:
        return None
    params = {k: v for k, v in query.items() if v is not None}
    return params or None


class SnappClient(BaseClient):
    """Synchronous API client for Snapp Shop.

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
        client: httpx.Client | None = None,
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

    def list_products(
        self, *, query: VendorProductsQuery | None = None
    ) -> VendorProductsResponse:
        """List the vendor's products.

        Args:
            query: Optional filters; see :class:`VendorProductsQuery`.
        """
        return self._get(
            vendor_products_endpoint(self._seller_id),
            params=_build_query(query),
        )

    def list_orders(
        self, *, query: VendorOrdersQuery | None = None
    ) -> VendorOrdersResponse:
        """List the vendor's orders.

        The endpoint is cursor-paginated: pass ``meta.pagination.
        next_cursor`` from the previous response back as ``query["cursor"]``
        to fetch the next page while ``meta.pagination.has_more`` is true.

        Args:
            query: Optional filters; see :class:`VendorOrdersQuery`.
        """
        return self._get(
            vendor_orders_endpoint(self._seller_id),
            params=_build_query(query),
        )

    def get_order(self, order_number: str | int) -> VendorOrderResponse:
        """Fetch a single vendor order's detail.

        Args:
            order_number: The order's ``order_number``.
        """
        return self._get(
            vendor_order_endpoint(self._seller_id, order_number),
        )

    def update_products(
        self, body: list[ProductUpdate]
    ) -> list[ProductUpdateResult]:
        """Batch-update the vendor's products.

        Args:
            body: The product changes; see :class:`ProductUpdate`. The
                endpoint returns a per-product result list.
        """
        return self._patch(
            vendor_products_endpoint(self._seller_id),
            json=[dict(item) for item in body],
        )
