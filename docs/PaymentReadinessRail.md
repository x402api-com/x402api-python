# PaymentReadinessRail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [readonly]
**network** | **str** |  | [readonly]
**symbol** | **str** |  | [readonly]
**selected** | **bool** |  | [readonly]
**wallet_ready** | **bool** |  | [readonly]
**platform_available** | **bool** |  | [readonly]
**accepting_new_payments** | **bool** |  | [readonly]
**status** | **str** |  | [readonly]
**blockers** | [**List[PaymentReadinessBlocker]**](PaymentReadinessBlocker.md) |  | [readonly]
**tenant_challenges_enabled** | **bool** |  | [readonly]
**tenant_settlement_enabled** | **bool** |  | [readonly]
**network_assistance_enabled** | **bool** |  | [readonly]
**challenge_control_ready** | **bool** |  | [readonly]
**settlement_control_ready** | **bool** |  | [readonly]
**assets** | [**List[PaymentReadinessAsset]**](PaymentReadinessAsset.md) |  | [readonly]

## Example

```python
from x402api.models.payment_readiness_rail import PaymentReadinessRail

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReadinessRail from a JSON string
payment_readiness_rail_instance = PaymentReadinessRail.from_json(json)
# print the JSON string representation of the object
print(PaymentReadinessRail.to_json())

# convert the object into a dict
payment_readiness_rail_dict = payment_readiness_rail_instance.to_dict()
# create an instance of PaymentReadinessRail from a dict
payment_readiness_rail_from_dict = PaymentReadinessRail.from_dict(payment_readiness_rail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
