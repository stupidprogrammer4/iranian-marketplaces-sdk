# مرجع متدهای دیجی‌کالا

این جدول ۲۷۴ عملیات موجود در SDK را بر اساس بخش مرتب می‌کند. هر متد در کلاینت sync و async
وجود دارد؛ در حالت async از `await` استفاده کنید. آرگومان‌ها برای کوتاه‌شدن جدول حذف شده‌اند؛
امضای متد در IDE نام و نوع ورودی‌های لازم را نشان می‌دهد.

- برای شروع: [راهنمای دیجی‌کالا](../digikala/README.md)
- برای پاسخ‌های فایل و `RawResponse`: [ویرایش و فایل‌ها](../digikala/updates-and-files.md)
- منبع مسیرها: [Swagger فروشندگان](https://seller.digikala.com/open-api/v1/doc/)، نسخهٔ ۲۰۲۶-۰۹-۱۵

## health

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/` | `client.health_check()` | Typed model |

## auth

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/auth/scopes` | `client.auth.list_scopes()` | Typed model |
| GET | `/open-api/v1/auth/scopes/{client_code}` | `client.auth.get_client_scopes()` | Typed model |
| POST | `/open-api/v1/auth/token` | `client.create_token()` | Typed model |
| POST | `/open-api/v1/auth/refresh-token` | `client.refresh_token()` | Typed model |
| POST | `/open-api/v1/auth/revoke` | `client.auth.revoke()` | Typed model |

## categories

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/categories/tree` | `client.categories.tree()` | Typed model |

## products

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/product-creation/search/v2` | `client.products.search()` | Typed model |
| GET | `/open-api/v1/product-creation/search/suggestion/v2` | `client.products.suggestions()` | Typed model |
| GET | `/open-api/v1/product-creation/be-seller/{product_id}` | `client.products.seller_permission()` | Typed model |
| GET | `/open-api/v1/product-creation/search/category/v2/{keyword}` | `client.products.search_categories()` | Typed model |
| GET | `/open-api/v1/product-creation/category/{category_id}/validation` | `client.products.validate_category()` | Typed model |
| POST | `/open-api/v1/product-creation/product/detail/validation` | `client.products.validate_details()` | Typed model |
| GET | `/open-api/v1/product-creation/draft-product/count` | `client.products.count_drafts()` | Typed model |
| GET | `/open-api/v1/product-creation/draft-product/{draft_product_id}` | `client.products.get_draft()` | Typed model |
| GET | `/open-api/v1/product-creation/{draft_product_id}/auto-title` | `client.products.get_auto_title()` | Typed model |
| POST | `/open-api/v1/product-creation/auto-title/save` | `client.products.save_auto_title()` | Typed model |
| GET | `/open-api/v1/product-creation/attributes/{category_id}` | `client.products.get_attributes()` | Typed model |
| POST | `/open-api/v1/product-creation/attributes` | `client.products.save_attributes()` | RawResponse |
| POST | `/open-api/v1/product-creation/images/requests/brand-logo/upload` | `client.products.upload_brand_logo()` | Typed model |
| POST | `/open-api/v1/product-creation/images/requests/upload` | `client.products.upload_request_image()` | Typed model |
| POST | `/open-api/v1/product-creation/images/upload` | `client.products.upload_image()` | Typed model |
| POST | `/open-api/v1/product-creation/images/ai` | `client.products.generate_image()` | Typed model |
| POST | `/open-api/v1/product-creation/save` | `client.products.save()` | Typed model |
| POST | `/open-api/v1/product-creation/assign` | `client.products.assign()` | Typed model |
| POST | `/open-api/v1/product-creation/brand/request` | `client.products.request_brand()` | Typed model |
| GET | `/open-api/v1/product-creation/brand` | `client.products.list_brands()` | Typed model |
| GET | `/open-api/v1/draft-products/seller` | `client.products.list_drafts()` | Typed model |
| DELETE | `/open-api/v1/draft-products/{draft_product_id}` | `client.products.delete_draft()` | RawResponse |
| GET | `/open-api/v1/products/seller` | `client.products.list_seller()` | Typed model |
| GET | `/open-api/v1/products/{product_id}/score` | `client.products.score()` | Typed model |
| POST | `/open-api/v1/product-edit/{product_id}/publish` | `client.products.publish()` | Typed model |
| GET | `/open-api/v1/product-edit/{product_id}` | `client.products.get_edit()` | Typed model |
| PUT | `/open-api/v1/product-edit/{product_id}` | `client.products.update()` | RawResponse |
| POST | `/open-api/v1/product-edit/{category_id}/auto-title` | `client.products.generate_title()` | Typed model |

## variants

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/variants` | `client.variants.list()` | Typed model |
| GET | `/open-api/v1/variants/{variant_id}` | `client.variants.get()` | Typed model |
| PUT | `/open-api/v1/variants/{variant_id}` | `client.variants.update()` | Typed model |
| PUT | `/open-api/v1/variants/b2b-activation` | `client.variants.update_b2b_activation()` | Typed model |
| POST | `/open-api/v1/variants/export` | `client.variants.export()` | Typed model |
| GET | `/open-api/v1/variants/{variant_id}/gold` | `client.variants.get_gold()` | Typed model |
| PUT | `/open-api/v1/variants/{variant_id}/gold` | `client.variants.update_gold()` | Typed model |
| GET | `/open-api/v1/variants/{variant_id}/price-calculator` | `client.variants.calculate_price()` | Typed model |
| PUT | `/open-api/v1/variants/{variant_id}/activation` | `client.variants.update_activation()` | Typed model |
| GET | `/open-api/v1/variants/{variant_id}/b2b-prices` | `client.variants.get_b2b_prices()` | Typed model |
| PUT | `/open-api/v1/variants/{variant_id}/b2b-prices` | `client.variants.update_b2b_prices()` | Typed model |
| PUT | `/open-api/v1/variants/{variant_id}/archive` | `client.variants.archive()` | Typed model |
| GET | `/open-api/v1/variants/{variant_id}/seller-stock` | `client.variants.get_seller_stock()` | Typed model |
| PATCH | `/open-api/v1/variants/{variant_id}/seller-stock` | `client.variants.update_seller_stock()` | Typed model |
| PATCH | `/open-api/v1/variants/selling-price` | `client.variants.update_selling_price()` | Typed model |

## variant_creation

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/variants/creation/{product_id}` | `client.variant_creation.get()` | Typed model |
| POST | `/open-api/v1/variants/creation/{product_id}` | `client.variant_creation.create()` | Typed model |
| PUT | `/open-api/v1/variants/creation/{product_id}/{variant_id}` | `client.variant_creation.update()` | Typed model |
| GET | `/open-api/v1/variants/creation/size/types` | `client.variant_creation.list_size_types()` | Typed model |
| POST | `/open-api/v1/variants/creation/size/request` | `client.variant_creation.request_size()` | Typed model |
| POST | `/open-api/v1/variants/creation/color/request` | `client.variant_creation.request_color()` | Typed model |
| POST | `/open-api/v1/variants/creation/warranty/request` | `client.variant_creation.request_warranty()` | Typed model |

## themes

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/variants/creation/themes/{theme_id}/theme-values` | `client.themes.list_values()` | Typed model |

## orders

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/orders` | `client.orders.list()` | Typed model |
| GET | `/open-api/v1/orders/statistics` | `client.orders.statistics()` | Typed model |
| GET | `/open-api/v1/orders/history` | `client.orders.history()` | Typed model |
| DELETE | `/open-api/v1/orders/{order_item_id}` | `client.orders.cancel()` | Typed model |

## inventories

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/inventories` | `client.inventories.list()` | Typed model |
| GET | `/open-api/v1/inventories/{product_variant_id}` | `client.inventories.dead_stock()` | Typed model |
| GET | `/open-api/v1/inventories/{product_variant_id}/export` | `client.inventories.export_dead_stock()` | Typed model |
| POST | `/open-api/v1/inventories/export` | `client.inventories.export()` | Typed model |

## packages

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/packages` | `client.packages.list()` | Typed model |
| POST | `/open-api/v1/packages` | `client.packages.create()` | RawResponse |
| GET | `/open-api/v1/packages/warehouses` | `client.packages.warehouses()` | Typed model |
| GET | `/open-api/v1/packages/warehouses/{warehouse_id}/capacities` | `client.packages.warehouse_capacities()` | Typed model |
| POST | `/open-api/v1/packages/warehouses/{warehouse_id}/capacities` | `client.packages.calculate_warehouse_capacities()` | Typed model |
| GET | `/open-api/v1/packages/{package_id}` | `client.packages.get()` | Typed model |
| DELETE | `/open-api/v1/packages/{package_id}` | `client.packages.delete()` | RawResponse |
| GET | `/open-api/v1/packages/{package_id}/excel/export` | `client.packages.export()` | Typed model |
| GET | `/open-api/v1/packages/consignment/variants` | `client.packages.consignment_variants()` | Typed model |
| GET | `/open-api/v1/packages/order-fulfilment/variants` | `client.packages.fulfilment_variants()` | Typed model |
| POST | `/open-api/v1/packages/order-fulfilment/variants` | `client.packages.filter_fulfilment_variants()` | Typed model |
| GET | `/open-api/v1/variants/packages/consignment` | `client.packages.consignment()` | Typed model |

## shipments

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/shipments/dk` | `client.shipments.list()` | Typed model |
| POST | `/open-api/v1/shipments/dk` | `client.shipments.create()` | Typed model |
| GET | `/open-api/v1/shipments/dk/packages` | `client.shipments.packages()` | Typed model |
| GET | `/open-api/v1/shipments/dk/{shipment_id}` | `client.shipments.get()` | Typed model |
| DELETE | `/open-api/v1/shipments/dk/{shipment_id}` | `client.shipments.delete()` | RawResponse |

## profile

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/profile` | `client.profile.get()` | Typed model |
| GET | `/open-api/v1/profile/business` | `client.profile.business()` | Typed model |
| PATCH | `/open-api/v1/profile/business` | `client.profile.update_business()` | Typed model |
| GET | `/open-api/v1/profile/store` | `client.profile.store()` | Typed model |
| GET | `/open-api/v1/profile/address` | `client.profile.addresses()` | Typed model |
| GET | `/open-api/v1/profile/warehouse` | `client.profile.warehouses()` | Typed model |
| GET | `/open-api/v1/profile/document` | `client.profile.documents()` | Typed model |
| GET | `/open-api/v1/profile/training` | `client.profile.training()` | Typed model |
| GET | `/open-api/v1/profile/performance` | `client.profile.performance()` | Typed model |

## questions

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/questions` | `client.questions.list()` | Typed model |
| GET | `/open-api/v1/questions/{question_id}` | `client.questions.get()` | Typed model |
| POST | `/open-api/v1/questions/answer` | `client.questions.answer()` | Typed model |

## insight

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/insight/overview` | `client.insight.overview()` | Typed model |
| GET | `/open-api/v1/insight/top-deactivated` | `client.insight.top_deactivated()` | Typed model |
| GET | `/open-api/v1/insight/trend-sales-reports` | `client.insight.sales_trend()` | Typed model |
| GET | `/open-api/v1/insight/sales-reports` | `client.insight.sales_report()` | Typed model |
| POST | `/open-api/v1/insight/overview/export` | `client.insight.export()` | Typed model |

## lightning_deals

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/lightening-deal/products` | `client.lightning_deals.products()` | Typed model |
| GET | `/open-api/v1/lightening-deal/products/{product_id}` | `client.lightning_deals.get_product()` | Typed model |
| GET | `/open-api/v1/lightening-deal/promotions` | `client.lightning_deals.promotions()` | Typed model |
| GET | `/open-api/v1/lightening-deal/promotions/{productId}` | `client.lightning_deals.get_promotions()` | Typed model |
| POST | `/open-api/v1/lightening-deal/bids` | `client.lightning_deals.create_bids()` | Typed model |
| GET | `/open-api/v1/lightening-deal/bids` | `client.lightning_deals.bids()` | Typed model |
| GET | `/open-api/v1/lightening-deal/bidsSummary` | `client.lightning_deals.bids_summary()` | Typed model |
| GET | `/open-api/v1/lightening-deal/check-duplicate-dkp-in-promotion/{promotionId}/{productId}` | `client.lightning_deals.check_duplicate()` | Typed model |
| POST | `/open-api/v1/lightening-deal/bids/{bidId}/payment-method` | `client.lightning_deals.update_payment_method()` | RawResponse |

## buybox

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/pricing/buybox/price-suggestion/winning-price` | `client.buybox.winning_price()` | Typed model |
| GET | `/open-api/v1/pricing/buybox/price-suggestion/nth-rank-winning-price` | `client.buybox.ranked_winning_price()` | Typed model |

## smart_discount

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/pricing/smart-discount/variants/eligible` | `client.smart_discount.eligible()` | Typed model |
| GET | `/open-api/v1/pricing/smart-discount/variants/{active_status}` | `client.smart_discount.list()` | Typed model |
| POST | `/open-api/v1/pricing/smart-discount/variants/batch` | `client.smart_discount.create_batch()` | Typed model |
| PUT | `/open-api/v1/pricing/smart-discount/variants/batch` | `client.smart_discount.update_batch()` | Typed model |
| POST | `/open-api/v1/pricing/smart-discount/variants` | `client.smart_discount.create()` | Typed model |
| PUT | `/open-api/v1/pricing/smart-discount/variants` | `client.smart_discount.update()` | Typed model |
| DELETE | `/open-api/v1/pricing/smart-discount/variants` | `client.smart_discount.delete()` | Typed model |
| DELETE | `/open-api/v1/pricing/smart-discount/variants/all` | `client.smart_discount.delete_all()` | Typed model |
| GET | `/open-api/v1/pricing/smart-discount/variants/eligible/excel` | `client.smart_discount.export_eligible()` | RawResponse |
| GET | `/open-api/v1/pricing/smart-discount/variants/excel/sample` | `client.smart_discount.sample_excel()` | RawResponse |
| GET | `/open-api/v1/pricing/smart-discount/variants/excel/async-export` | `client.smart_discount.export()` | Typed model |
| POST | `/open-api/v1/pricing/smart-discount/variants/excel` | `client.smart_discount.import_excel()` | Typed model |
| POST | `/open-api/v1/pricing/smart-discount/variants/excel/delete-all-async` | `client.smart_discount.delete_all_async()` | Typed model |
| GET | `/open-api/v1/pricing/smart-discount/auto-joined/{campaign_name}` | `client.smart_discount.auto_joined()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/{promotion_id}/variants/eligible/excel` | `client.smart_discount.export_promotion_eligible()` | RawResponse |

## promotions

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/pricing/promotions` | `client.promotions.list()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/configs` | `client.promotions.configs()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/recommended` | `client.promotions.recommended()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/eligible` | `client.promotions.eligible()` | Typed model |
| POST | `/open-api/v1/pricing/promotions/eligible/min-discounts` | `client.promotions.minimum_discounts()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/unjoined` | `client.promotions.unjoined()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/variant-current-promotions/{product_variant_id}` | `client.promotions.current_for_variant()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/variants` | `client.promotions.variants()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/variants/{variant_id}` | `client.promotions.get_variant()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/variants/rejection-reason/{promotion_variant_id}` | `client.promotions.rejection_reason()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/{promotion_id}` | `client.promotions.get()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/{promotion_id}/variants` | `client.promotions.list_variants()` | Typed model |
| POST | `/open-api/v1/pricing/promotions/{promotion_id}/variants` | `client.promotions.add_variants()` | Typed model |
| PATCH | `/open-api/v1/pricing/promotions/{promotion_id}/variants` | `client.promotions.update_variants()` | Typed model |
| DELETE | `/open-api/v1/pricing/promotions/{promotion_id}/variants` | `client.promotions.delete_variants()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/{promotion_id}/variants/rejected` | `client.promotions.rejected_variants()` | Typed model |
| POST | `/open-api/v1/pricing/promotions/{promotion_id}/variants/batch` | `client.promotions.add_variants_batch()` | Typed model |
| PATCH | `/open-api/v1/pricing/promotions/{promotion_id}/variants/batch` | `client.promotions.update_variants_batch()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/{promotion_id}/variants/eligible` | `client.promotions.eligible_variants()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/{promotion_id}/variants/eligible_v2` | `client.promotions.eligible_variants_v2()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/{promotion_id}/variants/to-join` | `client.promotions.variants_to_join()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/{promotion_id}/variants/{variant_id}/commission-discount` | `client.promotions.commission_discount()` | Typed model |
| GET | `/open-api/v1/pricing/promotions/{promotion_id}/variants/excel/sample` | `client.promotions.sample_excel()` | RawResponse |
| POST | `/open-api/v1/pricing/promotions/{promotion_id}/variants/excel` | `client.promotions.import_excel()` | Typed model |

## plp

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/pricing/plp` | `client.plp.list()` | Typed model |
| DELETE | `/open-api/v1/pricing/plp` | `client.plp.delete()` | Typed model |
| POST | `/open-api/v1/pricing/plp` | `client.plp.create()` | Typed model |
| PUT | `/open-api/v1/pricing/plp` | `client.plp.update()` | Typed model |
| GET | `/open-api/v1/pricing/plp/{promotion_id}` | `client.plp.get()` | Typed model |
| DELETE | `/open-api/v1/pricing/plp/variants` | `client.plp.delete_variants()` | Typed model |
| GET | `/open-api/v1/pricing/plp/variants/eligible` | `client.plp.eligible_variants()` | Typed model |
| GET | `/open-api/v1/pricing/plp/excel/import/sample` | `client.plp.sample_excel()` | Typed model |
| GET | `/open-api/v1/pricing/plp/excel/{promotion_id}` | `client.plp.export()` | Typed model |
| POST | `/open-api/v1/pricing/plp/excel` | `client.plp.import_excel()` | Typed model |

## vouchers

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/pricing/vouchers` | `client.vouchers.list()` | Typed model |
| POST | `/open-api/v1/pricing/vouchers` | `client.vouchers.create()` | Typed model |
| PUT | `/open-api/v1/pricing/vouchers` | `client.vouchers.update()` | Typed model |
| GET | `/open-api/v1/pricing/vouchers/types` | `client.vouchers.types()` | Typed model |
| GET | `/open-api/v1/pricing/vouchers/{voucher_id}` | `client.vouchers.get()` | Typed model |
| GET | `/open-api/v1/pricing/vouchers/variants/eligible` | `client.vouchers.eligible_variants()` | Typed model |

## price_stats

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/pricing/price-stats/{variant_id}/boundary` | `client.price_stats.boundary()` | Typed model |

## multi_pricing

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/pricing/multi-pricing/estimate` | `client.multi_pricing.estimate()` | Typed model |

## batch

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| POST | `/open-api/v1/batch/inquiry` | `client.batch.inquiry()` | Typed model |
| POST | `/open-api/v1/batch/variant/update` | `client.batch.update_variants()` | Typed model |
| POST | `/open-api/v1/batch/variant/activation/update` | `client.batch.update_activation()` | Typed model |
| POST | `/open-api/v1/batch/variant/seller-stock/update` | `client.batch.update_stock()` | Typed model |

## seller_shipping

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| POST | `/open-api/v1/shipments/seller/new-settings` | `client.seller_shipping.create()` | Typed model |
| GET | `/open-api/v1/shipments/seller/new-settings` | `client.seller_shipping.list()` | Typed model |
| PATCH | `/open-api/v1/shipments/seller/new-settings/{id}` | `client.seller_shipping.update()` | Typed model |
| GET | `/open-api/v1/shipments/seller/new-settings/{id}` | `client.seller_shipping.get()` | Typed model |
| GET | `/open-api/v1/shipments/seller/new-settings/state` | `client.seller_shipping.states()` | Typed model |
| GET | `/open-api/v1/shipments/seller/new-settings/time-scope` | `client.seller_shipping.time_scopes()` | Typed model |
| POST | `/open-api/v1/shipments/seller/new-settings/deactivate-cities` | `client.seller_shipping.deactivate_cities()` | RawResponse |

## seller_orders

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/ship-by-seller-orders` | `client.seller_orders.list()` | Typed model |
| GET | `/open-api/v1/ship-by-seller-orders/statistics` | `client.seller_orders.statistics()` | Typed model |
| GET | `/open-api/v1/ship-by-seller-orders/{shipment_id}` | `client.seller_orders.get()` | Typed model |
| GET | `/open-api/v1/ship-by-seller-orders/customer/{shipment_id}` | `client.seller_orders.customer()` | Typed model |
| GET | `/open-api/v1/ship-by-seller-orders/post-data/{shipment_id}` | `client.seller_orders.post_data()` | Typed model |
| GET | `/open-api/v1/ship-by-seller-orders/time-scopes/{shipment_id}` | `client.seller_orders.time_scopes()` | Typed model |
| GET | `/open-api/v1/ship-by-seller-orders/failed-delivery/time-scopes/{shipment_id}` | `client.seller_orders.failed_delivery_time_scopes()` | Typed model |
| POST | `/open-api/v1/ship-by-seller-orders/cancel-item` | `client.seller_orders.cancel_item()` | RawResponse |
| POST | `/open-api/v1/ship-by-seller-orders/cancel-shipment` | `client.seller_orders.cancel_shipment()` | RawResponse |
| POST | `/open-api/v1/ship-by-seller-orders/tracking-code` | `client.seller_orders.update_tracking_code()` | RawResponse |
| PUT | `/open-api/v1/ship-by-seller-orders/update-status` | `client.seller_orders.update_status()` | RawResponse |
| POST | `/open-api/v1/ship-by-seller-orders/full-delivered` | `client.seller_orders.mark_delivered()` | RawResponse |
| PUT | `/open-api/v1/ship-by-seller-orders/update-edited` | `client.seller_orders.update_edited()` | RawResponse |
| POST | `/open-api/v1/ship-by-seller-orders/failed-delivery` | `client.seller_orders.report_failed_delivery()` | RawResponse |
| PUT | `/open-api/v1/ship-by-seller-orders/change-time-scope` | `client.seller_orders.change_time_scope()` | RawResponse |
| GET | `/open-api/v1/ship-by-seller-orders/post-order/{shipment_id}` | `client.seller_orders.post_order()` | Typed model |
| POST | `/open-api/v1/ship-by-seller-orders/batch-update-status` | `client.seller_orders.batch_update_status()` | RawResponse |

## webhooks

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/webhook/event-types` | `client.webhooks.event_types()` | Typed model |
| POST | `/open-api/v1/webhook/subscription` | `client.webhooks.subscribe()` | Typed model |
| POST | `/open-api/v1/webhook/unsubscription` | `client.webhooks.unsubscribe()` | Typed model |
| POST | `/open-api/v1/webhook/subscription/change-activation` | `client.webhooks.change_activation()` | Typed model |

## commissions

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/commissions/` | `client.commissions.list()` | Typed model |

## shipping_services

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/shipping-services/postex-status` | `client.shipping_services.postex_status()` | RawResponse |
| GET | `/open-api/v1/shipping-services/wallet/balance` | `client.shipping_services.wallet_balance()` | RawResponse |
| GET | `/open-api/v1/shipping-services/user` | `client.shipping_services.get_user()` | RawResponse |
| GET | `/open-api/v1/shipping-services/wallet/transactions/{transaction_id}` | `client.shipping_services.transaction()` | RawResponse |
| GET | `/open-api/v1/shipping-services/wallet/verify` | `client.shipping_services.verify_wallet()` | RawResponse |
| GET | `/open-api/v1/shipping-services/boxes` | `client.shipping_services.boxes()` | Typed model |
| GET | `/open-api/v1/shipping-services/token-status` | `client.shipping_services.token_status()` | RawResponse |
| POST | `/open-api/v1/shipping-services/parcels/post-tracking-code/bulk` | `client.shipping_services.bulk_tracking_codes()` | RawResponse |
| POST | `/open-api/v1/shipping-services/parcels/excel` | `client.shipping_services.import_parcels()` | RawResponse |
| POST | `/open-api/v1/shipping-services/parcels/cost` | `client.shipping_services.calculate_cost()` | RawResponse |
| GET | `/open-api/v1/shipping-services/order/{shipment_id}` | `client.shipping_services.get_order()` | RawResponse |
| GET | `/open-api/v1/shipping-services/order/detail/{order_id}` | `client.shipping_services.order_detail()` | Typed model |
| GET | `/open-api/v1/shipping-services/user/info` | `client.shipping_services.user_info()` | RawResponse |
| GET | `/open-api/v1/shipping-services/label/{registration_method}/{parcel_number}` | `client.shipping_services.label()` | RawResponse |
| POST | `/open-api/v1/shipping-services/label-request` | `client.shipping_services.request_label()` | RawResponse |
| GET | `/open-api/v1/shipping-services/label-request/{request_id}` | `client.shipping_services.label_request_status()` | RawResponse |

## postex

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| POST | `/open-api/v1/shipping-services/user` | `client.postex.create_user()` | RawResponse |
| POST | `/open-api/v1/shipping-services/wallet/charge` | `client.postex.charge_wallet()` | RawResponse |
| GET | `/open-api/v1/shipping-services/wallet/transactions` | `client.postex.transactions()` | Typed model |
| POST | `/open-api/v1/shipping-services/parcels/calculate-price` | `client.postex.calculate_price()` | RawResponse |

## post_tracking

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/shipping-services/excel/post-tracking-sample` | `client.post_tracking.sample_excel()` | RawResponse |
| POST | `/open-api/v1/shipping-services/import/tracking-code` | `client.post_tracking.import_tracking_codes()` | RawResponse |

## drop_shipping

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| POST | `/open-api/v1/shipping-services/send_otp` | `client.drop_shipping.send_otp()` | RawResponse |
| GET | `/open-api/v1/shipping-services/parcels/total-weight` | `client.drop_shipping.total_weight()` | RawResponse |
| POST | `/open-api/v1/shipping-services/user/register` | `client.drop_shipping.register_user()` | RawResponse |

## bulk_shipping

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| PUT | `/open-api/v1/shipping-services/order/cancel/{shipment_id}` | `client.bulk_shipping.cancel_order()` | RawResponse |
| POST | `/open-api/v1/bulk-shipping-services/packaging` | `client.bulk_shipping.package()` | RawResponse |
| POST | `/open-api/v1/bulk-shipping-services/bulk-packaging` | `client.bulk_shipping.bulk_package()` | RawResponse |
| POST | `/open-api/v1/bulk-shipping-services/simple-packaging` | `client.bulk_shipping.simple_package()` | RawResponse |
| POST | `/open-api/v1/bulk-shipping-services/pickup` | `client.bulk_shipping.pickup()` | RawResponse |
| GET | `/open-api/v1/bulk-shipping-services/detail/{shipment_ids}` | `client.bulk_shipping.detail()` | Typed model |
| GET | `/open-api/v1/bulk-shipping-services/promise-date/{shipment_ids}` | `client.bulk_shipping.promise_date()` | RawResponse |

## invoices

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/invoices` | `client.invoices.list()` | Typed model |
| GET | `/open-api/v1/invoices/{invoice_id}/details` | `client.invoices.details()` | Typed model |
| GET | `/open-api/v1/invoices/{invoice_id}/items/{financial_notation_id}/{calculation_type}` | `client.invoices.items()` | Typed model |
| POST | `/open-api/v1/invoices/vat` | `client.invoices.submit_vat()` | RawResponse |

## finance

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/finance/overview/v2` | `client.finance.overview()` | Typed model |
| GET | `/open-api/v1/finance/transactions` | `client.finance.transactions()` | Typed model |
| GET | `/open-api/v1/finance/transactions/rows` | `client.finance.transaction_rows()` | Typed model |
| GET | `/open-api/v1/finance/transactions/summary` | `client.finance.transaction_summary()` | Typed model |
| GET | `/open-api/v1/finance/transactions/{transaction_id}` | `client.finance.get_transaction()` | Typed model |
| GET | `/open-api/v1/finance/payouts` | `client.finance.payouts()` | Typed model |
| GET | `/open-api/v1/finance/payouts/{payout_id}` | `client.finance.get_payout()` | Typed model |
| GET | `/open-api/v1/finance/seller-invoices` | `client.finance.seller_invoices()` | Typed model |
| POST | `/open-api/v1/finance/transactions/export/excel` | `client.finance.export_transactions()` | RawResponse |

## commitments

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/commitments` | `client.commitments.list()` | Typed model |
| GET | `/open-api/v1/commitments/metadata` | `client.commitments.metadata()` | Typed model |
| POST | `/open-api/v1/commitments/export` | `client.commitments.export()` | Typed model |
| POST | `/open-api/v1/commitments/report/export` | `client.commitments.export_report()` | Typed model |
| GET | `/open-api/v1/commitments/{variant_id}` | `client.commitments.get()` | Typed model |

## search_ads

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/search-ads/campaigns` | `client.search_ads.list()` | Typed model |
| POST | `/open-api/v1/search-ads/campaigns` | `client.search_ads.create()` | Typed model |
| GET | `/open-api/v1/search-ads/campaigns/{campaignId}` | `client.search_ads.get()` | Typed model |
| GET | `/open-api/v1/search-ads/campaigns/recommended-products` | `client.search_ads.recommended_products()` | Typed model |
| PUT | `/open-api/v1/search-ads/campaigns/{campaign_id}` | `client.search_ads.update()` | Typed model |
| PATCH | `/open-api/v1/search-ads/campaigns/{campaignId}/status` | `client.search_ads.update_status()` | Typed model |

## search_ads_v2

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/search-ads/v2/products` | `client.search_ads_v2.products()` | Typed model |
| GET | `/open-api/v1/search-ads/v2/setting` | `client.search_ads_v2.settings()` | Typed model |
| POST | `/open-api/v1/search-ads/v2/campaigns` | `client.search_ads_v2.create()` | Typed model |
| GET | `/open-api/v1/search-ads/v2/campaigns` | `client.search_ads_v2.list()` | Typed model |
| GET | `/open-api/v1/search-ads/v2/campaigns/{campaign_id}` | `client.search_ads_v2.get()` | Typed model |
| PATCH | `/open-api/v1/search-ads/v2/campaigns/{campaign_id}` | `client.search_ads_v2.update()` | Typed model |
| GET | `/open-api/v1/search-ads/v2/campaigns/{campaign_id}/report` | `client.search_ads_v2.report()` | Typed model |
| GET | `/open-api/v1/search-ads/v2/campaigns/{campaign_id}/overview` | `client.search_ads_v2.overview()` | Typed model |
| GET | `/open-api/v1/search-ads/v2/campaigns/{campaign_id}/products/{product_id}/overview` | `client.search_ads_v2.campaign_product_overview()` | Typed model |
| GET | `/open-api/v1/search-ads/v2/products/{product_id}/overview` | `client.search_ads_v2.product_overview()` | Typed model |
| GET | `/open-api/v1/search-ads/v2/seller/overview` | `client.search_ads_v2.seller_overview()` | Typed model |
| PATCH | `/open-api/v1/search-ads/v2/campaigns/{campaign_id}/status/{status}` | `client.search_ads_v2.update_status()` | Typed model |
| PATCH | `/open-api/v1/search-ads/v2/campaigns/{campaign_id}/bid` | `client.search_ads_v2.update_bid()` | Typed model |
| POST | `/open-api/v1/search-ads/v2/campaigns/{campaign_id}/products` | `client.search_ads_v2.add_products()` | Typed model |
| PATCH | `/open-api/v1/search-ads/v2/campaigns/{campaign_id}/products/{product_id}/status` | `client.search_ads_v2.update_product_status()` | Typed model |

## nearby_stores

| Method | Path | SDK call | Response |
| --- | --- | --- | --- |
| GET | `/open-api/v1/near-by-stores` | `client.nearby_stores.list()` | Typed model |
| POST | `/open-api/v1/near-by-stores/customer-not-respond` | `client.nearby_stores.customer_not_responding()` | RawResponse |

