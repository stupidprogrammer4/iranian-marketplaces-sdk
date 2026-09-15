# Iranian Marketplaces SDK

A Python SDK for **Digikala**, **Snapp Shop**, **Basalam** and **Tapsi Shop**, with synchronous
and asynchronous clients, Pydantic models and shared error handling.

## Installation

Requires Python 3.13 or newer.

```bash
pip install iranian-marketplaces-sdk
```

To use the examples and features on the current branch, install this checkout:

```bash
python -m pip install -e .
```

## First request

Set `DIGIKALA_ACCESS_TOKEN` in your environment, then:

```python
import os

from iranian_marketplaces_sdk import DigikalaSync

with DigikalaSync(os.environ["DIGIKALA_ACCESS_TOKEN"]) as client:
    response = client.health_check()
    print(response.status, response.data.mode)
```

Use `DigikalaAsync`, `async with` and `await` for async applications.

## Learn the SDK

The [learning path](docs/README.md) walks through installation, models, pagination, async usage
and error handling, followed by marketplace-specific workflows. Guides are written in Persian.

- [Getting started](docs/getting-started.md)
- [Digikala guide](docs/digikala/README.md)
- [Snapp Shop](docs/marketplaces/snapp.md), [Basalam](docs/marketplaces/basalam.md),
  [Tapsi Shop](docs/marketplaces/tapsi.md)
- [Runnable examples](examples/README.md)
- [Digikala method reference](docs/reference/digikala-endpoints.md)

## Coverage

| Marketplace | Available operations |
| --- | --- |
| Digikala | 274 operations across 37 resource groups: products, variants, orders, inventory, shipping, pricing, finance, advertising, webhooks and more |
| Snapp Shop | Products, batch product updates, orders and order detail |
| Basalam | Products, batch product updates, parcels and discounts |
| Tapsi Shop | Products, batch product updates and orders |

Both client types expose the same methods and models. Existing flat Digikala methods such as
`list_variants()` remain supported alongside resource methods such as `client.variants.list()`.
Documented responses use Pydantic models; undocumented Digikala responses preserve bytes and headers
in `RawResponse`.

## Repository layout

```text
iranian_marketplaces_sdk/   Installable SDK
examples/                  Runnable examples, grouped by marketplace
  digikala/
  snapp/
  basalam/
  tapsi/
docs/                      Learning path, guides and API reference
tests/                     Offline tests and API fixtures
```

For development and checks, see [Contributing](CONTRIBUTING.md).
Release instructions are in [Releasing](RELEASING.md).

## License

MIT. See [LICENSE](LICENSE).
