# SettlementJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**order_id** | **UUID** |  | [readonly]
**reservation_id** | **UUID** |  | [readonly]
**state** | [**SettlementJobStateEnum**](SettlementJobStateEnum.md) |  | [readonly]
**confirmed** | **bool** |  | [optional] [readonly]
**finalized** | **bool** |  | [optional] [readonly]
**network** | **str** |  | [readonly]
**transaction_hash** | **str** |  | [readonly]
**original_transaction_hash** | **str** |  | [readonly]
**replaced_by_hash** | **str** |  | [readonly]
**gas_execution_state** | **str** |  | [readonly]
**gas_execution_sequence** | **int** |  | [readonly]
**gas_execution_material_digest** | **str** |  | [readonly]
**gas_execution_observed_at** | **datetime** |  | [readonly]
**payer** | **str** |  | [readonly]
**last_error_code** | **str** |  | [readonly]
**broadcast_attempt_count** | **int** |  | [readonly]
**settlement_result** | **object** |  | [readonly]
**confirmed_at** | **datetime** |  | [readonly]
**finalized_at** | **datetime** |  | [readonly]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]
**order** | [**TenantPaymentOrderProjection**](TenantPaymentOrderProjection.md) |  | [readonly]
**resource** | [**TenantPaymentResourceProjection**](TenantPaymentResourceProjection.md) |  | [readonly]
**asset** | [**TenantPaymentAssetProjection**](TenantPaymentAssetProjection.md) |  | [readonly]
**chain** | [**TenantPaymentChainProjection**](TenantPaymentChainProjection.md) |  | [readonly]
**receipt** | [**TenantPaymentReceiptProjection**](TenantPaymentReceiptProjection.md) |  | [readonly]
**screening** | [**TenantPaymentScreeningProjection**](TenantPaymentScreeningProjection.md) |  | [readonly]
**fulfillment** | [**TenantPaymentFulfillmentProjection**](TenantPaymentFulfillmentProjection.md) |  | [readonly]

## Example

```python
from x402api.models.settlement_job import SettlementJob

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementJob from a JSON string
settlement_job_instance = SettlementJob.from_json(json)
# print the JSON string representation of the object
print(SettlementJob.to_json())

# convert the object into a dict
settlement_job_dict = settlement_job_instance.to_dict()
# create an instance of SettlementJob from a dict
settlement_job_from_dict = SettlementJob.from_dict(settlement_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
