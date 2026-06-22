# DeleteFeedPostPublicResponse


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
from client.models.delete_feed_post_public_response import DeleteFeedPostPublicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFeedPostPublicResponse from a JSON string
delete_feed_post_public_response_instance = DeleteFeedPostPublicResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteFeedPostPublicResponse.to_json())

# convert the object into a dict
delete_feed_post_public_response_dict = delete_feed_post_public_response_instance.to_dict()
# create an instance of DeleteFeedPostPublicResponse from a dict
delete_feed_post_public_response_from_dict = DeleteFeedPostPublicResponse.from_dict(delete_feed_post_public_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


