# PaymentReadinessBlocker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [readonly]
**owner** | [**PaymentReadinessBlockerOwnerEnum**](PaymentReadinessBlockerOwnerEnum.md) |  | [readonly]
**message** | **str** |  | [readonly]
**action_url** | **str** |  | [optional]

## Example

```python
from x402api.models.payment_readiness_blocker import PaymentReadinessBlocker

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReadinessBlocker from a JSON string
payment_readiness_blocker_instance = PaymentReadinessBlocker.from_json(json)
# print the JSON string representation of the object
print(PaymentReadinessBlocker.to_json())

# convert the object into a dict
payment_readiness_blocker_dict = payment_readiness_blocker_instance.to_dict()
# create an instance of PaymentReadinessBlocker from a dict
payment_readiness_blocker_from_dict = PaymentReadinessBlocker.from_dict(payment_readiness_blocker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
