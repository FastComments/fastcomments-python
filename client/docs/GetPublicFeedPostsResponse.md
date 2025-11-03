# GetPublicFeedPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**feed_posts** | [**List[FeedPost]**](FeedPost.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | [optional] 

## Example

```python
from generated.models.get_public_feed_posts_response import GetPublicFeedPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicFeedPostsResponse from a JSON string
get_public_feed_posts_response_instance = GetPublicFeedPostsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPublicFeedPostsResponse.to_json())

# convert the object into a dict
get_public_feed_posts_response_dict = get_public_feed_posts_response_instance.to_dict()
# create an instance of GetPublicFeedPostsResponse from a dict
get_public_feed_posts_response_from_dict = GetPublicFeedPostsResponse.from_dict(get_public_feed_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


