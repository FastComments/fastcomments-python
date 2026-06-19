# APIBanUserChangedValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**ip_hash** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**banned_by_user_id** | **str** |  | [optional] 
**banned_comment_text** | **str** |  | [optional] 
**ban_type** | **str** |  | [optional] 
**banned_until** | **datetime** |  | [optional] 
**has_email_wildcard** | **bool** |  | [optional] 
**ban_reason** | **str** |  | [optional] 

## Example

```python
from client.models.api_ban_user_changed_values import APIBanUserChangedValues

# TODO update the JSON string below
json = "{}"
# create an instance of APIBanUserChangedValues from a JSON string
api_ban_user_changed_values_instance = APIBanUserChangedValues.from_json(json)
# print the JSON string representation of the object
print(APIBanUserChangedValues.to_json())

# convert the object into a dict
api_ban_user_changed_values_dict = api_ban_user_changed_values_instance.to_dict()
# create an instance of APIBanUserChangedValues from a dict
api_ban_user_changed_values_from_dict = APIBanUserChangedValues.from_dict(api_ban_user_changed_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


