# PaymentReceipt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**order_id** | **UUID** |  | [readonly]
**settlement_job_id** | **UUID** |  | [readonly]
**receipt** | **object** |  | [readonly]
**receipt_digest** | **str** |  | [readonly]
**signature** | **str** |  | [readonly]
**signing_key_version** | **str** |  | [readonly]
**eligible_alternatives** | [**List[NetworkFeeAlternative]**](NetworkFeeAlternative.md) |  | [readonly]
**fee_policy** | [**FeePolicyDocument**](FeePolicyDocument.md) |  | [readonly]
**fee_evidence** | [**NetworkFeeEvidence**](NetworkFeeEvidence.md) |  | [readonly]
**fee_quote_digest** | **str** |  | [readonly]
**fee_quote_expires_at** | **datetime** |  | [readonly]
**settlement_amount_atomic** | **str** |  | [readonly]
**gas_mode** | **str** |  | [readonly]
**buyer_native_fee_atomic** | **str** |  | [readonly]
**sponsored_native_fee_atomic** | **str** |  | [readonly]
**sponsored_native_symbol** | **str** |  | [readonly]
**tenant_gas_charge_micros** | **str** |  | [readonly]
**gas_sponsorship_evidence_digest** | **str** |  | [readonly]
**created_at** | **datetime** |  | [readonly]

## Example

```python
from x402api.models.payment_receipt import PaymentReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReceipt from a JSON string
payment_receipt_instance = PaymentReceipt.from_json(json)
# print the JSON string representation of the object
print(PaymentReceipt.to_json())

# convert the object into a dict
payment_receipt_dict = payment_receipt_instance.to_dict()
# create an instance of PaymentReceipt from a dict
payment_receipt_from_dict = PaymentReceipt.from_dict(payment_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
