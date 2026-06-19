# ModerationAPIGetCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**translations** | **object** |  | 
**comments** | [**List[ModerationAPIComment]**](ModerationAPIComment.md) |  | 
**moderation_filter** | [**ModerationFilter**](ModerationFilter.md) |  | [optional] 

## Example

```python
from client.models.moderation_api_get_comments_response import ModerationAPIGetCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationAPIGetCommentsResponse from a JSON string
moderation_api_get_comments_response_instance = ModerationAPIGetCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationAPIGetCommentsResponse.to_json())

# convert the object into a dict
moderation_api_get_comments_response_dict = moderation_api_get_comments_response_instance.to_dict()
# create an instance of ModerationAPIGetCommentsResponse from a dict
moderation_api_get_comments_response_from_dict = ModerationAPIGetCommentsResponse.from_dict(moderation_api_get_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


