# UpdateNotificationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewed** | **bool** |  | [optional] 
**opted_out** | **bool** |  | [optional] 

## Example

```python
from client.models.update_notification_body import UpdateNotificationBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationBody from a JSON string
update_notification_body_instance = UpdateNotificationBody.from_json(json)
# print the JSON string representation of the object
print(UpdateNotificationBody.to_json())

# convert the object into a dict
update_notification_body_dict = update_notification_body_instance.to_dict()
# create an instance of UpdateNotificationBody from a dict
update_notification_body_from_dict = UpdateNotificationBody.from_dict(update_notification_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


