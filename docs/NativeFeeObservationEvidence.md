# NativeFeeObservationEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  |
**native_fee_atomic** | **str** |  |
**observed_at** | **datetime** |  |

## Example

```python
from x402api.models.native_fee_observation_evidence import NativeFeeObservationEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of NativeFeeObservationEvidence from a JSON string
native_fee_observation_evidence_instance = NativeFeeObservationEvidence.from_json(json)
# print the JSON string representation of the object
print(NativeFeeObservationEvidence.to_json())

# convert the object into a dict
native_fee_observation_evidence_dict = native_fee_observation_evidence_instance.to_dict()
# create an instance of NativeFeeObservationEvidence from a dict
native_fee_observation_evidence_from_dict = NativeFeeObservationEvidence.from_dict(native_fee_observation_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
