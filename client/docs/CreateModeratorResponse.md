# CreateModeratorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**moderator** | [**Moderator**](Moderator.md) |  | 

## Example

```python
from client.models.create_moderator_response import CreateModeratorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModeratorResponse from a JSON string
create_moderator_response_instance = CreateModeratorResponse.from_json(json)
# print the JSON string representation of the object
print(CreateModeratorResponse.to_json())

# convert the object into a dict
create_moderator_response_dict = create_moderator_response_instance.to_dict()
# create an instance of CreateModeratorResponse from a dict
create_moderator_response_from_dict = CreateModeratorResponse.from_dict(create_moderator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


