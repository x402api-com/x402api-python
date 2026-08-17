# x402api.OrdersAndPaymentsApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_orders_list**](OrdersAndPaymentsApi.md#v1_orders_list) | **GET** /v1/orders |
[**v1_orders_retrieve**](OrdersAndPaymentsApi.md#v1_orders_retrieve) | **GET** /v1/orders/{id} |
[**v1_payment_receipt_verification_keys_retrieve**](OrdersAndPaymentsApi.md#v1_payment_receipt_verification_keys_retrieve) | **GET** /v1/payment-receipt-verification-keys |
[**v1_payments_list**](OrdersAndPaymentsApi.md#v1_payments_list) | **GET** /v1/payments |
[**v1_payments_observations_list**](OrdersAndPaymentsApi.md#v1_payments_observations_list) | **GET** /v1/payments/{id}/observations |
[**v1_payments_receipt_retrieve**](OrdersAndPaymentsApi.md#v1_payments_receipt_retrieve) | **GET** /v1/payments/{id}/receipt |
[**v1_payments_retrieve**](OrdersAndPaymentsApi.md#v1_payments_retrieve) | **GET** /v1/payments/{id} |


# **v1_orders_list**
> List[Order] v1_orders_list(cursor=cursor, page_size=page_size)

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.order import Order
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
    api_instance = x402api.OrdersAndPaymentsApi(api_client)
    cursor = 'cursor_example' # str | Opaque pagination cursor from X-X402API-Next-Cursor or rel=next Link. (optional)
    page_size = 100 # int | Number of results in the bounded array page (default and maximum 100). (optional) (default to 100)

    try:
        api_response = api_instance.v1_orders_list(cursor=cursor, page_size=page_size)
        print("The response of OrdersAndPaymentsApi->v1_orders_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->v1_orders_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]
 **page_size** | **int**| Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100]

### Return type

[**List[Order]**](Order.md)

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

# **v1_orders_retrieve**
> Order v1_orders_retrieve(id)

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.order import Order
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
    api_instance = x402api.OrdersAndPaymentsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.v1_orders_retrieve(id)
        print("The response of OrdersAndPaymentsApi->v1_orders_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->v1_orders_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  |

### Return type

[**Order**](Order.md)

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

# **v1_payment_receipt_verification_keys_retrieve**
> ReceiptVerificationKeyHistory v1_payment_receipt_verification_keys_retrieve()

Public key history; authenticity still requires an out-of-band pin.

### Example


```python
import x402api
from x402api.models.receipt_verification_key_history import ReceiptVerificationKeyHistory
from x402api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.x402api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = x402api.Configuration(
    host = "https://api.x402api.com"
)


# Enter a context with an instance of the API client
with x402api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = x402api.OrdersAndPaymentsApi(api_client)

    try:
        api_response = api_instance.v1_payment_receipt_verification_keys_retrieve()
        print("The response of OrdersAndPaymentsApi->v1_payment_receipt_verification_keys_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->v1_payment_receipt_verification_keys_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReceiptVerificationKeyHistory**](ReceiptVerificationKeyHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_payments_list**
> List[SettlementJob] v1_payments_list(cursor=cursor, page_size=page_size)

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.settlement_job import SettlementJob
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
    api_instance = x402api.OrdersAndPaymentsApi(api_client)
    cursor = 'cursor_example' # str | Opaque pagination cursor from X-X402API-Next-Cursor or rel=next Link. (optional)
    page_size = 100 # int | Number of results in the bounded array page (default and maximum 100). (optional) (default to 100)

    try:
        api_response = api_instance.v1_payments_list(cursor=cursor, page_size=page_size)
        print("The response of OrdersAndPaymentsApi->v1_payments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->v1_payments_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]
 **page_size** | **int**| Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100]

### Return type

[**List[SettlementJob]**](SettlementJob.md)

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

# **v1_payments_observations_list**
> List[SettlementChainObservation] v1_payments_observations_list(id, cursor=cursor, page_size=page_size)

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.settlement_chain_observation import SettlementChainObservation
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
    api_instance = x402api.OrdersAndPaymentsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    cursor = 'cursor_example' # str | Opaque pagination cursor from X-X402API-Next-Cursor or rel=next Link. (optional)
    page_size = 100 # int | Number of results in the bounded array page (default and maximum 100). (optional) (default to 100)

    try:
        api_response = api_instance.v1_payments_observations_list(id, cursor=cursor, page_size=page_size)
        print("The response of OrdersAndPaymentsApi->v1_payments_observations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->v1_payments_observations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  |
 **cursor** | **str**| Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]
 **page_size** | **int**| Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100]

### Return type

[**List[SettlementChainObservation]**](SettlementChainObservation.md)

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

# **v1_payments_receipt_retrieve**
> PaymentReceipt v1_payments_receipt_retrieve(id)

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.payment_receipt import PaymentReceipt
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
    api_instance = x402api.OrdersAndPaymentsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.v1_payments_receipt_retrieve(id)
        print("The response of OrdersAndPaymentsApi->v1_payments_receipt_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->v1_payments_receipt_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  |

### Return type

[**PaymentReceipt**](PaymentReceipt.md)

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

# **v1_payments_retrieve**
> SettlementJob v1_payments_retrieve(id)

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.settlement_job import SettlementJob
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
    api_instance = x402api.OrdersAndPaymentsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.v1_payments_retrieve(id)
        print("The response of OrdersAndPaymentsApi->v1_payments_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->v1_payments_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  |

### Return type

[**SettlementJob**](SettlementJob.md)

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
