# GetUserPresenceStatuses200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**user_ids_online** | **Dict[str, bool]** | Construct a type with a set of properties K of type T | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_user_presence_statuses200_response import GetUserPresenceStatuses200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserPresenceStatuses200Response from a JSON string
get_user_presence_statuses200_response_instance = GetUserPresenceStatuses200Response.from_json(json)
# print the JSON string representation of the object
print(GetUserPresenceStatuses200Response.to_json())

# convert the object into a dict
get_user_presence_statuses200_response_dict = get_user_presence_statuses200_response_instance.to_dict()
# create an instance of GetUserPresenceStatuses200Response from a dict
get_user_presence_statuses200_response_from_dict = GetUserPresenceStatuses200Response.from_dict(get_user_presence_statuses200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


