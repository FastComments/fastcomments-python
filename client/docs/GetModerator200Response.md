# GetModerator200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**moderator** | [**Moderator**](Moderator.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_moderator200_response import GetModerator200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetModerator200Response from a JSON string
get_moderator200_response_instance = GetModerator200Response.from_json(json)
# print the JSON string representation of the object
print(GetModerator200Response.to_json())

# convert the object into a dict
get_moderator200_response_dict = get_moderator200_response_instance.to_dict()
# create an instance of GetModerator200Response from a dict
get_moderator200_response_from_dict = GetModerator200Response.from_dict(get_moderator200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


