# RemoveUserBadgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.remove_user_badge_response import RemoveUserBadgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveUserBadgeResponse from a JSON string
remove_user_badge_response_instance = RemoveUserBadgeResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveUserBadgeResponse.to_json())

# convert the object into a dict
remove_user_badge_response_dict = remove_user_badge_response_instance.to_dict()
# create an instance of RemoveUserBadgeResponse from a dict
remove_user_badge_response_from_dict = RemoveUserBadgeResponse.from_dict(remove_user_badge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


