# CommentsByIdsParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 

## Example

```python
from client.models.comments_by_ids_params import CommentsByIdsParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsByIdsParams from a JSON string
comments_by_ids_params_instance = CommentsByIdsParams.from_json(json)
# print the JSON string representation of the object
print(CommentsByIdsParams.to_json())

# convert the object into a dict
comments_by_ids_params_dict = comments_by_ids_params_instance.to_dict()
# create an instance of CommentsByIdsParams from a dict
comments_by_ids_params_from_dict = CommentsByIdsParams.from_dict(comments_by_ids_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


