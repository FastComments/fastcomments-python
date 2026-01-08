# GetCachedNotificationCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**data** | [**UserNotificationCount**](UserNotificationCount.md) |  | 

## Example

```python
from client.models.get_cached_notification_count_response import GetCachedNotificationCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCachedNotificationCountResponse from a JSON string
get_cached_notification_count_response_instance = GetCachedNotificationCountResponse.from_json(json)
# print the JSON string representation of the object
print(GetCachedNotificationCountResponse.to_json())

# convert the object into a dict
get_cached_notification_count_response_dict = get_cached_notification_count_response_instance.to_dict()
# create an instance of GetCachedNotificationCountResponse from a dict
get_cached_notification_count_response_from_dict = GetCachedNotificationCountResponse.from_dict(get_cached_notification_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


