# UnLockCommentResponse


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
from client.models.un_lock_comment_response import UnLockCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnLockCommentResponse from a JSON string
un_lock_comment_response_instance = UnLockCommentResponse.from_json(json)
# print the JSON string representation of the object
print(UnLockCommentResponse.to_json())

# convert the object into a dict
un_lock_comment_response_dict = un_lock_comment_response_instance.to_dict()
# create an instance of UnLockCommentResponse from a dict
un_lock_comment_response_from_dict = UnLockCommentResponse.from_dict(un_lock_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


