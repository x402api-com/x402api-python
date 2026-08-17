# ExternalAddressControlCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**networks** | [**List[ExternalAddressControlCapability]**](ExternalAddressControlCapability.md) |  | [readonly]

## Example

```python
from x402api.models.external_address_control_capabilities import ExternalAddressControlCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAddressControlCapabilities from a JSON string
external_address_control_capabilities_instance = ExternalAddressControlCapabilities.from_json(json)
# print the JSON string representation of the object
print(ExternalAddressControlCapabilities.to_json())

# convert the object into a dict
external_address_control_capabilities_dict = external_address_control_capabilities_instance.to_dict()
# create an instance of ExternalAddressControlCapabilities from a dict
external_address_control_capabilities_from_dict = ExternalAddressControlCapabilities.from_dict(external_address_control_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
