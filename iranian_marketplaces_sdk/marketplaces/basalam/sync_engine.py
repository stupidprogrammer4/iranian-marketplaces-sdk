"""Basalam, sync engine."""

from types import TracebackType
from typing import Any, Self

import httpx

from iranian_marketplaces_sdk.common.constants import DEFAULT_TIMEOUT
from iranian_marketplaces_sdk.common.data import parse, parse_list
from iranian_marketplaces_sdk.common.http import SyncTransport
from iranian_marketplaces_sdk.marketplaces.basalam.constants import (
    BASE_URL,
    NAME,
    VENDOR_PARCELS_ENDPOINT,
    vendor_discounts_endpoint,
    vendor_products_batch_updates_endpoint,
    vendor_products_endpoint,
)
from iranian_marketplaces_sdk.marketplaces.basalam.data import (
    BasalamConfig,
    BatchProductUpdateRequest,
    BatchProductUpdateResult,
    CreateVendorDiscountRequest,
    DeleteVendorDiscountRequest,
    VendorParcelsQuery,
    VendorParcelsResponse,
    VendorProductsQuery,
    VendorProductsResponse,
)
from iranian_marketplaces_sdk.marketplaces.basalam.helpers import (
    auth_headers,
    parcels_params,
    products_params,
)


class BasalamSync:
    """Basalam over the sync engine.

    Satisfies :class:`~iranian_marketplaces_sdk.common.interfaces.ISyncMarketplaceClient`.
    """

    name = NAME

    def __init__(
        self,
        vendor_id: int,
        access_token: str,
        *,
        timeout: float = DEFAULT_TIMEOUT,
        client: httpx.Client | None = None,
    ) -> None:
        self.config = BasalamConfig(vendor_id=vendor_id, access_token=access_token)
        self._transport = SyncTransport(
            BASE_URL, headers=auth_headers(self.config), timeout=timeout, client=client
        )

    @property
    def base_url(self) -> str:
        return self._transport.base_url

    @property
    def vendor_id(self) -> int:
        return self.config.vendor_id

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

    def list_vendor_products(
        self, *, query: VendorProductsQuery | None = None
    ) -> VendorProductsResponse:
        """List the vendor's products.

        The paginated payload is at the top level — ``result_count``, ``total_count``, ``page``
        sit beside ``data`` rather than under a ``meta`` key.
        """
        return parse(
            VendorProductsResponse,
            self._transport.get(
                vendor_products_endpoint(self.config.vendor_id), params=products_params(query)
            ),
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
            continue_on_error: By default the batch stops at the first failed product. Set this to
                apply the rest anyway — then check ``has_error`` on every returned element, since
                a 200 no longer means every product went through.

        Returns one result per product, as a bare array with no envelope.
        """
        return parse_list(
            BatchProductUpdateResult,
            self._transport.patch(
                vendor_products_batch_updates_endpoint(self.config.vendor_id),
                json=body.to_payload(),
                params={"continue_on_error": continue_on_error},
            ),
        )

    def create_vendor_discount(self, body: CreateVendorDiscountRequest) -> Any:
        """Discount every product the ``product_filter`` selects.

        Answers ``202``: accepted, applied asynchronously. Basalam documents the body as
        unspecified, so it is returned decoded but unvalidated — there is no schema to check it
        against.
        """
        return self._transport.post(
            vendor_discounts_endpoint(self.config.vendor_id), json=body.to_payload()
        )

    def delete_vendor_discount(self, body: DeleteVendorDiscountRequest) -> Any:
        """Remove the discount from every product the ``product_filter`` selects.

        Answers ``202``, with the same unspecified body as the create call.
        """
        return self._transport.delete(
            vendor_discounts_endpoint(self.config.vendor_id), json=body.to_payload()
        )

    def list_vendor_parcels(
        self, *, query: VendorParcelsQuery | None = None
    ) -> VendorParcelsResponse:
        """List vendor parcels. Cursor-paginated.

        Pass the response's ``next_cursor`` back as ``query.cursor`` for the following page.
        """
        return parse(
            VendorParcelsResponse,
            self._transport.get(VENDOR_PARCELS_ENDPOINT, params=parcels_params(query)),
        )
