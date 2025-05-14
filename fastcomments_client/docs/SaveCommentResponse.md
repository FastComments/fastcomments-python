# SaveCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**comment** | [**FComment**](FComment.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | 
**module_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from openapi_client.models.save_comment_response import SaveCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCommentResponse from a JSON string
save_comment_response_instance = SaveCommentResponse.from_json(json)
# print the JSON string representation of the object
print(SaveCommentResponse.to_json())

# convert the object into a dict
save_comment_response_dict = save_comment_response_instance.to_dict()
# create an instance of SaveCommentResponse from a dict
save_comment_response_from_dict = SaveCommentResponse.from_dict(save_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


