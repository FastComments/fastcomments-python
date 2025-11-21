# GetUserPresenceStatusesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**user_ids_online** | **Dict[str, bool]** | Construct a type with a set of properties K of type T | 

## Example

```python
from client.models.get_user_presence_statuses_response import GetUserPresenceStatusesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserPresenceStatusesResponse from a JSON string
get_user_presence_statuses_response_instance = GetUserPresenceStatusesResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserPresenceStatusesResponse.to_json())

# convert the object into a dict
get_user_presence_statuses_response_dict = get_user_presence_statuses_response_instance.to_dict()
# create an instance of GetUserPresenceStatusesResponse from a dict
get_user_presence_statuses_response_from_dict = GetUserPresenceStatusesResponse.from_dict(get_user_presence_statuses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


