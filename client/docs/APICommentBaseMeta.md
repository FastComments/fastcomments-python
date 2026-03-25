# APICommentBaseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wp_user_id** | **str** |  | [optional] 
**wp_post_id** | **str** |  | [optional] 

## Example

```python
from client.models.api_comment_base_meta import APICommentBaseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of APICommentBaseMeta from a JSON string
api_comment_base_meta_instance = APICommentBaseMeta.from_json(json)
# print the JSON string representation of the object
print(APICommentBaseMeta.to_json())

# convert the object into a dict
api_comment_base_meta_dict = api_comment_base_meta_instance.to_dict()
# create an instance of APICommentBaseMeta from a dict
api_comment_base_meta_from_dict = APICommentBaseMeta.from_dict(api_comment_base_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


