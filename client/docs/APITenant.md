# APITenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | [optional] 
**sign_up_date** | **float** |  | 
**package_id** | **str** |  | 
**payment_frequency** | **float** |  | 
**billing_info_valid** | **bool** |  | 
**billing_handled_externally** | **bool** |  | [optional] 
**created_by** | **str** |  | 
**is_setup** | **bool** |  | 
**domain_configuration** | [**List[APIDomainConfiguration]**](APIDomainConfiguration.md) |  | 
**billing_info** | [**BillingInfo**](BillingInfo.md) |  | [optional] 
**stripe_customer_id** | **str** |  | [optional] 
**stripe_subscription_id** | **str** |  | [optional] 
**stripe_plan_id** | **str** |  | [optional] 
**enable_profanity_filter** | **bool** |  | 
**enable_spam_filter** | **bool** |  | 
**last_billing_issue_reminder_date** | **datetime** |  | [optional] 
**remove_unverified_comments** | **bool** |  | [optional] 
**unverified_comments_tt_lms** | **float** |  | [optional] 
**comments_require_approval** | **bool** |  | [optional] 
**auto_approve_comment_on_verification** | **bool** |  | [optional] 
**send_profane_to_spam** | **bool** |  | [optional] 
**has_flex_pricing** | **bool** |  | [optional] 
**has_auditing** | **bool** |  | [optional] 
**flex_last_billed_amount** | **float** |  | [optional] 
**de_anon_ip_addr** | **float** |  | [optional] 
**meta** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.api_tenant import APITenant

# TODO update the JSON string below
json = "{}"
# create an instance of APITenant from a JSON string
api_tenant_instance = APITenant.from_json(json)
# print the JSON string representation of the object
print(APITenant.to_json())

# convert the object into a dict
api_tenant_dict = api_tenant_instance.to_dict()
# create an instance of APITenant from a dict
api_tenant_from_dict = APITenant.from_dict(api_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


