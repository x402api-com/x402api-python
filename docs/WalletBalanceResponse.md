# WalletBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **UUID** |  |
**network** | **str** |  |
**wallet_address** | **str** |  |
**requested_finality** | [**WalletObservationFinalityEnum**](WalletObservationFinalityEnum.md) |  |
**observation_state** | [**ObservationStateEnum**](ObservationStateEnum.md) |  |
**tracking_status** | [**TrackingStatusEnum**](TrackingStatusEnum.md) |  |
**observed_at** | **datetime** |  |
**assets** | [**List[BalanceAsset]**](BalanceAsset.md) |  |
**wallet_versions** | [**List[WalletVersionBalance]**](WalletVersionBalance.md) |  |
**reseed_contexts** | [**List[WalletFencedChainReseedContext]**](WalletFencedChainReseedContext.md) |  |

## Example

```python
from x402api.models.wallet_balance_response import WalletBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WalletBalanceResponse from a JSON string
wallet_balance_response_instance = WalletBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(WalletBalanceResponse.to_json())

# convert the object into a dict
wallet_balance_response_dict = wallet_balance_response_instance.to_dict()
# create an instance of WalletBalanceResponse from a dict
wallet_balance_response_from_dict = WalletBalanceResponse.from_dict(wallet_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
