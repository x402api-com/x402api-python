# ExternalReceivingAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**wallet_id** | **UUID** |  | [readonly]
**wallet_version_id** | **UUID** |  | [readonly]
**label** | **str** |  | [readonly]
**network** | **str** |  | [readonly]
**asset_id** | **str** |  | [readonly]
**address** | **str** |  | [readonly]
**status** | **str** |  | [readonly]
**proof_method** | [**ExternalAddressProofInputMethodEnum**](ExternalAddressProofInputMethodEnum.md) |  | [readonly]
**proof_verified_at** | **datetime** |  | [readonly]
**readiness_state** | **str** |  | [readonly]
**readiness_usable** | **bool** |  | [readonly]
**readiness_refresh_eligible** | **bool** |  | [readonly]
**readiness_status** | [**ReadinessStatusEnum**](ReadinessStatusEnum.md) |  | [readonly]
**activation_eligible** | **bool** |  | [readonly]
**activation_eligible_at** | **datetime** |  | [readonly]
**verified_at** | **datetime** |  | [readonly]
**expires_at** | **datetime** |  | [readonly]
**activated_at** | **datetime** |  | [readonly]
**observed_balance_atomic** | **str** |  | [readonly]
**created_at** | **datetime** |  | [readonly]

## Example

```python
from x402api.models.external_receiving_address import ExternalReceivingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalReceivingAddress from a JSON string
external_receiving_address_instance = ExternalReceivingAddress.from_json(json)
# print the JSON string representation of the object
print(ExternalReceivingAddress.to_json())

# convert the object into a dict
external_receiving_address_dict = external_receiving_address_instance.to_dict()
# create an instance of ExternalReceivingAddress from a dict
external_receiving_address_from_dict = ExternalReceivingAddress.from_dict(external_receiving_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
