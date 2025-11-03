# UpdateAPISSOUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_ids** | **List[str]** |  | [optional] 
**has_blocked_users** | **bool** |  | [optional] 
**is_profile_dm_disabled** | **bool** |  | [optional] 
**is_profile_comments_private** | **bool** |  | [optional] 
**is_profile_activity_private** | **bool** |  | [optional] 
**is_comment_moderator_admin** | **bool** |  | [optional] 
**is_admin_admin** | **bool** |  | [optional] 
**is_account_owner** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**display_label** | **str** |  | [optional] 
**opted_in_subscription_notifications** | **bool** |  | [optional] 
**opted_in_notifications** | **bool** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**login_count** | **int** |  | [optional] 
**created_from_url_id** | **str** |  | [optional] 
**sign_up_date** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from generated.models.update_apisso_user_data import UpdateAPISSOUserData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAPISSOUserData from a JSON string
update_apisso_user_data_instance = UpdateAPISSOUserData.from_json(json)
# print the JSON string representation of the object
print(UpdateAPISSOUserData.to_json())

# convert the object into a dict
update_apisso_user_data_dict = update_apisso_user_data_instance.to_dict()
# create an instance of UpdateAPISSOUserData from a dict
update_apisso_user_data_from_dict = UpdateAPISSOUserData.from_dict(update_apisso_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


