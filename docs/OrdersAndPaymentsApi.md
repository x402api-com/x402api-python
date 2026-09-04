# x402api.OrdersAndPaymentsApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_list**](OrdersAndPaymentsApi.md#orders_list) | **GET** /v1/orders | List orders
[**orders_retrieve**](OrdersAndPaymentsApi.md#orders_retrieve) | **GET** /v1/orders/{id} | Retrieve an order
[**payments_list**](OrdersAndPaymentsApi.md#payments_list) | **GET** /v1/payments | List payments
[**payments_list_observations**](OrdersAndPaymentsApi.md#payments_list_observations) | **GET** /v1/payments/{id}/observations | List payment observations
[**payments_retrieve**](OrdersAndPaymentsApi.md#payments_retrieve) | **GET** /v1/payments/{id} | Retrieve a payment
[**payments_retrieve_receipt**](OrdersAndPaymentsApi.md#payments_retrieve_receipt) | **GET** /v1/payments/{id}/receipt | Retrieve a payment receipt
[**receipt_verification_keys_retrieve**](OrdersAndPaymentsApi.md#receipt_verification_keys_retrieve) | **GET** /v1/payment-receipt-verification-keys | Retrieve receipt verification keys


# **orders_list**
> List[Order] orders_list(cursor=cursor, page_size=page_size)

List orders

List tenant-visible orders using opaque cursor pagination. Requires a tenant API key with the `orders:read` scope.

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
        # List orders
        api_response = api_instance.orders_list(cursor=cursor, page_size=page_size)
        print("The response of OrdersAndPaymentsApi->orders_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->orders_list: %s\n" % e)
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
**200** | Successful response for list orders. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_retrieve**
> Order orders_retrieve(id)

Retrieve an order

Retrieve one tenant-visible order by its canonical identifier. Requires a tenant API key with the `orders:read` scope.

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
        # Retrieve an order
        api_response = api_instance.orders_retrieve(id)
        print("The response of OrdersAndPaymentsApi->orders_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->orders_retrieve: %s\n" % e)
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
**200** | Successful response for retrieve an order. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_list**
> List[SettlementJob] payments_list(cursor=cursor, page_size=page_size)

List payments

List tenant-visible payments using opaque cursor pagination. Requires a tenant API key with the `payments:read` scope.

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
        # List payments
        api_response = api_instance.payments_list(cursor=cursor, page_size=page_size)
        print("The response of OrdersAndPaymentsApi->payments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->payments_list: %s\n" % e)
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
**200** | Successful response for list payments. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_list_observations**
> List[SettlementChainObservation] payments_list_observations(id, cursor=cursor, page_size=page_size)

List payment observations

List finalized and pending chain observations for one tenant-visible payment. Requires a tenant API key with the `payments:read` scope.

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
        # List payment observations
        api_response = api_instance.payments_list_observations(id, cursor=cursor, page_size=page_size)
        print("The response of OrdersAndPaymentsApi->payments_list_observations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->payments_list_observations: %s\n" % e)
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
**200** | Successful response for list payment observations. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_retrieve**
> SettlementJob payments_retrieve(id)

Retrieve a payment

Retrieve one tenant-visible payment by its canonical identifier. Requires a tenant API key with the `payments:read` scope.

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
        # Retrieve a payment
        api_response = api_instance.payments_retrieve(id)
        print("The response of OrdersAndPaymentsApi->payments_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->payments_retrieve: %s\n" % e)
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
**200** | Successful response for retrieve a payment. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_retrieve_receipt**
> Union[PaymentReceipt, PaymentReceiptStatus] payments_retrieve_receipt(id)

Retrieve a payment receipt

Retrieve the signed receipt projection for one tenant-visible payment. HTTP 202 returns confirmation and finality state while the signed receipt is pending. Requires a tenant API key with the `payments:read` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.payment_receipt import PaymentReceipt
from x402api.models.payment_receipt_status import PaymentReceiptStatus
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
        # Retrieve a payment receipt
        api_response = api_instance.payments_retrieve_receipt(id)
        print("The response of OrdersAndPaymentsApi->payments_retrieve_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->payments_retrieve_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  |

### Return type

[**PaymentReceipt**](PaymentReceipt.md) or [**PaymentReceiptStatus**](PaymentReceiptStatus.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for retrieve a payment receipt. |  * X-Request-ID -  <br>  |
**202** | Payment status while the signed finalized receipt is pending. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |
**409** | The request failed. |  * X-Request-ID -  <br>  |
**503** | The request failed. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receipt_verification_keys_retrieve**
> ReceiptVerificationKeyHistory receipt_verification_keys_retrieve()

Retrieve receipt verification keys

Return the public receipt verification-key history for out-of-band-pinned verification. Public endpoint; no API key or scope is required.

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
        # Retrieve receipt verification keys
        api_response = api_instance.receipt_verification_keys_retrieve()
        print("The response of OrdersAndPaymentsApi->receipt_verification_keys_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersAndPaymentsApi->receipt_verification_keys_retrieve: %s\n" % e)
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
**200** | Successful response for retrieve receipt verification keys. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
