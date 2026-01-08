# ReplaceTenantPackageBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**monthly_cost_usd** | **float** |  | 
**yearly_cost_usd** | **float** |  | 
**max_monthly_page_loads** | **float** |  | 
**max_monthly_api_credits** | **float** |  | 
**max_monthly_comments** | **float** |  | 
**max_concurrent_users** | **float** |  | 
**max_tenant_users** | **float** |  | 
**max_sso_users** | **float** |  | 
**max_moderators** | **float** |  | 
**max_domains** | **float** |  | 
**has_debranding** | **bool** |  | 
**for_who_text** | **str** |  | 
**feature_taglines** | **List[str]** |  | 
**has_flex_pricing** | **bool** |  | 
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
from client.models.replace_tenant_package_body import ReplaceTenantPackageBody

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceTenantPackageBody from a JSON string
replace_tenant_package_body_instance = ReplaceTenantPackageBody.from_json(json)
# print the JSON string representation of the object
print(ReplaceTenantPackageBody.to_json())

# convert the object into a dict
replace_tenant_package_body_dict = replace_tenant_package_body_instance.to_dict()
# create an instance of ReplaceTenantPackageBody from a dict
replace_tenant_package_body_from_dict = ReplaceTenantPackageBody.from_dict(replace_tenant_package_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


