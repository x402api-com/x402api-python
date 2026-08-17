# TenantPaymentChainProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  |
**transaction_hash** | **str** |  |
**block_number** | **str** |  |
**block_hash** | **str** |  |
**confirmations** | **int** |  |
**confirmations_required** | **int** |  |
**observed_at** | **datetime** |  |

## Example

```python
from x402api.models.tenant_payment_chain_projection import TenantPaymentChainProjection

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPaymentChainProjection from a JSON string
tenant_payment_chain_projection_instance = TenantPaymentChainProjection.from_json(json)
# print the JSON string representation of the object
print(TenantPaymentChainProjection.to_json())

# convert the object into a dict
tenant_payment_chain_projection_dict = tenant_payment_chain_projection_instance.to_dict()
# create an instance of TenantPaymentChainProjection from a dict
tenant_payment_chain_projection_from_dict = TenantPaymentChainProjection.from_dict(tenant_payment_chain_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
