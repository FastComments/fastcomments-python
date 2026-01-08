# UpdateTenantBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**sign_up_date** | **float** |  | [optional] 
**package_id** | **str** |  | [optional] 
**payment_frequency** | **float** |  | [optional] 
**billing_info_valid** | **bool** |  | [optional] 
**billing_handled_externally** | **bool** |  | [optional] 
**created_by** | **str** |  | [optional] 
**is_setup** | **bool** |  | [optional] 
**domain_configuration** | [**List[APIDomainConfiguration]**](APIDomainConfiguration.md) |  | [optional] 
**billing_info** | [**BillingInfo**](BillingInfo.md) |  | [optional] 
**stripe_customer_id** | **str** |  | [optional] 
**stripe_subscription_id** | **str** |  | [optional] 
**stripe_plan_id** | **str** |  | [optional] 
**enable_profanity_filter** | **bool** |  | [optional] 
**enable_spam_filter** | **bool** |  | [optional] 
**remove_unverified_comments** | **bool** |  | [optional] 
**unverified_comments_tt_lms** | **float** |  | [optional] 
**comments_require_approval** | **bool** |  | [optional] 
**auto_approve_comment_on_verification** | **bool** |  | [optional] 
**send_profane_to_spam** | **bool** |  | [optional] 
**de_anon_ip_addr** | **float** |  | [optional] 
**meta** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 
**managed_by_tenant_id** | **str** |  | [optional] 

## Example

```python
from client.models.update_tenant_body import UpdateTenantBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantBody from a JSON string
update_tenant_body_instance = UpdateTenantBody.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantBody.to_json())

# convert the object into a dict
update_tenant_body_dict = update_tenant_body_instance.to_dict()
# create an instance of UpdateTenantBody from a dict
update_tenant_body_from_dict = UpdateTenantBody.from_dict(update_tenant_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


