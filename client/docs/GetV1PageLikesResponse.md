# GetV1PageLikesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_id_ws** | **str** |  | 
**did_like** | **bool** |  | 
**comment_count** | **int** |  | 
**like_count** | **int** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_v1_page_likes_response import GetV1PageLikesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetV1PageLikesResponse from a JSON string
get_v1_page_likes_response_instance = GetV1PageLikesResponse.from_json(json)
# print the JSON string representation of the object
print(GetV1PageLikesResponse.to_json())

# convert the object into a dict
get_v1_page_likes_response_dict = get_v1_page_likes_response_instance.to_dict()
# create an instance of GetV1PageLikesResponse from a dict
get_v1_page_likes_response_from_dict = GetV1PageLikesResponse.from_dict(get_v1_page_likes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


