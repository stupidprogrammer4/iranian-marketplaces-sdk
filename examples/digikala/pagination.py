"""Read at most three pages of variants: python -m examples.digikala.pagination"""

from examples._credentials import required_env
from iranian_marketplaces_sdk import DigikalaSync
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.variants import ListQuery


def main() -> None:
    with DigikalaSync(required_env("DIGIKALA_ACCESS_TOKEN")) as client:
        for page_number in range(1, 4):
            result = client.variants.list(query=ListQuery(page=page_number, size=5))
            items = result.data.items or []
            for variant in items:
                print(variant.id, variant.title, variant.price_sale)

            pager = result.data.pager
            if not items or pager is None or pager.total_pages is None:
                break
            if page_number >= pager.total_pages:
                break


if __name__ == "__main__":
    main()
