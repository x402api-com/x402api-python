# DynamicChargePaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_id** | **UUID** |  |
**order_id** | **UUID** |  |
**payment_id** | **UUID** | Durable settlement identifier used by payment and receipt APIs. |
**state** | **str** |  |
**confirmed** | **bool** |  | [optional]
**finalized** | **bool** |  | [optional]
**payer** | **str** |  |
**transaction** | **str** |  |
**network** | **str** |  |
**error_reason** | **str** |  |

## Example

```python
from x402api.models.dynamic_charge_payment_response import DynamicChargePaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicChargePaymentResponse from a JSON string
dynamic_charge_payment_response_instance = DynamicChargePaymentResponse.from_json(json)
# print the JSON string representation of the object
print(DynamicChargePaymentResponse.to_json())

# convert the object into a dict
dynamic_charge_payment_response_dict = dynamic_charge_payment_response_instance.to_dict()
# create an instance of DynamicChargePaymentResponse from a dict
dynamic_charge_payment_response_from_dict = DynamicChargePaymentResponse.from_dict(dynamic_charge_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
