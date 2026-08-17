# DynamicChargePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  |
**amount_atomic** | **str** |  |

## Example

```python
from x402api.models.dynamic_charge_price import DynamicChargePrice

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicChargePrice from a JSON string
dynamic_charge_price_instance = DynamicChargePrice.from_json(json)
# print the JSON string representation of the object
print(DynamicChargePrice.to_json())

# convert the object into a dict
dynamic_charge_price_dict = dynamic_charge_price_instance.to_dict()
# create an instance of DynamicChargePrice from a dict
dynamic_charge_price_from_dict = DynamicChargePrice.from_dict(dynamic_charge_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
