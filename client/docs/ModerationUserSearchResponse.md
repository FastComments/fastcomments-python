# ModerationUserSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[ModerationUserSearchProjected]**](ModerationUserSearchProjected.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.moderation_user_search_response import ModerationUserSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationUserSearchResponse from a JSON string
moderation_user_search_response_instance = ModerationUserSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationUserSearchResponse.to_json())

# convert the object into a dict
moderation_user_search_response_dict = moderation_user_search_response_instance.to_dict()
# create an instance of ModerationUserSearchResponse from a dict
moderation_user_search_response_from_dict = ModerationUserSearchResponse.from_dict(moderation_user_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


