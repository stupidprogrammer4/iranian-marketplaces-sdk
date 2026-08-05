"""Snapp Shop — headers and query building.

Pure functions over the models in ``data/``, shared by both engines so they cannot drift apart.
"""

from typing import Any

from iranian_marketplaces_sdk.marketplaces.snapp.data import ProductUpdate, SnappConfig

__all__ = ["auth_headers", "product_updates_payload", "query_params"]


def auth_headers(config: SnappConfig) -> dict[str, str]:
    """The session headers for an authenticated client.

    ``User-Agent`` is not a browser string here — Snapp uses it to carry the account's
    ``unique_code``, and overriding it with a real user agent breaks authentication.
    """
    return {
        "User-Agent": config.unique_code,
        "Authorization": f"Bearer {config.access_token}",
    }


def query_params(query: Any) -> dict[str, Any] | None:
    """A query model's parameters, or ``None`` when there is nothing to send."""
    if query is None:
        return None
    return query.to_params() or None


def product_updates_payload(updates: list[ProductUpdate]) -> list[dict[str, Any]]:
    """The JSON array the products PATCH endpoint expects.

    Each entry carries only the fields that were set, so a stock-only update cannot silently clear
    a special price that is already live.
    """
    return [item.to_payload() for item in updates]
