# TenantPaymentScreeningSubjectProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TenantPaymentScreeningSubjectProjectionStatusEnum**](TenantPaymentScreeningSubjectProjectionStatusEnum.md) |  |

## Example

```python
from x402api.models.tenant_payment_screening_subject_projection import TenantPaymentScreeningSubjectProjection

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPaymentScreeningSubjectProjection from a JSON string
tenant_payment_screening_subject_projection_instance = TenantPaymentScreeningSubjectProjection.from_json(json)
# print the JSON string representation of the object
print(TenantPaymentScreeningSubjectProjection.to_json())

# convert the object into a dict
tenant_payment_screening_subject_projection_dict = tenant_payment_screening_subject_projection_instance.to_dict()
# create an instance of TenantPaymentScreeningSubjectProjection from a dict
tenant_payment_screening_subject_projection_from_dict = TenantPaymentScreeningSubjectProjection.from_dict(tenant_payment_screening_subject_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
