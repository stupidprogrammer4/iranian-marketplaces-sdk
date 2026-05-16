"""Synchronous client for the Basalam Open API."""

from __future__ import annotations

from typing import Mapping

import httpx

from ..base_client import BaseClient
from ..exceptions import ConfigurationError
from .constants import (
    BASE_URL,
    VENDOR_PARCELS_ENDPOINT,
    vendor_discounts_endpoint,
    vendor_products_batch_updates_endpoint,
    vendor_products_endpoint,
)
from .types import (
    BatchProductUpdateRequest,
    BatchProductUpdateResult,
    CreateVendorDiscountRequest,
    DeleteVendorDiscountRequest,
    VendorParcelsQuery,
    VendorParcelsResponse,
    VendorProductsQuery,
    VendorProductsResponse,
)

# Pythonic query keys that map to a different Basalam query parameter name.
_PRODUCTS_QUERY_KEY_MAP = {
    "stock_gte": "stock[gte]",
    "stock_lte": "stock[lte]",
    "preparation_day_gte": "preparation_day[gte]",
    "preparation_day_lte": "preparation_day[lte]",
    "price_gte": "price[gte]",
    "price_lte": "price[lte]",
}

_PARCELS_QUERY_KEY_MAP = {
    "items_customer_ids": "items.customer_ids",
    "items_vendor_ids": "items.vendor_ids",
    "items_product_ids": "items.product_ids",
    "items_order_ids": "items.order_ids",
    "estimate_send_at_gte": "estimate_send_at[gte]",
    "estimate_send_at_lte": "estimate_send_at[lte]",
    "created_at_gte": "created_at[gte]",
    "created_at_lte": "created_at[lte]",
}


def _map_query_params(
    query: Mapping[str, object] | None,
    key_map: Mapping[str, str],
) -> dict[str, object] | None:
    """Map a pythonic query dict to Basalam's query parameter names.

    ``None`` values are dropped; keys absent from ``key_map`` pass through
    unchanged. List values are passed through so ``httpx`` repeats them
    (FastAPI-style array params), never comma-joined.
    """
    if not query:
        return None
    params: dict[str, object] = {}
    for key, value in query.items():
        if value is None:
            continue
        params[key_map.get(key, key)] = value
    return params or None


def _build_vendor_products_params(
    query: Mapping[str, object] | None,
) -> dict[str, object] | None:
    """Map a :class:`VendorProductsQuery` to Basalam's query parameters."""
    return _map_query_params(query, _PRODUCTS_QUERY_KEY_MAP)


def _build_vendor_parcels_params(
    query: Mapping[str, object] | None,
) -> dict[str, object] | None:
    """Map a :class:`VendorParcelsQuery` to Basalam's query parameters."""
    return _map_query_params(query, _PARCELS_QUERY_KEY_MAP)


class BasalamClient(BaseClient):
    """Synchronous API client for Basalam.

    Authenticated requests send ``Authorization: Bearer <access_token>``.
    ``vendor_id`` is required because it is part of the vendor endpoints'
    URL path.
    """

    def __init__(
        self,
        vendor_id: int,
        access_token: str,
        *,
        timeout: float = 30.0,
        client: httpx.Client | None = None,
    ) -> None:
        if not access_token:
            raise ConfigurationError("access_token is required")
        self._vendor_id = vendor_id
        self._access_token = access_token
        super().__init__(
            BASE_URL,
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=timeout,
            client=client,
        )

    @property
    def vendor_id(self) -> int:
        return self._vendor_id

    def list_vendor_products(
        self, *, query: VendorProductsQuery | None = None
    ) -> VendorProductsResponse:
        """List the vendor's products.

        Args:
            query: Optional filters; see :class:`VendorProductsQuery`.
        """
        return self._get(
            vendor_products_endpoint(self._vendor_id),
            params=_build_vendor_products_params(query),
        )

    def batch_update_vendor_products(
        self,
        body: BatchProductUpdateRequest,
        *,
        continue_on_error: bool = False,
    ) -> list[BatchProductUpdateResult]:
        """Batch-update the vendor's products.

        Args:
            body: The products to update; see :class:`BatchProductUpdateRequest`.
            continue_on_error: If true, keep applying remaining updates when
                one fails (Basalam ``continue_on_error`` query param).

        Returns a per-product result list (no response envelope).
        """
        return self._patch(
            vendor_products_batch_updates_endpoint(self._vendor_id),
            json=dict(body),
            params={"continue_on_error": continue_on_error},
        )

    def create_vendor_discount(
        self, body: CreateVendorDiscountRequest
    ) -> object:
        """Create a vendor discount.

        Responds ``202``; Basalam documents the body as unspecified
        (``any``), so the return type is :class:`object`.
        """
        return self._post(
            vendor_discounts_endpoint(self._vendor_id),
            json=dict(body),
        )

    def delete_vendor_discount(
        self, body: DeleteVendorDiscountRequest
    ) -> object:
        """Delete a vendor discount.

        Responds ``202``; Basalam documents the body as unspecified
        (``any``), so the return type is :class:`object`.
        """
        return self._request(
            "DELETE",
            vendor_discounts_endpoint(self._vendor_id),
            json=dict(body),
        )

    def list_vendor_parcels(
        self, *, query: VendorParcelsQuery | None = None
    ) -> VendorParcelsResponse:
        """List vendor parcels (cursor-paginated).

        Args:
            query: Optional filters; see :class:`VendorParcelsQuery`. Use
                ``cursor`` / the response ``next_cursor`` to paginate.
        """
        return self._get(
            VENDOR_PARCELS_ENDPOINT,
            params=_build_vendor_parcels_params(query),
        )
