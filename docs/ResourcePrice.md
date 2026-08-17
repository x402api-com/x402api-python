# ResourcePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [readonly]
**network** | **str** |  | [readonly]
**contract_address** | **str** |  | [readonly]
**display_name** | **str** |  | [readonly]
**symbol** | **str** |  | [readonly]
**decimals** | **int** |  | [readonly]
**wallet_id** | **UUID** |  | [readonly]
**wallet_version_id** | **UUID** |  | [readonly]
**recipient** | **str** |  | [readonly]
**amount_atomic** | **str** |  | [readonly]
**listed_amount_atomic** | **str** |  | [readonly]
**max_timeout_seconds** | **int** |  | [readonly]

## Example

```python
from x402api.models.resource_price import ResourcePrice

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePrice from a JSON string
resource_price_instance = ResourcePrice.from_json(json)
# print the JSON string representation of the object
print(ResourcePrice.to_json())

# convert the object into a dict
resource_price_dict = resource_price_instance.to_dict()
# create an instance of ResourcePrice from a dict
resource_price_from_dict = ResourcePrice.from_dict(resource_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
