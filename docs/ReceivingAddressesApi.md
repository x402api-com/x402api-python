# x402api.ReceivingAddressesApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_receiving_address_control_capabilities_retrieve**](ReceivingAddressesApi.md#v1_receiving_address_control_capabilities_retrieve) | **GET** /v1/receiving-address-control-capabilities |
[**v1_receiving_address_control_challenges_create**](ReceivingAddressesApi.md#v1_receiving_address_control_challenges_create) | **POST** /v1/receiving-address-control-challenges |
[**v1_receiving_addresses_activate_create**](ReceivingAddressesApi.md#v1_receiving_addresses_activate_create) | **POST** /v1/receiving-addresses/{readiness_id}/activate |
[**v1_receiving_addresses_create**](ReceivingAddressesApi.md#v1_receiving_addresses_create) | **POST** /v1/receiving-addresses |
[**v1_receiving_addresses_list**](ReceivingAddressesApi.md#v1_receiving_addresses_list) | **GET** /v1/receiving-addresses |
[**v1_receiving_addresses_readiness_refreshes_create**](ReceivingAddressesApi.md#v1_receiving_addresses_readiness_refreshes_create) | **POST** /v1/receiving-addresses/{readiness_id}/readiness-refreshes |
[**v1_receiving_addresses_rotations_create**](ReceivingAddressesApi.md#v1_receiving_addresses_rotations_create) | **POST** /v1/receiving-addresses/{readiness_id}/rotations |


# **v1_receiving_address_control_capabilities_retrieve**
> ExternalAddressControlCapabilities v1_receiving_address_control_capabilities_retrieve()

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
        api_response = api_instance.v1_receiving_address_control_capabilities_retrieve()
        print("The response of ReceivingAddressesApi->v1_receiving_address_control_capabilities_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->v1_receiving_address_control_capabilities_retrieve: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_receiving_address_control_challenges_create**
> ExternalAddressControlChallenge v1_receiving_address_control_challenges_create(idempotency_key, external_address_control_challenge_create)

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
    idempotency_key = 'idempotency_key_example' # str | Unique mutation key; replaying different content returns HTTP 409.
    external_address_control_challenge_create = x402api.ExternalAddressControlChallengeCreate() # ExternalAddressControlChallengeCreate |

    try:
        api_response = api_instance.v1_receiving_address_control_challenges_create(idempotency_key, external_address_control_challenge_create)
        print("The response of ReceivingAddressesApi->v1_receiving_address_control_challenges_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->v1_receiving_address_control_challenges_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique mutation key; replaying different content returns HTTP 409. |
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_receiving_addresses_activate_create**
> ExternalReceivingAddress v1_receiving_addresses_activate_create(idempotency_key, readiness_id)

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
    idempotency_key = 'idempotency_key_example' # str | Unique mutation key; replaying different content returns HTTP 409.
    readiness_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.v1_receiving_addresses_activate_create(idempotency_key, readiness_id)
        print("The response of ReceivingAddressesApi->v1_receiving_addresses_activate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->v1_receiving_addresses_activate_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique mutation key; replaying different content returns HTTP 409. |
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_receiving_addresses_create**
> ExternalReceivingAddress v1_receiving_addresses_create(idempotency_key, external_receiving_address_create)

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
    idempotency_key = 'idempotency_key_example' # str | Unique mutation key; replaying different content returns HTTP 409.
    external_receiving_address_create = x402api.ExternalReceivingAddressCreate() # ExternalReceivingAddressCreate |

    try:
        api_response = api_instance.v1_receiving_addresses_create(idempotency_key, external_receiving_address_create)
        print("The response of ReceivingAddressesApi->v1_receiving_addresses_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->v1_receiving_addresses_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique mutation key; replaying different content returns HTTP 409. |
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_receiving_addresses_list**
> List[ExternalReceivingAddress] v1_receiving_addresses_list(cursor=cursor, page_size=page_size)

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
        api_response = api_instance.v1_receiving_addresses_list(cursor=cursor, page_size=page_size)
        print("The response of ReceivingAddressesApi->v1_receiving_addresses_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->v1_receiving_addresses_list: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_receiving_addresses_readiness_refreshes_create**
> ExternalReceivingAddress v1_receiving_addresses_readiness_refreshes_create(idempotency_key, readiness_id)

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
    idempotency_key = 'idempotency_key_example' # str | Unique mutation key; replaying different content returns HTTP 409.
    readiness_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.v1_receiving_addresses_readiness_refreshes_create(idempotency_key, readiness_id)
        print("The response of ReceivingAddressesApi->v1_receiving_addresses_readiness_refreshes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->v1_receiving_addresses_readiness_refreshes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique mutation key; replaying different content returns HTTP 409. |
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
**200** |  |  -  |
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_receiving_addresses_rotations_create**
> ExternalReceivingAddress v1_receiving_addresses_rotations_create(idempotency_key, readiness_id, external_receiving_address_rotation)

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
    idempotency_key = 'idempotency_key_example' # str | Unique mutation key; replaying different content returns HTTP 409.
    readiness_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    external_receiving_address_rotation = x402api.ExternalReceivingAddressRotation() # ExternalReceivingAddressRotation |

    try:
        api_response = api_instance.v1_receiving_addresses_rotations_create(idempotency_key, readiness_id, external_receiving_address_rotation)
        print("The response of ReceivingAddressesApi->v1_receiving_addresses_rotations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceivingAddressesApi->v1_receiving_addresses_rotations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique mutation key; replaying different content returns HTTP 409. |
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
