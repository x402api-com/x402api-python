# NetworkFeePreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_policy** | [**PublicFeePolicyDocument**](PublicFeePolicyDocument.md) |  |
**alternatives** | [**List[PublicNetworkFeeAlternative]**](PublicNetworkFeeAlternative.md) |  |
**fee_quote_digest** | **str** |  |

## Example

```python
from x402api.models.network_fee_preview_response import NetworkFeePreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkFeePreviewResponse from a JSON string
network_fee_preview_response_instance = NetworkFeePreviewResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkFeePreviewResponse.to_json())

# convert the object into a dict
network_fee_preview_response_dict = network_fee_preview_response_instance.to_dict()
# create an instance of NetworkFeePreviewResponse from a dict
network_fee_preview_response_from_dict = NetworkFeePreviewResponse.from_dict(network_fee_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
