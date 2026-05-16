"""Asynchronous client for the Basalam Open API."""

from __future__ import annotations

import httpx

from ..base_async_client import BaseAsyncClient
from ..exceptions import ConfigurationError
from .constants import (
    BASE_URL,
    VENDOR_PARCELS_ENDPOINT,
    vendor_discounts_endpoint,
    vendor_products_batch_updates_endpoint,
    vendor_products_endpoint,
)
from .engine import _build_vendor_parcels_params, _build_vendor_products_params
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


class AsyncBasalamClient(BaseAsyncClient):
    """Asynchronous API client for Basalam.

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
        client: httpx.AsyncClient | None = None,
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

    async def list_vendor_products(
        self, *, query: VendorProductsQuery | None = None
    ) -> VendorProductsResponse:
        """List the vendor's products.

        Args:
            query: Optional filters; see :class:`VendorProductsQuery`.
        """
        return await self._get(
            vendor_products_endpoint(self._vendor_id),
            params=_build_vendor_products_params(query),
        )

    async def batch_update_vendor_products(
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
        return await self._patch(
            vendor_products_batch_updates_endpoint(self._vendor_id),
            json=dict(body),
            params={"continue_on_error": continue_on_error},
        )

    async def create_vendor_discount(
        self, body: CreateVendorDiscountRequest
    ) -> object:
        """Create a vendor discount.

        Responds ``202``; Basalam documents the body as unspecified
        (``any``), so the return type is :class:`object`.
        """
        return await self._post(
            vendor_discounts_endpoint(self._vendor_id),
            json=dict(body),
        )

    async def delete_vendor_discount(
        self, body: DeleteVendorDiscountRequest
    ) -> object:
        """Delete a vendor discount.

        Responds ``202``; Basalam documents the body as unspecified
        (``any``), so the return type is :class:`object`.
        """
        return await self._request(
            "DELETE",
            vendor_discounts_endpoint(self._vendor_id),
            json=dict(body),
        )

    async def list_vendor_parcels(
        self, *, query: VendorParcelsQuery | None = None
    ) -> VendorParcelsResponse:
        """List vendor parcels (cursor-paginated).

        Args:
            query: Optional filters; see :class:`VendorParcelsQuery`. Use
                ``cursor`` / the response ``next_cursor`` to paginate.
        """
        return await self._get(
            VENDOR_PARCELS_ENDPOINT,
            params=_build_vendor_parcels_params(query),
        )
