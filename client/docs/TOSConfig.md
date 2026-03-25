# TOSConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**text_by_locale** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 
**last_updated** | **datetime** |  | [optional] 

## Example

```python
from client.models.tos_config import TOSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TOSConfig from a JSON string
tos_config_instance = TOSConfig.from_json(json)
# print the JSON string representation of the object
print(TOSConfig.to_json())

# convert the object into a dict
tos_config_dict = tos_config_instance.to_dict()
# create an instance of TOSConfig from a dict
tos_config_from_dict = TOSConfig.from_dict(tos_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


