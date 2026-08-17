# TenantPaymentScreeningProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluated_at** | **datetime** |  |
**buyer** | [**TenantPaymentScreeningSubjectProjection**](TenantPaymentScreeningSubjectProjection.md) |  |
**recipient** | [**TenantPaymentScreeningSubjectProjection**](TenantPaymentScreeningSubjectProjection.md) |  |

## Example

```python
from x402api.models.tenant_payment_screening_projection import TenantPaymentScreeningProjection

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPaymentScreeningProjection from a JSON string
tenant_payment_screening_projection_instance = TenantPaymentScreeningProjection.from_json(json)
# print the JSON string representation of the object
print(TenantPaymentScreeningProjection.to_json())

# convert the object into a dict
tenant_payment_screening_projection_dict = tenant_payment_screening_projection_instance.to_dict()
# create an instance of TenantPaymentScreeningProjection from a dict
tenant_payment_screening_projection_from_dict = TenantPaymentScreeningProjection.from_dict(tenant_payment_screening_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
