# CanonicalPaymentReadinessRail


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
**status** | [**PaymentReadinessRailStatusEnum**](PaymentReadinessRailStatusEnum.md) |  | [readonly]
**blockers** | [**List[PaymentReadinessBlocker]**](PaymentReadinessBlocker.md) |  | [readonly]

## Example

```python
from x402api.models.canonical_payment_readiness_rail import CanonicalPaymentReadinessRail

# TODO update the JSON string below
json = "{}"
# create an instance of CanonicalPaymentReadinessRail from a JSON string
canonical_payment_readiness_rail_instance = CanonicalPaymentReadinessRail.from_json(json)
# print the JSON string representation of the object
print(CanonicalPaymentReadinessRail.to_json())

# convert the object into a dict
canonical_payment_readiness_rail_dict = canonical_payment_readiness_rail_instance.to_dict()
# create an instance of CanonicalPaymentReadinessRail from a dict
canonical_payment_readiness_rail_from_dict = CanonicalPaymentReadinessRail.from_dict(canonical_payment_readiness_rail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
