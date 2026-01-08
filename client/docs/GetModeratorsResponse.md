# GetModeratorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**moderators** | [**List[Moderator]**](Moderator.md) |  | 

## Example

```python
from client.models.get_moderators_response import GetModeratorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModeratorsResponse from a JSON string
get_moderators_response_instance = GetModeratorsResponse.from_json(json)
# print the JSON string representation of the object
print(GetModeratorsResponse.to_json())

# convert the object into a dict
get_moderators_response_dict = get_moderators_response_instance.to_dict()
# create an instance of GetModeratorsResponse from a dict
get_moderators_response_from_dict = GetModeratorsResponse.from_dict(get_moderators_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


