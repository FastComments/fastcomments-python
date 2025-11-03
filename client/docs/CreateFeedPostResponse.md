# CreateFeedPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**feed_post** | [**FeedPost**](FeedPost.md) |  | 

## Example

```python
from generated.models.create_feed_post_response import CreateFeedPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFeedPostResponse from a JSON string
create_feed_post_response_instance = CreateFeedPostResponse.from_json(json)
# print the JSON string representation of the object
print(CreateFeedPostResponse.to_json())

# convert the object into a dict
create_feed_post_response_dict = create_feed_post_response_instance.to_dict()
# create an instance of CreateFeedPostResponse from a dict
create_feed_post_response_from_dict = CreateFeedPostResponse.from_dict(create_feed_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


