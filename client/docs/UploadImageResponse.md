# UploadImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**url** | **str** |  | [optional] 
**media** | [**List[MediaAsset]**](MediaAsset.md) |  | [optional] 
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from generated.models.upload_image_response import UploadImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadImageResponse from a JSON string
upload_image_response_instance = UploadImageResponse.from_json(json)
# print the JSON string representation of the object
print(UploadImageResponse.to_json())

# convert the object into a dict
upload_image_response_dict = upload_image_response_instance.to_dict()
# create an instance of UploadImageResponse from a dict
upload_image_response_from_dict = UploadImageResponse.from_dict(upload_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


