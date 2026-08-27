# x402api.ProgrammaticChargesApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**charges_create**](ProgrammaticChargesApi.md#charges_create) | **POST** /v1/charges | Create a programmatic charge
[**charges_retrieve**](ProgrammaticChargesApi.md#charges_retrieve) | **GET** /v1/charges/{charge_id} | Retrieve a programmatic charge


# **charges_create**
> DynamicChargeResponse charges_create(idempotency_key, dynamic_charge_create)

Create a programmatic charge

Create one idempotent dynamic charge and immutable PAYMENT-REQUIRED challenge from an active resource template. The 201 management response contains the canonical buyer challenge; it does not submit or settle payment. Requires a tenant API key with the `commerce:write` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.dynamic_charge_create import DynamicChargeCreate
from x402api.models.dynamic_charge_response import DynamicChargeResponse
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
    api_instance = x402api.ProgrammaticChargesApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome.
    dynamic_charge_create = x402api.DynamicChargeCreate() # DynamicChargeCreate |

    try:
        # Create a programmatic charge
        api_response = api_instance.charges_create(idempotency_key, dynamic_charge_create)
        print("The response of ProgrammaticChargesApi->charges_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProgrammaticChargesApi->charges_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
 **dynamic_charge_create** | [**DynamicChargeCreate**](DynamicChargeCreate.md)|  |

### Return type

[**DynamicChargeResponse**](DynamicChargeResponse.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response for create a programmatic charge. |  * X-Request-ID -  <br>  |
**409** | The request failed. |  * X-Request-ID -  <br>  |
**422** | The request failed. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charges_retrieve**
> DynamicChargeResponse charges_retrieve(charge_id)

Retrieve a programmatic charge

Retrieve the frozen terms and current projected status of a tenant charge. Requires a tenant API key with the `commerce:read` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.dynamic_charge_response import DynamicChargeResponse
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
    api_instance = x402api.ProgrammaticChargesApi(api_client)
    charge_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Retrieve a programmatic charge
        api_response = api_instance.charges_retrieve(charge_id)
        print("The response of ProgrammaticChargesApi->charges_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProgrammaticChargesApi->charges_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **UUID**|  |

### Return type

[**DynamicChargeResponse**](DynamicChargeResponse.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for retrieve a programmatic charge. |  * X-Request-ID -  <br>  |
**404** | The request failed. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
