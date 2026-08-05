"""Constants shared by every marketplace and both engines.

Values that are facts about a *specific* marketplace — its base URL, its endpoint paths, its
documented enum values — live in that marketplace's own ``constants.py``. Only what genuinely
applies everywhere belongs here.
"""

DEFAULT_TIMEOUT = 30.0
"""Seconds. Long enough for a sluggish seller panel, short enough that a dead one is not a hung
worker. Marketplace list endpoints paginate, so no single call should ever run long."""

JSON_CONTENT_TYPE = "application/json"
"""Sent on every request that carries a body, and by the marketplaces that demand it on GET too."""
