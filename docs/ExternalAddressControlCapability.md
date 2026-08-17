# ExternalAddressControlCapability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [readonly]
**proof_methods** | [**List[ExternalAddressProofInputMethodEnum]**](ExternalAddressProofInputMethodEnum.md) |  | [readonly]

## Example

```python
from x402api.models.external_address_control_capability import ExternalAddressControlCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAddressControlCapability from a JSON string
external_address_control_capability_instance = ExternalAddressControlCapability.from_json(json)
# print the JSON string representation of the object
print(ExternalAddressControlCapability.to_json())

# convert the object into a dict
external_address_control_capability_dict = external_address_control_capability_instance.to_dict()
# create an instance of ExternalAddressControlCapability from a dict
external_address_control_capability_from_dict = ExternalAddressControlCapability.from_dict(external_address_control_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
