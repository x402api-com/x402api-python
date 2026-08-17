# x402api.ResourcesAndPricingApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_network_fee_quotes_create**](ResourcesAndPricingApi.md#v1_network_fee_quotes_create) | **POST** /v1/network-fee-quotes |
[**v1_resources_create**](ResourcesAndPricingApi.md#v1_resources_create) | **POST** /v1/resources |
[**v1_resources_list**](ResourcesAndPricingApi.md#v1_resources_list) | **GET** /v1/resources |
[**v1_resources_versions_activate_create**](ResourcesAndPricingApi.md#v1_resources_versions_activate_create) | **POST** /v1/resources/{resource_id}/versions/{version_id}/activate |
[**v1_resources_versions_create**](ResourcesAndPricingApi.md#v1_resources_versions_create) | **POST** /v1/resources/{resource_id}/versions |
[**v1_resources_versions_list**](ResourcesAndPricingApi.md#v1_resources_versions_list) | **GET** /v1/resources/{resource_id}/versions |
[**v1_resources_versions_retire_create**](ResourcesAndPricingApi.md#v1_resources_versions_retire_create) | **POST** /v1/resources/{resource_id}/versions/{version_id}/retire |


# **v1_network_fee_quotes_create**
> NetworkFeePreviewResponse v1_network_fee_quotes_create(network_fee_preview)

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
        api_response = api_instance.v1_network_fee_quotes_create(network_fee_preview)
        print("The response of ResourcesAndPricingApi->v1_network_fee_quotes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->v1_network_fee_quotes_create: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_resources_create**
> Resource v1_resources_create(idempotency_key, resource_create)

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
    idempotency_key = 'idempotency_key_example' # str | Unique mutation key; replaying different content returns HTTP 409.
    resource_create = x402api.ResourceCreate() # ResourceCreate |

    try:
        api_response = api_instance.v1_resources_create(idempotency_key, resource_create)
        print("The response of ResourcesAndPricingApi->v1_resources_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->v1_resources_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique mutation key; replaying different content returns HTTP 409. |
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_resources_list**
> List[Resource] v1_resources_list(cursor=cursor, page_size=page_size)

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
        api_response = api_instance.v1_resources_list(cursor=cursor, page_size=page_size)
        print("The response of ResourcesAndPricingApi->v1_resources_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->v1_resources_list: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_resources_versions_activate_create**
> ResourceVersion v1_resources_versions_activate_create(idempotency_key, resource_id, version_id, resource_version_activate)

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.resource_version import ResourceVersion
from x402api.models.resource_version_activate import ResourceVersionActivate
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
    idempotency_key = 'idempotency_key_example' # str | Unique mutation key; replaying different content returns HTTP 409.
    resource_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    version_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    resource_version_activate = x402api.ResourceVersionActivate() # ResourceVersionActivate |

    try:
        api_response = api_instance.v1_resources_versions_activate_create(idempotency_key, resource_id, version_id, resource_version_activate)
        print("The response of ResourcesAndPricingApi->v1_resources_versions_activate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->v1_resources_versions_activate_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique mutation key; replaying different content returns HTTP 409. |
 **resource_id** | **UUID**|  |
 **version_id** | **UUID**|  |
 **resource_version_activate** | [**ResourceVersionActivate**](ResourceVersionActivate.md)|  |

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
**200** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_resources_versions_create**
> ResourceVersion v1_resources_versions_create(idempotency_key, resource_id, resource_version_create)

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
    idempotency_key = 'idempotency_key_example' # str | Unique mutation key; replaying different content returns HTTP 409.
    resource_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    resource_version_create = x402api.ResourceVersionCreate() # ResourceVersionCreate |

    try:
        api_response = api_instance.v1_resources_versions_create(idempotency_key, resource_id, resource_version_create)
        print("The response of ResourcesAndPricingApi->v1_resources_versions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->v1_resources_versions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique mutation key; replaying different content returns HTTP 409. |
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
**201** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_resources_versions_list**
> List[ResourceVersion] v1_resources_versions_list(resource_id, cursor=cursor, page_size=page_size)

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
        api_response = api_instance.v1_resources_versions_list(resource_id, cursor=cursor, page_size=page_size)
        print("The response of ResourcesAndPricingApi->v1_resources_versions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->v1_resources_versions_list: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_resources_versions_retire_create**
> ResourceVersion v1_resources_versions_retire_create(idempotency_key, resource_id, version_id, resource_version_retire)

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.resource_version import ResourceVersion
from x402api.models.resource_version_retire import ResourceVersionRetire
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
    idempotency_key = 'idempotency_key_example' # str | Unique mutation key; replaying different content returns HTTP 409.
    resource_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    version_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    resource_version_retire = x402api.ResourceVersionRetire() # ResourceVersionRetire |

    try:
        api_response = api_instance.v1_resources_versions_retire_create(idempotency_key, resource_id, version_id, resource_version_retire)
        print("The response of ResourcesAndPricingApi->v1_resources_versions_retire_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesAndPricingApi->v1_resources_versions_retire_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique mutation key; replaying different content returns HTTP 409. |
 **resource_id** | **UUID**|  |
 **version_id** | **UUID**|  |
 **resource_version_retire** | [**ResourceVersionRetire**](ResourceVersionRetire.md)|  |

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
**200** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
