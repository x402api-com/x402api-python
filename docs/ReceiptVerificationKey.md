# ReceiptVerificationKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** |  |
**public_key_base64** | **str** |  |
**key_fingerprint** | **str** |  |

## Example

```python
from x402api.models.receipt_verification_key import ReceiptVerificationKey

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptVerificationKey from a JSON string
receipt_verification_key_instance = ReceiptVerificationKey.from_json(json)
# print the JSON string representation of the object
print(ReceiptVerificationKey.to_json())

# convert the object into a dict
receipt_verification_key_dict = receipt_verification_key_instance.to_dict()
# create an instance of ReceiptVerificationKey from a dict
receipt_verification_key_from_dict = ReceiptVerificationKey.from_dict(receipt_verification_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
