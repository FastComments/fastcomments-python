# GetUserInternalProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**GetUserInternalProfileResponseProfile**](GetUserInternalProfileResponseProfile.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_user_internal_profile_response import GetUserInternalProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserInternalProfileResponse from a JSON string
get_user_internal_profile_response_instance = GetUserInternalProfileResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserInternalProfileResponse.to_json())

# convert the object into a dict
get_user_internal_profile_response_dict = get_user_internal_profile_response_instance.to_dict()
# create an instance of GetUserInternalProfileResponse from a dict
get_user_internal_profile_response_from_dict = GetUserInternalProfileResponse.from_dict(get_user_internal_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


