# ResourceVersionCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_mode** | [**FeePolicyModeInputEnum**](FeePolicyModeInputEnum.md) |  | [optional]
**quote_currency** | [**FeePolicyQuoteCurrencyInputEnum**](FeePolicyQuoteCurrencyInputEnum.md) |  | [optional]
**fee_allowance_cap_quote_micros** | **str** |  | [optional] [default to '0']
**expected_latest_version** | **int** |  |
**method** | [**HTTPMethodEnum**](HTTPMethodEnum.md) |  |
**path** | **str** |  |
**description** | **str** |  |
**mime_type** | **str** |  | [optional] [default to 'application/json']
**fulfillment_mode** | [**ResourceInputFulfillmentModeEnum**](ResourceInputFulfillmentModeEnum.md) |  |
**fulfillment_config** | [**ResourceCreateFulfillmentConfig**](ResourceCreateFulfillmentConfig.md) |  | [optional]
**prices** | [**List[PriceInput]**](PriceInput.md) |  |

## Example

```python
from x402api.models.resource_version_create import ResourceVersionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceVersionCreate from a JSON string
resource_version_create_instance = ResourceVersionCreate.from_json(json)
# print the JSON string representation of the object
print(ResourceVersionCreate.to_json())

# convert the object into a dict
resource_version_create_dict = resource_version_create_instance.to_dict()
# create an instance of ResourceVersionCreate from a dict
resource_version_create_from_dict = ResourceVersionCreate.from_dict(resource_version_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
