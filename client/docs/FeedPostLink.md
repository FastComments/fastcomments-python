# FeedPostLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.feed_post_link import FeedPostLink

# TODO update the JSON string below
json = "{}"
# create an instance of FeedPostLink from a JSON string
feed_post_link_instance = FeedPostLink.from_json(json)
# print the JSON string representation of the object
print(FeedPostLink.to_json())

# convert the object into a dict
feed_post_link_dict = feed_post_link_instance.to_dict()
# create an instance of FeedPostLink from a dict
feed_post_link_from_dict = FeedPostLink.from_dict(feed_post_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


