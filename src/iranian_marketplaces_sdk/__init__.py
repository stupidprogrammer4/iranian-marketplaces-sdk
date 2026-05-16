"""Iranian Marketplaces SDK.

Unified API wrappers for major Iranian marketplaces (Digikala, Snapp,
Basalam, Tapsi). This top-level package exposes the shared base clients and
the common exception hierarchy; per-marketplace engines live in their own
sub-packages.
"""

from __future__ import annotations

from .base_async_client import BaseAsyncClient
from .base_client import BaseClient
from .exceptions import (
    APIError,
    AuthenticationError,
    ConfigurationError,
    MarketplaceError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    ServerError,
)

__version__ = "0.1.0"

__all__ = [
    "BaseClient",
    "BaseAsyncClient",
    "MarketplaceError",
    "ConfigurationError",
    "APIError",
    "AuthenticationError",
    "NotFoundError",
    "RateLimitError",
    "ServerError",
    "NetworkError",
]
