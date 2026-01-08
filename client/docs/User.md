# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | [optional] 
**username** | **str** |  | 
**display_name** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**email** | **str** |  | 
**pending_email** | **str** |  | [optional] 
**sign_up_date** | **int** |  | 
**created_from_url_id** | **str** |  | [optional] 
**created_from_tenant_id** | **str** |  | 
**created_from_ip_hashed** | **str** |  | 
**verified** | **bool** |  | 
**login_id** | **str** |  | 
**login_id_date** | **int** |  | 
**login_count** | **int** |  | [optional] 
**opted_in_notifications** | **bool** |  | [optional] 
**opted_in_tenant_notifications** | **bool** |  | [optional] 
**hide_account_code** | **bool** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**is_fast_comments_help_request_admin** | **bool** |  | [optional] 
**is_help_request_admin** | **bool** |  | [optional] 
**is_account_owner** | **bool** |  | [optional] 
**is_admin_admin** | **bool** |  | [optional] 
**is_billing_admin** | **bool** |  | [optional] 
**is_analytics_admin** | **bool** |  | [optional] 
**is_customization_admin** | **bool** |  | [optional] 
**is_manage_data_admin** | **bool** |  | [optional] 
**is_comment_moderator_admin** | **bool** |  | [optional] 
**is_api_admin** | **bool** |  | [optional] 
**moderator_ids** | **List[str]** |  | [optional] 
**is_impersonator** | **bool** |  | [optional] 
**is_coupon_manager** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**digest_email_frequency** | [**DigestEmailFrequency**](DigestEmailFrequency.md) |  | [optional] 
**ignored_add_to_my_site_messages** | **bool** |  | [optional] 
**last_login_date** | **datetime** |  | [optional] 
**display_label** | **str** |  | [optional] 
**is_profile_activity_private** | **bool** |  | [optional] 
**is_profile_comments_private** | **bool** |  | [optional] 
**is_profile_dm_disabled** | **bool** |  | [optional] 
**profile_comment_approval_mode** | **float** |  | [optional] 
**karma** | **float** |  | [optional] 
**password_hash** | **str** |  | [optional] 
**average_ticket_ack_time_ms** | **float** |  | [optional] 
**has_blocked_users** | **bool** |  | [optional] 
**bio** | **str** |  | [optional] 
**header_background_src** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**country_flag** | **str** |  | [optional] 
**social_links** | **List[str]** |  | [optional] 
**has_two_factor** | **bool** |  | [optional] 

## Example

```python
from client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


