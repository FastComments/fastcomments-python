# GetFeedPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**feed_posts** | [**List[FeedPost]**](FeedPost.md) |  | 

## Example

```python
from client.models.get_feed_posts_response import GetFeedPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeedPostsResponse from a JSON string
get_feed_posts_response_instance = GetFeedPostsResponse.from_json(json)
# print the JSON string representation of the object
print(GetFeedPostsResponse.to_json())

# convert the object into a dict
get_feed_posts_response_dict = get_feed_posts_response_instance.to_dict()
# create an instance of GetFeedPostsResponse from a dict
get_feed_posts_response_from_dict = GetFeedPostsResponse.from_dict(get_feed_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


