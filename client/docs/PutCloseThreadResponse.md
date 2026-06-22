# PutCloseThreadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.put_close_thread_response import PutCloseThreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutCloseThreadResponse from a JSON string
put_close_thread_response_instance = PutCloseThreadResponse.from_json(json)
# print the JSON string representation of the object
print(PutCloseThreadResponse.to_json())

# convert the object into a dict
put_close_thread_response_dict = put_close_thread_response_instance.to_dict()
# create an instance of PutCloseThreadResponse from a dict
put_close_thread_response_from_dict = PutCloseThreadResponse.from_dict(put_close_thread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


