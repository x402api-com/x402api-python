# x402api.ProgrammaticChargesApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dynamic_charge**](ProgrammaticChargesApi.md#create_dynamic_charge) | **POST** /v1/charges |
[**retrieve_dynamic_charge**](ProgrammaticChargesApi.md#retrieve_dynamic_charge) | **GET** /v1/charges/{charge_id} |


# **create_dynamic_charge**
> DynamicChargeResponse create_dynamic_charge(idempotency_key, dynamic_charge_create)

Create one idempotent dynamic charge from an active resource template. The immutable challenge freezes exact requested atomic amounts, eligible rails, verified tenant receiving addresses, fee policy and evidence, metadata, and expiry. The caller cannot supply a recipient address.

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
    idempotency_key = 'idempotency_key_example' # str | Unique mutation key; replaying different content returns HTTP 409.
    dynamic_charge_create = x402api.DynamicChargeCreate() # DynamicChargeCreate |

    try:
        api_response = api_instance.create_dynamic_charge(idempotency_key, dynamic_charge_create)
        print("The response of ProgrammaticChargesApi->create_dynamic_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProgrammaticChargesApi->create_dynamic_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique mutation key; replaying different content returns HTTP 409. |
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
**201** |  |  -  |
**409** |  |  -  |
**422** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_dynamic_charge**
> DynamicChargeResponse retrieve_dynamic_charge(charge_id)

Return the tenant-scoped frozen charge terms and current projected status without recomputing prices, recipients, rails, or fee evidence.

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
        api_response = api_instance.retrieve_dynamic_charge(charge_id)
        print("The response of ProgrammaticChargesApi->retrieve_dynamic_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProgrammaticChargesApi->retrieve_dynamic_charge: %s\n" % e)
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
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
