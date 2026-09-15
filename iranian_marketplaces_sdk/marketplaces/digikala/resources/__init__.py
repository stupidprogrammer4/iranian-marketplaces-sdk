"""Lazy access to the Digikala resource clients."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from iranian_marketplaces_sdk.common.http import AsyncTransport, SyncTransport

if TYPE_CHECKING:
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.auth import AuthAsync, AuthSync
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.batch import BatchAsync, BatchSync
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.bulk_shipping import (
        BulkShippingAsync,
        BulkShippingSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.buybox import (
        BuyboxAsync,
        BuyboxSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.categories import (
        CategoriesAsync,
        CategoriesSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.commissions import (
        CommissionsAsync,
        CommissionsSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.commitments import (
        CommitmentsAsync,
        CommitmentsSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.drop_shipping import (
        DropShippingAsync,
        DropShippingSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.finance import (
        FinanceAsync,
        FinanceSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.insight import (
        InsightAsync,
        InsightSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.inventories import (
        InventoriesAsync,
        InventoriesSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.invoices import (
        InvoicesAsync,
        InvoicesSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.lightning_deals import (
        LightningDealsAsync,
        LightningDealsSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.multi_pricing import (
        MultiPricingAsync,
        MultiPricingSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.nearby_stores import (
        NearbyStoresAsync,
        NearbyStoresSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.orders import (
        OrdersAsync,
        OrdersSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.packages import (
        PackagesAsync,
        PackagesSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.plp import PlpAsync, PlpSync
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.post_tracking import (
        PostTrackingAsync,
        PostTrackingSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.postex import (
        PostexAsync,
        PostexSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.price_stats import (
        PriceStatsAsync,
        PriceStatsSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.products import (
        ProductsAsync,
        ProductsSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.profile import (
        ProfileAsync,
        ProfileSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.promotions import (
        PromotionsAsync,
        PromotionsSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.questions import (
        QuestionsAsync,
        QuestionsSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.search_ads import (
        SearchAdsAsync,
        SearchAdsSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.search_ads_v2 import (
        SearchAdsV2Async,
        SearchAdsV2Sync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.seller_orders import (
        SellerOrdersAsync,
        SellerOrdersSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.seller_shipping import (
        SellerShippingAsync,
        SellerShippingSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.shipments import (
        ShipmentsAsync,
        ShipmentsSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.shipping_services import (
        ShippingServicesAsync,
        ShippingServicesSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.smart_discount import (
        SmartDiscountAsync,
        SmartDiscountSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.themes import (
        ThemesAsync,
        ThemesSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.variant_creation import (
        VariantCreationAsync,
        VariantCreationSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.variants import (
        VariantsAsync,
        VariantsSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.vouchers import (
        VouchersAsync,
        VouchersSync,
    )
    from iranian_marketplaces_sdk.marketplaces.digikala.resources.webhooks import (
        WebhooksAsync,
        WebhooksSync,
    )


class SyncResources:
    _transport: SyncTransport

    @cached_property
    def auth(self) -> AuthSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.auth import AuthSync

        return AuthSync(self._transport)

    @cached_property
    def batch(self) -> BatchSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.batch import BatchSync

        return BatchSync(self._transport)

    @cached_property
    def bulk_shipping(self) -> BulkShippingSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.bulk_shipping import (
            BulkShippingSync,
        )

        return BulkShippingSync(self._transport)

    @cached_property
    def buybox(self) -> BuyboxSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.buybox import BuyboxSync

        return BuyboxSync(self._transport)

    @cached_property
    def categories(self) -> CategoriesSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.categories import (
            CategoriesSync,
        )

        return CategoriesSync(self._transport)

    @cached_property
    def commissions(self) -> CommissionsSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.commissions import (
            CommissionsSync,
        )

        return CommissionsSync(self._transport)

    @cached_property
    def commitments(self) -> CommitmentsSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.commitments import (
            CommitmentsSync,
        )

        return CommitmentsSync(self._transport)

    @cached_property
    def drop_shipping(self) -> DropShippingSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.drop_shipping import (
            DropShippingSync,
        )

        return DropShippingSync(self._transport)

    @cached_property
    def finance(self) -> FinanceSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.finance import FinanceSync

        return FinanceSync(self._transport)

    @cached_property
    def insight(self) -> InsightSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.insight import InsightSync

        return InsightSync(self._transport)

    @cached_property
    def inventories(self) -> InventoriesSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.inventories import (
            InventoriesSync,
        )

        return InventoriesSync(self._transport)

    @cached_property
    def invoices(self) -> InvoicesSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.invoices import InvoicesSync

        return InvoicesSync(self._transport)

    @cached_property
    def lightning_deals(self) -> LightningDealsSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.lightning_deals import (
            LightningDealsSync,
        )

        return LightningDealsSync(self._transport)

    @cached_property
    def multi_pricing(self) -> MultiPricingSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.multi_pricing import (
            MultiPricingSync,
        )

        return MultiPricingSync(self._transport)

    @cached_property
    def nearby_stores(self) -> NearbyStoresSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.nearby_stores import (
            NearbyStoresSync,
        )

        return NearbyStoresSync(self._transport)

    @cached_property
    def orders(self) -> OrdersSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.orders import OrdersSync

        return OrdersSync(self._transport)

    @cached_property
    def packages(self) -> PackagesSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.packages import PackagesSync

        return PackagesSync(self._transport)

    @cached_property
    def plp(self) -> PlpSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.plp import PlpSync

        return PlpSync(self._transport)

    @cached_property
    def post_tracking(self) -> PostTrackingSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.post_tracking import (
            PostTrackingSync,
        )

        return PostTrackingSync(self._transport)

    @cached_property
    def postex(self) -> PostexSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.postex import PostexSync

        return PostexSync(self._transport)

    @cached_property
    def price_stats(self) -> PriceStatsSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.price_stats import (
            PriceStatsSync,
        )

        return PriceStatsSync(self._transport)

    @cached_property
    def products(self) -> ProductsSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.products import ProductsSync

        return ProductsSync(self._transport)

    @cached_property
    def profile(self) -> ProfileSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.profile import ProfileSync

        return ProfileSync(self._transport)

    @cached_property
    def promotions(self) -> PromotionsSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.promotions import (
            PromotionsSync,
        )

        return PromotionsSync(self._transport)

    @cached_property
    def questions(self) -> QuestionsSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.questions import QuestionsSync

        return QuestionsSync(self._transport)

    @cached_property
    def search_ads(self) -> SearchAdsSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.search_ads import (
            SearchAdsSync,
        )

        return SearchAdsSync(self._transport)

    @cached_property
    def search_ads_v2(self) -> SearchAdsV2Sync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.search_ads_v2 import (
            SearchAdsV2Sync,
        )

        return SearchAdsV2Sync(self._transport)

    @cached_property
    def seller_orders(self) -> SellerOrdersSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.seller_orders import (
            SellerOrdersSync,
        )

        return SellerOrdersSync(self._transport)

    @cached_property
    def seller_shipping(self) -> SellerShippingSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.seller_shipping import (
            SellerShippingSync,
        )

        return SellerShippingSync(self._transport)

    @cached_property
    def shipments(self) -> ShipmentsSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.shipments import ShipmentsSync

        return ShipmentsSync(self._transport)

    @cached_property
    def shipping_services(self) -> ShippingServicesSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.shipping_services import (
            ShippingServicesSync,
        )

        return ShippingServicesSync(self._transport)

    @cached_property
    def smart_discount(self) -> SmartDiscountSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.smart_discount import (
            SmartDiscountSync,
        )

        return SmartDiscountSync(self._transport)

    @cached_property
    def themes(self) -> ThemesSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.themes import ThemesSync

        return ThemesSync(self._transport)

    @cached_property
    def variant_creation(self) -> VariantCreationSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.variant_creation import (
            VariantCreationSync,
        )

        return VariantCreationSync(self._transport)

    @cached_property
    def variants(self) -> VariantsSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.variants import VariantsSync

        return VariantsSync(self._transport)

    @cached_property
    def vouchers(self) -> VouchersSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.vouchers import VouchersSync

        return VouchersSync(self._transport)

    @cached_property
    def webhooks(self) -> WebhooksSync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.webhooks import WebhooksSync

        return WebhooksSync(self._transport)


class AsyncResources:
    _transport: AsyncTransport

    @cached_property
    def auth(self) -> AuthAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.auth import AuthAsync

        return AuthAsync(self._transport)

    @cached_property
    def batch(self) -> BatchAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.batch import BatchAsync

        return BatchAsync(self._transport)

    @cached_property
    def bulk_shipping(self) -> BulkShippingAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.bulk_shipping import (
            BulkShippingAsync,
        )

        return BulkShippingAsync(self._transport)

    @cached_property
    def buybox(self) -> BuyboxAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.buybox import BuyboxAsync

        return BuyboxAsync(self._transport)

    @cached_property
    def categories(self) -> CategoriesAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.categories import (
            CategoriesAsync,
        )

        return CategoriesAsync(self._transport)

    @cached_property
    def commissions(self) -> CommissionsAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.commissions import (
            CommissionsAsync,
        )

        return CommissionsAsync(self._transport)

    @cached_property
    def commitments(self) -> CommitmentsAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.commitments import (
            CommitmentsAsync,
        )

        return CommitmentsAsync(self._transport)

    @cached_property
    def drop_shipping(self) -> DropShippingAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.drop_shipping import (
            DropShippingAsync,
        )

        return DropShippingAsync(self._transport)

    @cached_property
    def finance(self) -> FinanceAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.finance import FinanceAsync

        return FinanceAsync(self._transport)

    @cached_property
    def insight(self) -> InsightAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.insight import InsightAsync

        return InsightAsync(self._transport)

    @cached_property
    def inventories(self) -> InventoriesAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.inventories import (
            InventoriesAsync,
        )

        return InventoriesAsync(self._transport)

    @cached_property
    def invoices(self) -> InvoicesAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.invoices import InvoicesAsync

        return InvoicesAsync(self._transport)

    @cached_property
    def lightning_deals(self) -> LightningDealsAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.lightning_deals import (
            LightningDealsAsync,
        )

        return LightningDealsAsync(self._transport)

    @cached_property
    def multi_pricing(self) -> MultiPricingAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.multi_pricing import (
            MultiPricingAsync,
        )

        return MultiPricingAsync(self._transport)

    @cached_property
    def nearby_stores(self) -> NearbyStoresAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.nearby_stores import (
            NearbyStoresAsync,
        )

        return NearbyStoresAsync(self._transport)

    @cached_property
    def orders(self) -> OrdersAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.orders import OrdersAsync

        return OrdersAsync(self._transport)

    @cached_property
    def packages(self) -> PackagesAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.packages import PackagesAsync

        return PackagesAsync(self._transport)

    @cached_property
    def plp(self) -> PlpAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.plp import PlpAsync

        return PlpAsync(self._transport)

    @cached_property
    def post_tracking(self) -> PostTrackingAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.post_tracking import (
            PostTrackingAsync,
        )

        return PostTrackingAsync(self._transport)

    @cached_property
    def postex(self) -> PostexAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.postex import PostexAsync

        return PostexAsync(self._transport)

    @cached_property
    def price_stats(self) -> PriceStatsAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.price_stats import (
            PriceStatsAsync,
        )

        return PriceStatsAsync(self._transport)

    @cached_property
    def products(self) -> ProductsAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.products import ProductsAsync

        return ProductsAsync(self._transport)

    @cached_property
    def profile(self) -> ProfileAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.profile import ProfileAsync

        return ProfileAsync(self._transport)

    @cached_property
    def promotions(self) -> PromotionsAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.promotions import (
            PromotionsAsync,
        )

        return PromotionsAsync(self._transport)

    @cached_property
    def questions(self) -> QuestionsAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.questions import (
            QuestionsAsync,
        )

        return QuestionsAsync(self._transport)

    @cached_property
    def search_ads(self) -> SearchAdsAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.search_ads import (
            SearchAdsAsync,
        )

        return SearchAdsAsync(self._transport)

    @cached_property
    def search_ads_v2(self) -> SearchAdsV2Async:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.search_ads_v2 import (
            SearchAdsV2Async,
        )

        return SearchAdsV2Async(self._transport)

    @cached_property
    def seller_orders(self) -> SellerOrdersAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.seller_orders import (
            SellerOrdersAsync,
        )

        return SellerOrdersAsync(self._transport)

    @cached_property
    def seller_shipping(self) -> SellerShippingAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.seller_shipping import (
            SellerShippingAsync,
        )

        return SellerShippingAsync(self._transport)

    @cached_property
    def shipments(self) -> ShipmentsAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.shipments import (
            ShipmentsAsync,
        )

        return ShipmentsAsync(self._transport)

    @cached_property
    def shipping_services(self) -> ShippingServicesAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.shipping_services import (
            ShippingServicesAsync,
        )

        return ShippingServicesAsync(self._transport)

    @cached_property
    def smart_discount(self) -> SmartDiscountAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.smart_discount import (
            SmartDiscountAsync,
        )

        return SmartDiscountAsync(self._transport)

    @cached_property
    def themes(self) -> ThemesAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.themes import ThemesAsync

        return ThemesAsync(self._transport)

    @cached_property
    def variant_creation(self) -> VariantCreationAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.variant_creation import (
            VariantCreationAsync,
        )

        return VariantCreationAsync(self._transport)

    @cached_property
    def variants(self) -> VariantsAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.variants import VariantsAsync

        return VariantsAsync(self._transport)

    @cached_property
    def vouchers(self) -> VouchersAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.vouchers import VouchersAsync

        return VouchersAsync(self._transport)

    @cached_property
    def webhooks(self) -> WebhooksAsync:
        from iranian_marketplaces_sdk.marketplaces.digikala.resources.webhooks import WebhooksAsync

        return WebhooksAsync(self._transport)
