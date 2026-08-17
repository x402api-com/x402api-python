# NetworkFeePreviewPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  |
**listed_amount_atomic** | **str** |  |

## Example

```python
from x402api.models.network_fee_preview_price import NetworkFeePreviewPrice

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkFeePreviewPrice from a JSON string
network_fee_preview_price_instance = NetworkFeePreviewPrice.from_json(json)
# print the JSON string representation of the object
print(NetworkFeePreviewPrice.to_json())

# convert the object into a dict
network_fee_preview_price_dict = network_fee_preview_price_instance.to_dict()
# create an instance of NetworkFeePreviewPrice from a dict
network_fee_preview_price_from_dict = NetworkFeePreviewPrice.from_dict(network_fee_preview_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
