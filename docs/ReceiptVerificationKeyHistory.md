# ReceiptVerificationKeyHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |
**keys** | [**Dict[str, ReceiptVerificationKey]**](ReceiptVerificationKey.md) |  |

## Example

```python
from x402api.models.receipt_verification_key_history import ReceiptVerificationKeyHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptVerificationKeyHistory from a JSON string
receipt_verification_key_history_instance = ReceiptVerificationKeyHistory.from_json(json)
# print the JSON string representation of the object
print(ReceiptVerificationKeyHistory.to_json())

# convert the object into a dict
receipt_verification_key_history_dict = receipt_verification_key_history_instance.to_dict()
# create an instance of ReceiptVerificationKeyHistory from a dict
receipt_verification_key_history_from_dict = ReceiptVerificationKeyHistory.from_dict(receipt_verification_key_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
