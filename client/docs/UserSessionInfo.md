# UserSessionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**authorized** | **bool** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**display_label** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**group_ids** | **List[str]** |  | [optional] 
**has_blocked_users** | **bool** |  | [optional] 
**is_anon_session** | **bool** |  | [optional] 
**session_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 

## Example

```python
from client.models.user_session_info import UserSessionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserSessionInfo from a JSON string
user_session_info_instance = UserSessionInfo.from_json(json)
# print the JSON string representation of the object
print(UserSessionInfo.to_json())

# convert the object into a dict
user_session_info_dict = user_session_info_instance.to_dict()
# create an instance of UserSessionInfo from a dict
user_session_info_from_dict = UserSessionInfo.from_dict(user_session_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


