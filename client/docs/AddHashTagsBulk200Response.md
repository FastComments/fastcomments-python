# AddHashTagsBulk200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**results** | [**List[AddHashTag200Response]**](AddHashTag200Response.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.add_hash_tags_bulk200_response import AddHashTagsBulk200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddHashTagsBulk200Response from a JSON string
add_hash_tags_bulk200_response_instance = AddHashTagsBulk200Response.from_json(json)
# print the JSON string representation of the object
print(AddHashTagsBulk200Response.to_json())

# convert the object into a dict
add_hash_tags_bulk200_response_dict = add_hash_tags_bulk200_response_instance.to_dict()
# create an instance of AddHashTagsBulk200Response from a dict
add_hash_tags_bulk200_response_from_dict = AddHashTagsBulk200Response.from_dict(add_hash_tags_bulk200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


