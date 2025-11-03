# FeedPostStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reacts** | **Dict[str, int]** |  | [optional] 
**comment_count** | **int** |  | [optional] 

## Example

```python
from client.models.feed_post_stats import FeedPostStats

# TODO update the JSON string below
json = "{}"
# create an instance of FeedPostStats from a JSON string
feed_post_stats_instance = FeedPostStats.from_json(json)
# print the JSON string representation of the object
print(FeedPostStats.to_json())

# convert the object into a dict
feed_post_stats_dict = feed_post_stats_instance.to_dict()
# create an instance of FeedPostStats from a dict
feed_post_stats_from_dict = FeedPostStats.from_dict(feed_post_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


