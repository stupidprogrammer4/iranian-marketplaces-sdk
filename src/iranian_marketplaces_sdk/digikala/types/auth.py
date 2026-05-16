"""TypedDicts for the Digikala auth/token endpoints."""

from typing import TypedDict

from .common import DigikalaDateTime, Pager, SortData

__all__ = [
    "Scope",
    "ScopesData",
    "ScopesResponse",
    "TokenRequest",
    "RefreshTokenRequest",
    "TokenData",
    "TokenResponse",
]


class Scope(TypedDict):
    """A single permission scope grantable to an access token."""

    key: str
    title: str
    description: str
    access: str


class ScopesData(TypedDict):
    """The ``data`` payload of an auth-scopes response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[Scope]
    meta_data: dict[str, object]


class ScopesResponse(TypedDict):
    """Full response body returned by ``GET /auth/scopes``."""

    status: str
    data: ScopesData


class TokenRequest(TypedDict):
    """Request body for ``POST /auth/token``."""

    authorization_code: str


class RefreshTokenRequest(TypedDict):
    """Request body for ``POST /auth/refresh-token``."""

    access_token: str
    refresh_token: str


class TokenData(TypedDict):
    """The ``data`` payload of a token-generation response."""

    access_token: str
    refresh_token: str
    access_token_expires_at: DigikalaDateTime
    refresh_token_expires_at: DigikalaDateTime


class TokenResponse(TypedDict):
    """Full response body returned by ``POST /auth/token``."""

    status: str
    data: TokenData
