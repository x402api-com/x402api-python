# PaymentReadiness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**PaymentReadinessStateEnum**](PaymentReadinessStateEnum.md) |  | [readonly]
**accepting_new_payments** | **bool** |  | [readonly]
**paused_by_tenant** | **bool** |  | [readonly]
**platform_available** | **bool** |  | [readonly]
**health_valid_until** | **datetime** |  | [readonly]
**observed_at** | **datetime** |  | [readonly]
**tenant_status** | **str** |  | [readonly]
**tenant_accepting_new_challenges** | **bool** |  | [readonly]
**global_challenges_enabled** | **bool** |  | [readonly]
**global_settlement_enabled** | **bool** |  | [readonly]
**control_plane_ready_for_new_challenges** | **bool** |  | [readonly]
**control_plane_ready_for_settlement** | **bool** |  | [readonly]
**external_onboarding** | **object** |  | [readonly]
**rails** | [**List[PaymentReadinessRail]**](PaymentReadinessRail.md) |  | [readonly]
**canonical_rails** | [**List[CanonicalPaymentReadinessRail]**](CanonicalPaymentReadinessRail.md) |  | [readonly]

## Example

```python
from x402api.models.payment_readiness import PaymentReadiness

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReadiness from a JSON string
payment_readiness_instance = PaymentReadiness.from_json(json)
# print the JSON string representation of the object
print(PaymentReadiness.to_json())

# convert the object into a dict
payment_readiness_dict = payment_readiness_instance.to_dict()
# create an instance of PaymentReadiness from a dict
payment_readiness_from_dict = PaymentReadiness.from_dict(payment_readiness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
