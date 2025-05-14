# CreateFeedPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**feed_post** | [**FeedPost**](FeedPost.md) |  | 

## Example

```python
from openapi_client.models.create_feed_posts_response import CreateFeedPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFeedPostsResponse from a JSON string
create_feed_posts_response_instance = CreateFeedPostsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateFeedPostsResponse.to_json())

# convert the object into a dict
create_feed_posts_response_dict = create_feed_posts_response_instance.to_dict()
# create an instance of CreateFeedPostsResponse from a dict
create_feed_posts_response_from_dict = CreateFeedPostsResponse.from_dict(create_feed_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


