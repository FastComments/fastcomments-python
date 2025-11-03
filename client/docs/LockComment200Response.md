# LockComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from generated.models.lock_comment200_response import LockComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LockComment200Response from a JSON string
lock_comment200_response_instance = LockComment200Response.from_json(json)
# print the JSON string representation of the object
print(LockComment200Response.to_json())

# convert the object into a dict
lock_comment200_response_dict = lock_comment200_response_instance.to_dict()
# create an instance of LockComment200Response from a dict
lock_comment200_response_from_dict = LockComment200Response.from_dict(lock_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


