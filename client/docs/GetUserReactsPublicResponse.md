# GetUserReactsPublicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**reacts** | **Dict[str, Dict[str, bool]]** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_user_reacts_public_response import GetUserReactsPublicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserReactsPublicResponse from a JSON string
get_user_reacts_public_response_instance = GetUserReactsPublicResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserReactsPublicResponse.to_json())

# convert the object into a dict
get_user_reacts_public_response_dict = get_user_reacts_public_response_instance.to_dict()
# create an instance of GetUserReactsPublicResponse from a dict
get_user_reacts_public_response_from_dict = GetUserReactsPublicResponse.from_dict(get_user_reacts_public_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


