"""The public model surface for the Basalam Open API.

Split by scope, presented flat: import from here, not from a submodule path.
"""

from iranian_marketplaces_sdk.marketplaces.basalam.data import common as common
from iranian_marketplaces_sdk.marketplaces.basalam.data import config as config
from iranian_marketplaces_sdk.marketplaces.basalam.data import discounts as discounts
from iranian_marketplaces_sdk.marketplaces.basalam.data import parcels as parcels
from iranian_marketplaces_sdk.marketplaces.basalam.data import products as products
from iranian_marketplaces_sdk.marketplaces.basalam.data.common import *
from iranian_marketplaces_sdk.marketplaces.basalam.data.config import *
from iranian_marketplaces_sdk.marketplaces.basalam.data.discounts import *
from iranian_marketplaces_sdk.marketplaces.basalam.data.parcels import *
from iranian_marketplaces_sdk.marketplaces.basalam.data.products import *

# Built with `+=` rather than a starred literal so that a static type checker can follow
# it: the supported form for an aggregate `__all__` is appending a submodule's own.
__all__: list[str] = []
__all__ += common.__all__
__all__ += config.__all__
__all__ += products.__all__
__all__ += discounts.__all__
__all__ += parcels.__all__
