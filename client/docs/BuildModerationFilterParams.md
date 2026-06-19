# BuildModerationFilterParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**tenant_id** | **str** |  | 
**filters** | **str** |  | [optional] 
**search_filters** | **str** |  | [optional] 
**text_search** | **str** |  | [optional] 

## Example

```python
from client.models.build_moderation_filter_params import BuildModerationFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of BuildModerationFilterParams from a JSON string
build_moderation_filter_params_instance = BuildModerationFilterParams.from_json(json)
# print the JSON string representation of the object
print(BuildModerationFilterParams.to_json())

# convert the object into a dict
build_moderation_filter_params_dict = build_moderation_filter_params_instance.to_dict()
# create an instance of BuildModerationFilterParams from a dict
build_moderation_filter_params_from_dict = BuildModerationFilterParams.from_dict(build_moderation_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


