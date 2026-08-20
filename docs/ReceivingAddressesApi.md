# x402api.ReceivingAddressesApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receiving_addresses_activate**](ReceivingAddressesApi.md#receiving_addresses_activate) | **POST** /v1/receiving-addresses/{readiness_id}/activate | Activate a receiving address
[**receiving_addresses_create_control_challenge**](ReceivingAddressesApi.md#receiving_addresses_create_control_challenge) | **POST** /v1/receiving-address-control-challenges | Create a receiving-address control challenge
[**receiving_addresses_get_control_capabilities**](ReceivingAddressesApi.md#receiving_addresses_get_control_capabilities) | **GET** /v1/receiving-address-control-capabilities | Get receiving-address control capabilities
[**receiving_addresses_list**](ReceivingAddressesApi.md#receiving_addresses_list) | **GET** /v1/receiving-addresses | List receiving addresses
[**receiving_addresses_refresh_readiness**](ReceivingAddressesApi.md#receiving_addresses_refresh_readiness) | **POST** /v1/receiving-addresses/{readiness_id}/readiness-refreshes | Refresh receiving-address readiness
[**receiving_addresses_register**](ReceivingAddressesApi.md#receiving_addresses_register) | **POST** /v1/receiving-addresses | Register a receiving address
[**receiving_addresses_rotate**](ReceivingAddressesApi.md#receiving_addresses_rotate) | **POST** /v1/receiving-addresses/{readiness_id}/rotations | Rotate a receiving address


# **receiving_addresses_activate**
> ExternalReceivingAddress receiving_addresses_activate(idempotency_key, readiness_id)

Activate a receiving address

Activate a ready external receiving-address registration idempotently.

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
    idempotency_key = 'idempotency_key_example' # str | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome.
    readiness_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Activate a receiving address
        api_response = api_instance.receiving_addresses_activate(idempotency_key, readiness_id)
        print("The response of ReceivingAddressesApi->receiving_addresses_activate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->receiving_addresses_activate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
 **readiness_id** | **UUID**|  |

### Return type

[**ExternalReceivingAddress**](ExternalReceivingAddress.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for activate a receiving address. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receiving_addresses_create_control_challenge**
> ExternalAddressControlChallenge receiving_addresses_create_control_challenge(idempotency_key, external_address_control_challenge_create)

Create a receiving-address control challenge

Create an idempotent proof-of-control challenge for an external receiving address.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.external_address_control_challenge import ExternalAddressControlChallenge
from x402api.models.external_address_control_challenge_create import ExternalAddressControlChallengeCreate
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
    idempotency_key = 'idempotency_key_example' # str | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome.
    external_address_control_challenge_create = x402api.ExternalAddressControlChallengeCreate() # ExternalAddressControlChallengeCreate |

    try:
        # Create a receiving-address control challenge
        api_response = api_instance.receiving_addresses_create_control_challenge(idempotency_key, external_address_control_challenge_create)
        print("The response of ReceivingAddressesApi->receiving_addresses_create_control_challenge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->receiving_addresses_create_control_challenge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
 **external_address_control_challenge_create** | [**ExternalAddressControlChallengeCreate**](ExternalAddressControlChallengeCreate.md)|  |

### Return type

[**ExternalAddressControlChallenge**](ExternalAddressControlChallenge.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response for create a receiving-address control challenge. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receiving_addresses_get_control_capabilities**
> ExternalAddressControlCapabilities receiving_addresses_get_control_capabilities()

Get receiving-address control capabilities

Return the supported proof and control capabilities for external receiving addresses.

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

List tenant receiving-address registrations using opaque cursor pagination.

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

# **receiving_addresses_refresh_readiness**
> ExternalReceivingAddress receiving_addresses_refresh_readiness(idempotency_key, readiness_id)

Refresh receiving-address readiness

Request an idempotent refresh of external receiving-address readiness evidence.

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
    idempotency_key = 'idempotency_key_example' # str | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome.
    readiness_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        # Refresh receiving-address readiness
        api_response = api_instance.receiving_addresses_refresh_readiness(idempotency_key, readiness_id)
        print("The response of ReceivingAddressesApi->receiving_addresses_refresh_readiness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->receiving_addresses_refresh_readiness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
 **readiness_id** | **UUID**|  |

### Return type

[**ExternalReceivingAddress**](ExternalReceivingAddress.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for refresh receiving-address readiness. |  * X-Request-ID -  <br>  |
**201** | Successful response for refresh receiving-address readiness. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receiving_addresses_register**
> ExternalReceivingAddress receiving_addresses_register(idempotency_key, external_receiving_address_create)

Register a receiving address

Register a proven external receiving address without transferring wallet custody.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.external_receiving_address import ExternalReceivingAddress
from x402api.models.external_receiving_address_create import ExternalReceivingAddressCreate
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
    idempotency_key = 'idempotency_key_example' # str | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome.
    external_receiving_address_create = x402api.ExternalReceivingAddressCreate() # ExternalReceivingAddressCreate |

    try:
        # Register a receiving address
        api_response = api_instance.receiving_addresses_register(idempotency_key, external_receiving_address_create)
        print("The response of ReceivingAddressesApi->receiving_addresses_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->receiving_addresses_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
 **external_receiving_address_create** | [**ExternalReceivingAddressCreate**](ExternalReceivingAddressCreate.md)|  |

### Return type

[**ExternalReceivingAddress**](ExternalReceivingAddress.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response for register a receiving address. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receiving_addresses_rotate**
> ExternalReceivingAddress receiving_addresses_rotate(idempotency_key, readiness_id, external_receiving_address_rotation)

Rotate a receiving address

Create an idempotent receiving-address rotation from a proven replacement.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.external_receiving_address import ExternalReceivingAddress
from x402api.models.external_receiving_address_rotation import ExternalReceivingAddressRotation
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
    idempotency_key = 'idempotency_key_example' # str | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome.
    readiness_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    external_receiving_address_rotation = x402api.ExternalReceivingAddressRotation() # ExternalReceivingAddressRotation |

    try:
        # Rotate a receiving address
        api_response = api_instance.receiving_addresses_rotate(idempotency_key, readiness_id, external_receiving_address_rotation)
        print("The response of ReceivingAddressesApi->receiving_addresses_rotate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->receiving_addresses_rotate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
 **readiness_id** | **UUID**|  |
 **external_receiving_address_rotation** | [**ExternalReceivingAddressRotation**](ExternalReceivingAddressRotation.md)|  |

### Return type

[**ExternalReceivingAddress**](ExternalReceivingAddress.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response for rotate a receiving address. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
