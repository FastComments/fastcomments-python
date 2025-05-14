# APIEmptyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 

## Example

```python
from openapi_client.models.api_empty_response import APIEmptyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIEmptyResponse from a JSON string
api_empty_response_instance = APIEmptyResponse.from_json(json)
# print the JSON string representation of the object
print(APIEmptyResponse.to_json())

# convert the object into a dict
api_empty_response_dict = api_empty_response_instance.to_dict()
# create an instance of APIEmptyResponse from a dict
api_empty_response_from_dict = APIEmptyResponse.from_dict(api_empty_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


