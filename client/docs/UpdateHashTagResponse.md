# UpdateHashTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**hash_tag** | [**TenantHashTag**](TenantHashTag.md) |  | 

## Example

```python
from client.models.update_hash_tag_response import UpdateHashTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHashTagResponse from a JSON string
update_hash_tag_response_instance = UpdateHashTagResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateHashTagResponse.to_json())

# convert the object into a dict
update_hash_tag_response_dict = update_hash_tag_response_instance.to_dict()
# create an instance of UpdateHashTagResponse from a dict
update_hash_tag_response_from_dict = UpdateHashTagResponse.from_dict(update_hash_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


