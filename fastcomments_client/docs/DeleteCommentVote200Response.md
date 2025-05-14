# DeleteCommentVote200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**was_pending_vote** | **bool** |  | [optional] 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **float** |  | [optional] 
**max_character_length** | **float** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from openapi_client.models.delete_comment_vote200_response import DeleteCommentVote200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCommentVote200Response from a JSON string
delete_comment_vote200_response_instance = DeleteCommentVote200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteCommentVote200Response.to_json())

# convert the object into a dict
delete_comment_vote200_response_dict = delete_comment_vote200_response_instance.to_dict()
# create an instance of DeleteCommentVote200Response from a dict
delete_comment_vote200_response_from_dict = DeleteCommentVote200Response.from_dict(delete_comment_vote200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


