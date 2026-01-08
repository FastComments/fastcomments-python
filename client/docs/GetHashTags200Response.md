# GetHashTags200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**hash_tags** | [**List[TenantHashTag]**](TenantHashTag.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_hash_tags200_response import GetHashTags200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetHashTags200Response from a JSON string
get_hash_tags200_response_instance = GetHashTags200Response.from_json(json)
# print the JSON string representation of the object
print(GetHashTags200Response.to_json())

# convert the object into a dict
get_hash_tags200_response_dict = get_hash_tags200_response_instance.to_dict()
# create an instance of GetHashTags200Response from a dict
get_hash_tags200_response_from_dict = GetHashTags200Response.from_dict(get_hash_tags200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


