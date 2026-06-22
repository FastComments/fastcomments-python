# SetCommentTextResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**SetCommentTextResult**](SetCommentTextResult.md) |  | 
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
from client.models.set_comment_text_response1 import SetCommentTextResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of SetCommentTextResponse1 from a JSON string
set_comment_text_response1_instance = SetCommentTextResponse1.from_json(json)
# print the JSON string representation of the object
print(SetCommentTextResponse1.to_json())

# convert the object into a dict
set_comment_text_response1_dict = set_comment_text_response1_instance.to_dict()
# create an instance of SetCommentTextResponse1 from a dict
set_comment_text_response1_from_dict = SetCommentTextResponse1.from_dict(set_comment_text_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


