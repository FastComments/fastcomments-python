# FlagCommentPublicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.flag_comment_public_response import FlagCommentPublicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlagCommentPublicResponse from a JSON string
flag_comment_public_response_instance = FlagCommentPublicResponse.from_json(json)
# print the JSON string representation of the object
print(FlagCommentPublicResponse.to_json())

# convert the object into a dict
flag_comment_public_response_dict = flag_comment_public_response_instance.to_dict()
# create an instance of FlagCommentPublicResponse from a dict
flag_comment_public_response_from_dict = FlagCommentPublicResponse.from_dict(flag_comment_public_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


