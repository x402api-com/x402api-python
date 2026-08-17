# BalanceAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  |
**display_name** | **str** |  |
**symbol** | **str** |  |
**contract_address** | **str** |  |
**decimals** | **int** |  |
**amount_atomic** | **str** |  |
**amount** | **str** |  |
**issuer_native** | **bool** |  |
**observed_at** | **datetime** |  |
**node_source** | **str** |  |
**source_consensus** | **str** |  |
**block** | [**ObservationBlock**](ObservationBlock.md) |  |

## Example

```python
from x402api.models.balance_asset import BalanceAsset

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceAsset from a JSON string
balance_asset_instance = BalanceAsset.from_json(json)
# print the JSON string representation of the object
print(BalanceAsset.to_json())

# convert the object into a dict
balance_asset_dict = balance_asset_instance.to_dict()
# create an instance of BalanceAsset from a dict
balance_asset_from_dict = BalanceAsset.from_dict(balance_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
