# PublicPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **int** |  | 
**comment_count** | **int** |  | 
**title** | **str** |  | 
**url** | **str** |  | 
**url_id** | **str** |  | 

## Example

```python
from client.models.public_page import PublicPage

# TODO update the JSON string below
json = "{}"
# create an instance of PublicPage from a JSON string
public_page_instance = PublicPage.from_json(json)
# print the JSON string representation of the object
print(PublicPage.to_json())

# convert the object into a dict
public_page_dict = public_page_instance.to_dict()
# create an instance of PublicPage from a dict
public_page_from_dict = PublicPage.from_dict(public_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


