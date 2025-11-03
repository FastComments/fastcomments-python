# PublicBlockFromCommentParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_ids** | **List[str]** | A list of comment ids to check if are blocked after performing the update. | 

## Example

```python
from client.models.public_block_from_comment_params import PublicBlockFromCommentParams

# TODO update the JSON string below
json = "{}"
# create an instance of PublicBlockFromCommentParams from a JSON string
public_block_from_comment_params_instance = PublicBlockFromCommentParams.from_json(json)
# print the JSON string representation of the object
print(PublicBlockFromCommentParams.to_json())

# convert the object into a dict
public_block_from_comment_params_dict = public_block_from_comment_params_instance.to_dict()
# create an instance of PublicBlockFromCommentParams from a dict
public_block_from_comment_params_from_dict = PublicBlockFromCommentParams.from_dict(public_block_from_comment_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


