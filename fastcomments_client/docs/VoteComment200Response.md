# VoteComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**vote_id** | **str** |  | [optional] 
**is_verified** | **bool** |  | [optional] 
**user** | [**VoteResponseUser**](VoteResponseUser.md) |  | [optional] 
**edit_key** | **str** |  | [optional] 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **float** |  | [optional] 
**max_character_length** | **float** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from openapi_client.models.vote_comment200_response import VoteComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VoteComment200Response from a JSON string
vote_comment200_response_instance = VoteComment200Response.from_json(json)
# print the JSON string representation of the object
print(VoteComment200Response.to_json())

# convert the object into a dict
vote_comment200_response_dict = vote_comment200_response_instance.to_dict()
# create an instance of VoteComment200Response from a dict
vote_comment200_response_from_dict = VoteComment200Response.from_dict(vote_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


