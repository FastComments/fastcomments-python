# SaveCommentResponseOptimized


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**comment** | [**PublicComment**](PublicComment.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | 
**module_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from openapi_client.models.save_comment_response_optimized import SaveCommentResponseOptimized

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCommentResponseOptimized from a JSON string
save_comment_response_optimized_instance = SaveCommentResponseOptimized.from_json(json)
# print the JSON string representation of the object
print(SaveCommentResponseOptimized.to_json())

# convert the object into a dict
save_comment_response_optimized_dict = save_comment_response_optimized_instance.to_dict()
# create an instance of SaveCommentResponseOptimized from a dict
save_comment_response_optimized_from_dict = SaveCommentResponseOptimized.from_dict(save_comment_response_optimized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


