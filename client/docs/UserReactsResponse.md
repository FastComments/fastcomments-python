# UserReactsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**reacts** | **Dict[str, Dict[str, bool]]** |  | 

## Example

```python
from generated.models.user_reacts_response import UserReactsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserReactsResponse from a JSON string
user_reacts_response_instance = UserReactsResponse.from_json(json)
# print the JSON string representation of the object
print(UserReactsResponse.to_json())

# convert the object into a dict
user_reacts_response_dict = user_reacts_response_instance.to_dict()
# create an instance of UserReactsResponse from a dict
user_reacts_response_from_dict = UserReactsResponse.from_dict(user_reacts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


