"""Snapp Shop (اسنپ‌شاپ) — the Automation API.

Vendor products and orders. Products are offset-paginated, orders cursor-paginated, and both
endpoints are scoped by the ``seller_id`` the client is built with.
"""

from iranian_marketplaces_sdk.marketplaces.snapp.async_engine import SnappAsync as SnappAsync
from iranian_marketplaces_sdk.marketplaces.snapp.data import SnappConfig as SnappConfig
from iranian_marketplaces_sdk.marketplaces.snapp.sync_engine import SnappSync as SnappSync
