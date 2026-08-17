# ResourceVersionFulfillmentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_endpoint_id** | **UUID** |  |
**entitlement_key** | **str** |  |
**quantity_atomic** | **str** |  |
**provisioner_adapter_id** | **UUID** |  |

## Example

```python
from x402api.models.resource_version_fulfillment_config import ResourceVersionFulfillmentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceVersionFulfillmentConfig from a JSON string
resource_version_fulfillment_config_instance = ResourceVersionFulfillmentConfig.from_json(json)
# print the JSON string representation of the object
print(ResourceVersionFulfillmentConfig.to_json())

# convert the object into a dict
resource_version_fulfillment_config_dict = resource_version_fulfillment_config_instance.to_dict()
# create an instance of ResourceVersionFulfillmentConfig from a dict
resource_version_fulfillment_config_from_dict = ResourceVersionFulfillmentConfig.from_dict(resource_version_fulfillment_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
