"""Basalam — headers and query building.

Pure functions over the models in ``data/``, shared by both engines so they cannot drift apart.
"""

from typing import Any

from iranian_marketplaces_sdk.common.utils import rename_keys
from iranian_marketplaces_sdk.marketplaces.basalam.constants import (
    PARCELS_QUERY_KEY_MAP,
    PRODUCTS_QUERY_KEY_MAP,
)
from iranian_marketplaces_sdk.marketplaces.basalam.data import BasalamConfig

__all__ = ["auth_headers", "parcels_params", "products_params"]


def auth_headers(config: BasalamConfig) -> dict[str, str]:
    """The session headers for an authenticated client."""
    return {"Authorization": f"Bearer {config.access_token}"}


def _params(query: Any, key_map: dict[str, str]) -> dict[str, Any] | None:
    """A query model's parameters under Basalam's own key names, or ``None`` when empty.

    List values are left as lists on purpose: ``httpx`` repeats them as separate parameters, which
    is what Basalam's FastAPI layer expects. Joining them with commas would send one item whose
    value happens to contain commas.
    """
    if query is None:
        return None
    return rename_keys(query.to_params(), key_map) or None


def products_params(query: Any) -> dict[str, Any] | None:
    """Query parameters for the vendor-products endpoint."""
    return _params(query, PRODUCTS_QUERY_KEY_MAP)


def parcels_params(query: Any) -> dict[str, Any] | None:
    """Query parameters for the vendor-parcels endpoint."""
    return _params(query, PARCELS_QUERY_KEY_MAP)
