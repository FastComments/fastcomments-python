# UnFlagCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 
**code** | **str** |  | 
**reason** | **str** |  | 
**was_unapproved** | **bool** |  | [optional] 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.un_flag_comment_response import UnFlagCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnFlagCommentResponse from a JSON string
un_flag_comment_response_instance = UnFlagCommentResponse.from_json(json)
# print the JSON string representation of the object
print(UnFlagCommentResponse.to_json())

# convert the object into a dict
un_flag_comment_response_dict = un_flag_comment_response_instance.to_dict()
# create an instance of UnFlagCommentResponse from a dict
un_flag_comment_response_from_dict = UnFlagCommentResponse.from_dict(un_flag_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


