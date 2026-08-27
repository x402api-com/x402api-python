# DynamicChargeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_id** | **UUID** | Immutable challenge UUID created for this charge. |
**charge_digest** | **str** |  |
**order_id** | **UUID** |  |
**status** | **str** | Current projected order status; payment terms remain immutable. |
**resource_version_id** | **UUID** |  |
**payment_identifier** | **str** | Opaque server challenge handle. Return it to the buyer as X-X402API-Challenge-Handle; it is not the buyer payment identifier. |
**expires_at** | **datetime** |  |
**created_at** | **datetime** |  |
**prices** | [**List[DynamicChargePrice]**](DynamicChargePrice.md) |  |
**requested_expires_in_seconds** | **int** |  |
**metadata** | **Dict[str, object]** | Tenant application metadata frozen into the charge digest. Maximum canonical size is 16 KiB; floating-point numbers are not accepted. |
**metadata_digest** | **str** |  |
**payment_required** | **object** | Complete immutable x402 v2 PAYMENT-REQUIRED document. |
**payment_required_header** | **str** | Canonical base64-encoded value to return in the buyer-facing PAYMENT-REQUIRED header. |
**eligible_alternatives** | [**List[NetworkFeeAlternative]**](NetworkFeeAlternative.md) |  |
**fee_policy** | [**FeePolicyDocument**](FeePolicyDocument.md) |  |
**fee_quote_digest** | **str** |  |

## Example

```python
from x402api.models.dynamic_charge_response import DynamicChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicChargeResponse from a JSON string
dynamic_charge_response_instance = DynamicChargeResponse.from_json(json)
# print the JSON string representation of the object
print(DynamicChargeResponse.to_json())

# convert the object into a dict
dynamic_charge_response_dict = dynamic_charge_response_instance.to_dict()
# create an instance of DynamicChargeResponse from a dict
dynamic_charge_response_from_dict = DynamicChargeResponse.from_dict(dynamic_charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
