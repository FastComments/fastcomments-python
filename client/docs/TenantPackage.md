# TenantPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**tenant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**monthly_cost_usd** | **float** |  | 
**yearly_cost_usd** | **float** |  | 
**monthly_stripe_plan_id** | **str** |  | 
**yearly_stripe_plan_id** | **str** |  | 
**max_monthly_page_loads** | **float** |  | 
**max_monthly_api_credits** | **float** |  | 
**max_monthly_small_widgets_credits** | **float** |  | 
**max_monthly_comments** | **float** |  | 
**max_concurrent_users** | **float** |  | 
**max_tenant_users** | **float** |  | 
**max_sso_users** | **float** |  | 
**max_moderators** | **float** |  | 
**max_domains** | **float** |  | 
**max_white_labeled_tenants** | **float** |  | 
**max_monthly_event_log_requests** | **float** |  | 
**has_white_labeling** | **bool** |  | 
**has_debranding** | **bool** |  | 
**has_llm_spam_detection** | **bool** |  | 
**for_who_text** | **str** |  | 
**feature_taglines** | **List[str]** |  | 
**has_auditing** | **bool** |  | 
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
**is_sso_billing_monthly_active_users** | **bool** |  | [optional] 

## Example

```python
from client.models.tenant_package import TenantPackage

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPackage from a JSON string
tenant_package_instance = TenantPackage.from_json(json)
# print the JSON string representation of the object
print(TenantPackage.to_json())

# convert the object into a dict
tenant_package_dict = tenant_package_instance.to_dict()
# create an instance of TenantPackage from a dict
tenant_package_from_dict = TenantPackage.from_dict(tenant_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


