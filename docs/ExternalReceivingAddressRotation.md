# ExternalReceivingAddressRotation

Reject extra or missing JSON keys instead of silently projecting them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_id** | **UUID** |  |
**proof** | [**ExternalAddressControlProofInput**](ExternalAddressControlProofInput.md) |  |
**reason** | **str** |  |

## Example

```python
from x402api.models.external_receiving_address_rotation import ExternalReceivingAddressRotation

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalReceivingAddressRotation from a JSON string
external_receiving_address_rotation_instance = ExternalReceivingAddressRotation.from_json(json)
# print the JSON string representation of the object
print(ExternalReceivingAddressRotation.to_json())

# convert the object into a dict
external_receiving_address_rotation_dict = external_receiving_address_rotation_instance.to_dict()
# create an instance of ExternalReceivingAddressRotation from a dict
external_receiving_address_rotation_from_dict = ExternalReceivingAddressRotation.from_dict(external_receiving_address_rotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
