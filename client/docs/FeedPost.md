# FeedPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**title** | **str** |  | [optional] 
**from_user_id** | **str** |  | [optional] 
**from_user_display_name** | **str** |  | [optional] 
**from_user_avatar** | **str** |  | [optional] 
**from_ip_hash** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**weight** | **float** |  | [optional] 
**meta** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 
**content_html** | **str** |  | [optional] 
**media** | [**List[FeedPostMediaItem]**](FeedPostMediaItem.md) |  | [optional] 
**links** | [**List[FeedPostLink]**](FeedPostLink.md) |  | [optional] 
**created_at** | **datetime** |  | 
**reacts** | **Dict[str, float]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from openapi_client.models.feed_post import FeedPost

# TODO update the JSON string below
json = "{}"
# create an instance of FeedPost from a JSON string
feed_post_instance = FeedPost.from_json(json)
# print the JSON string representation of the object
print(FeedPost.to_json())

# convert the object into a dict
feed_post_dict = feed_post_instance.to_dict()
# create an instance of FeedPost from a dict
feed_post_from_dict = FeedPost.from_dict(feed_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


