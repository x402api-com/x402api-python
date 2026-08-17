# SupportedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kinds** | [**List[SupportedKind]**](SupportedKind.md) |  |
**extensions** | **List[str]** |  |
**signers** | **Dict[str, List[str]]** |  |

## Example

```python
from x402api.models.supported_response import SupportedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedResponse from a JSON string
supported_response_instance = SupportedResponse.from_json(json)
# print the JSON string representation of the object
print(SupportedResponse.to_json())

# convert the object into a dict
supported_response_dict = supported_response_instance.to_dict()
# create an instance of SupportedResponse from a dict
supported_response_from_dict = SupportedResponse.from_dict(supported_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
