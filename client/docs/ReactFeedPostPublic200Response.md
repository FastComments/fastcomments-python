# ReactFeedPostPublic200Response


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
from client.models.react_feed_post_public200_response import ReactFeedPostPublic200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReactFeedPostPublic200Response from a JSON string
react_feed_post_public200_response_instance = ReactFeedPostPublic200Response.from_json(json)
# print the JSON string representation of the object
print(ReactFeedPostPublic200Response.to_json())

# convert the object into a dict
react_feed_post_public200_response_dict = react_feed_post_public200_response_instance.to_dict()
# create an instance of ReactFeedPostPublic200Response from a dict
react_feed_post_public200_response_from_dict = ReactFeedPostPublic200Response.from_dict(react_feed_post_public200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


