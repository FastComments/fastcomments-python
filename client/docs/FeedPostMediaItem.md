# FeedPostMediaItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**link_url** | **str** |  | [optional] 
**sizes** | [**List[FeedPostMediaItemAsset]**](FeedPostMediaItemAsset.md) |  | 

## Example

```python
from client.models.feed_post_media_item import FeedPostMediaItem

# TODO update the JSON string below
json = "{}"
# create an instance of FeedPostMediaItem from a JSON string
feed_post_media_item_instance = FeedPostMediaItem.from_json(json)
# print the JSON string representation of the object
print(FeedPostMediaItem.to_json())

# convert the object into a dict
feed_post_media_item_dict = feed_post_media_item_instance.to_dict()
# create an instance of FeedPostMediaItem from a dict
feed_post_media_item_from_dict = FeedPostMediaItem.from_dict(feed_post_media_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


