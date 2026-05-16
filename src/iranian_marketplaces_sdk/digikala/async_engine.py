"""Asynchronous client for the Digikala Seller Open API."""

from __future__ import annotations

import httpx

from ..base_async_client import BaseAsyncClient
from ..exceptions import ConfigurationError
from .constants import (
    AUTH_REFRESH_TOKEN_ENDPOINT,
    AUTH_SCOPES_ENDPOINT,
    AUTH_TOKEN_ENDPOINT,
    BASE_URL,
    HEALTH_CHECK_ENDPOINT,
    INVENTORIES_ENDPOINT,
    INVOICES_ENDPOINT,
    invoice_details_endpoint,
    invoice_items_endpoint,
    ORDERS_ENDPOINT,
    PACKAGES_ENDPOINT,
    ORDERS_HISTORY_ENDPOINT,
    VARIANTS_ENDPOINT,
    VARIANTS_SELLING_PRICE_ENDPOINT,
    auth_client_scopes_endpoint,
    SMART_DISCOUNT_VARIANTS_BATCH_ENDPOINT,
    SMART_DISCOUNT_VARIANTS_ENDPOINT,
    inventory_dead_stock_endpoint,
    package_endpoint,
    smart_discount_variants_endpoint,
    variant_activation_endpoint,
    variant_endpoint,
    variant_gold_endpoint,
    variant_seller_stock_endpoint,
)
from .engine import _build_flat_list_params, _build_list_params
from .types import (
    HealthCheckResponse,
    InventoriesResponse,
    InventoryDeadStockResponse,
    InventorySearch,
    InvoiceCalculationType,
    InvoiceDetailResponse,
    InvoiceItemsResponse,
    InvoiceItemsSearch,
    InvoiceSearch,
    InvoicesResponse,
    OrderHistoryFilters,
    OrderHistoryResponse,
    OrderSearch,
    OrdersResponse,
    PackageDetailResponse,
    PackageDetailSearch,
    PackageSearch,
    PackagesResponse,
    ScopesResponse,
    BatchEditSmartDiscountVariantsRequest,
    BatchEditSmartDiscountVariantsResponse,
    CreateSmartDiscountVariantsRequest,
    CreateSmartDiscountVariantsResponse,
    DeleteSmartDiscountVariantsRequest,
    DeleteSmartDiscountVariantsResponse,
    SmartDiscountActiveStatus,
    SmartDiscountVariantSearch,
    SmartDiscountVariantsResponse,
    TokenResponse,
    UpdateVariantGoldRequest,
    UpdateVariantGoldResponse,
    UpdateVariantActivationRequest,
    UpdateVariantActivationResponse,
    UpdateVariantRequest,
    UpdateVariantResponse,
    UpdateVariantSellerStockRequest,
    UpdateVariantSellerStockResponse,
    UpdateVariantSellingPriceRequest,
    UpdateVariantSellingPriceResponse,
    VariantGoldResponse,
    VariantSellerStockResponse,
    VariantResponse,
    VariantSearch,
    VariantsResponse,
)


class AsyncDigikalaClient(BaseAsyncClient):
    """Asynchronous API client for Digikala.

    Authenticated endpoints send the token as ``Authorization: Bearer
    <access_token>``. The health-check endpoint is unauthenticated but is
    served by the same client.
    """

    def __init__(
        self,
        access_token: str,
        refresh_token: str,
        *,
        timeout: float = 30.0,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        if not access_token:
            raise ConfigurationError("access_token is required")
        self._access_token = access_token
        self._refresh_token = refresh_token
        super().__init__(
            BASE_URL,
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=timeout,
            client=client,
        )

    @classmethod
    async def create_token(
        cls,
        authorization_code: str,
        *,
        timeout: float = 30.0,
        client: httpx.AsyncClient | None = None,
    ) -> TokenResponse:
        """Exchange an ``authorization_code`` for access/refresh tokens.

        Unauthenticated: this is the call that bootstraps credentials, so it
        does not require an existing ``access_token``.
        """
        bootstrap = BaseAsyncClient(BASE_URL, timeout=timeout, client=client)
        try:
            return await bootstrap._post(
                AUTH_TOKEN_ENDPOINT,
                json={"authorization_code": authorization_code},
                headers={"Content-Type": "application/json"},
            )
        finally:
            if client is None:
                await bootstrap.aclose()

    async def refresh_token(self) -> TokenResponse:
        """Exchange the stored expired tokens for a fresh pair.

        Uses the ``access_token``/``refresh_token`` this client was built
        with, then updates the client in place so subsequent calls use the
        new access token.
        """
        response: TokenResponse = await self._post(
            AUTH_REFRESH_TOKEN_ENDPOINT,
            json={
                "access_token": self._access_token,
                "refresh_token": self._refresh_token,
            },
            headers={"Content-Type": "application/json"},
        )
        data = response["data"]
        self._access_token = data["access_token"]
        self._refresh_token = data["refresh_token"]
        self._client.headers["Authorization"] = f"Bearer {self._access_token}"
        return response

    async def health_check(self) -> HealthCheckResponse:
        """Return the service health status, mode, time and rate-limit info."""
        return await self._get(HEALTH_CHECK_ENDPOINT)

    async def get_scopes(self) -> ScopesResponse:
        """Return the permission scopes granted to the current access token."""
        return await self._get(AUTH_SCOPES_ENDPOINT)

    async def get_client_scopes(self, client_code: str) -> ScopesResponse:
        """Return the scopes available to the application ``client_code``."""
        return await self._get(
            auth_client_scopes_endpoint(client_code),
            headers={"Content-Type": "application/json"},
        )

    async def list_variants(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: VariantSearch | None = None,
    ) -> VariantsResponse:
        """List the seller's variants (scope: ``variant``).

        Args:
            page: 1-based page number.
            size: Page size.
            sort: Sort column (see ``data.sort_data.sort_columns``).
            order: Sort order, e.g. ``"asc"`` / ``"desc"``.
            search: Optional ``search[...]`` filters; see :class:`VariantSearch`.
        """
        return await self._get(
            VARIANTS_ENDPOINT,
            params=_build_list_params(page, size, sort, order, search),
            headers={"Content-Type": "application/json"},
        )

    async def get_variant(self, variant_id: int) -> VariantResponse:
        """Get a single variant by id (scope: ``variant``)."""
        return await self._get(
            variant_endpoint(variant_id),
            headers={"Content-Type": "application/json"},
        )

    async def update_variant(
        self, variant_id: int, body: UpdateVariantRequest
    ) -> UpdateVariantResponse:
        """Edit a seller variant (scope: ``variant``).

        ``body`` is a partial update; only the keys present are sent.
        """
        return await self._put(
            variant_endpoint(variant_id),
            json=dict(body),
            headers={"Content-Type": "application/json"},
        )

    async def get_variant_gold(self, variant_id: int) -> VariantGoldResponse:
        """Get a gold variant's modal pricing data (scope: ``variant``)."""
        return await self._get(
            variant_gold_endpoint(variant_id),
            headers={"Content-Type": "application/json"},
        )

    async def get_variant_seller_stock(
        self, variant_id: int
    ) -> VariantSellerStockResponse:
        """Get a variant's seller stock detail (scope: ``variant``)."""
        return await self._get(
            variant_seller_stock_endpoint(variant_id),
            headers={"Content-Type": "application/json"},
        )

    async def update_variant_seller_stock(
        self, variant_id: int, body: UpdateVariantSellerStockRequest
    ) -> UpdateVariantSellerStockResponse:
        """Update a variant's seller-stock amount (scope: ``variant``)."""
        return await self._patch(
            variant_seller_stock_endpoint(variant_id),
            json=dict(body),
            headers={"Content-Type": "application/json"},
        )

    async def update_variant_selling_price(
        self, body: UpdateVariantSellingPriceRequest
    ) -> UpdateVariantSellingPriceResponse:
        """Update a variant's selling price (scope: ``variant``).

        ``variant_id`` is part of the request body, not the URL path.
        """
        return await self._patch(
            VARIANTS_SELLING_PRICE_ENDPOINT,
            json=dict(body),
            headers={"Content-Type": "application/json"},
        )

    async def update_variant_gold(
        self, variant_id: int, body: UpdateVariantGoldRequest
    ) -> UpdateVariantGoldResponse:
        """Edit a gold variant's pricing data (scope: ``variant``)."""
        return await self._put(
            variant_gold_endpoint(variant_id),
            json=dict(body),
            headers={"Content-Type": "application/json"},
        )

    async def update_variant_activation(
        self, variant_id: int, body: UpdateVariantActivationRequest
    ) -> UpdateVariantActivationResponse:
        """Edit a seller variant's activation status (scope: ``variant``)."""
        return await self._put(
            variant_activation_endpoint(variant_id),
            json=dict(body),
            headers={"Content-Type": "application/json"},
        )

    async def list_orders(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: OrderSearch | None = None,
    ) -> OrdersResponse:
        """List the seller's active order items (scope: ``order``).

        Args:
            page: 1-based page number.
            size: Page size.
            sort: Sort column (e.g. ``"order_created_at"``).
            order: Sort order, e.g. ``"asc"`` / ``"desc"``.
            search: Optional ``search[...]`` filters; see :class:`OrderSearch`.
        """
        return await self._get(
            ORDERS_ENDPOINT,
            params=_build_list_params(page, size, sort, order, search),
            headers={"Content-Type": "application/json"},
        )

    async def list_inventories(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: InventorySearch | None = None,
    ) -> InventoriesResponse:
        """List the seller's inventories (scope: ``inventory``).

        Args:
            page: 1-based page number.
            size: Page size.
            sort: Sort column (e.g. ``"id"``).
            order: Sort order, e.g. ``"asc"`` / ``"desc"``.
            search: Optional ``search[...]`` filters; see :class:`InventorySearch`.
        """
        return await self._get(
            INVENTORIES_ENDPOINT,
            params=_build_list_params(page, size, sort, order, search),
            headers={"Content-Type": "application/json"},
        )

    async def list_packages(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: PackageSearch | None = None,
    ) -> PackagesResponse:
        """List the seller's packages (scope: ``package``).

        Args:
            page: 1-based page number.
            size: Page size.
            sort: Sort column (e.g. ``"created_at"``).
            order: Sort order, e.g. ``"asc"`` / ``"desc"``.
            search: Optional ``search[...]`` filters; see :class:`PackageSearch`.
        """
        return await self._get(
            PACKAGES_ENDPOINT,
            params=_build_list_params(page, size, sort, order, search),
            headers={"Content-Type": "application/json"},
        )

    async def get_package(
        self, package_id: int, *, search: PackageDetailSearch | None = None
    ) -> PackageDetailResponse:
        """Get a single package's detail view (scope: ``package``).

        Args:
            package_id: The package id (path).
            search: Optional ``search[...]`` filters; see
                :class:`PackageDetailSearch`.
        """
        return await self._get(
            package_endpoint(package_id),
            params=_build_list_params(None, None, None, None, search) or None,
            headers={"Content-Type": "application/json"},
        )

    async def list_smart_discount_variants(
        self,
        active_status: SmartDiscountActiveStatus,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: SmartDiscountVariantSearch | None = None,
    ) -> SmartDiscountVariantsResponse:
        """List variants with periodic (smart-discount) prices.

        Scope: ``promotion``.

        Args:
            active_status: ``"active"`` or ``"inactive"`` (path).
            page: 1-based page number.
            size: Page size.
            sort: Sort column (only ``"id"`` is supported).
            order: Sort order, e.g. ``"asc"`` / ``"desc"``.
            search: Optional ``search[...]`` filters; see
                :class:`SmartDiscountVariantSearch`.
        """
        return await self._get(
            smart_discount_variants_endpoint(active_status),
            params=_build_list_params(page, size, sort, order, search),
            headers={"Content-Type": "application/json"},
        )

    async def create_smart_discount_variants(
        self, body: CreateSmartDiscountVariantsRequest
    ) -> CreateSmartDiscountVariantsResponse:
        """Atomically create periodic-price variants (scope: ``promotion``)."""
        return await self._post(
            SMART_DISCOUNT_VARIANTS_ENDPOINT,
            json=dict(body),
            headers={"Content-Type": "application/json"},
        )

    async def delete_smart_discount_variants(
        self, body: DeleteSmartDiscountVariantsRequest
    ) -> DeleteSmartDiscountVariantsResponse:
        """Batch-delete periodic-price variants (scope: ``promotion``)."""
        return await self._request(
            "DELETE",
            SMART_DISCOUNT_VARIANTS_ENDPOINT,
            json=dict(body),
            headers={"Content-Type": "application/json"},
        )

    async def batch_edit_smart_discount_variants(
        self, body: BatchEditSmartDiscountVariantsRequest
    ) -> BatchEditSmartDiscountVariantsResponse:
        """Batch-edit periodic-price variants (scope: ``promotion``)."""
        return await self._put(
            SMART_DISCOUNT_VARIANTS_BATCH_ENDPOINT,
            json=dict(body),
            headers={"Content-Type": "application/json"},
        )

    async def get_inventory_dead_stock(
        self, product_variant_id: int, *, serial: str | None = None
    ) -> InventoryDeadStockResponse:
        """Get dead-stock detail for a product variant (scope: ``inventory``).

        Args:
            product_variant_id: The product variant id (path).
            serial: Optional serial to search for.
        """
        params: dict[str, object] = {}
        if serial is not None:
            params["serial"] = serial
        return await self._get(
            inventory_dead_stock_endpoint(product_variant_id),
            params=params or None,
            headers={"Content-Type": "application/json"},
        )

    async def list_invoices(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: InvoiceSearch | None = None,
    ) -> InvoicesResponse:
        """List the seller's invoices (scope: ``invoice``).

        Args:
            page: 1-based page number.
            size: Page size.
            sort: Sort column (e.g. ``"id"``).
            order: Sort order, e.g. ``"asc"`` / ``"desc"``.
            search: Optional ``search[...]`` filters; see :class:`InvoiceSearch`.
        """
        return await self._get(
            INVOICES_ENDPOINT,
            params=_build_list_params(page, size, sort, order, search),
            headers={"Content-Type": "application/json"},
        )

    async def get_invoice_details(
        self, invoice_id: int
    ) -> InvoiceDetailResponse:
        """Get a single invoice's detail view (scope: ``invoice``)."""
        return await self._get(
            invoice_details_endpoint(invoice_id),
            headers={"Content-Type": "application/json"},
        )

    async def list_invoice_items(
        self,
        invoice_id: int,
        financial_notation_id: int,
        calculation_type: InvoiceCalculationType,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: InvoiceItemsSearch | None = None,
    ) -> InvoiceItemsResponse:
        """List an invoice's financial items (scope: ``invoice``).

        Args:
            invoice_id: The invoice id (path).
            financial_notation_id: The financial-notation id (path).
            calculation_type: The notation calculation model (path).
            page: 1-based page number.
            size: Page size.
            sort: Sort column (e.g. ``"id"``).
            order: Sort order, e.g. ``"asc"`` / ``"desc"``.
            search: Optional ``search[...]`` filters; see
                :class:`InvoiceItemsSearch`.
        """
        return await self._get(
            invoice_items_endpoint(
                invoice_id, financial_notation_id, calculation_type
            ),
            params=_build_list_params(page, size, sort, order, search),
            headers={"Content-Type": "application/json"},
        )

    async def list_order_history(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        filters: OrderHistoryFilters | None = None,
    ) -> OrderHistoryResponse:
        """List the history of all seller orders (scope: ``order``).

        Args:
            page: 1-based page number.
            size: Page size.
            sort: Sort column.
            order: Sort order, e.g. ``"asc"`` / ``"desc"``.
            filters: Optional flat query filters; see :class:`OrderHistoryFilters`.
        """
        return await self._get(
            ORDERS_HISTORY_ENDPOINT,
            params=_build_flat_list_params(page, size, sort, order, filters),
            headers={"Content-Type": "application/json"},
        )
