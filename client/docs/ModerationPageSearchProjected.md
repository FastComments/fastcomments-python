# ModerationPageSearchProjected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_id** | **str** |  | 
**url** | **str** |  | 
**title** | **str** |  | 
**comment_count** | **float** |  | 

## Example

```python
from client.models.moderation_page_search_projected import ModerationPageSearchProjected

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationPageSearchProjected from a JSON string
moderation_page_search_projected_instance = ModerationPageSearchProjected.from_json(json)
# print the JSON string representation of the object
print(ModerationPageSearchProjected.to_json())

# convert the object into a dict
moderation_page_search_projected_dict = moderation_page_search_projected_instance.to_dict()
# create an instance of ModerationPageSearchProjected from a dict
moderation_page_search_projected_from_dict = ModerationPageSearchProjected.from_dict(moderation_page_search_projected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


