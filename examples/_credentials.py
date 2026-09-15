"""Read credentials only when an example is explicitly run."""

import os


def required_env(name: str) -> str:
    """Stop before opening a connection if a required environment variable is missing."""
    value = os.environ.get(name, "")
    if not value.strip():
        raise SystemExit(f"Set {name} before running this example (see examples/README.md).")
    return value
