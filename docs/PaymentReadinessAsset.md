# PaymentReadinessAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [readonly]
**display_name** | **str** |  | [readonly]
**contract_address** | **str** |  | [readonly]
**issuer_native** | **bool** |  | [readonly]
**registry_enabled** | **bool** |  | [readonly]
**tenant_enabled** | **bool** |  | [readonly]
**operator_assistance_enabled** | **bool** |  | [readonly]
**base_readiness_blockers** | **List[str]** |  | [readonly]
**challenge_control_ready** | **bool** |  | [readonly]
**settlement_control_ready** | **bool** |  | [readonly]

## Example

```python
from x402api.models.payment_readiness_asset import PaymentReadinessAsset

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReadinessAsset from a JSON string
payment_readiness_asset_instance = PaymentReadinessAsset.from_json(json)
# print the JSON string representation of the object
print(PaymentReadinessAsset.to_json())

# convert the object into a dict
payment_readiness_asset_dict = payment_readiness_asset_instance.to_dict()
# create an instance of PaymentReadinessAsset from a dict
payment_readiness_asset_from_dict = PaymentReadinessAsset.from_dict(payment_readiness_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
