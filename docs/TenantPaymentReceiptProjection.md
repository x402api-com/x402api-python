# TenantPaymentReceiptProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TenantPaymentReceiptProjectionStatusEnum**](TenantPaymentReceiptProjectionStatusEnum.md) |  |
**id** | **UUID** |  |
**receipt_digest** | **str** |  |
**signing_key_version** | **str** |  |
**created_at** | **datetime** |  |

## Example

```python
from x402api.models.tenant_payment_receipt_projection import TenantPaymentReceiptProjection

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPaymentReceiptProjection from a JSON string
tenant_payment_receipt_projection_instance = TenantPaymentReceiptProjection.from_json(json)
# print the JSON string representation of the object
print(TenantPaymentReceiptProjection.to_json())

# convert the object into a dict
tenant_payment_receipt_projection_dict = tenant_payment_receipt_projection_instance.to_dict()
# create an instance of TenantPaymentReceiptProjection from a dict
tenant_payment_receipt_projection_from_dict = TenantPaymentReceiptProjection.from_dict(tenant_payment_receipt_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
