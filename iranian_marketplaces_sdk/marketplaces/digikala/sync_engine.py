"""Digikala, sync engine."""

from types import TracebackType
from typing import Self

import httpx

from iranian_marketplaces_sdk.common.constants import DEFAULT_TIMEOUT
from iranian_marketplaces_sdk.common.data import parse
from iranian_marketplaces_sdk.common.exceptions import ConfigurationError
from iranian_marketplaces_sdk.common.http import SyncTransport
from iranian_marketplaces_sdk.marketplaces.digikala.constants import (
    AUTH_REFRESH_TOKEN_ENDPOINT,
    AUTH_SCOPES_ENDPOINT,
    AUTH_TOKEN_ENDPOINT,
    BASE_URL,
    HEALTH_CHECK_ENDPOINT,
    INVENTORIES_ENDPOINT,
    INVOICES_ENDPOINT,
    NAME,
    ORDERS_ENDPOINT,
    ORDERS_HISTORY_ENDPOINT,
    PACKAGES_ENDPOINT,
    SMART_DISCOUNT_VARIANTS_BATCH_ENDPOINT,
    SMART_DISCOUNT_VARIANTS_ENDPOINT,
    VARIANTS_ENDPOINT,
    VARIANTS_SELLING_PRICE_ENDPOINT,
    auth_client_scopes_endpoint,
    inventory_dead_stock_endpoint,
    invoice_details_endpoint,
    invoice_items_endpoint,
    package_endpoint,
    smart_discount_variants_endpoint,
    variant_activation_endpoint,
    variant_endpoint,
    variant_gold_endpoint,
    variant_seller_stock_endpoint,
)
from iranian_marketplaces_sdk.marketplaces.digikala.data import (
    BatchEditSmartDiscountVariantsRequest,
    BatchEditSmartDiscountVariantsResponse,
    CreateSmartDiscountVariantsRequest,
    CreateSmartDiscountVariantsResponse,
    DeleteSmartDiscountVariantsRequest,
    DeleteSmartDiscountVariantsResponse,
    DigikalaConfig,
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
    RefreshTokenRequest,
    ScopesResponse,
    SmartDiscountActiveStatus,
    SmartDiscountVariantSearch,
    SmartDiscountVariantsResponse,
    TokenRequest,
    TokenResponse,
    UpdateVariantActivationRequest,
    UpdateVariantActivationResponse,
    UpdateVariantGoldRequest,
    UpdateVariantGoldResponse,
    UpdateVariantRequest,
    UpdateVariantResponse,
    UpdateVariantSellerStockRequest,
    UpdateVariantSellerStockResponse,
    UpdateVariantSellingPriceRequest,
    UpdateVariantSellingPriceResponse,
    VariantGoldResponse,
    VariantResponse,
    VariantSearch,
    VariantSellerStockResponse,
    VariantsResponse,
)
from iranian_marketplaces_sdk.marketplaces.digikala.helpers import (
    JSON_HEADERS,
    auth_headers,
    flat_list_params,
    list_params,
)
from iranian_marketplaces_sdk.marketplaces.digikala.resources import SyncResources


class DigikalaSync(SyncResources):
    """Digikala over the sync engine.

    Satisfies :class:`~iranian_marketplaces_sdk.common.interfaces.ISyncMarketplaceClient`.

    Every authenticated call sends ``Authorization: Bearer <access_token>``. Each endpoint's scope
    is named in its docstring: a token granted only ``variant`` will 403 on ``list_orders()``.
    ``get_scopes()`` lists the service catalog; ``get_client_scopes()`` lists application scopes.
    """

    name = NAME

    def __init__(
        self,
        access_token: str,
        refresh_token: str = "",
        *,
        timeout: float = DEFAULT_TIMEOUT,
        client: httpx.Client | None = None,
    ) -> None:
        self.config = DigikalaConfig(access_token=access_token, refresh_token=refresh_token)
        self._transport = SyncTransport(
            BASE_URL, headers=auth_headers(self.config), timeout=timeout, client=client
        )

    @property
    def base_url(self) -> str:
        return self._transport.base_url

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

    # --- auth ------------------------------------------------------------------------------

    @classmethod
    def create_token(
        cls,
        authorization_code: str,
        *,
        timeout: float = DEFAULT_TIMEOUT,
        client: httpx.Client | None = None,
    ) -> TokenResponse:
        """Exchange a one-time ``authorization_code`` for an access/refresh pair.

        Unauthenticated, and a classmethod for that reason: this is the call that *produces* the
        credentials, so it cannot require a configured client to make it.
        """
        transport = SyncTransport(BASE_URL, timeout=timeout, client=client)
        try:
            raw = transport.post(
                AUTH_TOKEN_ENDPOINT,
                json=TokenRequest(authorization_code=authorization_code).to_payload(),
                headers=JSON_HEADERS,
            )
        finally:
            if client is None:
                transport.close()
        return parse(TokenResponse, raw)

    def refresh_token(self) -> TokenResponse:
        """Trade the stored token pair for a fresh one, and keep using it.

        On success the config and the live session header are both replaced, so calls made after
        this one authenticate with the new token without any work at the call site. Store the
        returned pair: the old refresh token is spent.
        """
        if not self.config.refresh_token:
            raise ConfigurationError(
                "the digikala client needs a refresh_token to refresh — it was built without one"
            )
        raw = self._transport.post(
            AUTH_REFRESH_TOKEN_ENDPOINT,
            json=RefreshTokenRequest(
                access_token=self.config.access_token,
                refresh_token=self.config.refresh_token,
            ).to_payload(),
            headers=JSON_HEADERS,
        )
        response = parse(TokenResponse, raw)
        self.config = self.config.model_copy(
            update={
                "access_token": response.data.access_token,
                "refresh_token": response.data.refresh_token,
            }
        )
        self._transport.set_header("Authorization", f"Bearer {self.config.access_token}")
        return response

    def health_check(self) -> HealthCheckResponse:
        """Service health, mode, time and the current rate-limit window. Unauthenticated."""
        return parse(HealthCheckResponse, self._transport.get(HEALTH_CHECK_ENDPOINT))

    def get_scopes(self) -> ScopesResponse:
        """All scopes defined by the service, not the current token's permissions."""
        return parse(ScopesResponse, self._transport.get(AUTH_SCOPES_ENDPOINT))

    def get_client_scopes(self, client_code: str) -> ScopesResponse:
        """The scopes an application (``client_code``) is allowed to ask for."""
        return parse(
            ScopesResponse,
            self._transport.get(auth_client_scopes_endpoint(client_code), headers=JSON_HEADERS),
        )

    # --- variants --------------------------------------------------------------------------

    def list_variants(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: VariantSearch | None = None,
    ) -> VariantsResponse:
        """List the seller's variants. Scope: ``variant``.

        Args:
            page: 1-based page number.
            size: Page size.
            sort: Sort column — the valid ones come back in ``data.sort_data.sort_columns``.
            order: ``"asc"`` or ``"desc"``.
            search: Optional filters; see :class:`VariantSearch`.
        """
        return parse(
            VariantsResponse,
            self._transport.get(
                VARIANTS_ENDPOINT,
                params=list_params(page=page, size=size, sort=sort, order=order, search=search),
                headers=JSON_HEADERS,
            ),
        )

    def get_variant(self, variant_id: int) -> VariantResponse:
        """One variant by id. Scope: ``variant``."""
        return parse(
            VariantResponse,
            self._transport.get(variant_endpoint(variant_id), headers=JSON_HEADERS),
        )

    def update_variant(self, variant_id: int, body: UpdateVariantRequest) -> UpdateVariantResponse:
        """Edit a variant. Scope: ``variant``.

        A partial update — only the fields set on ``body`` are sent.
        """
        return parse(
            UpdateVariantResponse,
            self._transport.put(
                variant_endpoint(variant_id), json=body.to_payload(), headers=JSON_HEADERS
            ),
        )

    def get_variant_gold(self, variant_id: int) -> VariantGoldResponse:
        """A gold variant's pricing parameters. Scope: ``variant``."""
        return parse(
            VariantGoldResponse,
            self._transport.get(variant_gold_endpoint(variant_id), headers=JSON_HEADERS),
        )

    def get_variant_seller_stock(self, variant_id: int) -> VariantSellerStockResponse:
        """A variant's stock, broken down by where it currently is. Scope: ``variant``."""
        return parse(
            VariantSellerStockResponse,
            self._transport.get(variant_seller_stock_endpoint(variant_id), headers=JSON_HEADERS),
        )

    def update_variant_seller_stock(
        self, variant_id: int, body: UpdateVariantSellerStockRequest
    ) -> UpdateVariantSellerStockResponse:
        """Set a variant's seller stock. Scope: ``variant``."""
        return parse(
            UpdateVariantSellerStockResponse,
            self._transport.patch(
                variant_seller_stock_endpoint(variant_id),
                json=body.to_payload(),
                headers=JSON_HEADERS,
            ),
        )

    def update_variant_selling_price(
        self, body: UpdateVariantSellingPriceRequest
    ) -> UpdateVariantSellingPriceResponse:
        """Set a variant's selling price. Scope: ``variant``.

        ``variant_id`` goes in the body here, not the path.
        """
        return parse(
            UpdateVariantSellingPriceResponse,
            self._transport.patch(
                VARIANTS_SELLING_PRICE_ENDPOINT, json=body.to_payload(), headers=JSON_HEADERS
            ),
        )

    def update_variant_gold(
        self, variant_id: int, body: UpdateVariantGoldRequest
    ) -> UpdateVariantGoldResponse:
        """Edit a gold variant's pricing parameters. Scope: ``variant``."""
        return parse(
            UpdateVariantGoldResponse,
            self._transport.put(
                variant_gold_endpoint(variant_id), json=body.to_payload(), headers=JSON_HEADERS
            ),
        )

    def update_variant_activation(
        self, variant_id: int, body: UpdateVariantActivationRequest
    ) -> UpdateVariantActivationResponse:
        """Turn a variant's listing on or off. Scope: ``variant``."""
        return parse(
            UpdateVariantActivationResponse,
            self._transport.put(
                variant_activation_endpoint(variant_id),
                json=body.to_payload(),
                headers=JSON_HEADERS,
            ),
        )

    # --- orders ----------------------------------------------------------------------------

    def list_orders(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: OrderSearch | None = None,
    ) -> OrdersResponse:
        """The seller's open order items — what is still owed to a customer. Scope: ``order``."""
        return parse(
            OrdersResponse,
            self._transport.get(
                ORDERS_ENDPOINT,
                params=list_params(page=page, size=size, sort=sort, order=order, search=search),
                headers=JSON_HEADERS,
            ),
        )

    def list_order_history(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        filters: OrderHistoryFilters | None = None,
    ) -> OrderHistoryResponse:
        """Every order ever placed with this seller, with serials. Scope: ``order``.

        ``filters`` are flat query parameters here, not the ``search[...]`` form the other list
        endpoints use.
        """
        return parse(
            OrderHistoryResponse,
            self._transport.get(
                ORDERS_HISTORY_ENDPOINT,
                params=flat_list_params(
                    page=page, size=size, sort=sort, order=order, filters=filters
                ),
                headers=JSON_HEADERS,
            ),
        )

    # --- inventories -----------------------------------------------------------------------

    def list_inventories(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: InventorySearch | None = None,
    ) -> InventoriesResponse:
        """The seller's stock as Digikala holds it. Scope: ``inventory``."""
        return parse(
            InventoriesResponse,
            self._transport.get(
                INVENTORIES_ENDPOINT,
                params=list_params(page=page, size=size, sort=sort, order=order, search=search),
                headers=JSON_HEADERS,
            ),
        )

    def get_inventory_dead_stock(
        self, product_variant_id: int, *, serial: str | None = None
    ) -> InventoryDeadStockResponse:
        """Units of a product variant that have aged into dead stock. Scope: ``inventory``.

        Args:
            product_variant_id: The product variant id (path).
            serial: Narrow the result to one serial.
        """
        params = {"serial": serial} if serial is not None else None
        return parse(
            InventoryDeadStockResponse,
            self._transport.get(
                inventory_dead_stock_endpoint(product_variant_id),
                params=params,
                headers=JSON_HEADERS,
            ),
        )

    # --- packages --------------------------------------------------------------------------

    def list_packages(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: PackageSearch | None = None,
    ) -> PackagesResponse:
        """The seller's stock deliveries to Digikala warehouses. Scope: ``package``."""
        return parse(
            PackagesResponse,
            self._transport.get(
                PACKAGES_ENDPOINT,
                params=list_params(page=page, size=size, sort=sort, order=order, search=search),
                headers=JSON_HEADERS,
            ),
        )

    def get_package(
        self, package_id: int, *, search: PackageDetailSearch | None = None
    ) -> PackageDetailResponse:
        """What is inside one package, down to the serial. Scope: ``package``."""
        params = list_params(search=search)
        return parse(
            PackageDetailResponse,
            self._transport.get(
                package_endpoint(package_id), params=params or None, headers=JSON_HEADERS
            ),
        )

    # --- pricing / smart discount ----------------------------------------------------------

    def list_smart_discount_variants(
        self,
        active_status: SmartDiscountActiveStatus,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: SmartDiscountVariantSearch | None = None,
    ) -> SmartDiscountVariantsResponse:
        """Variants carrying a periodic (smart-discount) price. Scope: ``promotion``.

        Args:
            active_status: ``"active"`` or ``"inactive"`` (path). It also decides which ``status``
                filter values are valid — see :class:`SmartDiscountVariantSearch`.
            page: 1-based page number.
            size: Page size.
            sort: Only ``"id"`` is supported here.
            order: ``"asc"`` or ``"desc"``.
            search: Optional filters.
        """
        return parse(
            SmartDiscountVariantsResponse,
            self._transport.get(
                smart_discount_variants_endpoint(active_status),
                params=list_params(page=page, size=size, sort=sort, order=order, search=search),
                headers=JSON_HEADERS,
            ),
        )

    def create_smart_discount_variants(
        self, body: CreateSmartDiscountVariantsRequest
    ) -> CreateSmartDiscountVariantsResponse:
        """Open periodic prices on a batch of variants, atomically. Scope: ``promotion``."""
        return parse(
            CreateSmartDiscountVariantsResponse,
            self._transport.post(
                SMART_DISCOUNT_VARIANTS_ENDPOINT, json=body.to_payload(), headers=JSON_HEADERS
            ),
        )

    def delete_smart_discount_variants(
        self, body: DeleteSmartDiscountVariantsRequest
    ) -> DeleteSmartDiscountVariantsResponse:
        """End periodic prices on a batch of variants. Scope: ``promotion``."""
        return parse(
            DeleteSmartDiscountVariantsResponse,
            self._transport.delete(
                SMART_DISCOUNT_VARIANTS_ENDPOINT, json=body.to_payload(), headers=JSON_HEADERS
            ),
        )

    def batch_edit_smart_discount_variants(
        self, body: BatchEditSmartDiscountVariantsRequest
    ) -> BatchEditSmartDiscountVariantsResponse:
        """Re-price a batch of live promotions. Scope: ``promotion``."""
        return parse(
            BatchEditSmartDiscountVariantsResponse,
            self._transport.put(
                SMART_DISCOUNT_VARIANTS_BATCH_ENDPOINT,
                json=body.to_payload(),
                headers=JSON_HEADERS,
            ),
        )

    # --- invoices --------------------------------------------------------------------------

    def list_invoices(
        self,
        *,
        page: int | None = None,
        size: int | None = None,
        sort: str | None = None,
        order: str | None = None,
        search: InvoiceSearch | None = None,
    ) -> InvoicesResponse:
        """The seller's invoices. Scope: ``invoice``."""
        return parse(
            InvoicesResponse,
            self._transport.get(
                INVOICES_ENDPOINT,
                params=list_params(page=page, size=size, sort=sort, order=order, search=search),
                headers=JSON_HEADERS,
            ),
        )

    def get_invoice_details(self, invoice_id: int) -> InvoiceDetailResponse:
        """One invoice's summary, broken into notation groups. Scope: ``invoice``.

        The notation ids in the result are what :meth:`list_invoice_items` needs.
        """
        return parse(
            InvoiceDetailResponse,
            self._transport.get(invoice_details_endpoint(invoice_id), headers=JSON_HEADERS),
        )

    def list_invoice_items(
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
        """The individual financial lines behind one notation. Scope: ``invoice``.

        Args:
            invoice_id: The invoice id (path).
            financial_notation_id: From ``get_invoice_details`` — a notation's ``id``.
            calculation_type: That notation's ``calculation_model_type``.
            page: 1-based page number.
            size: Page size.
            sort: Sort column.
            order: ``"asc"`` or ``"desc"``.
            search: Optional filters.
        """
        return parse(
            InvoiceItemsResponse,
            self._transport.get(
                invoice_items_endpoint(invoice_id, financial_notation_id, calculation_type),
                params=list_params(page=page, size=size, sort=sort, order=order, search=search),
                headers=JSON_HEADERS,
            ),
        )
