# x402api.FacilitatorDiscoveryApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facilitator_get_supported**](FacilitatorDiscoveryApi.md#facilitator_get_supported) | **GET** /v1/facilitator/supported | Get supported facilitator profiles


# **facilitator_get_supported**
> SupportedResponse facilitator_get_supported()

Get supported facilitator profiles

Return the currently approved public x402 facilitator profiles.

### Example


```python
import x402api
from x402api.models.supported_response import SupportedResponse
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
    api_instance = x402api.FacilitatorDiscoveryApi(api_client)

    try:
        # Get supported facilitator profiles
        api_response = api_instance.facilitator_get_supported()
        print("The response of FacilitatorDiscoveryApi->facilitator_get_supported:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacilitatorDiscoveryApi->facilitator_get_supported: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SupportedResponse**](SupportedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response for get supported facilitator profiles. |  * X-Request-ID -  <br>  |
**0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
