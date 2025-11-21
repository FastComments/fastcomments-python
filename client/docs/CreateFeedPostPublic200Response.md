# CreateFeedPostPublic200Response


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
from client.models.create_feed_post_public200_response import CreateFeedPostPublic200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFeedPostPublic200Response from a JSON string
create_feed_post_public200_response_instance = CreateFeedPostPublic200Response.from_json(json)
# print the JSON string representation of the object
print(CreateFeedPostPublic200Response.to_json())

# convert the object into a dict
create_feed_post_public200_response_dict = create_feed_post_public200_response_instance.to_dict()
# create an instance of CreateFeedPostPublic200Response from a dict
create_feed_post_public200_response_from_dict = CreateFeedPostPublic200Response.from_dict(create_feed_post_public200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


