# PublicFeePolicyDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |
**version** | **int** |  |
**fee_mode** | [**FeePolicyModeInputEnum**](FeePolicyModeInputEnum.md) |  |
**quote_currency** | [**FeePolicyQuoteCurrencyInputEnum**](FeePolicyQuoteCurrencyInputEnum.md) |  |

## Example

```python
from x402api.models.public_fee_policy_document import PublicFeePolicyDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PublicFeePolicyDocument from a JSON string
public_fee_policy_document_instance = PublicFeePolicyDocument.from_json(json)
# print the JSON string representation of the object
print(PublicFeePolicyDocument.to_json())

# convert the object into a dict
public_fee_policy_document_dict = public_fee_policy_document_instance.to_dict()
# create an instance of PublicFeePolicyDocument from a dict
public_fee_policy_document_from_dict = PublicFeePolicyDocument.from_dict(public_fee_policy_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
