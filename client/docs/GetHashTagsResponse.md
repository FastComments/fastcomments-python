# GetHashTagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**hash_tags** | [**List[TenantHashTag]**](TenantHashTag.md) |  | 

## Example

```python
from client.models.get_hash_tags_response import GetHashTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHashTagsResponse from a JSON string
get_hash_tags_response_instance = GetHashTagsResponse.from_json(json)
# print the JSON string representation of the object
print(GetHashTagsResponse.to_json())

# convert the object into a dict
get_hash_tags_response_dict = get_hash_tags_response_instance.to_dict()
# create an instance of GetHashTagsResponse from a dict
get_hash_tags_response_from_dict = GetHashTagsResponse.from_dict(get_hash_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


