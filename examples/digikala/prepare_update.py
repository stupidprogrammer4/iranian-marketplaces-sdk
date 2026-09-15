"""Build a stock-update payload offline: python -m examples.digikala.prepare_update"""

import json

from iranian_marketplaces_sdk.marketplaces.digikala.data.api.variants import UpdateRequest


def main() -> None:
    body = UpdateRequest(seller_stock=7)
    print(json.dumps(body.to_payload()))
    # To apply it with an authenticated client and your chosen variant:
    # client.variants.update(variant_id, body=body)


if __name__ == "__main__":
    main()
