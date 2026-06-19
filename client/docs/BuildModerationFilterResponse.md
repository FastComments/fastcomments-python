# BuildModerationFilterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**moderation_filter** | [**ModerationFilter**](ModerationFilter.md) |  | 

## Example

```python
from client.models.build_moderation_filter_response import BuildModerationFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuildModerationFilterResponse from a JSON string
build_moderation_filter_response_instance = BuildModerationFilterResponse.from_json(json)
# print the JSON string representation of the object
print(BuildModerationFilterResponse.to_json())

# convert the object into a dict
build_moderation_filter_response_dict = build_moderation_filter_response_instance.to_dict()
# create an instance of BuildModerationFilterResponse from a dict
build_moderation_filter_response_from_dict = BuildModerationFilterResponse.from_dict(build_moderation_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


