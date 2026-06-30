# PostRemoveCommentApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from client.models.post_remove_comment_api_response import PostRemoveCommentApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRemoveCommentApiResponse from a JSON string
post_remove_comment_api_response_instance = PostRemoveCommentApiResponse.from_json(json)
# print the JSON string representation of the object
print(PostRemoveCommentApiResponse.to_json())

# convert the object into a dict
post_remove_comment_api_response_dict = post_remove_comment_api_response_instance.to_dict()
# create an instance of PostRemoveCommentApiResponse from a dict
post_remove_comment_api_response_from_dict = PostRemoveCommentApiResponse.from_dict(post_remove_comment_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


