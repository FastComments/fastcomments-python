# CreateAPIUserSubscriptionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**url_id** | **str** |  | 
**anon_user_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from client.models.create_api_user_subscription_data import CreateAPIUserSubscriptionData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPIUserSubscriptionData from a JSON string
create_api_user_subscription_data_instance = CreateAPIUserSubscriptionData.from_json(json)
# print the JSON string representation of the object
print(CreateAPIUserSubscriptionData.to_json())

# convert the object into a dict
create_api_user_subscription_data_dict = create_api_user_subscription_data_instance.to_dict()
# create an instance of CreateAPIUserSubscriptionData from a dict
create_api_user_subscription_data_from_dict = CreateAPIUserSubscriptionData.from_dict(create_api_user_subscription_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


