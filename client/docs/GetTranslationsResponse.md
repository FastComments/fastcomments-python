# GetTranslationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**translations** | **Dict[str, str]** | Construct a type with a set of properties K of type T | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_translations_response import GetTranslationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTranslationsResponse from a JSON string
get_translations_response_instance = GetTranslationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTranslationsResponse.to_json())

# convert the object into a dict
get_translations_response_dict = get_translations_response_instance.to_dict()
# create an instance of GetTranslationsResponse from a dict
get_translations_response_from_dict = GetTranslationsResponse.from_dict(get_translations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


