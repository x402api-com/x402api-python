# TenantPaymentOrderProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  |
**status** | **str** |  |
**buyer_payment_identifier** | **str** |  |
**paid_at** | **datetime** |  |
**fulfilled_at** | **datetime** |  |

## Example

```python
from x402api.models.tenant_payment_order_projection import TenantPaymentOrderProjection

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPaymentOrderProjection from a JSON string
tenant_payment_order_projection_instance = TenantPaymentOrderProjection.from_json(json)
# print the JSON string representation of the object
print(TenantPaymentOrderProjection.to_json())

# convert the object into a dict
tenant_payment_order_projection_dict = tenant_payment_order_projection_instance.to_dict()
# create an instance of TenantPaymentOrderProjection from a dict
tenant_payment_order_projection_from_dict = TenantPaymentOrderProjection.from_dict(tenant_payment_order_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
