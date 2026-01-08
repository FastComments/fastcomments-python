# CreateTenantPackageBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**monthly_cost_usd** | **float** |  | [optional] 
**yearly_cost_usd** | **float** |  | [optional] 
**monthly_stripe_plan_id** | **str** |  | [optional] 
**yearly_stripe_plan_id** | **str** |  | [optional] 
**max_monthly_page_loads** | **float** |  | 
**max_monthly_api_credits** | **float** |  | 
**max_monthly_small_widgets_credits** | **float** |  | [optional] 
**max_monthly_comments** | **float** |  | 
**max_concurrent_users** | **float** |  | 
**max_tenant_users** | **float** |  | 
**max_sso_users** | **float** |  | 
**max_moderators** | **float** |  | 
**max_domains** | **float** |  | 
**max_white_labeled_tenants** | **float** |  | [optional] 
**max_monthly_event_log_requests** | **float** |  | [optional] 
**has_white_labeling** | **bool** |  | [optional] 
**has_debranding** | **bool** |  | 
**has_llm_spam_detection** | **bool** |  | [optional] 
**for_who_text** | **str** |  | 
**feature_taglines** | **List[str]** |  | 
**has_auditing** | **bool** |  | [optional] 
**has_flex_pricing** | **bool** |  | 
**enable_saml** | **bool** |  | [optional] 
**flex_page_load_cost_cents** | **float** |  | [optional] 
**flex_page_load_unit** | **float** |  | [optional] 
**flex_comment_cost_cents** | **float** |  | [optional] 
**flex_comment_unit** | **float** |  | [optional] 
**flex_sso_user_cost_cents** | **float** |  | [optional] 
**flex_sso_user_unit** | **float** |  | [optional] 
**flex_api_credit_cost_cents** | **float** |  | [optional] 
**flex_api_credit_unit** | **float** |  | [optional] 
**flex_small_widgets_credit_cost_cents** | **float** |  | [optional] 
**flex_small_widgets_credit_unit** | **float** |  | [optional] 
**flex_moderator_cost_cents** | **float** |  | [optional] 
**flex_moderator_unit** | **float** |  | [optional] 
**flex_admin_cost_cents** | **float** |  | [optional] 
**flex_admin_unit** | **float** |  | [optional] 
**flex_domain_cost_cents** | **float** |  | [optional] 
**flex_domain_unit** | **float** |  | [optional] 
**flex_chat_gpt_cost_cents** | **float** |  | [optional] 
**flex_chat_gpt_unit** | **float** |  | [optional] 
**flex_minimum_cost_cents** | **float** |  | [optional] 
**flex_managed_tenant_cost_cents** | **float** |  | [optional] 
**flex_sso_admin_cost_cents** | **float** |  | [optional] 
**flex_sso_admin_unit** | **float** |  | [optional] 
**flex_sso_moderator_cost_cents** | **float** |  | [optional] 
**flex_sso_moderator_unit** | **float** |  | [optional] 

## Example

```python
from client.models.create_tenant_package_body import CreateTenantPackageBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantPackageBody from a JSON string
create_tenant_package_body_instance = CreateTenantPackageBody.from_json(json)
# print the JSON string representation of the object
print(CreateTenantPackageBody.to_json())

# convert the object into a dict
create_tenant_package_body_dict = create_tenant_package_body_instance.to_dict()
# create an instance of CreateTenantPackageBody from a dict
create_tenant_package_body_from_dict = CreateTenantPackageBody.from_dict(create_tenant_package_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


