# ResourceCreateFulfillmentConfigOneOf1

Provider-neutral paid-entitlement fulfillment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_key** | **str** |  |
**quantity_atomic** | **str** |  |
**provisioner_adapter_id** | **UUID** |  |

## Example

```python
from x402api.models.resource_create_fulfillment_config_one_of1 import ResourceCreateFulfillmentConfigOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCreateFulfillmentConfigOneOf1 from a JSON string
resource_create_fulfillment_config_one_of1_instance = ResourceCreateFulfillmentConfigOneOf1.from_json(json)
# print the JSON string representation of the object
print(ResourceCreateFulfillmentConfigOneOf1.to_json())

# convert the object into a dict
resource_create_fulfillment_config_one_of1_dict = resource_create_fulfillment_config_one_of1_instance.to_dict()
# create an instance of ResourceCreateFulfillmentConfigOneOf1 from a dict
resource_create_fulfillment_config_one_of1_from_dict = ResourceCreateFulfillmentConfigOneOf1.from_dict(resource_create_fulfillment_config_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
