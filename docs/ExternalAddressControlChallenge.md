# ExternalAddressControlChallenge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**network** | **str** |  | [readonly]
**asset_id** | **str** |  | [readonly]
**address_display** | **str** |  | [readonly]
**proof_method** | [**ExternalAddressProofMethodEnum**](ExternalAddressProofMethodEnum.md) |  | [readonly]
**message** | **str** |  | [readonly]
**challenge_digest** | **str** |  | [readonly]
**canary_instructions** | **object** |  | [readonly]
**expires_at** | **datetime** |  | [readonly]
**consumed_at** | **datetime** |  | [readonly]
**created_at** | **datetime** |  | [readonly]

## Example

```python
from x402api.models.external_address_control_challenge import ExternalAddressControlChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAddressControlChallenge from a JSON string
external_address_control_challenge_instance = ExternalAddressControlChallenge.from_json(json)
# print the JSON string representation of the object
print(ExternalAddressControlChallenge.to_json())

# convert the object into a dict
external_address_control_challenge_dict = external_address_control_challenge_instance.to_dict()
# create an instance of ExternalAddressControlChallenge from a dict
external_address_control_challenge_from_dict = ExternalAddressControlChallenge.from_dict(external_address_control_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
