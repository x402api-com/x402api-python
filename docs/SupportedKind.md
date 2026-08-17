# SupportedKind


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x402_version** | **int** |  |
**scheme** | **str** |  |
**network** | **str** |  |
**extra** | **object** |  | [optional]

## Example

```python
from x402api.models.supported_kind import SupportedKind

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedKind from a JSON string
supported_kind_instance = SupportedKind.from_json(json)
# print the JSON string representation of the object
print(SupportedKind.to_json())

# convert the object into a dict
supported_kind_dict = supported_kind_instance.to_dict()
# create an instance of SupportedKind from a dict
supported_kind_from_dict = SupportedKind.from_dict(supported_kind_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
