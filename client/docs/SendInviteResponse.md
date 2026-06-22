# SendInviteResponse


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
from client.models.send_invite_response import SendInviteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendInviteResponse from a JSON string
send_invite_response_instance = SendInviteResponse.from_json(json)
# print the JSON string representation of the object
print(SendInviteResponse.to_json())

# convert the object into a dict
send_invite_response_dict = send_invite_response_instance.to_dict()
# create an instance of SendInviteResponse from a dict
send_invite_response_from_dict = SendInviteResponse.from_dict(send_invite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


