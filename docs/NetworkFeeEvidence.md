# NetworkFeeEvidence

Published shape for available and explicitly unavailable fee evidence.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |
**version** | **int** |  |
**network** | **str** |  |
**asset_id** | **str** |  |
**payload_profile** | **str** |  |
**native_symbol** | **str** |  | [optional]
**native_decimals** | **int** |  | [optional]
**native_fee_observations** | [**List[NativeFeeObservationEvidence]**](NativeFeeObservationEvidence.md) |  | [optional]
**native_usd_observations** | [**List[NativeUsdObservationEvidence]**](NativeUsdObservationEvidence.md) |  | [optional]
**expires_at** | **datetime** |  | [optional]

## Example

```python
from x402api.models.network_fee_evidence import NetworkFeeEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkFeeEvidence from a JSON string
network_fee_evidence_instance = NetworkFeeEvidence.from_json(json)
# print the JSON string representation of the object
print(NetworkFeeEvidence.to_json())

# convert the object into a dict
network_fee_evidence_dict = network_fee_evidence_instance.to_dict()
# create an instance of NetworkFeeEvidence from a dict
network_fee_evidence_from_dict = NetworkFeeEvidence.from_dict(network_fee_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
