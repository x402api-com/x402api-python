# NetworkFeeAlternative


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |
**version** | **int** |  |
**network** | **str** |  |
**asset_id** | **str** |  |
**contract_address** | **str** |  |
**fee_mode** | [**FeePolicyModeInputEnum**](FeePolicyModeInputEnum.md) |  |
**quote_currency** | [**FeePolicyQuoteCurrencyInputEnum**](FeePolicyQuoteCurrencyInputEnum.md) |  |
**listed_amount_atomic** | **str** |  |
**fee_allowance_cap_quote_micros** | **str** |  |
**estimated_native_fee_atomic** | **str** |  |
**native_symbol** | **str** |  |
**native_decimals** | **int** |  |
**native_usd_quote_micros** | **str** |  |
**estimated_fee_quote_micros** | **str** |  |
**gas_mode** | [**GasModeEnum**](GasModeEnum.md) |  |
**buyer_native_fee_atomic** | **str** |  |
**maximum_tenant_gas_reservation_micros** | **str** |  |
**provider_disagreement_bps** | **int** |  |
**fee_allowance_quote_micros** | **str** |  |
**fee_allowance_atomic** | **str** |  |
**buyer_payment_atomic** | **str** |  |
**tenant_proceeds_atomic** | **str** |  |
**quote_expires_at** | **datetime** |  |
**fee_evidence** | [**NetworkFeeEvidence**](NetworkFeeEvidence.md) |  |
**fee_evidence_digest** | **str** |  |
**eligible** | **bool** |  |
**exclusion_reason** | **str** |  |

## Example

```python
from x402api.models.network_fee_alternative import NetworkFeeAlternative

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkFeeAlternative from a JSON string
network_fee_alternative_instance = NetworkFeeAlternative.from_json(json)
# print the JSON string representation of the object
print(NetworkFeeAlternative.to_json())

# convert the object into a dict
network_fee_alternative_dict = network_fee_alternative_instance.to_dict()
# create an instance of NetworkFeeAlternative from a dict
network_fee_alternative_from_dict = NetworkFeeAlternative.from_dict(network_fee_alternative_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
