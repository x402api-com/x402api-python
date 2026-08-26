# x402api.IdempotencyApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idempotency_get_outcome**](IdempotencyApi.md#idempotency_get_outcome) | **GET** /v1/idempotency-outcomes/{idempotency_key} | Get an idempotency outcome


# **idempotency_get_outcome**
> IdempotencyOutcome idempotency_get_outcome(idempotency_key)

Get an idempotency outcome

Return the authoritative tenant-scoped outcome for a durable mutation key. Requires an authenticated tenant API key; no additional scope is required.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.idempotency_outcome import IdempotencyOutcome
from x402api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.x402api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = x402api.Configuration(
    host = "https://api.x402api.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tenantApiKey
configuration = x402api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with x402api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = x402api.IdempotencyApi(api_client)
    idempotency_key = 'idempotency_key_example' # str |

    try:
        # Get an idempotency outcome
        api_response = api_instance.idempotency_get_outcome(idempotency_key)
        print("The response of IdempotencyApi->idempotency_get_outcome:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdempotencyApi->idempotency_get_outcome: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**|  |

### Return type

[**IdempotencyOutcome**](IdempotencyOutcome.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for get an idempotency outcome. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
