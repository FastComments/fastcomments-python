# APISaveCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**comment** | [**APIComment**](APIComment.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | 
**module_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.api_save_comment_response import APISaveCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APISaveCommentResponse from a JSON string
api_save_comment_response_instance = APISaveCommentResponse.from_json(json)
# print the JSON string representation of the object
print(APISaveCommentResponse.to_json())

# convert the object into a dict
api_save_comment_response_dict = api_save_comment_response_instance.to_dict()
# create an instance of APISaveCommentResponse from a dict
api_save_comment_response_from_dict = APISaveCommentResponse.from_dict(api_save_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


