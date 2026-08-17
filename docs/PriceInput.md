# PriceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  |
**wallet_version_id** | **UUID** |  |
**amount_atomic** | **str** |  |
**max_timeout_seconds** | **int** |  |

## Example

```python
from x402api.models.price_input import PriceInput

# TODO update the JSON string below
json = "{}"
# create an instance of PriceInput from a JSON string
price_input_instance = PriceInput.from_json(json)
# print the JSON string representation of the object
print(PriceInput.to_json())

# convert the object into a dict
price_input_dict = price_input_instance.to_dict()
# create an instance of PriceInput from a dict
price_input_from_dict = PriceInput.from_dict(price_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
