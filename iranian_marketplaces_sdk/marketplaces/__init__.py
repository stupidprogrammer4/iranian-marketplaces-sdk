"""Every marketplace, plus a registry for picking one by name at runtime.

Each marketplace directory holds the same five things: ``constants.py`` (base URL, endpoint paths,
and the fixed values its API defines), ``data/`` (credentials and the marketplace's own request and
response models — pydantic only, split by scope), ``helpers.py`` (the pure functions that build
headers, queries and payloads), and ``sync_engine.py`` / ``async_engine.py``, which are thin shells
over both. That split is why the two engines cannot drift apart: every decision about what was
asked and what came back lives in ``helpers.py`` and ``data/`` and is shared, so only the transport
call differs.

The registry holds **classes, not instances**. One instance carries exactly one seller's
credentials, so build one per seller with :func:`get_sync_client` / :func:`get_async_client` rather
than caching a client globally.

The constructors differ by marketplace — Digikala takes tokens, Snapp takes a code, a token and a
seller id, Basalam a vendor id and a token, Tapsi a single token — so the registry takes them as
keyword arguments and passes them straight through.
"""

from typing import Any

from iranian_marketplaces_sdk.common.exceptions import ConfigurationError
from iranian_marketplaces_sdk.common.interfaces import (
    IAsyncMarketplaceClient,
    ISyncMarketplaceClient,
)
from iranian_marketplaces_sdk.marketplaces.basalam import BasalamAsync as BasalamAsync
from iranian_marketplaces_sdk.marketplaces.basalam import BasalamConfig as BasalamConfig
from iranian_marketplaces_sdk.marketplaces.basalam import BasalamSync as BasalamSync
from iranian_marketplaces_sdk.marketplaces.digikala import DigikalaAsync as DigikalaAsync
from iranian_marketplaces_sdk.marketplaces.digikala import DigikalaConfig as DigikalaConfig
from iranian_marketplaces_sdk.marketplaces.digikala import DigikalaSync as DigikalaSync
from iranian_marketplaces_sdk.marketplaces.snapp import SnappAsync as SnappAsync
from iranian_marketplaces_sdk.marketplaces.snapp import SnappConfig as SnappConfig
from iranian_marketplaces_sdk.marketplaces.snapp import SnappSync as SnappSync
from iranian_marketplaces_sdk.marketplaces.tapsi import TapsiAsync as TapsiAsync
from iranian_marketplaces_sdk.marketplaces.tapsi import TapsiConfig as TapsiConfig
from iranian_marketplaces_sdk.marketplaces.tapsi import TapsiSync as TapsiSync

SYNC_MARKETPLACES: dict[str, type[ISyncMarketplaceClient]] = {
    "basalam": BasalamSync,
    "digikala": DigikalaSync,
    "snapp": SnappSync,
    "tapsi": TapsiSync,
}

ASYNC_MARKETPLACES: dict[str, type[IAsyncMarketplaceClient]] = {
    "basalam": BasalamAsync,
    "digikala": DigikalaAsync,
    "snapp": SnappAsync,
    "tapsi": TapsiAsync,
}


def available() -> tuple[str, ...]:
    """Every marketplace name, sorted. The same names work in both engines."""
    return tuple(sorted(SYNC_MARKETPLACES))


def get_sync_client(name: str, **credentials: Any) -> ISyncMarketplaceClient:
    """Build a sync client by name, e.g. ``get_sync_client("digikala", access_token="…")``.

    The returned object is typed as the protocol, which only promises the shared surface. For the
    marketplace's own methods, import its engine class directly.
    """
    try:
        client_cls = SYNC_MARKETPLACES[name]
    except KeyError:
        raise ConfigurationError(
            f"unknown marketplace {name!r} — available: {', '.join(available())}"
        ) from None
    return client_cls(**credentials)


def get_async_client(name: str, **credentials: Any) -> IAsyncMarketplaceClient:
    """Build an async client by name, e.g. ``get_async_client("tapsi", token="…")``."""
    try:
        client_cls = ASYNC_MARKETPLACES[name]
    except KeyError:
        raise ConfigurationError(
            f"unknown marketplace {name!r} — available: {', '.join(available())}"
        ) from None
    return client_cls(**credentials)
