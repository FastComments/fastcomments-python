# ModerationSuggestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**pages** | [**List[ModerationPageSearchProjected]**](ModerationPageSearchProjected.md) |  | [optional] 
**users** | [**List[ModerationUserSearchProjected]**](ModerationUserSearchProjected.md) |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from client.models.moderation_suggest_response import ModerationSuggestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationSuggestResponse from a JSON string
moderation_suggest_response_instance = ModerationSuggestResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationSuggestResponse.to_json())

# convert the object into a dict
moderation_suggest_response_dict = moderation_suggest_response_instance.to_dict()
# create an instance of ModerationSuggestResponse from a dict
moderation_suggest_response_from_dict = ModerationSuggestResponse.from_dict(moderation_suggest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


