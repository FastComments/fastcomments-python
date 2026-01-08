# CreateTenantUserBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**email** | **str** |  | 
**display_name** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**sign_up_date** | **float** |  | [optional] 
**locale** | **str** |  | [optional] 
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
**digest_email_frequency** | **float** |  | [optional] 
**display_label** | **str** |  | [optional] 

## Example

```python
from client.models.create_tenant_user_body import CreateTenantUserBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantUserBody from a JSON string
create_tenant_user_body_instance = CreateTenantUserBody.from_json(json)
# print the JSON string representation of the object
print(CreateTenantUserBody.to_json())

# convert the object into a dict
create_tenant_user_body_dict = create_tenant_user_body_instance.to_dict()
# create an instance of CreateTenantUserBody from a dict
create_tenant_user_body_from_dict = CreateTenantUserBody.from_dict(create_tenant_user_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


