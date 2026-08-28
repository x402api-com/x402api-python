# PublicNetworkFeeAlternative


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |
**version** | **int** |  |
**network** | **str** |  |
**asset_id** | **str** |  |
**contract_address** | **str** |  |
**listed_amount_atomic** | **str** |  |
**gas_mode** | [**GasModeEnum**](GasModeEnum.md) |  |
**buyer_native_fee_atomic** | **str** |  |
**buyer_payment_atomic** | **str** |  |
**tenant_proceeds_atomic** | **str** |  |
**quote_expires_at** | **datetime** |  |
**eligible** | **bool** |  |
**exclusion_reason** | **str** |  |

## Example

```python
from x402api.models.public_network_fee_alternative import PublicNetworkFeeAlternative

# TODO update the JSON string below
json = "{}"
# create an instance of PublicNetworkFeeAlternative from a JSON string
public_network_fee_alternative_instance = PublicNetworkFeeAlternative.from_json(json)
# print the JSON string representation of the object
print(PublicNetworkFeeAlternative.to_json())

# convert the object into a dict
public_network_fee_alternative_dict = public_network_fee_alternative_instance.to_dict()
# create an instance of PublicNetworkFeeAlternative from a dict
public_network_fee_alternative_from_dict = PublicNetworkFeeAlternative.from_dict(public_network_fee_alternative_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
