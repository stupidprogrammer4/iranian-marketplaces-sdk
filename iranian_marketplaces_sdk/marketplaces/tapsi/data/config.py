"""Tapsi Shop — the credentials both engines are built from."""

from pydantic import model_validator

from iranian_marketplaces_sdk.common.data import MarketplaceConfig
from iranian_marketplaces_sdk.common.utils import require_text
from iranian_marketplaces_sdk.marketplaces.tapsi.constants import (
    DEFAULT_CLIENT_NAME,
    DEFAULT_CLIENT_VERSION,
    NAME,
)

__all__ = ["TapsiConfig"]


class TapsiConfig(MarketplaceConfig):
    """Tapsi Shop Hub vendor API credentials.

    The token goes in Tapsi's own ``TapsiShop.Hub.Authorization`` header — not ``Authorization``,
    and with no ``Bearer`` prefix.

    ``client_name`` and ``client_version`` identify the calling application. They are not secret
    and default to the values in Tapsi's own documentation; set them to your own to make your
    traffic identifiable in Tapsi's logs.
    """

    token: str
    client_name: str = DEFAULT_CLIENT_NAME
    client_version: str = DEFAULT_CLIENT_VERSION

    @model_validator(mode="after")
    def _check(self) -> "TapsiConfig":
        require_text(self.token, field="token", marketplace=NAME)
        return self
