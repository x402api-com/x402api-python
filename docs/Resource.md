# Resource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**public_payment_id** | **str** |  | [readonly]
**key** | **str** |  | [readonly]
**name** | **str** |  | [readonly]
**active_version** | [**ResourceVersion**](ResourceVersion.md) |  | [readonly]
**versions** | [**List[ResourceVersion]**](ResourceVersion.md) |  | [readonly]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]

## Example

```python
from x402api.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print(Resource.to_json())

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_from_dict = Resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
