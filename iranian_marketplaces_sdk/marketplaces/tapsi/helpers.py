"""Tapsi Shop — headers and payload building.

Pure functions over the models in ``data/``, shared by both engines so they cannot drift apart.
"""

from typing import Any

from iranian_marketplaces_sdk.marketplaces.tapsi.data import (
    OrdersQuery,
    ProductUpdate,
    ProductUpdatePayload,
    TapsiConfig,
)

__all__ = ["auth_headers", "orders_body", "product_updates_body"]


def auth_headers(config: TapsiConfig) -> dict[str, str]:
    """The session headers for an authenticated client.

    The token goes in Tapsi's own header, unprefixed — there is no ``Bearer`` here. ``accept:
    text/plain`` is what the documented client sends, and the gateway answers JSON regardless.
    """
    return {
        "TapsiShop.Hub.Authorization": config.token,
        "client-name": config.client_name,
        "client-version": config.client_version,
        "accept": "text/plain",
    }


def orders_body(query: OrdersQuery | None) -> dict[str, Any]:
    """The JSON body for the orders endpoint — ``{}`` when no filters were given.

    An empty object is a valid request: it means the first page with the server's defaults.
    """
    if query is None:
        return {}
    return query.to_payload()


def product_updates_body(updates: list[ProductUpdate]) -> dict[str, Any]:
    """The JSON body for the products PUT endpoint, under its ``products`` wrapper."""
    return ProductUpdatePayload(products=updates).to_payload()
