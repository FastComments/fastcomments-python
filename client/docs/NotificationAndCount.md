# NotificationAndCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NotificationType**](NotificationType.md) |  | 
**count** | **float** |  | 

## Example

```python
from openapi_client.models.notification_and_count import NotificationAndCount

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationAndCount from a JSON string
notification_and_count_instance = NotificationAndCount.from_json(json)
# print the JSON string representation of the object
print(NotificationAndCount.to_json())

# convert the object into a dict
notification_and_count_dict = notification_and_count_instance.to_dict()
# create an instance of NotificationAndCount from a dict
notification_and_count_from_dict = NotificationAndCount.from_dict(notification_and_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


