# APISSOUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | 
**website_url** | **str** |  | 
**email** | **str** |  | 
**sign_up_date** | **int** |  | 
**created_from_url_id** | **str** |  | 
**login_count** | **int** |  | 
**avatar_src** | **str** |  | 
**opted_in_notifications** | **bool** |  | 
**opted_in_subscription_notifications** | **bool** |  | 
**display_label** | **str** |  | 
**display_name** | **str** |  | 
**is_account_owner** | **bool** |  | [optional] 
**is_admin_admin** | **bool** |  | [optional] 
**is_comment_moderator_admin** | **bool** |  | [optional] 
**is_profile_activity_private** | **bool** |  | [optional] 
**is_profile_comments_private** | **bool** |  | [optional] 
**is_profile_dm_disabled** | **bool** |  | [optional] 
**has_blocked_users** | **bool** |  | [optional] 
**group_ids** | **List[str]** |  | [optional] 

## Example

```python
from generated.models.apisso_user import APISSOUser

# TODO update the JSON string below
json = "{}"
# create an instance of APISSOUser from a JSON string
apisso_user_instance = APISSOUser.from_json(json)
# print the JSON string representation of the object
print(APISSOUser.to_json())

# convert the object into a dict
apisso_user_dict = apisso_user_instance.to_dict()
# create an instance of APISSOUser from a dict
apisso_user_from_dict = APISSOUser.from_dict(apisso_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


