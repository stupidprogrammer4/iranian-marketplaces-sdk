"""Basalam — the credentials both engines are built from."""

from pydantic import model_validator

from iranian_marketplaces_sdk.common.data import MarketplaceConfig
from iranian_marketplaces_sdk.common.utils import require_text
from iranian_marketplaces_sdk.marketplaces.basalam.constants import NAME

__all__ = ["BasalamConfig"]


class BasalamConfig(MarketplaceConfig):
    """Basalam Open API credentials.

    ``access_token`` goes up as a bearer token. ``vendor_id`` is not a credential but is required
    all the same: it is part of the path of every vendor endpoint, so a client without one can
    only reach the parcels list.
    """

    vendor_id: int
    access_token: str

    @model_validator(mode="after")
    def _check(self) -> "BasalamConfig":
        require_text(self.access_token, field="access_token", marketplace=NAME)
        return self
