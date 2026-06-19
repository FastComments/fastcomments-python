# APIBannedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**ip_hash** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**banned_by_user_id** | **str** |  | 
**banned_comment_text** | **str** |  | 
**ban_type** | **str** |  | 
**banned_until** | **datetime** |  | 
**has_email_wildcard** | **bool** |  | 
**ban_reason** | **str** |  | [optional] 

## Example

```python
from client.models.api_banned_user import APIBannedUser

# TODO update the JSON string below
json = "{}"
# create an instance of APIBannedUser from a JSON string
api_banned_user_instance = APIBannedUser.from_json(json)
# print the JSON string representation of the object
print(APIBannedUser.to_json())

# convert the object into a dict
api_banned_user_dict = api_banned_user_instance.to_dict()
# create an instance of APIBannedUser from a dict
api_banned_user_from_dict = APIBannedUser.from_dict(api_banned_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


