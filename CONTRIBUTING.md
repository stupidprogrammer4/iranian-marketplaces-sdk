# Contributing

User-facing guides belong in `docs/`, organized as a learning path with complete usage examples.
Keep implementation notes and contributor workflows here.

## Local setup and checks

```bash
python -m pip install -e .
python -m pip install pytest pytest-asyncio anyio ruff mypy pyright build hatchling twine
pytest -q
ruff check .
ruff format --check .
mypy
pyright
python -m build
```

The automated suite runs offline. Runnable examples live in `examples/<marketplace>/`; they must
read credentials at execution time and make no network calls when imported. The examples are
included in static type checks and the source distribution, while the wheel contains only the SDK.

## Package organization

- `common/` holds transport, exceptions and model bases shared by marketplaces.
- Each marketplace owns its clients, constants, helpers and data models.
- Digikala's `resources/` groups sync and async methods by business area; `data/api/` contains
  their shared models. Existing flat methods and `data` imports remain public API.
- `operations.py` records supported Digikala methods and paths.
- `tests/fixtures/digikala_openapi.json` is the public Swagger snapshot used by contract tests,
  with credential-like example values redacted.

Maintain resource clients and models directly. When an upstream operation changes, update both
engines, shared models, the operation catalog, relevant tests and the method reference. Review any
snapshot update independently of implementation changes. Runtime imports must not read the fixture.

## Digikala schema differences

The models deliberately account for these differences from the 2026-09-15 Swagger snapshot:

| Area | Interpretation |
| --- | --- |
| PLP Excel imports | `startAt` and `endAt` use date strings as in the request example, despite the integer declaration. |
| Variant dates | `created_at` accepts the observed datetime object and the documented string; the existing detail contract supports the same object. |
| Inventory sorting | `sort_columns` is a list of strings, matching live responses. |
| Invoice items | Items are a list of the documented alternatives; payment-method keys and titles are strings, preserving the existing contract. |
| Current variant promotions | The malformed object-properties wrapper describes a nested collection. |
| Webhook events | `all_event_types` maps event keys to descriptions, matching the example and observed response. |

Keep regressions for observed response differences. Contract tests verify the documented routes
without contacting a seller. A passing mock test does not establish live permission or success for
an account. Live testing should use explicit, reviewed operations; some GET routes start exports
or verification workflows.

For release procedures, see [RELEASING.md](RELEASING.md).
