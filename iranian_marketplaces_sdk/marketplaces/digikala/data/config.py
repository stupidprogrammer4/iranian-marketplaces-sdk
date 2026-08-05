"""Digikala — the credentials both engines are built from."""

from pydantic import model_validator

from iranian_marketplaces_sdk.common.data import MarketplaceConfig
from iranian_marketplaces_sdk.common.utils import require_text
from iranian_marketplaces_sdk.marketplaces.digikala.constants import NAME

__all__ = ["DigikalaConfig"]


class DigikalaConfig(MarketplaceConfig):
    """Digikala Seller Open API credentials.

    Both tokens come from ``POST /auth/token``, which trades a one-time ``authorization_code`` for
    the pair. ``access_token`` authenticates every call; ``refresh_token`` is only used by
    ``refresh_token()``, and is kept on the config so that the refresh call needs nothing extra.

    ``refresh_token`` is optional: a client built for a single short job does not need one, and
    demanding it would block the common read-only case. Calling ``refresh_token()`` without one
    raises rather than sending an empty string Digikala would reject anyway.
    """

    access_token: str
    refresh_token: str = ""

    @model_validator(mode="after")
    def _check(self) -> "DigikalaConfig":
        require_text(self.access_token, field="access_token", marketplace=NAME)
        return self
