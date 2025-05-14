# FlagCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **float** |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 
**code** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**was_unapproved** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.flag_comment_response import FlagCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlagCommentResponse from a JSON string
flag_comment_response_instance = FlagCommentResponse.from_json(json)
# print the JSON string representation of the object
print(FlagCommentResponse.to_json())

# convert the object into a dict
flag_comment_response_dict = flag_comment_response_instance.to_dict()
# create an instance of FlagCommentResponse from a dict
flag_comment_response_from_dict = FlagCommentResponse.from_dict(flag_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


