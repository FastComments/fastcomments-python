# ModerationAPICommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**ModerationAPIComment**](ModerationAPIComment.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.moderation_api_comment_response import ModerationAPICommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationAPICommentResponse from a JSON string
moderation_api_comment_response_instance = ModerationAPICommentResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationAPICommentResponse.to_json())

# convert the object into a dict
moderation_api_comment_response_dict = moderation_api_comment_response_instance.to_dict()
# create an instance of ModerationAPICommentResponse from a dict
moderation_api_comment_response_from_dict = ModerationAPICommentResponse.from_dict(moderation_api_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


