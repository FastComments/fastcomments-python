# CreateHashTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**hash_tag** | [**TenantHashTag**](TenantHashTag.md) |  | 

## Example

```python
from client.models.create_hash_tag_response import CreateHashTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHashTagResponse from a JSON string
create_hash_tag_response_instance = CreateHashTagResponse.from_json(json)
# print the JSON string representation of the object
print(CreateHashTagResponse.to_json())

# convert the object into a dict
create_hash_tag_response_dict = create_hash_tag_response_instance.to_dict()
# create an instance of CreateHashTagResponse from a dict
create_hash_tag_response_from_dict = CreateHashTagResponse.from_dict(create_hash_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


