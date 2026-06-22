# UnPinCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_positions** | [**Dict[str, RecordStringBeforeStringOrNullAfterStringOrNullValue]**](RecordStringBeforeStringOrNullAfterStringOrNullValue.md) | Construct a type with a set of properties K of type T | 
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
from client.models.un_pin_comment_response import UnPinCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnPinCommentResponse from a JSON string
un_pin_comment_response_instance = UnPinCommentResponse.from_json(json)
# print the JSON string representation of the object
print(UnPinCommentResponse.to_json())

# convert the object into a dict
un_pin_comment_response_dict = un_pin_comment_response_instance.to_dict()
# create an instance of UnPinCommentResponse from a dict
un_pin_comment_response_from_dict = UnPinCommentResponse.from_dict(un_pin_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


