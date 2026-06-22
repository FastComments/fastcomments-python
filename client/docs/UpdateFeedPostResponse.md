# UpdateFeedPostResponse


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
from client.models.update_feed_post_response import UpdateFeedPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeedPostResponse from a JSON string
update_feed_post_response_instance = UpdateFeedPostResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateFeedPostResponse.to_json())

# convert the object into a dict
update_feed_post_response_dict = update_feed_post_response_instance.to_dict()
# create an instance of UpdateFeedPostResponse from a dict
update_feed_post_response_from_dict = UpdateFeedPostResponse.from_dict(update_feed_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


