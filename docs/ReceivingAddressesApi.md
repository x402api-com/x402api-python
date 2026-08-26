# x402api.ReceivingAddressesApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receiving_addresses_get_control_capabilities**](ReceivingAddressesApi.md#receiving_addresses_get_control_capabilities) | **GET** /v1/receiving-address-control-capabilities | Get receiving-address control capabilities
[**receiving_addresses_list**](ReceivingAddressesApi.md#receiving_addresses_list) | **GET** /v1/receiving-addresses | List receiving addresses


# **receiving_addresses_get_control_capabilities**
> ExternalAddressControlCapabilities receiving_addresses_get_control_capabilities()

Get receiving-address control capabilities

Return the supported proof and control capabilities for external receiving addresses. Requires a tenant API key with the `wallets:read` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.external_address_control_capabilities import ExternalAddressControlCapabilities
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
    api_instance = x402api.ReceivingAddressesApi(api_client)

    try:
        # Get receiving-address control capabilities
        api_response = api_instance.receiving_addresses_get_control_capabilities()
        print("The response of ReceivingAddressesApi->receiving_addresses_get_control_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->receiving_addresses_get_control_capabilities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ExternalAddressControlCapabilities**](ExternalAddressControlCapabilities.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for get receiving-address control capabilities. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receiving_addresses_list**
> List[ExternalReceivingAddress] receiving_addresses_list(cursor=cursor, page_size=page_size)

List receiving addresses

List tenant receiving-address registrations using opaque cursor pagination. Requires a tenant API key with the `wallets:read` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.external_receiving_address import ExternalReceivingAddress
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
    api_instance = x402api.ReceivingAddressesApi(api_client)
    cursor = 'cursor_example' # str | Opaque pagination cursor from X-X402API-Next-Cursor or rel=next Link. (optional)
    page_size = 100 # int | Number of results in the bounded array page (default and maximum 100). (optional) (default to 100)

    try:
        # List receiving addresses
        api_response = api_instance.receiving_addresses_list(cursor=cursor, page_size=page_size)
        print("The response of ReceivingAddressesApi->receiving_addresses_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->receiving_addresses_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]
 **page_size** | **int**| Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100]

### Return type

[**List[ExternalReceivingAddress]**](ExternalReceivingAddress.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for list receiving addresses. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
