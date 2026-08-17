# ResourceVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**version** | **int** |  | [readonly]
**method** | **str** |  | [readonly]
**path** | **str** |  | [readonly]
**description** | **str** |  | [readonly]
**mime_type** | **str** |  | [readonly]
**fulfillment_mode** | [**ResourceVersionFulfillmentModeEnum**](ResourceVersionFulfillmentModeEnum.md) |  | [readonly]
**fulfillment_config** | [**ResourceVersionFulfillmentConfig**](ResourceVersionFulfillmentConfig.md) |  |
**fee_mode** | [**ResourceFeeModeEnum**](ResourceFeeModeEnum.md) |  | [readonly]
**quote_currency** | [**ResourceQuoteCurrencyEnum**](ResourceQuoteCurrencyEnum.md) |  | [readonly]
**fee_allowance_cap_quote_micros** | **str** |  | [readonly]
**state** | [**ResourceVersionStateEnum**](ResourceVersionStateEnum.md) |  | [readonly]
**prices** | [**List[ResourcePrice]**](ResourcePrice.md) |  | [readonly]

## Example

```python
from x402api.models.resource_version import ResourceVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceVersion from a JSON string
resource_version_instance = ResourceVersion.from_json(json)
# print the JSON string representation of the object
print(ResourceVersion.to_json())

# convert the object into a dict
resource_version_dict = resource_version_instance.to_dict()
# create an instance of ResourceVersion from a dict
resource_version_from_dict = ResourceVersion.from_dict(resource_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
