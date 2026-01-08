# GetNotificationCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**count** | **float** |  | 

## Example

```python
from client.models.get_notification_count_response import GetNotificationCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotificationCountResponse from a JSON string
get_notification_count_response_instance = GetNotificationCountResponse.from_json(json)
# print the JSON string representation of the object
print(GetNotificationCountResponse.to_json())

# convert the object into a dict
get_notification_count_response_dict = get_notification_count_response_instance.to_dict()
# create an instance of GetNotificationCountResponse from a dict
get_notification_count_response_from_dict = GetNotificationCountResponse.from_dict(get_notification_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


