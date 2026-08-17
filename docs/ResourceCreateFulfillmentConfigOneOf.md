# ResourceCreateFulfillmentConfigOneOf

Signed-webhook fulfillment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_endpoint_id** | **UUID** |  |

## Example

```python
from x402api.models.resource_create_fulfillment_config_one_of import ResourceCreateFulfillmentConfigOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCreateFulfillmentConfigOneOf from a JSON string
resource_create_fulfillment_config_one_of_instance = ResourceCreateFulfillmentConfigOneOf.from_json(json)
# print the JSON string representation of the object
print(ResourceCreateFulfillmentConfigOneOf.to_json())

# convert the object into a dict
resource_create_fulfillment_config_one_of_dict = resource_create_fulfillment_config_one_of_instance.to_dict()
# create an instance of ResourceCreateFulfillmentConfigOneOf from a dict
resource_create_fulfillment_config_one_of_from_dict = ResourceCreateFulfillmentConfigOneOf.from_dict(resource_create_fulfillment_config_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
