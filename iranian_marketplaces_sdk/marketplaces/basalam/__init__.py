"""Basalam (باسلام) — the Open API.

Vendor products, parcels, and discounts. Products are updated in batches; discounts are applied by
filter rather than by id, so a discount call reaches everything the filter matches.
"""

from iranian_marketplaces_sdk.marketplaces.basalam.async_engine import BasalamAsync as BasalamAsync
from iranian_marketplaces_sdk.marketplaces.basalam.data import BasalamConfig as BasalamConfig
from iranian_marketplaces_sdk.marketplaces.basalam.sync_engine import BasalamSync as BasalamSync
