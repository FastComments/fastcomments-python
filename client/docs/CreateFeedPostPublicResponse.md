# CreateFeedPostPublicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**feed_post** | [**FeedPost**](FeedPost.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.create_feed_post_public_response import CreateFeedPostPublicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFeedPostPublicResponse from a JSON string
create_feed_post_public_response_instance = CreateFeedPostPublicResponse.from_json(json)
# print the JSON string representation of the object
print(CreateFeedPostPublicResponse.to_json())

# convert the object into a dict
create_feed_post_public_response_dict = create_feed_post_public_response_instance.to_dict()
# create an instance of CreateFeedPostPublicResponse from a dict
create_feed_post_public_response_from_dict = CreateFeedPostPublicResponse.from_dict(create_feed_post_public_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


