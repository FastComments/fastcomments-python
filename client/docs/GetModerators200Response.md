# GetModerators200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**moderators** | [**List[Moderator]**](Moderator.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_moderators200_response import GetModerators200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetModerators200Response from a JSON string
get_moderators200_response_instance = GetModerators200Response.from_json(json)
# print the JSON string representation of the object
print(GetModerators200Response.to_json())

# convert the object into a dict
get_moderators200_response_dict = get_moderators200_response_instance.to_dict()
# create an instance of GetModerators200Response from a dict
get_moderators200_response_from_dict = GetModerators200Response.from_dict(get_moderators200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


