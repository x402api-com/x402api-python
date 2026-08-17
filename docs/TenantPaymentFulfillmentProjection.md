# TenantPaymentFulfillmentProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TenantPaymentFulfillmentProjectionStatusEnum**](TenantPaymentFulfillmentProjectionStatusEnum.md) |  |
**id** | **UUID** |  |
**mode** | **str** |  |
**state** | **str** |  |
**attempt_count** | **int** |  |
**last_error_code** | **str** |  |
**completed_at** | **datetime** |  |

## Example

```python
from x402api.models.tenant_payment_fulfillment_projection import TenantPaymentFulfillmentProjection

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPaymentFulfillmentProjection from a JSON string
tenant_payment_fulfillment_projection_instance = TenantPaymentFulfillmentProjection.from_json(json)
# print the JSON string representation of the object
print(TenantPaymentFulfillmentProjection.to_json())

# convert the object into a dict
tenant_payment_fulfillment_projection_dict = tenant_payment_fulfillment_projection_instance.to_dict()
# create an instance of TenantPaymentFulfillmentProjection from a dict
tenant_payment_fulfillment_projection_from_dict = TenantPaymentFulfillmentProjection.from_dict(tenant_payment_fulfillment_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
