"""Snapp Shop — the credentials both engines are built from."""

from pydantic import model_validator

from iranian_marketplaces_sdk.common.data import MarketplaceConfig
from iranian_marketplaces_sdk.common.utils import require_text
from iranian_marketplaces_sdk.marketplaces.snapp.constants import NAME

__all__ = ["SnappConfig"]


class SnappConfig(MarketplaceConfig):
    """Snapp Shop Automation API credentials.

    Snapp splits authentication across two headers: ``Authorization`` carries the bearer
    ``access_token``, and ``User-Agent`` carries the account's ``unique_code`` — an identifier, not
    a browser string. Both are required; a request with only the token is rejected.

    ``seller_id`` is not a credential but is required all the same: every vendor endpoint is
    scoped by it in the URL path, so a client without one cannot address anything.
    """

    unique_code: str
    access_token: str
    seller_id: str

    @model_validator(mode="after")
    def _check(self) -> "SnappConfig":
        require_text(self.unique_code, field="unique_code", marketplace=NAME)
        require_text(self.access_token, field="access_token", marketplace=NAME)
        require_text(self.seller_id, field="seller_id", marketplace=NAME)
        return self
