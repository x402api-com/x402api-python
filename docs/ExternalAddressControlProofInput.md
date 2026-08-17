# ExternalAddressControlProofInput

Reject extra or missing JSON keys instead of silently projecting them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**ExternalAddressProofInputMethodEnum**](ExternalAddressProofInputMethodEnum.md) |  |
**signature** | **str** |  | [optional]
**transaction_hash** | **str** |  | [optional]

## Example

```python
from x402api.models.external_address_control_proof_input import ExternalAddressControlProofInput

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAddressControlProofInput from a JSON string
external_address_control_proof_input_instance = ExternalAddressControlProofInput.from_json(json)
# print the JSON string representation of the object
print(ExternalAddressControlProofInput.to_json())

# convert the object into a dict
external_address_control_proof_input_dict = external_address_control_proof_input_instance.to_dict()
# create an instance of ExternalAddressControlProofInput from a dict
external_address_control_proof_input_from_dict = ExternalAddressControlProofInput.from_dict(external_address_control_proof_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
