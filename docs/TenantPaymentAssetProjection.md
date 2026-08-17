# TenantPaymentAssetProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  |
**contract_address** | **str** |  |
**amount_atomic** | **str** |  |
**recipient** | **str** |  |

## Example

```python
from x402api.models.tenant_payment_asset_projection import TenantPaymentAssetProjection

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPaymentAssetProjection from a JSON string
tenant_payment_asset_projection_instance = TenantPaymentAssetProjection.from_json(json)
# print the JSON string representation of the object
print(TenantPaymentAssetProjection.to_json())

# convert the object into a dict
tenant_payment_asset_projection_dict = tenant_payment_asset_projection_instance.to_dict()
# create an instance of TenantPaymentAssetProjection from a dict
tenant_payment_asset_projection_from_dict = TenantPaymentAssetProjection.from_dict(tenant_payment_asset_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
