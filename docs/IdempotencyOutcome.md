# IdempotencyOutcome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**IdempotencyOutcomeStateEnum**](IdempotencyOutcomeStateEnum.md) |  | [readonly]

## Example

```python
from x402api.models.idempotency_outcome import IdempotencyOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of IdempotencyOutcome from a JSON string
idempotency_outcome_instance = IdempotencyOutcome.from_json(json)
# print the JSON string representation of the object
print(IdempotencyOutcome.to_json())

# convert the object into a dict
idempotency_outcome_dict = idempotency_outcome_instance.to_dict()
# create an instance of IdempotencyOutcome from a dict
idempotency_outcome_from_dict = IdempotencyOutcome.from_dict(idempotency_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
