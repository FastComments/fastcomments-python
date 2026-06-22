# FlagCommentResponse1


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
from client.models.flag_comment_response1 import FlagCommentResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of FlagCommentResponse1 from a JSON string
flag_comment_response1_instance = FlagCommentResponse1.from_json(json)
# print the JSON string representation of the object
print(FlagCommentResponse1.to_json())

# convert the object into a dict
flag_comment_response1_dict = flag_comment_response1_instance.to_dict()
# create an instance of FlagCommentResponse1 from a dict
flag_comment_response1_from_dict = FlagCommentResponse1.from_dict(flag_comment_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


