# SettlementChainObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**settlement_job_id** | **UUID** |  | [readonly]
**network** | **str** |  | [readonly]
**transaction_hash** | **str** |  | [readonly]
**state** | [**SettlementChainObservationStateEnum**](SettlementChainObservationStateEnum.md) |  | [readonly]
**observation_digest** | **str** |  | [readonly]
**log_index** | **int** |  | [readonly]
**block_number** | **str** |  | [readonly]
**block_hash** | **str** |  | [readonly]
**asset_contract** | **str** |  | [readonly]
**payer** | **str** |  | [readonly]
**recipient** | **str** |  | [readonly]
**amount_atomic** | **str** |  | [readonly]
**execution_success** | **bool** |  | [readonly]
**observed_at** | **datetime** |  | [readonly]
**created_at** | **datetime** |  | [readonly]

## Example

```python
from x402api.models.settlement_chain_observation import SettlementChainObservation

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementChainObservation from a JSON string
settlement_chain_observation_instance = SettlementChainObservation.from_json(json)
# print the JSON string representation of the object
print(SettlementChainObservation.to_json())

# convert the object into a dict
settlement_chain_observation_dict = settlement_chain_observation_instance.to_dict()
# create an instance of SettlementChainObservation from a dict
settlement_chain_observation_from_dict = SettlementChainObservation.from_dict(settlement_chain_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
