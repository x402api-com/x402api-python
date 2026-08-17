# TenantPaymentResourceProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  |
**key** | **str** |  |
**name** | **str** |  |
**version** | **int** |  |
**method** | **str** |  |
**path** | **str** |  |
**description** | **str** |  |
**fulfillment_mode** | **str** |  |

## Example

```python
from x402api.models.tenant_payment_resource_projection import TenantPaymentResourceProjection

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPaymentResourceProjection from a JSON string
tenant_payment_resource_projection_instance = TenantPaymentResourceProjection.from_json(json)
# print the JSON string representation of the object
print(TenantPaymentResourceProjection.to_json())

# convert the object into a dict
tenant_payment_resource_projection_dict = tenant_payment_resource_projection_instance.to_dict()
# create an instance of TenantPaymentResourceProjection from a dict
tenant_payment_resource_projection_from_dict = TenantPaymentResourceProjection.from_dict(tenant_payment_resource_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
