# x402api Python SDK

Official server-side Python client for the [x402api public API](https://api.x402api.com/openapi/openapi.json). It provides typed request and response models for programmatic x402 charges, resources, receiving addresses, payments, receipts, and wallet balances.

The generated package is `x402api`, targets Python 3.9+, and uses `urllib3` and Pydantic v2. The production base URL is `https://api.x402api.com`.

> Package registry publishing is separate from SDK generation. Until the first PyPI release is available, install from this repository.

## Installation

From PyPI after a release is published:

```bash
python -m pip install x402api
```

From GitHub today:

```bash
python -m pip install "git+https://github.com/x402api-com/x402api-python.git"
```

## Authentication

Create a scoped tenant API key and provide it as a bearer token. Keep it in a server-side secret store; do not ship tenant credentials in browser, mobile, or desktop applications.

```python
import os
import x402api

configuration = x402api.Configuration(
    host="https://api.x402api.com",
    access_token=os.environ["X402API_TENANT_API_KEY"],
)
```

`facilitator_get_supported()` and `receipt_verification_keys_retrieve()` are public and may be called without a token. All other operations use tenant bearer authentication.

Tenant API keys must also grant the exact scope documented by each operation:

- charges: `commerce:write` to create and `commerce:read` to retrieve;
- network-fee quotes and resource reads: `resources:read`;
- resource creation and new versions: `resources:write`;
- orders: `orders:read`;
- payment readiness: `payment-controls:read`;
- payments, observations, and receipts: `payments:read`;
- receiving-address capabilities and lists: `wallets:read`; and
- wallet balances: `balances:read`.

The SDK excludes dashboard-only mutations that require a human tenant owner with recent step-up. A tenant API key cannot call those operations regardless of its scopes.

## Quick start: create a charge

```python
import os
from uuid import UUID

import x402api
from x402api.rest import ApiException

configuration = x402api.Configuration(
    access_token=os.environ["X402API_TENANT_API_KEY"],
)

request = x402api.DynamicChargeCreate(
    resource_version_id=UUID("00000000-0000-4000-8000-000000000001"),
    resource_url="https://merchant.example.com/premium-report",
    prices=[
        x402api.DynamicChargePrice(
            asset_id="base_usdc",
            amount_atomic="1000000",
        )
    ],
    expires_in_seconds=900,
    metadata={"customer_reference": "customer-123"},
)

try:
    with x402api.ApiClient(configuration) as api_client:
        charges = x402api.ProgrammaticChargesApi(api_client)
        charge = charges.charges_create("charge-example-001", request)
        print(charge.to_dict())
except ApiException as error:
    print(error.status, error.reason, error.body)
    raise
```

The first argument to `charges_create` is the `Idempotency-Key`. Use a new key for each intended mutation. If the outcome is uncertain, retry the identical payload with the same key.

## Response metadata and pagination

Normal methods return the decoded model. Add `_with_http_info` to receive `data`, `status_code`, and `headers`:

```python
with x402api.ApiClient(configuration) as api_client:
    payments_api = x402api.OrdersAndPaymentsApi(api_client)
    response = payments_api.payments_list_with_http_info(page_size=25)

    for payment in response.data:
        print(payment)

    next_cursor = response.headers.get("X-X402API-Next-Cursor")
    if next_cursor:
        next_page = payments_api.payments_list(
            cursor=next_cursor,
            page_size=25,
        )
```

Cursors are opaque. Pass them back unchanged; do not decode or construct them. `_request_timeout=10` sets a total timeout, while `_request_timeout=(3, 10)` sets connect and read timeouts.

The client does not retry automatically. For connection failures and HTTP `408`, `429`, `500`, `502`, `503`, or `504`, add bounded exponential backoff in your application. Respect `Retry-After`, and preserve the same idempotency key and body when retrying a mutation.

## API classes and functions

Every function has `*_with_http_info` and `*_without_preload_content` variants in addition to the normal method shown below. Links lead to generated parameter, response, and status-code documentation.

| API class | Function | HTTP endpoint |
| --- | --- | --- |
| [`ProgrammaticChargesApi`](docs/ProgrammaticChargesApi.md) | `charges_create(idempotency_key, dynamic_charge_create)` | `POST /v1/charges` |
| [`ProgrammaticChargesApi`](docs/ProgrammaticChargesApi.md) | `charges_retrieve(charge_id)` | `GET /v1/charges/{charge_id}` |
| [`FacilitatorDiscoveryApi`](docs/FacilitatorDiscoveryApi.md) | `facilitator_get_supported()` | `GET /v1/facilitator/supported` |
| [`IdempotencyApi`](docs/IdempotencyApi.md) | `idempotency_get_outcome(idempotency_key)` | `GET /v1/idempotency-outcomes/{idempotency_key}` |
| [`ResourcesAndPricingApi`](docs/ResourcesAndPricingApi.md) | `network_fees_create_quote(network_fee_preview)` | `POST /v1/network-fee-quotes` |
| [`OrdersAndPaymentsApi`](docs/OrdersAndPaymentsApi.md) | `orders_list(cursor=None, page_size=None)` | `GET /v1/orders` |
| [`OrdersAndPaymentsApi`](docs/OrdersAndPaymentsApi.md) | `orders_retrieve(id)` | `GET /v1/orders/{id}` |
| [`AssetsAndPaymentControlsApi`](docs/AssetsAndPaymentControlsApi.md) | `payment_readiness_retrieve()` | `GET /v1/payment-readiness` |
| [`OrdersAndPaymentsApi`](docs/OrdersAndPaymentsApi.md) | `payments_list(cursor=None, page_size=None)` | `GET /v1/payments` |
| [`OrdersAndPaymentsApi`](docs/OrdersAndPaymentsApi.md) | `payments_retrieve(id)` | `GET /v1/payments/{id}` |
| [`OrdersAndPaymentsApi`](docs/OrdersAndPaymentsApi.md) | `payments_list_observations(id, cursor=None, page_size=None)` | `GET /v1/payments/{id}/observations` |
| [`OrdersAndPaymentsApi`](docs/OrdersAndPaymentsApi.md) | `payments_retrieve_receipt(id)` | `GET /v1/payments/{id}/receipt` |
| [`OrdersAndPaymentsApi`](docs/OrdersAndPaymentsApi.md) | `receipt_verification_keys_retrieve()` | `GET /v1/payment-receipt-verification-keys` |
| [`ReceivingAddressesApi`](docs/ReceivingAddressesApi.md) | `receiving_addresses_get_control_capabilities()` | `GET /v1/receiving-address-control-capabilities` |
| [`ReceivingAddressesApi`](docs/ReceivingAddressesApi.md) | `receiving_addresses_list(cursor=None, page_size=None)` | `GET /v1/receiving-addresses` |
| [`ResourcesAndPricingApi`](docs/ResourcesAndPricingApi.md) | `resources_list(cursor=None, page_size=None)` | `GET /v1/resources` |
| [`ResourcesAndPricingApi`](docs/ResourcesAndPricingApi.md) | `resources_create(idempotency_key, resource_create)` | `POST /v1/resources` |
| [`ResourcesAndPricingApi`](docs/ResourcesAndPricingApi.md) | `resources_list_versions(resource_id, cursor=None, page_size=None)` | `GET /v1/resources/{resource_id}/versions` |
| [`ResourcesAndPricingApi`](docs/ResourcesAndPricingApi.md) | `resources_create_version(idempotency_key, resource_id, body)` | `POST /v1/resources/{resource_id}/versions` |
| [`WalletsAndTransfersApi`](docs/WalletsAndTransfersApi.md) | `wallets_retrieve_balance(id, finality=None)` | `GET /v1/wallets/{id}/balances` |

All models are exported from `x402api`; individual model documentation is in [`docs/`](docs/). See [`USAGE.md`](USAGE.md) for more complete patterns.

## Automatic generation

This repository uses OpenAPI Generator 7.24.0, pinned by Docker image and digest in [`scripts/generate-sdk.sh`](scripts/generate-sdk.sh). The [`SDK generation workflow`](.github/workflows/sdk_generation.yaml) checks the live OpenAPI document hourly and on manual or repository dispatch. When its normalized contract changes, GitHub Actions regenerates, validates, and commits the SDK to `main`.

To regenerate locally with Docker:

```bash
./scripts/generate-sdk.sh
python -m pip install .
python -m compileall -q x402api
```

Persistent files such as this README, `USAGE.md`, workflow configuration, and generator scripts are protected by [`.openapi-generator-ignore`](.openapi-generator-ignore). Generated client and model files should not be edited manually.

Licensed under the [MIT License](LICENSE).
