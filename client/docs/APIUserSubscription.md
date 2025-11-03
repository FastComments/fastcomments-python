# APIUserSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**page_title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**url_id** | **str** |  | 
**anon_user_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**id** | **str** |  | 

## Example

```python
from generated.models.api_user_subscription import APIUserSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of APIUserSubscription from a JSON string
api_user_subscription_instance = APIUserSubscription.from_json(json)
# print the JSON string representation of the object
print(APIUserSubscription.to_json())

# convert the object into a dict
api_user_subscription_dict = api_user_subscription_instance.to_dict()
# create an instance of APIUserSubscription from a dict
api_user_subscription_from_dict = APIUserSubscription.from_dict(api_user_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


