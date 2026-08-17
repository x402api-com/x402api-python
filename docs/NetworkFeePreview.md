# NetworkFeePreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_mode** | [**FeePolicyModeInputEnum**](FeePolicyModeInputEnum.md) |  | [optional]
**quote_currency** | [**FeePolicyQuoteCurrencyInputEnum**](FeePolicyQuoteCurrencyInputEnum.md) |  | [optional]
**fee_allowance_cap_quote_micros** | **str** |  | [optional] [default to '0']
**prices** | [**List[NetworkFeePreviewPrice]**](NetworkFeePreviewPrice.md) |  |

## Example

```python
from x402api.models.network_fee_preview import NetworkFeePreview

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkFeePreview from a JSON string
network_fee_preview_instance = NetworkFeePreview.from_json(json)
# print the JSON string representation of the object
print(NetworkFeePreview.to_json())

# convert the object into a dict
network_fee_preview_dict = network_fee_preview_instance.to_dict()
# create an instance of NetworkFeePreview from a dict
network_fee_preview_from_dict = NetworkFeePreview.from_dict(network_fee_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
