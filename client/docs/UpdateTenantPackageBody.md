# UpdateTenantPackageBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**monthly_cost_usd** | **float** |  | [optional] 
**yearly_cost_usd** | **float** |  | [optional] 
**max_monthly_page_loads** | **float** |  | [optional] 
**max_monthly_api_credits** | **float** |  | [optional] 
**max_monthly_comments** | **float** |  | [optional] 
**max_concurrent_users** | **float** |  | [optional] 
**max_tenant_users** | **float** |  | [optional] 
**max_sso_users** | **float** |  | [optional] 
**max_moderators** | **float** |  | [optional] 
**max_domains** | **float** |  | [optional] 
**has_debranding** | **bool** |  | [optional] 
**has_white_labeling** | **bool** |  | [optional] 
**for_who_text** | **str** |  | [optional] 
**feature_taglines** | **List[str]** |  | [optional] 
**has_flex_pricing** | **bool** |  | [optional] 
**flex_page_load_cost_cents** | **float** |  | [optional] 
**flex_page_load_unit** | **float** |  | [optional] 
**flex_comment_cost_cents** | **float** |  | [optional] 
**flex_comment_unit** | **float** |  | [optional] 
**flex_sso_user_cost_cents** | **float** |  | [optional] 
**flex_sso_user_unit** | **float** |  | [optional] 
**flex_api_credit_cost_cents** | **float** |  | [optional] 
**flex_api_credit_unit** | **float** |  | [optional] 
**flex_moderator_cost_cents** | **float** |  | [optional] 
**flex_moderator_unit** | **float** |  | [optional] 
**flex_admin_cost_cents** | **float** |  | [optional] 
**flex_admin_unit** | **float** |  | [optional] 
**flex_domain_cost_cents** | **float** |  | [optional] 
**flex_domain_unit** | **float** |  | [optional] 
**flex_minimum_cost_cents** | **float** |  | [optional] 

## Example

```python
from client.models.update_tenant_package_body import UpdateTenantPackageBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantPackageBody from a JSON string
update_tenant_package_body_instance = UpdateTenantPackageBody.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantPackageBody.to_json())

# convert the object into a dict
update_tenant_package_body_dict = update_tenant_package_body_instance.to_dict()
# create an instance of UpdateTenantPackageBody from a dict
update_tenant_package_body_from_dict = UpdateTenantPackageBody.from_dict(update_tenant_package_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


