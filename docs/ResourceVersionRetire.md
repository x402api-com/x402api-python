# ResourceVersionRetire


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_version** | **int** |  |
**expected_state** | [**ResourceVersionRetireExpectedStateEnum**](ResourceVersionRetireExpectedStateEnum.md) |  |

## Example

```python
from x402api.models.resource_version_retire import ResourceVersionRetire

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceVersionRetire from a JSON string
resource_version_retire_instance = ResourceVersionRetire.from_json(json)
# print the JSON string representation of the object
print(ResourceVersionRetire.to_json())

# convert the object into a dict
resource_version_retire_dict = resource_version_retire_instance.to_dict()
# create an instance of ResourceVersionRetire from a dict
resource_version_retire_from_dict = ResourceVersionRetire.from_dict(resource_version_retire_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
