# FeedPostsStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**stats** | [**Dict[str, FeedPostStats]**](FeedPostStats.md) |  | 

## Example

```python
from client.models.feed_posts_stats_response import FeedPostsStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeedPostsStatsResponse from a JSON string
feed_posts_stats_response_instance = FeedPostsStatsResponse.from_json(json)
# print the JSON string representation of the object
print(FeedPostsStatsResponse.to_json())

# convert the object into a dict
feed_posts_stats_response_dict = feed_posts_stats_response_instance.to_dict()
# create an instance of FeedPostsStatsResponse from a dict
feed_posts_stats_response_from_dict = FeedPostsStatsResponse.from_dict(feed_posts_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


