# ModerationAPIChildCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[ModerationAPIComment]**](ModerationAPIComment.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.moderation_api_child_comments_response import ModerationAPIChildCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationAPIChildCommentsResponse from a JSON string
moderation_api_child_comments_response_instance = ModerationAPIChildCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationAPIChildCommentsResponse.to_json())

# convert the object into a dict
moderation_api_child_comments_response_dict = moderation_api_child_comments_response_instance.to_dict()
# create an instance of ModerationAPIChildCommentsResponse from a dict
moderation_api_child_comments_response_from_dict = ModerationAPIChildCommentsResponse.from_dict(moderation_api_child_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


