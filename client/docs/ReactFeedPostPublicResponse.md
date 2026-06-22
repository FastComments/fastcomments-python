# ReactFeedPostPublicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**react_type** | **str** |  | 
**is_undo** | **bool** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.react_feed_post_public_response import ReactFeedPostPublicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReactFeedPostPublicResponse from a JSON string
react_feed_post_public_response_instance = ReactFeedPostPublicResponse.from_json(json)
# print the JSON string representation of the object
print(ReactFeedPostPublicResponse.to_json())

# convert the object into a dict
react_feed_post_public_response_dict = react_feed_post_public_response_instance.to_dict()
# create an instance of ReactFeedPostPublicResponse from a dict
react_feed_post_public_response_from_dict = ReactFeedPostPublicResponse.from_dict(react_feed_post_public_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


