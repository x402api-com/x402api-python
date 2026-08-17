# WalletChainReseedContext


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

## Example

```python
from x402api.models.wallet_chain_reseed_context import WalletChainReseedContext

# TODO update the JSON string below
json = "{}"
# create an instance of WalletChainReseedContext from a JSON string
wallet_chain_reseed_context_instance = WalletChainReseedContext.from_json(json)
# print the JSON string representation of the object
print(WalletChainReseedContext.to_json())

# convert the object into a dict
wallet_chain_reseed_context_dict = wallet_chain_reseed_context_instance.to_dict()
# create an instance of WalletChainReseedContext from a dict
wallet_chain_reseed_context_from_dict = WalletChainReseedContext.from_dict(wallet_chain_reseed_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
