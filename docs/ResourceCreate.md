# ResourceCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_mode** | [**FeePolicyModeInputEnum**](FeePolicyModeInputEnum.md) |  | [optional]
**quote_currency** | [**FeePolicyQuoteCurrencyInputEnum**](FeePolicyQuoteCurrencyInputEnum.md) |  | [optional]
**fee_allowance_cap_quote_micros** | **str** |  | [optional] [default to '0']
**key** | **str** |  |
**name** | **str** |  |
**method** | [**HTTPMethodEnum**](HTTPMethodEnum.md) |  |
**path** | **str** |  |
**description** | **str** |  |
**mime_type** | **str** |  | [optional] [default to 'application/json']
**fulfillment_mode** | [**ResourceInputFulfillmentModeEnum**](ResourceInputFulfillmentModeEnum.md) |  |
**fulfillment_config** | [**ResourceCreateFulfillmentConfig**](ResourceCreateFulfillmentConfig.md) |  | [optional]
**prices** | [**List[PriceInput]**](PriceInput.md) |  |

## Example

```python
from x402api.models.resource_create import ResourceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCreate from a JSON string
resource_create_instance = ResourceCreate.from_json(json)
# print the JSON string representation of the object
print(ResourceCreate.to_json())

# convert the object into a dict
resource_create_dict = resource_create_instance.to_dict()
# create an instance of ResourceCreate from a dict
resource_create_from_dict = ResourceCreate.from_dict(resource_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
