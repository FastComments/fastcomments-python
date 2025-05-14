# HeaderState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**notification_type** | **object** |  | 
**user_id** | **str** |  | 
**user_id_ws** | **str** |  | 
**notification_counts** | [**List[NotificationAndCount]**](NotificationAndCount.md) |  | 

## Example

```python
from openapi_client.models.header_state import HeaderState

# TODO update the JSON string below
json = "{}"
# create an instance of HeaderState from a JSON string
header_state_instance = HeaderState.from_json(json)
# print the JSON string representation of the object
print(HeaderState.to_json())

# convert the object into a dict
header_state_dict = header_state_instance.to_dict()
# create an instance of HeaderState from a dict
header_state_from_dict = HeaderState.from_dict(header_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


