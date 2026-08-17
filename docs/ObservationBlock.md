# ObservationBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  |
**hash** | **str** |  |
**finality** | **str** |  |

## Example

```python
from x402api.models.observation_block import ObservationBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationBlock from a JSON string
observation_block_instance = ObservationBlock.from_json(json)
# print the JSON string representation of the object
print(ObservationBlock.to_json())

# convert the object into a dict
observation_block_dict = observation_block_instance.to_dict()
# create an instance of ObservationBlock from a dict
observation_block_from_dict = ObservationBlock.from_dict(observation_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
