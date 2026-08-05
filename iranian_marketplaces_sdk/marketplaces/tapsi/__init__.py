"""Tapsi Shop (تپسی‌شاپ) — the Hub vendor API.

Vendor products and orders. The only one of the four that authenticates through a custom header
rather than ``Authorization``, and the only one whose order filters travel as a POST body.
"""

from iranian_marketplaces_sdk.marketplaces.tapsi.async_engine import TapsiAsync as TapsiAsync
from iranian_marketplaces_sdk.marketplaces.tapsi.data import TapsiConfig as TapsiConfig
from iranian_marketplaces_sdk.marketplaces.tapsi.sync_engine import TapsiSync as TapsiSync
