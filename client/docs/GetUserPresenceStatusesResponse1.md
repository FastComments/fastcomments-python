# GetUserPresenceStatusesResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
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
from client.models.get_user_presence_statuses_response1 import GetUserPresenceStatusesResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserPresenceStatusesResponse1 from a JSON string
get_user_presence_statuses_response1_instance = GetUserPresenceStatusesResponse1.from_json(json)
# print the JSON string representation of the object
print(GetUserPresenceStatusesResponse1.to_json())

# convert the object into a dict
get_user_presence_statuses_response1_dict = get_user_presence_statuses_response1_instance.to_dict()
# create an instance of GetUserPresenceStatusesResponse1 from a dict
get_user_presence_statuses_response1_from_dict = GetUserPresenceStatusesResponse1.from_dict(get_user_presence_statuses_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


