# DynamicChargeCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_version_id** | **UUID** |  |
**method** | [**HTTPMethodEnum**](HTTPMethodEnum.md) |  | [optional]
**resource_url** | **str** |  |
**body_base64** | **str** |  | [optional] [default to '']
**content_type** | **str** |  | [optional]
**description** | **str** |  | [optional]
**prices** | [**List[DynamicChargePrice]**](DynamicChargePrice.md) |  |
**fee_mode** | [**FeePolicyModeInputEnum**](FeePolicyModeInputEnum.md) |  | [optional]
**quote_currency** | [**FeePolicyQuoteCurrencyInputEnum**](FeePolicyQuoteCurrencyInputEnum.md) |  | [optional]
**fee_allowance_cap_quote_micros** | **str** |  | [optional]
**expires_in_seconds** | **int** |  |
**metadata** | **Dict[str, object]** | Tenant application metadata frozen into the charge digest. Maximum canonical size is 16 KiB; floating-point numbers are not accepted. | [optional]

## Example

```python
from x402api.models.dynamic_charge_create import DynamicChargeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicChargeCreate from a JSON string
dynamic_charge_create_instance = DynamicChargeCreate.from_json(json)
# print the JSON string representation of the object
print(DynamicChargeCreate.to_json())

# convert the object into a dict
dynamic_charge_create_dict = dynamic_charge_create_instance.to_dict()
# create an instance of DynamicChargeCreate from a dict
dynamic_charge_create_from_dict = DynamicChargeCreate.from_dict(dynamic_charge_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
