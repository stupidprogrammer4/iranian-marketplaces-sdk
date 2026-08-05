"""The public model surface for the Digikala Seller Open API.

Split by scope so no single file has to hold the whole API, but presented as one flat namespace:
``from iranian_marketplaces_sdk.marketplaces.digikala.data import Variant`` works regardless of
which submodule defines it. Import from here, never from a submodule path — the split is an
implementation detail and may move.
"""

from iranian_marketplaces_sdk.marketplaces.digikala.data import auth as auth
from iranian_marketplaces_sdk.marketplaces.digikala.data import common as common
from iranian_marketplaces_sdk.marketplaces.digikala.data import config as config
from iranian_marketplaces_sdk.marketplaces.digikala.data import health as health
from iranian_marketplaces_sdk.marketplaces.digikala.data import inventories as inventories
from iranian_marketplaces_sdk.marketplaces.digikala.data import invoices as invoices
from iranian_marketplaces_sdk.marketplaces.digikala.data import orders as orders
from iranian_marketplaces_sdk.marketplaces.digikala.data import packages as packages
from iranian_marketplaces_sdk.marketplaces.digikala.data import pricing as pricing
from iranian_marketplaces_sdk.marketplaces.digikala.data import variants as variants
from iranian_marketplaces_sdk.marketplaces.digikala.data.auth import *
from iranian_marketplaces_sdk.marketplaces.digikala.data.common import *
from iranian_marketplaces_sdk.marketplaces.digikala.data.config import *
from iranian_marketplaces_sdk.marketplaces.digikala.data.health import *
from iranian_marketplaces_sdk.marketplaces.digikala.data.inventories import *
from iranian_marketplaces_sdk.marketplaces.digikala.data.invoices import *
from iranian_marketplaces_sdk.marketplaces.digikala.data.orders import *
from iranian_marketplaces_sdk.marketplaces.digikala.data.packages import *
from iranian_marketplaces_sdk.marketplaces.digikala.data.pricing import *
from iranian_marketplaces_sdk.marketplaces.digikala.data.variants import *

# Built with `+=` rather than a starred literal so that a static type checker can follow
# it: the supported form for an aggregate `__all__` is appending a submodule's own.
__all__: list[str] = []
__all__ += common.__all__
__all__ += config.__all__
__all__ += health.__all__
__all__ += auth.__all__
__all__ += variants.__all__
__all__ += orders.__all__
__all__ += inventories.__all__
__all__ += invoices.__all__
__all__ += packages.__all__
__all__ += pricing.__all__
