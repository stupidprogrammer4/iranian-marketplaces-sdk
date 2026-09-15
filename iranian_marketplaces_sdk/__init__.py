"""A unified SDK for the major Iranian marketplaces, in a sync and an async flavour.

Four marketplaces — Digikala, Snapp Shop, Basalam and Tapsi Shop — behind one shape. Every one
ships ``<Name>Sync`` and ``<Name>Async`` with the same methods, taking and returning the same
pydantic models; porting a call site from one engine to the other is adding or removing ``await``.

    from iranian_marketplaces_sdk import SnappSync
    from iranian_marketplaces_sdk.marketplaces.snapp.data import VendorProductsQuery

    with SnappSync(unique_code="…", access_token="…", seller_id="…") as snapp:
        page = snapp.list_products(query=VendorProductsQuery(per_page=50))
        for product in page.data:
            print(product.sku, product.price, product.stock)

What each marketplace exposes is its own — a Digikala invoice has no counterpart at Tapsi — so the
engine classes are where the real surface lives. What *is* uniform: credentials are required
explicitly at construction, responses are validated pydantic models, errors all descend from
:class:`MarketplaceError`, and both engines are context managers that close their HTTP session.

Response models keep fields the marketplace adds later, so an upstream addition never breaks a
caller. A response that is missing something required raises
:class:`ResponseValidationError`, which carries the undecoded body on ``.raw``.

Each marketplace package is laid out the same way: ``constants.py`` (base URL, endpoint paths, and
the fixed values its API defines), ``data/`` (credentials and its own request/response models,
split by scope), ``helpers.py`` (the pure functions that build headers, queries and payloads), and
``sync_engine.py`` / ``async_engine.py``.

The names below are the shared surface: the engines, their credential records, the errors, and the
model bases. Request and response models are **not** re-exported here — two marketplaces both call
a model ``VendorProductsQuery`` and they are not the same type. Import those from
``iranian_marketplaces_sdk.marketplaces.<name>.data``, where the name says whose it is.
"""

from iranian_marketplaces_sdk.common.constants import DEFAULT_TIMEOUT as DEFAULT_TIMEOUT
from iranian_marketplaces_sdk.common.data import MarketplaceConfig as MarketplaceConfig
from iranian_marketplaces_sdk.common.data import QuerySchema as QuerySchema
from iranian_marketplaces_sdk.common.data import RequestSchema as RequestSchema
from iranian_marketplaces_sdk.common.data import ResponseSchema as ResponseSchema
from iranian_marketplaces_sdk.common.exceptions import APIError as APIError
from iranian_marketplaces_sdk.common.exceptions import AuthenticationError as AuthenticationError
from iranian_marketplaces_sdk.common.exceptions import ConfigurationError as ConfigurationError
from iranian_marketplaces_sdk.common.exceptions import MarketplaceError as MarketplaceError
from iranian_marketplaces_sdk.common.exceptions import NetworkError as NetworkError
from iranian_marketplaces_sdk.common.exceptions import NotFoundError as NotFoundError
from iranian_marketplaces_sdk.common.exceptions import RateLimitError as RateLimitError
from iranian_marketplaces_sdk.common.exceptions import (
    ResponseValidationError as ResponseValidationError,
)
from iranian_marketplaces_sdk.common.exceptions import ServerError as ServerError
from iranian_marketplaces_sdk.common.interfaces import (
    IAsyncMarketplaceClient as IAsyncMarketplaceClient,
)
from iranian_marketplaces_sdk.common.interfaces import (
    ISyncMarketplaceClient as ISyncMarketplaceClient,
)
from iranian_marketplaces_sdk.marketplaces import ASYNC_MARKETPLACES as ASYNC_MARKETPLACES
from iranian_marketplaces_sdk.marketplaces import SYNC_MARKETPLACES as SYNC_MARKETPLACES
from iranian_marketplaces_sdk.marketplaces import BasalamAsync as BasalamAsync
from iranian_marketplaces_sdk.marketplaces import BasalamConfig as BasalamConfig
from iranian_marketplaces_sdk.marketplaces import BasalamSync as BasalamSync
from iranian_marketplaces_sdk.marketplaces import DigikalaAsync as DigikalaAsync
from iranian_marketplaces_sdk.marketplaces import DigikalaConfig as DigikalaConfig
from iranian_marketplaces_sdk.marketplaces import DigikalaSync as DigikalaSync
from iranian_marketplaces_sdk.marketplaces import SnappAsync as SnappAsync
from iranian_marketplaces_sdk.marketplaces import SnappConfig as SnappConfig
from iranian_marketplaces_sdk.marketplaces import SnappSync as SnappSync
from iranian_marketplaces_sdk.marketplaces import TapsiAsync as TapsiAsync
from iranian_marketplaces_sdk.marketplaces import TapsiConfig as TapsiConfig
from iranian_marketplaces_sdk.marketplaces import TapsiSync as TapsiSync
from iranian_marketplaces_sdk.marketplaces import available as available
from iranian_marketplaces_sdk.marketplaces import get_async_client as get_async_client
from iranian_marketplaces_sdk.marketplaces import get_sync_client as get_sync_client

__version__ = "0.3.0"
