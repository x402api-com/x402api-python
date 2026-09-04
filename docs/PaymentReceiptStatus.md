# PaymentReceiptStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **UUID** |  |
**state** | **str** |  |
**confirmed** | **bool** |  |
**finalized** | **bool** |  |
**confirmed_at** | **datetime** |  |
**finalized_at** | **datetime** |  |
**transaction** | **str** |  |
**network** | **str** |  |
**receipt_status** | [**ReceiptStatusEnum**](ReceiptStatusEnum.md) |  |

## Example

```python
from x402api.models.payment_receipt_status import PaymentReceiptStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReceiptStatus from a JSON string
payment_receipt_status_instance = PaymentReceiptStatus.from_json(json)
# print the JSON string representation of the object
print(PaymentReceiptStatus.to_json())

# convert the object into a dict
payment_receipt_status_dict = payment_receipt_status_instance.to_dict()
# create an instance of PaymentReceiptStatus from a dict
payment_receipt_status_from_dict = PaymentReceiptStatus.from_dict(payment_receipt_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
