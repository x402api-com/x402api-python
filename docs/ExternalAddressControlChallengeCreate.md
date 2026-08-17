# ExternalAddressControlChallengeCreate

Reject extra or missing JSON keys instead of silently projecting them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  |
**asset_id** | **str** |  |
**address** | **str** |  |
**proof_method** | [**ExternalAddressProofInputMethodEnum**](ExternalAddressProofInputMethodEnum.md) |  |

## Example

```python
from x402api.models.external_address_control_challenge_create import ExternalAddressControlChallengeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAddressControlChallengeCreate from a JSON string
external_address_control_challenge_create_instance = ExternalAddressControlChallengeCreate.from_json(json)
# print the JSON string representation of the object
print(ExternalAddressControlChallengeCreate.to_json())

# convert the object into a dict
external_address_control_challenge_create_dict = external_address_control_challenge_create_instance.to_dict()
# create an instance of ExternalAddressControlChallengeCreate from a dict
external_address_control_challenge_create_from_dict = ExternalAddressControlChallengeCreate.from_dict(external_address_control_challenge_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
