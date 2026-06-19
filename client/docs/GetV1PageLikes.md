# GetV1PageLikes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_id_ws** | **str** |  | 
**did_like** | **bool** |  | 
**comment_count** | **int** |  | 
**like_count** | **int** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_v1_page_likes import GetV1PageLikes

# TODO update the JSON string below
json = "{}"
# create an instance of GetV1PageLikes from a JSON string
get_v1_page_likes_instance = GetV1PageLikes.from_json(json)
# print the JSON string representation of the object
print(GetV1PageLikes.to_json())

# convert the object into a dict
get_v1_page_likes_dict = get_v1_page_likes_instance.to_dict()
# create an instance of GetV1PageLikes from a dict
get_v1_page_likes_from_dict = GetV1PageLikes.from_dict(get_v1_page_likes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


