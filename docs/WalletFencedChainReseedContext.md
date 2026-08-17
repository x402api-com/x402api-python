# WalletFencedChainReseedContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkpoint_id** | **UUID** |  |
**network** | **str** |  |
**finality** | [**WalletObservationFinalityEnum**](WalletObservationFinalityEnum.md) |  |
**manifest_digest** | **str** |  |
**policy_digest** | **str** |  |
**expected_generation** | **int** |  |
**expected_next_block_number** | **str** |  |
**expected_last_scanned_block_number** | **str** |  |
**expected_last_scanned_block_hash** | **str** |  |
**expected_review_required_at** | **datetime** |  |
**expected_review_error_code** | **str** |  |
**observed_at** | **datetime** |  |
**wallet_version_id** | **UUID** |  |
**wallet_version** | **int** |  |
**wallet_address** | **str** |  |
**wallet_version_state** | [**WalletVersionStateEnum**](WalletVersionStateEnum.md) |  |

## Example

```python
from x402api.models.wallet_fenced_chain_reseed_context import WalletFencedChainReseedContext

# TODO update the JSON string below
json = "{}"
# create an instance of WalletFencedChainReseedContext from a JSON string
wallet_fenced_chain_reseed_context_instance = WalletFencedChainReseedContext.from_json(json)
# print the JSON string representation of the object
print(WalletFencedChainReseedContext.to_json())

# convert the object into a dict
wallet_fenced_chain_reseed_context_dict = wallet_fenced_chain_reseed_context_instance.to_dict()
# create an instance of WalletFencedChainReseedContext from a dict
wallet_fenced_chain_reseed_context_from_dict = WalletFencedChainReseedContext.from_dict(wallet_fenced_chain_reseed_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
