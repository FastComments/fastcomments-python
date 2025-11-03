# GetFeedPostsPublic200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**my_reacts** | **Dict[str, Dict[str, bool]]** |  | [optional] 
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**feed_posts** | [**List[FeedPost]**](FeedPost.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | [optional] 
**url_id_ws** | **str** |  | [optional] 
**user_id_ws** | **str** |  | [optional] 
**tenant_id_ws** | **str** |  | [optional] 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_feed_posts_public200_response import GetFeedPostsPublic200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeedPostsPublic200Response from a JSON string
get_feed_posts_public200_response_instance = GetFeedPostsPublic200Response.from_json(json)
# print the JSON string representation of the object
print(GetFeedPostsPublic200Response.to_json())

# convert the object into a dict
get_feed_posts_public200_response_dict = get_feed_posts_public200_response_instance.to_dict()
# create an instance of GetFeedPostsPublic200Response from a dict
get_feed_posts_public200_response_from_dict = GetFeedPostsPublic200Response.from_dict(get_feed_posts_public200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


