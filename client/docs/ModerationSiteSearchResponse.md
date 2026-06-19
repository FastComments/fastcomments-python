# ModerationSiteSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sites** | [**List[ModerationSiteSearchProjected]**](ModerationSiteSearchProjected.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.moderation_site_search_response import ModerationSiteSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationSiteSearchResponse from a JSON string
moderation_site_search_response_instance = ModerationSiteSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationSiteSearchResponse.to_json())

# convert the object into a dict
moderation_site_search_response_dict = moderation_site_search_response_instance.to_dict()
# create an instance of ModerationSiteSearchResponse from a dict
moderation_site_search_response_from_dict = ModerationSiteSearchResponse.from_dict(moderation_site_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


