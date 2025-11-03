# UserPresenceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_id_ws** | **str** |  | [optional] 
**user_id_ws** | **str** |  | [optional] 
**tenant_id_ws** | **str** |  | [optional] 

## Example

```python
from generated.models.user_presence_data import UserPresenceData

# TODO update the JSON string below
json = "{}"
# create an instance of UserPresenceData from a JSON string
user_presence_data_instance = UserPresenceData.from_json(json)
# print the JSON string representation of the object
print(UserPresenceData.to_json())

# convert the object into a dict
user_presence_data_dict = user_presence_data_instance.to_dict()
# create an instance of UserPresenceData from a dict
user_presence_data_from_dict = UserPresenceData.from_dict(user_presence_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


