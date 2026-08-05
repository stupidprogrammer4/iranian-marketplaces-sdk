"""The public model surface for the Tapsi Shop Hub vendor API.

Split by scope, presented flat: import from here, not from a submodule path.
"""

from iranian_marketplaces_sdk.marketplaces.tapsi.data import common as common
from iranian_marketplaces_sdk.marketplaces.tapsi.data import config as config
from iranian_marketplaces_sdk.marketplaces.tapsi.data import orders as orders
from iranian_marketplaces_sdk.marketplaces.tapsi.data import products as products
from iranian_marketplaces_sdk.marketplaces.tapsi.data.common import *
from iranian_marketplaces_sdk.marketplaces.tapsi.data.config import *
from iranian_marketplaces_sdk.marketplaces.tapsi.data.orders import *
from iranian_marketplaces_sdk.marketplaces.tapsi.data.products import *

# Built with `+=` rather than a starred literal so that a static type checker can follow
# it: the supported form for an aggregate `__all__` is appending a submodule's own.
__all__: list[str] = []
__all__ += common.__all__
__all__ += config.__all__
__all__ += products.__all__
__all__ += orders.__all__
