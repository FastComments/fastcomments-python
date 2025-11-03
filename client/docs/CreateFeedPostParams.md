# CreateFeedPostParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**content_html** | **str** |  | [optional] 
**media** | [**List[FeedPostMediaItem]**](FeedPostMediaItem.md) |  | [optional] 
**links** | [**List[FeedPostLink]**](FeedPostLink.md) |  | [optional] 
**from_user_id** | **str** |  | [optional] 
**from_user_display_name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**meta** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.create_feed_post_params import CreateFeedPostParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFeedPostParams from a JSON string
create_feed_post_params_instance = CreateFeedPostParams.from_json(json)
# print the JSON string representation of the object
print(CreateFeedPostParams.to_json())

# convert the object into a dict
create_feed_post_params_dict = create_feed_post_params_instance.to_dict()
# create an instance of CreateFeedPostParams from a dict
create_feed_post_params_from_dict = CreateFeedPostParams.from_dict(create_feed_post_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


