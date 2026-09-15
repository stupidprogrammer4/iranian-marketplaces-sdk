"""Digikala — the auth/token endpoints.

The token pair is obtained once from an ``authorization_code`` and refreshed from itself
afterwards. Both calls are unauthenticated: they are what *produces* the credential, so the
bootstrapping call cannot require one.
"""

from pydantic import Field, JsonValue

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
    ``invoice``, ...); ``access`` is the level described by this scope listing, not proof of
    authorization for the current seller token.
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
    meta_data: dict[str, JsonValue] | list[JsonValue]


class ScopesResponse(ResponseSchema):
    """Full response body returned by ``GET /auth/scopes``."""

    status: str
    data: ScopesData


class TokenRequest(RequestSchema):
    """Request body for ``POST /auth/token``."""

    authorization_code: str = Field(repr=False)


class RefreshTokenRequest(RequestSchema):
    """Request body for ``POST /auth/refresh-token``.

    Both tokens go up together: Digikala identifies the session from the expired access token and
    authorises the exchange with the refresh token.
    """

    access_token: str = Field(repr=False)
    refresh_token: str = Field(repr=False)


class TokenData(ResponseSchema):
    """The ``data`` payload of a token-generation response."""

    access_token: str = Field(repr=False)
    refresh_token: str = Field(repr=False)
    access_token_expires_at: DigikalaDateTime
    refresh_token_expires_at: DigikalaDateTime


class TokenResponse(ResponseSchema):
    """Full response body returned by ``POST /auth/token`` and ``/auth/refresh-token``."""

    status: str
    data: TokenData
