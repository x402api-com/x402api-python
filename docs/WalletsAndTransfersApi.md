# x402api.WalletsAndTransfersApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallets_retrieve_balance**](WalletsAndTransfersApi.md#wallets_retrieve_balance) | **GET** /v1/wallets/{id}/balances | Retrieve wallet balances


# **wallets_retrieve_balance**
> WalletBalanceResponse wallets_retrieve_balance(id, finality=finality)

Retrieve wallet balances

Retrieve finalized external-wallet balance observations at the requested finality. Requires a tenant API key with the `balances:read` scope.

### Example

* Bearer Authentication (tenantApiKey):

```python
import x402api
from x402api.models.wallet_balance_response import WalletBalanceResponse
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
    api_instance = x402api.WalletsAndTransfersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    finality = 'finalized' # str |  (optional) (default to 'finalized')

    try:
        # Retrieve wallet balances
        api_response = api_instance.wallets_retrieve_balance(id, finality=finality)
        print("The response of WalletsAndTransfersApi->wallets_retrieve_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsAndTransfersApi->wallets_retrieve_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  |
 **finality** | **str**|  | [optional] [default to &#39;finalized&#39;]

### Return type

[**WalletBalanceResponse**](WalletBalanceResponse.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for retrieve wallet balances. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
