# Python usage guide

The [README](README.md) contains installation instructions and the complete function index. This guide focuses on safe production patterns.

## Create and reuse a client

`ApiClient` owns the connection pool. Create one per configuration and reuse it instead of creating a new client for every request.

```python
import os
import x402api

configuration = x402api.Configuration(
    host="https://api.x402api.com",
    access_token=os.environ["X402API_TENANT_API_KEY"],
)

with x402api.ApiClient(configuration) as api_client:
    charges_api = x402api.ProgrammaticChargesApi(api_client)
    payments_api = x402api.OrdersAndPaymentsApi(api_client)
    resources_api = x402api.ResourcesAndPricingApi(api_client)
```

The context manager closes the underlying HTTP pool. For a long-running service, keep the client for the application lifetime and call `api_client.close()` during shutdown.

## Create and retrieve a charge

```python
from uuid import UUID

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
    metadata={"order_id": "order-123"},
)

idempotency_key = "charge-order-123-v1"
charge = charges_api.charges_create(idempotency_key, request)

same_charge = charges_api.charges_retrieve(charge.charge_id)
```

Prices use atomic-unit strings, not floating point. For example, `"1000000"` represents one token for an asset with six decimals.

## Pagination and HTTP headers

List operations return a bounded array. Use the `with_http_info` variant when you need the next cursor or request ID.

```python
cursor = None

while True:
    response = payments_api.payments_list_with_http_info(
        cursor=cursor,
        page_size=100,
        _request_timeout=(3, 15),
    )

    for payment in response.data:
        process(payment)

    request_id = response.headers.get("X-Request-ID")
    cursor = response.headers.get("X-X402API-Next-Cursor")
    if not cursor:
        break
```

Treat the cursor as opaque and pass it back unchanged. The same pattern applies to orders, payment observations, receiving addresses, resources, and resource versions.

## Poll a receipt without blocking fulfillment

The receipt endpoint returns either a finalized signed `PaymentReceipt` with HTTP `200` or a `PaymentReceiptStatus` with HTTP `202`. Use the HTTP-info variant when you need `Retry-After`:

```python
from x402api.models.payment_receipt import PaymentReceipt
from x402api.models.payment_receipt_status import PaymentReceiptStatus

response = payments_api.payments_retrieve_receipt_with_http_info(payment_id)

if isinstance(response.data, PaymentReceiptStatus):
    if response.data.confirmed:
        provision_once(payment_id=response.data.payment_id)
    schedule_receipt_poll(
        payment_id=response.data.payment_id,
        retry_after=response.headers.get("Retry-After"),
    )
else:
    assert isinstance(response.data, PaymentReceipt)
    provision_once(payment_id=payment_id)
    attach_signed_receipt(response.data)
```

Confirmation is sufficient to begin idempotent fulfillment. Finalization and the signed receipt arrive asynchronously; do not resubmit or create a second payment while receipt polling returns HTTP `202`.

## Error handling

```python
from x402api.rest import ApiException

try:
    payment = payments_api.payments_retrieve(payment_id)
except ApiException as error:
    request_id = None
    if error.headers:
        request_id = error.headers.get("X-Request-ID")

    if error.status == 404:
        handle_not_found()
    elif error.status == 429:
        handle_rate_limit(error.headers.get("Retry-After"))
    else:
        log_api_error(
            status=error.status,
            reason=error.reason,
            body=error.body,
            request_id=request_id,
        )
        raise
```

Pydantic rejects invalid request models before the request is sent. HTTP error bodies use the generated `ApiErrorEnvelope` schema when the server returned a documented JSON error.

## Idempotency and retries

Mutations require keys of 8-160 characters matching `[A-Za-z0-9._:-]+`. Persist the key with the intent you are executing.

- New intended mutation: generate a new key.
- Timeout or connection reset after sending: retry the identical body with the same key.
- Known validation failure: fix the request and use a new key.
- Uncertain durable outcome: call `IdempotencyApi.idempotency_get_outcome(key)`.

The SDK does not retry automatically. Bound application retries, use exponential backoff with jitter, respect `Retry-After`, and normally retry only connection failures plus HTTP `408`, `429`, `500`, `502`, `503`, and `504`.

## Public endpoints

These endpoints do not need a tenant key:

```python
public_configuration = x402api.Configuration()
with x402api.ApiClient(public_configuration) as public_client:
    supported = x402api.FacilitatorDiscoveryApi(
        public_client
    ).facilitator_get_supported()
    keys = x402api.OrdersAndPaymentsApi(
        public_client
    ).receipt_verification_keys_retrieve()
```

## Serialization

Generated models are Pydantic models. Use `model_dump()` for Python data, `to_dict()` for the API-shaped dictionary, and `to_json()` for JSON.

```python
payload = charge.to_dict()
json_payload = charge.to_json()
```

Do not edit generated files under `x402api/` or `docs/`; update the OpenAPI contract or generator configuration instead.
