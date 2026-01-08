# UpdateTenantUserBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**sign_up_date** | **float** |  | [optional] 
**verified** | **bool** |  | [optional] 
**login_count** | **float** |  | [optional] 
**opted_in_notifications** | **bool** |  | [optional] 
**opted_in_tenant_notifications** | **bool** |  | [optional] 
**hide_account_code** | **bool** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
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
**locale** | **str** |  | [optional] 
**digest_email_frequency** | **float** |  | [optional] 
**display_label** | **str** |  | [optional] 

## Example

```python
from client.models.update_tenant_user_body import UpdateTenantUserBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantUserBody from a JSON string
update_tenant_user_body_instance = UpdateTenantUserBody.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantUserBody.to_json())

# convert the object into a dict
update_tenant_user_body_dict = update_tenant_user_body_instance.to_dict()
# create an instance of UpdateTenantUserBody from a dict
update_tenant_user_body_from_dict = UpdateTenantUserBody.from_dict(update_tenant_user_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


