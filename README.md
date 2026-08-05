# Iranian Marketplaces SDK

A unified Python SDK for the major Iranian marketplaces — **Digikala**, **Snapp Shop**, **Basalam**
and **Tapsi Shop** — with a synchronous and an asynchronous engine for each, and pydantic models
for every request and response.

```python
from iranian_marketplaces_sdk import SnappSync
from iranian_marketplaces_sdk.marketplaces.snapp.data import VendorProductsQuery

with SnappSync(unique_code="…", access_token="…", seller_id="…") as snapp:
    page = snapp.list_products(query=VendorProductsQuery(per_page=50))
    for product in page.data:
        print(product.sku, product.price, product.stock)
```

The async engine is the same code with `await`:

```python
from iranian_marketplaces_sdk import SnappAsync

async with SnappAsync(unique_code="…", access_token="…", seller_id="…") as snapp:
    page = await snapp.list_products(query=VendorProductsQuery(per_page=50))
```

## What it gives you

- **Both engines, one shape.** Every marketplace ships `<Name>Sync` and `<Name>Async` with the same
  methods, taking and returning the same models. Porting a call site is adding or removing `await`.
- **Validated models, not dicts.** Requests and responses are pydantic v2 models, so a payload key
  typo fails before the request leaves and a response arrives with real attributes and real types.
- **Forward-compatible responses.** Response models keep fields the marketplace adds later — an
  upstream addition reaches you on `model_extra` instead of breaking the call.
- **One error hierarchy.** Everything descends from `MarketplaceError`, narrowing to
  `AuthenticationError`, `NotFoundError`, `RateLimitError`, `ServerError`, `NetworkError`,
  `ConfigurationError` and `ResponseValidationError`.
- **Credentials required up front.** Each engine's constructor names exactly what that marketplace
  needs, and a missing one fails at construction rather than mid-batch.

## Requirements

- Python ≥ 3.13
- `httpx` ≥ 0.27, `pydantic` ≥ 2.7

## Installation

```bash
pip install iranian-marketplaces-sdk
```

For local development (dev and test tools live in `[dependency-groups]`):

```bash
uv sync --group dev          # or: pip install -e . && pip install ruff mypy pyright pytest
```

## Credentials

| Marketplace | Constructor | Authentication |
| --- | --- | --- |
| Digikala | `DigikalaSync(access_token, refresh_token="")` | `Authorization: Bearer <token>` |
| Snapp Shop | `SnappSync(unique_code, access_token, seller_id)` | `Authorization: Bearer <token>` + `User-Agent: <unique_code>` |
| Basalam | `BasalamSync(vendor_id, access_token)` | `Authorization: Bearer <token>` |
| Tapsi Shop | `TapsiSync(token, client_name=…, client_version=…)` | `TapsiShop.Hub.Authorization: <token>` |

Digikala bootstraps its pair from an authorization code and can roll it over in place:

```python
from iranian_marketplaces_sdk import DigikalaSync

tokens = DigikalaSync.create_token("authorization-code-from-the-panel")

with DigikalaSync(tokens.data.access_token, tokens.data.refresh_token) as digikala:
    fresh = digikala.refresh_token()  # the client keeps using the new token; store the pair
```

Each Digikala endpoint sits behind a scope (`variant`, `order`, `inventory`, `package`, `invoice`,
`promotion`). `get_scopes()` reports what the current token may actually do.

## Coverage

| Marketplace | Endpoints |
| --- | --- |
| **Digikala** | health check, auth scopes, token create/refresh; variants (list, get, update, activation, gold, seller stock, selling price); orders and order history; inventories and dead stock; packages (list, detail); invoices (list, detail, financial items); smart-discount pricing (list, create, batch edit, delete) |
| **Snapp Shop** | vendor products (list, batch update); vendor orders (list, detail) |
| **Basalam** | vendor products (list, batch update); vendor parcels; vendor discounts (create, delete) |
| **Tapsi Shop** | vendor products (list, batch update); vendor orders |

## Working with the models

Request models send **only the fields you set**, so a partial update stays partial:

```python
from iranian_marketplaces_sdk.marketplaces.digikala.data import UpdateVariantRequest

digikala.update_variant(12345, UpdateVariantRequest(seller_stock=7))
# body on the wire: {"seller_stock": 7} — the price is untouched
```

Where a marketplace's wire name is not snake_case, the model carries an alias. Python stays
readable; the bytes stay exactly what the API documented:

```python
from iranian_marketplaces_sdk.marketplaces.tapsi.data import ProductUpdate

ProductUpdate(id="sku-1", stock=4, price=1000, reference_code="ref-1").to_payload()
# {"id": "sku-1", "stock": 4, "price": 1000, "referenceCode": "ref-1"}
```

Multi-value filters are Python lists; each marketplace joins or repeats them the way it wants:

```python
from iranian_marketplaces_sdk.marketplaces.digikala.data import VariantSearch

digikala.list_variants(search=VariantSearch(ids=[11, 22], category_ids=[3, 4]))
# search[ids]=11_22 & search[category_ids]=3,4
```

Timestamps are kept as the strings the marketplaces send. Between them these APIs use four
different formats — including the Persian calendar and Digikala's `{date, timezone_type, timezone}`
envelope — and several fields are documented as one and observed as another, so parsing them here
would mean a whole page failing to load over one odd value.

## Errors

```python
from iranian_marketplaces_sdk import (
    AuthenticationError,
    MarketplaceError,
    RateLimitError,
    ResponseValidationError,
)

try:
    page = snapp.list_products()
except AuthenticationError:
    ...  # 401/403 — refresh or re-issue the token
except RateLimitError as exc:
    time.sleep(exc.retry_after or 30)
except ResponseValidationError as exc:
    log.warning("schema drift: %s", exc.errors)
    raw = exc.raw  # the decoded body is still here
except MarketplaceError:
    ...  # everything else the SDK raises
```

## Picking a marketplace at runtime

```python
from iranian_marketplaces_sdk import available, get_sync_client

available()  # ('basalam', 'digikala', 'snapp', 'tapsi')
client = get_sync_client("digikala", access_token="…")
```

The registry holds classes, not instances — one instance carries one seller's credentials, so build
one per seller rather than caching a client globally.

## Layout

Every marketplace package is laid out the same way:

```
iranian_marketplaces_sdk/
├── common/                  # shared across every marketplace
│   ├── constants.py         #   timeouts and the like
│   ├── data.py              #   the pydantic bases: Response/Request/Query schemas
│   ├── exceptions.py        #   the error hierarchy
│   ├── http.py              #   SyncTransport / AsyncTransport over httpx
│   ├── interfaces.py        #   the two engine protocols
│   └── utils.py             #   query and credential helpers
└── marketplaces/
    └── <name>/
        ├── constants.py     #   base URL, endpoint paths, fixed API values
        ├── data/            #   credentials + request/response models, split by scope
        ├── helpers.py       #   pure functions: headers, queries, payloads
        ├── sync_engine.py   #   thin shell over the transport
        └── async_engine.py  #   the same, awaited
```

The two engines share every decision through `data/` and `helpers.py`, so only the transport call
differs — which is what stops them from drifting apart.

## Development

```bash
pytest                # the suite runs fully offline against a mock transport
ruff check . && ruff format --check .
mypy && pyright
```

`main.py` holds runnable examples for every marketplace, sync and async, driven by environment
variables.

## License

MIT.
