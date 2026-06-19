# GetUserInternalProfileResponseProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commenter_name** | **str** |  | [optional] 
**first_comment_date** | **datetime** |  | [optional] 
**ip_hash** | **str** |  | [optional] 
**country_flag** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**karma** | **float** |  | [optional] 
**locale** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**commenter_email** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**anon_user_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from client.models.get_user_internal_profile_response_profile import GetUserInternalProfileResponseProfile

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserInternalProfileResponseProfile from a JSON string
get_user_internal_profile_response_profile_instance = GetUserInternalProfileResponseProfile.from_json(json)
# print the JSON string representation of the object
print(GetUserInternalProfileResponseProfile.to_json())

# convert the object into a dict
get_user_internal_profile_response_profile_dict = get_user_internal_profile_response_profile_instance.to_dict()
# create an instance of GetUserInternalProfileResponseProfile from a dict
get_user_internal_profile_response_profile_from_dict = GetUserInternalProfileResponseProfile.from_dict(get_user_internal_profile_response_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


