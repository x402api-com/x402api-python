# ExternalReceivingAddressCreate

Reject extra or missing JSON keys instead of silently projecting them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  |
**challenge_id** | **UUID** |  |
**proof** | [**ExternalAddressControlProofInput**](ExternalAddressControlProofInput.md) |  |

## Example

```python
from x402api.models.external_receiving_address_create import ExternalReceivingAddressCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalReceivingAddressCreate from a JSON string
external_receiving_address_create_instance = ExternalReceivingAddressCreate.from_json(json)
# print the JSON string representation of the object
print(ExternalReceivingAddressCreate.to_json())

# convert the object into a dict
external_receiving_address_create_dict = external_receiving_address_create_instance.to_dict()
# create an instance of ExternalReceivingAddressCreate from a dict
external_receiving_address_create_from_dict = ExternalReceivingAddressCreate.from_dict(external_receiving_address_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
