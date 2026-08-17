# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**resource_version_id** | **UUID** |  | [readonly]
**request_fingerprint** | **str** |  | [readonly]
**payment_identifier** | **str** |  | [readonly]
**buyer_payment_identifier** | **str** |  | [readonly]
**status** | [**OrderStatusEnum**](OrderStatusEnum.md) |  | [readonly]
**paid_at** | **datetime** |  | [readonly]
**fulfilled_at** | **datetime** |  | [readonly]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]

## Example

```python
from x402api.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
