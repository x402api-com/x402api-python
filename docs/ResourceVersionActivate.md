# ResourceVersionActivate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_target_version** | **int** |  |
**expected_active_version_id** | **UUID** |  |

## Example

```python
from x402api.models.resource_version_activate import ResourceVersionActivate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceVersionActivate from a JSON string
resource_version_activate_instance = ResourceVersionActivate.from_json(json)
# print the JSON string representation of the object
print(ResourceVersionActivate.to_json())

# convert the object into a dict
resource_version_activate_dict = resource_version_activate_instance.to_dict()
# create an instance of ResourceVersionActivate from a dict
resource_version_activate_from_dict = ResourceVersionActivate.from_dict(resource_version_activate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
