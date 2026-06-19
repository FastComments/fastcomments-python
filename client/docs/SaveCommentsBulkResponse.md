# SaveCommentsBulkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**comment** | [**APIComment**](APIComment.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | 
**module_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.save_comments_bulk_response import SaveCommentsBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCommentsBulkResponse from a JSON string
save_comments_bulk_response_instance = SaveCommentsBulkResponse.from_json(json)
# print the JSON string representation of the object
print(SaveCommentsBulkResponse.to_json())

# convert the object into a dict
save_comments_bulk_response_dict = save_comments_bulk_response_instance.to_dict()
# create an instance of SaveCommentsBulkResponse from a dict
save_comments_bulk_response_from_dict = SaveCommentsBulkResponse.from_dict(save_comments_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


