"""Per-marketplace engine tests: what goes on the wire, and what comes back as a model.

Every test runs against a :class:`~tests.conftest.Recorder` rather than a live marketplace, so it
asserts on two things the SDK is actually responsible for — the exact request it built, and the
model it made of the response.
"""

import contextlib
import json
from typing import Any

import pytest

from iranian_marketplaces_sdk import (
    BasalamAsync,
    BasalamSync,
    ConfigurationError,
    DigikalaAsync,
    DigikalaSync,
    ResponseValidationError,
    ServerError,
    SnappAsync,
    SnappSync,
    TapsiAsync,
    TapsiSync,
    available,
    get_sync_client,
)
from iranian_marketplaces_sdk.marketplaces.basalam.data import (
    BatchProductUpdateRequest,
    CreateVendorDiscountRequest,
    ProductBatchUpdateItem,
    ProductFilterSchema,
    RangeInput,
    VendorProductsQuery,
)
from iranian_marketplaces_sdk.marketplaces.digikala.data import (
    CreateSmartDiscountVariantsRequest as SmartDiscountRequest,
)
from iranian_marketplaces_sdk.marketplaces.digikala.data import (
    SmartDiscountVariantInput,
    UpdateVariantRequest,
    VariantSearch,
)
from iranian_marketplaces_sdk.marketplaces.snapp.data import ProductUpdate as SnappProductUpdate
from iranian_marketplaces_sdk.marketplaces.snapp.data import VendorOrdersQuery
from iranian_marketplaces_sdk.marketplaces.tapsi.data import OrdersQuery
from iranian_marketplaces_sdk.marketplaces.tapsi.data import ProductUpdate as TapsiProductUpdate
from tests.conftest import Recorder, async_client, sync_client

# --- fixtures for the response bodies ---------------------------------------------------------

DIGIKALA_HEALTH: dict[str, Any] = {
    "status": "ok",
    "data": {
        "name": "seller-open-api",
        "mode": "production",
        "time": "2026-01-01 00:00:00",
        "routes": ["/variants"],
        "rate_limit": {
            "max": 100,
            "current": 3,
            "resetTime": {
                "date": "2026-01-01 00:01:00.000000",
                "timezone_type": 3,
                "timezone": "Asia/Tehran",
            },
        },
    },
}

SNAPP_ORDER: dict[str, Any] = {
    "order_number": 12345,
    "created_at": "2026-01-01 10:00:00",
    "delivery_type": "express",
    "order_status": "confirmed",
    "item_origin": "vendor",
    "point_of_sales_at": "2026-01-01 10:05:00",
    "pickup_time": {"start": "2026-01-01 11:00:00", "end": "2026-01-01 12:00:00"},
    "customer": {
        "first_name": "علی",
        "last_name": "رضایی",
        "phone": "09120000000",
        "national_id": "0000000000",
        "address": [],
    },
    "items": [
        {
            "sku": "SKU-1",
            "vendor_product_info_id": "vpi-1",
            "item_status": "confirmed",
            "quantity": 2,
            "canceled_quantity": 0,
            "original_price": 200_000,
            "discount_amount": 20_000,
            "final_price": 180_000,
        }
    ],
}

TAPSI_PRODUCTS: dict[str, Any] = {
    "success": True,
    "messages": [{"message": "ok", "code": "0", "type": 1}],
    "data": {
        "page": 1,
        "pageSize": 10,
        "totalCount": 1,
        "items": [
            {
                "id": "p-1",
                "hsin": "H-1",
                "sku": "SKU-1",
                "originalPrice": 250_000,
                "finalPrice": 200_000,
                "minimalPerOrder": 1,
                "maximalPerOrder": 5,
                "onHandQuantity": 12,
            }
        ],
    },
}

BASALAM_PRODUCTS: dict[str, Any] = {
    "data": [
        {
            "id": 1,
            "title": "کالا",
            "price": 100_000,
            "photo": {"url": "https://example.test/p.jpg"},
            "status": {"id": 2976},
            "inventory": 5,
            "primary_price": 120_000,
            "is_product_for_revision": False,
            "preparation_day": 2,
            "published": True,
            "shipping_data": None,
            "net_weight": 500,
            "packaged_weight": 700,
            "net_weight_decimal": 0.5,
            "variant": None,
        }
    ],
    "result_count": 1,
    "total_count": 1,
    "page": 1,
    "per_page": 10,
}


# --- registry ---------------------------------------------------------------------------------


def test_registry_lists_every_marketplace() -> None:
    assert available() == ("basalam", "digikala", "snapp", "tapsi")


def test_registry_builds_a_client() -> None:
    client = get_sync_client("tapsi", token="t")
    assert client.name == "tapsi"
    client.close()


def test_registry_rejects_an_unknown_name() -> None:
    with pytest.raises(ConfigurationError, match="unknown marketplace"):
        get_sync_client("amazon", token="t")


# --- digikala ---------------------------------------------------------------------------------


def test_digikala_health_check_parses(recorder: type[Recorder]) -> None:
    rec = recorder(DIGIKALA_HEALTH)
    with DigikalaSync("token", client=sync_client(rec)) as client:
        health = client.health_check()

    assert health.data.mode == "production"
    assert health.data.rate_limit.reset_time.timezone == "Asia/Tehran"
    assert rec.request.headers["Authorization"] == "Bearer token"


def test_digikala_list_variants_builds_search_params(recorder: type[Recorder]) -> None:
    """``ids`` is underscore-joined, every other list comma-joined, all under ``search[...]``."""
    rec = recorder({"status": "ok", "data": {}}, status_code=500)
    client = DigikalaSync("token", client=sync_client(rec))
    with pytest.raises(ServerError):
        client.list_variants(
            page=2,
            size=50,
            sort="id",
            order="desc",
            search=VariantSearch(ids=[11, 22], category_ids=[3, 4], active=True),
        )

    assert rec.params == {
        "page": "2",
        "size": "50",
        "sort": "id",
        "order": "desc",
        "search[ids]": "11_22",
        "search[active]": "true",
        "search[category_ids]": "3,4",
    }


def test_digikala_update_variant_sends_only_set_fields(recorder: type[Recorder]) -> None:
    rec = recorder({}, status_code=500)
    client = DigikalaSync("token", client=sync_client(rec))
    with pytest.raises(ServerError):
        client.update_variant(99, UpdateVariantRequest(seller_stock=7))

    assert rec.body == {"seller_stock": 7}
    assert rec.request.url.path.endswith("/variants/99")
    assert rec.request.method == "PUT"


def test_digikala_smart_discount_uses_camel_case_on_the_wire(recorder: type[Recorder]) -> None:
    rec = recorder({}, status_code=500)
    client = DigikalaSync("token", client=sync_client(rec))
    with pytest.raises(ServerError):
        client.create_smart_discount_variants(
            SmartDiscountRequest(
                data=[
                    SmartDiscountVariantInput(
                        variant_id=5,
                        promotion_price=90_000,
                        limit=10,
                        order_limit=2,
                        started_at="2026-01-01",
                        end_at="2026-01-07",
                    )
                ]
            )
        )

    assert rec.body == {
        "data": [
            {
                "variantId": 5,
                "promotionPrice": 90_000,
                "limit": 10,
                "orderLimit": 2,
                "startedAt": "2026-01-01",
                "endAt": "2026-01-07",
            }
        ]
    }


def test_digikala_refresh_without_a_refresh_token_raises() -> None:
    client = DigikalaSync("token")
    with pytest.raises(ConfigurationError, match="refresh_token"):
        client.refresh_token()
    client.close()


def test_digikala_refresh_rotates_the_session_header(recorder: type[Recorder]) -> None:
    rec = recorder(
        {
            "status": "ok",
            "data": {
                "access_token": "new-access",
                "refresh_token": "new-refresh",
                "access_token_expires_at": {
                    "date": "2026-02-01 00:00:00.000000",
                    "timezone_type": 3,
                    "timezone": "Asia/Tehran",
                },
                "refresh_token_expires_at": {
                    "date": "2026-03-01 00:00:00.000000",
                    "timezone_type": 3,
                    "timezone": "Asia/Tehran",
                },
            },
        }
    )
    with DigikalaSync("old-access", "old-refresh", client=sync_client(rec)) as client:
        response = client.refresh_token()

        assert response.data.access_token == "new-access"
        assert client.config.access_token == "new-access"
        assert client.config.refresh_token == "new-refresh"

        # The refresh itself went up with the *old* pair...
        refresh_request = rec.requests[0]
        assert json.loads(refresh_request.content) == {
            "access_token": "old-access",
            "refresh_token": "old-refresh",
        }
        assert refresh_request.headers["Authorization"] == "Bearer old-access"

        # ...and the very next call authenticates with the new token, with nothing done at the
        # call site to make that happen.
        # The recorder answers with a token body whatever is asked, so the parse fails; only
        # the header on the outgoing request matters here.
        with contextlib.suppress(ResponseValidationError):
            client.get_scopes()
        assert rec.requests[1].headers["Authorization"] == "Bearer new-access"


# --- snapp ------------------------------------------------------------------------------------


def test_snapp_sends_both_auth_headers(recorder: type[Recorder]) -> None:
    """The unique code rides on ``User-Agent`` — overwriting it breaks authentication."""
    rec = recorder({"status": True, "data": SNAPP_ORDER})
    with SnappSync("uniq-1", "tok-1", "seller-9", client=sync_client(rec)) as client:
        order = client.get_order(12345)

    assert rec.request.headers["User-Agent"] == "uniq-1"
    assert rec.request.headers["Authorization"] == "Bearer tok-1"
    assert rec.request.url.path == "/automation/v1/vendors/seller-9/orders/12345"
    assert order.data.customer.first_name == "علی"
    assert order.data.items[0].final_price == 180_000


def test_snapp_order_cursor_paging(recorder: type[Recorder]) -> None:
    rec = recorder(
        {
            "status": True,
            "data": [SNAPP_ORDER],
            "meta": {
                "pagination": {
                    "path": "/vendors/seller-9/orders",
                    "per_page": 1,
                    "count": 1,
                    "links": {"next": "https://example.test?cursor=abc"},
                    "has_more": True,
                    "next_cursor": "abc",
                }
            },
        }
    )
    with SnappSync("uniq-1", "tok-1", "seller-9", client=sync_client(rec)) as client:
        page = client.list_orders(query=VendorOrdersQuery(per_page=1))

    assert page.meta.pagination.has_more is True
    assert page.meta.pagination.next_cursor == "abc"
    assert rec.params == {"per_page": "1"}


def test_snapp_product_update_is_a_bare_array(recorder: type[Recorder]) -> None:
    rec = recorder([{"id": "1", "sku": "SKU-1", "status": True, "messages": []}])
    with SnappSync("uniq-1", "tok-1", "seller-9", client=sync_client(rec)) as client:
        results = client.update_products(
            [SnappProductUpdate(sku="SKU-1", id="1", price=1000, stock=5)]
        )

    assert rec.request.method == "PATCH"
    assert rec.body == [{"sku": "SKU-1", "id": "1", "price": 1000, "stock": 5}]
    assert results[0].status is True


# --- basalam ----------------------------------------------------------------------------------


def test_basalam_maps_bracket_query_keys(recorder: type[Recorder]) -> None:
    rec = recorder(BASALAM_PRODUCTS)
    with BasalamSync(42, "tok", client=sync_client(rec)) as client:
        page = client.list_vendor_products(
            query=VendorProductsQuery(stock_gte=1, price_lte=500_000, per_page=10)
        )

    assert rec.request.url.path == "/v1/vendors/42/products"
    assert rec.params == {"stock[gte]": "1", "price[lte]": "500000", "per_page": "10"}
    assert page.result_count == 1
    assert page.data is not None
    assert page.data[0].title == "کالا"


def test_basalam_repeats_array_query_params(recorder: type[Recorder]) -> None:
    """FastAPI arrays are repeated parameters, not a comma-joined string."""
    rec = recorder(BASALAM_PRODUCTS)
    with BasalamSync(42, "tok", client=sync_client(rec)) as client:
        client.list_vendor_products(query=VendorProductsQuery(ids=[1, 2, 3]))

    assert rec.request.url.params.get_list("ids") == ["1", "2", "3"]


def test_basalam_batch_update_sends_continue_on_error(recorder: type[Recorder]) -> None:
    rec = recorder(
        [{"id": 1, "is_product_for_revision": False, "has_error": False, "error_message": None}]
    )
    with BasalamSync(42, "tok", client=sync_client(rec)) as client:
        results = client.batch_update_vendor_products(
            BatchProductUpdateRequest(
                data=[
                    ProductBatchUpdateItem(
                        id=1,
                        illegal_for_iran=False,
                        illegal_for_same_city=False,
                        stock=9,
                    )
                ]
            ),
            continue_on_error=True,
        )

    assert rec.params == {"continue_on_error": "true"}
    assert rec.body == {
        "data": [{"id": 1, "illegal_for_iran": False, "illegal_for_same_city": False, "stock": 9}]
    }
    assert results[0].has_error is False


def test_basalam_discount_keeps_an_explicit_null_filter(recorder: type[Recorder]) -> None:
    """``product_filter`` is required *and* nullable — ``None`` must reach the wire as ``null``."""
    rec = recorder({"accepted": True})
    with BasalamSync(42, "tok", client=sync_client(rec)) as client:
        client.create_vendor_discount(
            CreateVendorDiscountRequest(product_filter=None, discount_percent=10, active_days=7)
        )

    assert rec.body == {"product_filter": None, "discount_percent": 10, "active_days": 7}


def test_basalam_discount_nests_a_range_filter(recorder: type[Recorder]) -> None:
    rec = recorder({"accepted": True})
    with BasalamSync(42, "tok", client=sync_client(rec)) as client:
        client.create_vendor_discount(
            CreateVendorDiscountRequest(
                product_filter=ProductFilterSchema(
                    category_id=[7], stock=RangeInput(start=1, end=None)
                ),
                discount_percent=15,
                active_days=3,
            )
        )

    assert rec.body["product_filter"] == {"category_id": [7], "stock": {"start": 1, "end": None}}


# --- tapsi ------------------------------------------------------------------------------------


def test_tapsi_uses_its_own_auth_header(recorder: type[Recorder]) -> None:
    rec = recorder(TAPSI_PRODUCTS)
    with TapsiSync("tok-t", client=sync_client(rec)) as client:
        page = client.get_products(1, 10)

    assert rec.request.headers["TapsiShop.Hub.Authorization"] == "tok-t"
    assert "Authorization" not in rec.request.headers
    assert rec.request.url.path == "/Web/Hub/vendors/v1/products/1/10"
    assert page.data.items[0].on_hand_quantity == 12
    assert page.data.total_count == 1


def test_tapsi_orders_post_a_camel_case_body(recorder: type[Recorder]) -> None:
    rec = recorder(
        {
            "success": True,
            "messages": [],
            "data": {"pageNumber": 0, "pageSize": 20, "totalItems": 0, "items": []},
        }
    )
    with TapsiSync("tok-t", client=sync_client(rec)) as client:
        page = client.list_orders(query=OrdersQuery(page_number=0, order_status_id=[4, 9]))

    assert rec.request.method == "POST"
    assert rec.body == {"pageNumber": 0, "orderStatusId": [4, 9]}
    assert page.data.total_items == 0


def test_tapsi_product_update_wraps_the_list(recorder: type[Recorder]) -> None:
    rec = recorder(
        {
            "success": True,
            "messages": [],
            "data": {
                "status": True,
                "data": [
                    {
                        "id": "p-1",
                        "sku": "SKU-1",
                        "status": True,
                        "messages": [],
                        "currentOriginalPrice": 1000,
                        "currentFinalPrice": 900,
                        "currentOnHandQuantity": 4,
                        "referenceCode": "ref-1",
                    }
                ],
            },
        }
    )
    with TapsiSync("tok-t", client=sync_client(rec)) as client:
        result = client.update_products(
            [TapsiProductUpdate(id="p-1", stock=4, price=1000, reference_code="ref-1")]
        )

    assert rec.body == {
        "products": [{"id": "p-1", "stock": 4, "price": 1000, "referenceCode": "ref-1"}]
    }
    assert result.data.data[0].current_final_price == 900
    assert result.data.data[0].reference_code == "ref-1"


# --- the async engines answer the same ---------------------------------------------------------
#
# Four separate tests rather than one parametrised over callables: the point of these is that the
# async engine returns the *same typed model* as its sync twin, and a table of lambdas would erase
# exactly the types being checked.


async def test_digikala_async_matches_its_sync_twin(recorder: type[Recorder]) -> None:
    rec = recorder(DIGIKALA_HEALTH)
    async with DigikalaAsync("token", client=async_client(rec)) as client:
        health = await client.health_check()

    assert health.data.mode == "production"
    assert health.data.rate_limit.reset_time.timezone == "Asia/Tehran"
    assert rec.request.headers["Authorization"] == "Bearer token"


async def test_snapp_async_matches_its_sync_twin(recorder: type[Recorder]) -> None:
    rec = recorder({"status": True, "data": SNAPP_ORDER})
    async with SnappAsync("uniq-1", "tok-1", "seller-9", client=async_client(rec)) as client:
        order = await client.get_order(12345)

    assert order.data.order_number == 12345
    assert order.data.items[0].final_price == 180_000
    assert rec.request.headers["User-Agent"] == "uniq-1"


async def test_basalam_async_matches_its_sync_twin(recorder: type[Recorder]) -> None:
    rec = recorder(BASALAM_PRODUCTS)
    async with BasalamAsync(42, "tok", client=async_client(rec)) as client:
        products = await client.list_vendor_products(query=VendorProductsQuery(stock_gte=1))

    assert products.result_count == 1
    assert rec.params == {"stock[gte]": "1"}


async def test_tapsi_async_matches_its_sync_twin(recorder: type[Recorder]) -> None:
    rec = recorder(TAPSI_PRODUCTS)
    async with TapsiAsync("tok-t", client=async_client(rec)) as client:
        products = await client.get_products(1, 10)

    assert products.data.total_count == 1
    assert products.data.items[0].on_hand_quantity == 12
    assert rec.request.headers["TapsiShop.Hub.Authorization"] == "tok-t"
