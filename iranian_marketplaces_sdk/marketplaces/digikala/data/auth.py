"""Digikala — the auth/token endpoints.

The token pair is obtained once from an ``authorization_code`` and refreshed from itself
afterwards. Both calls are unauthenticated: they are what *produces* the credential, so the
bootstrapping call cannot require one.
"""

from typing import Any

from iranian_marketplaces_sdk.common.data import RequestSchema, ResponseSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.common import (
    DigikalaDateTime,
    Pager,
    SortData,
)

__all__ = [
    "RefreshTokenRequest",
    "Scope",
    "ScopesData",
    "ScopesResponse",
    "TokenData",
    "TokenRequest",
    "TokenResponse",
]


class Scope(ResponseSchema):
    """A single permission scope grantable to an access token.

    ``key`` is what the endpoint documentation calls the scope (``variant``, ``order``,
    ``invoice``, ...); ``access`` is what this token may actually do with it.
    """

    key: str
    title: str
    description: str
    access: str


class ScopesData(ResponseSchema):
    """The ``data`` payload of an auth-scopes response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[Scope]
    meta_data: dict[str, Any]


class ScopesResponse(ResponseSchema):
    """Full response body returned by ``GET /auth/scopes``."""

    status: str
    data: ScopesData


class TokenRequest(RequestSchema):
    """Request body for ``POST /auth/token``."""

    authorization_code: str


class RefreshTokenRequest(RequestSchema):
    """Request body for ``POST /auth/refresh-token``.

    Both tokens go up together: Digikala identifies the session from the expired access token and
    authorises the exchange with the refresh token.
    """

    access_token: str
    refresh_token: str


class TokenData(ResponseSchema):
    """The ``data`` payload of a token-generation response."""

    access_token: str
    refresh_token: str
    access_token_expires_at: DigikalaDateTime
    refresh_token_expires_at: DigikalaDateTime


class TokenResponse(ResponseSchema):
    """Full response body returned by ``POST /auth/token`` and ``/auth/refresh-token``."""

    status: str
    data: TokenData
