# x402api.ResourcesAndPricingApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_fees_create_quote**](ResourcesAndPricingApi.md#network_fees_create_quote) | **POST** /v1/network-fee-quotes | Create a network-fee quote
[**resources_create**](ResourcesAndPricingApi.md#resources_create) | **POST** /v1/resources | Create a resource
[**resources_create_version**](ResourcesAndPricingApi.md#resources_create_version) | **POST** /v1/resources/{resource_id}/versions | Create a resource version
[**resources_list**](ResourcesAndPricingApi.md#resources_list) | **GET** /v1/resources | List resources
[**resources_list_versions**](ResourcesAndPricingApi.md#resources_list_versions) | **GET** /v1/resources/{resource_id}/versions | List resource versions


# **network_fees_create_quote**
> NetworkFeePreviewResponse network_fees_create_quote(network_fee_preview)

Create a network-fee quote

Preview bounded network fees for the requested resource prices and rails. Requires a tenant API key with the `resources:read` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.network_fee_preview import NetworkFeePreview
from x402api.models.network_fee_preview_response import NetworkFeePreviewResponse
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
    api_instance = x402api.ResourcesAndPricingApi(api_client)
    network_fee_preview = x402api.NetworkFeePreview() # NetworkFeePreview |

    try:
        # Create a network-fee quote
        api_response = api_instance.network_fees_create_quote(network_fee_preview)
        print("The response of ResourcesAndPricingApi->network_fees_create_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->network_fees_create_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_fee_preview** | [**NetworkFeePreview**](NetworkFeePreview.md)|  |

### Return type

[**NetworkFeePreviewResponse**](NetworkFeePreviewResponse.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for create a network-fee quote. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_create**
> Resource resources_create(idempotency_key, resource_create)

Create a resource

Create one tenant resource idempotently. Requires a tenant API key with the `resources:write` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.resource import Resource
from x402api.models.resource_create import ResourceCreate
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
    api_instance = x402api.ResourcesAndPricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome.
    resource_create = x402api.ResourceCreate() # ResourceCreate |

    try:
        # Create a resource
        api_response = api_instance.resources_create(idempotency_key, resource_create)
        print("The response of ResourcesAndPricingApi->resources_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->resources_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
 **resource_create** | [**ResourceCreate**](ResourceCreate.md)|  |

### Return type

[**Resource**](Resource.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response for create a resource. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_create_version**
> ResourceVersion resources_create_version(idempotency_key, resource_id, resource_version_create)

Create a resource version

Create an immutable priced version of one tenant resource idempotently. Requires a tenant API key with the `resources:write` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.resource_version import ResourceVersion
from x402api.models.resource_version_create import ResourceVersionCreate
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
    api_instance = x402api.ResourcesAndPricingApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome.
    resource_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    resource_version_create = x402api.ResourceVersionCreate() # ResourceVersionCreate |

    try:
        # Create a resource version
        api_response = api_instance.resources_create_version(idempotency_key, resource_id, resource_version_create)
        print("The response of ResourcesAndPricingApi->resources_create_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->resources_create_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |
 **resource_id** | **UUID**|  |
 **resource_version_create** | [**ResourceVersionCreate**](ResourceVersionCreate.md)|  |

### Return type

[**ResourceVersion**](ResourceVersion.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response for create a resource version. |  * X-Request-ID -  <br>  |
**409** | The request failed. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_list**
> List[Resource] resources_list(cursor=cursor, page_size=page_size)

List resources

List tenant resources and their visible versions using opaque cursor pagination. Requires a tenant API key with the `resources:read` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.resource import Resource
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
    api_instance = x402api.ResourcesAndPricingApi(api_client)
    cursor = 'cursor_example' # str | Opaque pagination cursor from X-X402API-Next-Cursor or rel=next Link. (optional)
    page_size = 100 # int | Number of results in the bounded array page (default and maximum 100). (optional) (default to 100)

    try:
        # List resources
        api_response = api_instance.resources_list(cursor=cursor, page_size=page_size)
        print("The response of ResourcesAndPricingApi->resources_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->resources_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]
 **page_size** | **int**| Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100]

### Return type

[**List[Resource]**](Resource.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for list resources. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_list_versions**
> List[ResourceVersion] resources_list_versions(resource_id, cursor=cursor, page_size=page_size)

List resource versions

List immutable versions of one tenant resource using opaque cursor pagination. Requires a tenant API key with the `resources:read` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.resource_version import ResourceVersion
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
    api_instance = x402api.ResourcesAndPricingApi(api_client)
    resource_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    cursor = 'cursor_example' # str | Opaque pagination cursor from X-X402API-Next-Cursor or rel=next Link. (optional)
    page_size = 100 # int | Number of results in the bounded array page (default and maximum 100). (optional) (default to 100)

    try:
        # List resource versions
        api_response = api_instance.resources_list_versions(resource_id, cursor=cursor, page_size=page_size)
        print("The response of ResourcesAndPricingApi->resources_list_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->resources_list_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **UUID**|  |
 **cursor** | **str**| Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]
 **page_size** | **int**| Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100]

### Return type

[**List[ResourceVersion]**](ResourceVersion.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for list resource versions. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
