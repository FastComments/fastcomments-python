# CheckedCommentsForBlocked200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_statuses** | **Dict[str, bool]** | Construct a type with a set of properties K of type T | 
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.checked_comments_for_blocked200_response import CheckedCommentsForBlocked200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CheckedCommentsForBlocked200Response from a JSON string
checked_comments_for_blocked200_response_instance = CheckedCommentsForBlocked200Response.from_json(json)
# print the JSON string representation of the object
print(CheckedCommentsForBlocked200Response.to_json())

# convert the object into a dict
checked_comments_for_blocked200_response_dict = checked_comments_for_blocked200_response_instance.to_dict()
# create an instance of CheckedCommentsForBlocked200Response from a dict
checked_comments_for_blocked200_response_from_dict = CheckedCommentsForBlocked200Response.from_dict(checked_comments_for_blocked200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


