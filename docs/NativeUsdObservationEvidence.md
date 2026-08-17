# NativeUsdObservationEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  |
**native_usd_quote_micros** | **str** |  |
**observed_at** | **datetime** |  |

## Example

```python
from x402api.models.native_usd_observation_evidence import NativeUsdObservationEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of NativeUsdObservationEvidence from a JSON string
native_usd_observation_evidence_instance = NativeUsdObservationEvidence.from_json(json)
# print the JSON string representation of the object
print(NativeUsdObservationEvidence.to_json())

# convert the object into a dict
native_usd_observation_evidence_dict = native_usd_observation_evidence_instance.to_dict()
# create an instance of NativeUsdObservationEvidence from a dict
native_usd_observation_evidence_from_dict = NativeUsdObservationEvidence.from_dict(native_usd_observation_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
