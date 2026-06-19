# GetCommentsForUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moderating_tenant_ids** | **List[str]** |  | [optional] 

## Example

```python
from client.models.get_comments_for_user_response import GetCommentsForUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommentsForUserResponse from a JSON string
get_comments_for_user_response_instance = GetCommentsForUserResponse.from_json(json)
# print the JSON string representation of the object
print(GetCommentsForUserResponse.to_json())

# convert the object into a dict
get_comments_for_user_response_dict = get_comments_for_user_response_instance.to_dict()
# create an instance of GetCommentsForUserResponse from a dict
get_comments_for_user_response_from_dict = GetCommentsForUserResponse.from_dict(get_comments_for_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


