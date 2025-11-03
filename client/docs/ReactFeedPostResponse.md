# ReactFeedPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**react_type** | **str** |  | 
**is_undo** | **bool** |  | 

## Example

```python
from generated.models.react_feed_post_response import ReactFeedPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReactFeedPostResponse from a JSON string
react_feed_post_response_instance = ReactFeedPostResponse.from_json(json)
# print the JSON string representation of the object
print(ReactFeedPostResponse.to_json())

# convert the object into a dict
react_feed_post_response_dict = react_feed_post_response_instance.to_dict()
# create an instance of ReactFeedPostResponse from a dict
react_feed_post_response_from_dict = ReactFeedPostResponse.from_dict(react_feed_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


