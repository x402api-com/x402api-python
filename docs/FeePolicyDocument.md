# FeePolicyDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |
**version** | **int** |  |
**fee_mode** | [**FeePolicyModeInputEnum**](FeePolicyModeInputEnum.md) |  |
**quote_currency** | [**FeePolicyQuoteCurrencyInputEnum**](FeePolicyQuoteCurrencyInputEnum.md) |  |
**fee_allowance_cap_quote_micros** | **str** |  |

## Example

```python
from x402api.models.fee_policy_document import FeePolicyDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FeePolicyDocument from a JSON string
fee_policy_document_instance = FeePolicyDocument.from_json(json)
# print the JSON string representation of the object
print(FeePolicyDocument.to_json())

# convert the object into a dict
fee_policy_document_dict = fee_policy_document_instance.to_dict()
# create an instance of FeePolicyDocument from a dict
fee_policy_document_from_dict = FeePolicyDocument.from_dict(fee_policy_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
