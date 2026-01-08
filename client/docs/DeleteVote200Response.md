# DeleteVote200Response


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
from client.models.delete_vote200_response import DeleteVote200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVote200Response from a JSON string
delete_vote200_response_instance = DeleteVote200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteVote200Response.to_json())

# convert the object into a dict
delete_vote200_response_dict = delete_vote200_response_instance.to_dict()
# create an instance of DeleteVote200Response from a dict
delete_vote200_response_from_dict = DeleteVote200Response.from_dict(delete_vote200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


