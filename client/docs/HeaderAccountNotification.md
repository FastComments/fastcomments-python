# HeaderAccountNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**message** | **str** |  | 
**messages_by_locale** | **Dict[str, str]** | Construct a type with a set of properties K of type T | 
**dates** | **Dict[str, str]** | Construct a type with a set of properties K of type T | 
**severity** | **str** |  | 
**link_url** | **str** |  | 
**link_text** | **str** |  | 
**created_at** | **datetime** |  | 
**type** | **str** | Discriminator for notifications with a special layout/click handler (e.g. \&quot;feedback-offer\&quot;). | [optional] 

## Example

```python
from client.models.header_account_notification import HeaderAccountNotification

# TODO update the JSON string below
json = "{}"
# create an instance of HeaderAccountNotification from a JSON string
header_account_notification_instance = HeaderAccountNotification.from_json(json)
# print the JSON string representation of the object
print(HeaderAccountNotification.to_json())

# convert the object into a dict
header_account_notification_dict = header_account_notification_instance.to_dict()
# create an instance of HeaderAccountNotification from a dict
header_account_notification_from_dict = HeaderAccountNotification.from_dict(header_account_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


