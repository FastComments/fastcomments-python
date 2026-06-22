# CheckedCommentsForBlockedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_statuses** | **Dict[str, bool]** | Construct a type with a set of properties K of type T | 
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
from client.models.checked_comments_for_blocked_response import CheckedCommentsForBlockedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckedCommentsForBlockedResponse from a JSON string
checked_comments_for_blocked_response_instance = CheckedCommentsForBlockedResponse.from_json(json)
# print the JSON string representation of the object
print(CheckedCommentsForBlockedResponse.to_json())

# convert the object into a dict
checked_comments_for_blocked_response_dict = checked_comments_for_blocked_response_instance.to_dict()
# create an instance of CheckedCommentsForBlockedResponse from a dict
checked_comments_for_blocked_response_from_dict = CheckedCommentsForBlockedResponse.from_dict(checked_comments_for_blocked_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


