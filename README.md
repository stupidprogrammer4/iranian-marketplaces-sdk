# Iranian Marketplaces SDK

A unified, robust, and fully-typed Python SDK for integrating with major Iranian marketplaces, including Digikala, Snapp, Basalam, and Tapsi.

This SDK provides both Synchronous and Asynchronous clients, utilizing `httpx` for high-performance HTTP requests, and strict `TypedDict` structures for predictable API responses.

## Features

- **Sync & Async Support:** Choose between blocking and non-blocking engines based on your architecture.
- **Fully Typed:** Built-in `TypedDict` definitions for all request payloads and responses.
- **Unified Architecture:** Consistent developer experience across all supported marketplaces.
- **Custom Exceptions:** Clean error handling with marketplace-specific exception classes.
- **Modern Python:** Built for Python 3.13 and above.

## Requirements

- Python >= 3.13
- `httpx` >= 0.24.0

## Installation

For local development and testing, you can install the package in editable mode. Run the following command in the root directory of the project (where `pyproject.toml` is located):

```bash
pip install -e .
```

(Once published to a registry, you will be able to install it via pip install iranian-marketplaces-sdk)

# Quick Start

## Synchronous Usage

```python
from iranian_marketplaces_sdk.digikala.engine import DigikalaClient

# Initialize the client with required credentials
client = DigikalaClient(access_token="your_access_token", refresh_token="your_refresh_token")

# Make a synchronous request
try:
    orders = client.get_orders()
    print(orders)
except Exception as e:
    print(f"An error occurred: {e}")
```

## Asynchronous Usage
```python
import asyncio
from iranian_marketplaces_sdk.digikala.async_engine import AsyncDigikalaClient

async def main():
    # Initialize the async client with required credentials
    client = AsyncDigikalaClient(access_token="your_access_token", refresh_token="your_refresh_token")
    
    # Make an asynchronous request
    try:
        orders = await client.get_orders()
        print(orders)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

# Supported Marketplaces
- **Digikala**: API integration for seller operations.

- **Snapp**: Integration for orders and dispatch management.

- **Basalam**: Vendor management and order processing.

- **Tapsi**: Delivery and shipment tracking operations.

# Directory Structure
```
src/
└── iranian_marketplaces_sdk/
    ├── digikala/
    ├── snapp/
    ├── basalam/
    └── tapsi/
```

# License
This project is licensed under the MIT License.