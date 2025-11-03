# PublicFeedPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**feed_posts** | [**List[FeedPost]**](FeedPost.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | [optional] 
**url_id_ws** | **str** |  | [optional] 
**user_id_ws** | **str** |  | [optional] 
**tenant_id_ws** | **str** |  | [optional] 
**my_reacts** | **Dict[str, Dict[str, bool]]** |  | [optional] 

## Example

```python
from generated.models.public_feed_posts_response import PublicFeedPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicFeedPostsResponse from a JSON string
public_feed_posts_response_instance = PublicFeedPostsResponse.from_json(json)
# print the JSON string representation of the object
print(PublicFeedPostsResponse.to_json())

# convert the object into a dict
public_feed_posts_response_dict = public_feed_posts_response_instance.to_dict()
# create an instance of PublicFeedPostsResponse from a dict
public_feed_posts_response_from_dict = PublicFeedPostsResponse.from_dict(public_feed_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


