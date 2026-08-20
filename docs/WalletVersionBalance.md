# WalletVersionBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_version_id** | **UUID** |  |
**version** | **int** |  |
**wallet_address** | **str** |  |
**state** | [**WalletVersionBalanceStateEnum**](WalletVersionBalanceStateEnum.md) |  |
**observation_state** | [**ObservationStateEnum**](ObservationStateEnum.md) |  |
**tracking_status** | [**TrackingStatusEnum**](TrackingStatusEnum.md) |  |
**observed_at** | **datetime** |  |
**assets** | [**List[BalanceAsset]**](BalanceAsset.md) |  |
**reseed_context** | [**WalletChainReseedContext**](WalletChainReseedContext.md) |  |

## Example

```python
from x402api.models.wallet_version_balance import WalletVersionBalance

# TODO update the JSON string below
json = "{}"
# create an instance of WalletVersionBalance from a JSON string
wallet_version_balance_instance = WalletVersionBalance.from_json(json)
# print the JSON string representation of the object
print(WalletVersionBalance.to_json())

# convert the object into a dict
wallet_version_balance_dict = wallet_version_balance_instance.to_dict()
# create an instance of WalletVersionBalance from a dict
wallet_version_balance_from_dict = WalletVersionBalance.from_dict(wallet_version_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
