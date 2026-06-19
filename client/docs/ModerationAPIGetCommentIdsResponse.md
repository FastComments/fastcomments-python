# ModerationAPIGetCommentIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 
**has_more** | **bool** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.moderation_api_get_comment_ids_response import ModerationAPIGetCommentIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationAPIGetCommentIdsResponse from a JSON string
moderation_api_get_comment_ids_response_instance = ModerationAPIGetCommentIdsResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationAPIGetCommentIdsResponse.to_json())

# convert the object into a dict
moderation_api_get_comment_ids_response_dict = moderation_api_get_comment_ids_response_instance.to_dict()
# create an instance of ModerationAPIGetCommentIdsResponse from a dict
moderation_api_get_comment_ids_response_from_dict = ModerationAPIGetCommentIdsResponse.from_dict(moderation_api_get_comment_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


