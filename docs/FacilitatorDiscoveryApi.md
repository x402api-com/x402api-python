# x402api.FacilitatorDiscoveryApi

All URIs are relative to *https://api.x402api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facilitator_supported_retrieve**](FacilitatorDiscoveryApi.md#facilitator_supported_retrieve) | **GET** /v1/facilitator/supported |


# **facilitator_supported_retrieve**
> SupportedResponse facilitator_supported_retrieve()

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
        api_response = api_instance.facilitator_supported_retrieve()
        print("The response of FacilitatorDiscoveryApi->facilitator_supported_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FacilitatorDiscoveryApi->facilitator_supported_retrieve: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
