# ModerationPageSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | [**List[ModerationPageSearchProjected]**](ModerationPageSearchProjected.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.moderation_page_search_response import ModerationPageSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationPageSearchResponse from a JSON string
moderation_page_search_response_instance = ModerationPageSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationPageSearchResponse.to_json())

# convert the object into a dict
moderation_page_search_response_dict = moderation_page_search_response_instance.to_dict()
# create an instance of ModerationPageSearchResponse from a dict
moderation_page_search_response_from_dict = ModerationPageSearchResponse.from_dict(moderation_page_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


