# PatchHashTag200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**hash_tag** | [**TenantHashTag**](TenantHashTag.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.patch_hash_tag200_response import PatchHashTag200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PatchHashTag200Response from a JSON string
patch_hash_tag200_response_instance = PatchHashTag200Response.from_json(json)
# print the JSON string representation of the object
print(PatchHashTag200Response.to_json())

# convert the object into a dict
patch_hash_tag200_response_dict = patch_hash_tag200_response_instance.to_dict()
# create an instance of PatchHashTag200Response from a dict
patch_hash_tag200_response_from_dict = PatchHashTag200Response.from_dict(patch_hash_tag200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


