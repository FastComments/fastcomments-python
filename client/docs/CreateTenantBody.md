# CreateTenantBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**domain_configuration** | [**List[APIDomainConfiguration]**](APIDomainConfiguration.md) |  | 
**email** | **str** |  | [optional] 
**sign_up_date** | **float** |  | [optional] 
**package_id** | **str** |  | [optional] 
**payment_frequency** | **float** |  | [optional] 
**billing_info_valid** | **bool** |  | [optional] 
**billing_handled_externally** | **bool** |  | [optional] 
**created_by** | **str** |  | [optional] 
**is_setup** | **bool** |  | [optional] 
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

## Example

```python
from client.models.create_tenant_body import CreateTenantBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantBody from a JSON string
create_tenant_body_instance = CreateTenantBody.from_json(json)
# print the JSON string representation of the object
print(CreateTenantBody.to_json())

# convert the object into a dict
create_tenant_body_dict = create_tenant_body_instance.to_dict()
# create an instance of CreateTenantBody from a dict
create_tenant_body_from_dict = CreateTenantBody.from_dict(create_tenant_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


