# GetSubscriptionsAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**subscriptions** | [**List[APIUserSubscription]**](APIUserSubscription.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from generated.models.get_subscriptions_api_response import GetSubscriptionsAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionsAPIResponse from a JSON string
get_subscriptions_api_response_instance = GetSubscriptionsAPIResponse.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionsAPIResponse.to_json())

# convert the object into a dict
get_subscriptions_api_response_dict = get_subscriptions_api_response_instance.to_dict()
# create an instance of GetSubscriptionsAPIResponse from a dict
get_subscriptions_api_response_from_dict = GetSubscriptionsAPIResponse.from_dict(get_subscriptions_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


