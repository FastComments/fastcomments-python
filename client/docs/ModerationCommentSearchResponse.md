# ModerationCommentSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_count** | **int** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.moderation_comment_search_response import ModerationCommentSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationCommentSearchResponse from a JSON string
moderation_comment_search_response_instance = ModerationCommentSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationCommentSearchResponse.to_json())

# convert the object into a dict
moderation_comment_search_response_dict = moderation_comment_search_response_instance.to_dict()
# create an instance of ModerationCommentSearchResponse from a dict
moderation_comment_search_response_from_dict = ModerationCommentSearchResponse.from_dict(moderation_comment_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


