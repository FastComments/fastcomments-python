# UpdateFeedPostParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**content_html** | **str** |  | [optional] 
**media** | [**List[FeedPostMediaItem]**](FeedPostMediaItem.md) |  | [optional] 
**links** | [**List[FeedPostLink]**](FeedPostLink.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**meta** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from generated.models.update_feed_post_params import UpdateFeedPostParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeedPostParams from a JSON string
update_feed_post_params_instance = UpdateFeedPostParams.from_json(json)
# print the JSON string representation of the object
print(UpdateFeedPostParams.to_json())

# convert the object into a dict
update_feed_post_params_dict = update_feed_post_params_instance.to_dict()
# create an instance of UpdateFeedPostParams from a dict
update_feed_post_params_from_dict = UpdateFeedPostParams.from_dict(update_feed_post_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


