# GetModeratorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**moderator** | [**Moderator**](Moderator.md) |  | 

## Example

```python
from client.models.get_moderator_response import GetModeratorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModeratorResponse from a JSON string
get_moderator_response_instance = GetModeratorResponse.from_json(json)
# print the JSON string representation of the object
print(GetModeratorResponse.to_json())

# convert the object into a dict
get_moderator_response_dict = get_moderator_response_instance.to_dict()
# create an instance of GetModeratorResponse from a dict
get_moderator_response_from_dict = GetModeratorResponse.from_dict(get_moderator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


