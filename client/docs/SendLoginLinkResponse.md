# SendLoginLinkResponse


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
from client.models.send_login_link_response import SendLoginLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendLoginLinkResponse from a JSON string
send_login_link_response_instance = SendLoginLinkResponse.from_json(json)
# print the JSON string representation of the object
print(SendLoginLinkResponse.to_json())

# convert the object into a dict
send_login_link_response_dict = send_login_link_response_instance.to_dict()
# create an instance of SendLoginLinkResponse from a dict
send_login_link_response_from_dict = SendLoginLinkResponse.from_dict(send_login_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


