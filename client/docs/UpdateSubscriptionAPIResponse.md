# UpdateSubscriptionAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**subscription** | [**APIUserSubscription**](APIUserSubscription.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from client.models.update_subscription_api_response import UpdateSubscriptionAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionAPIResponse from a JSON string
update_subscription_api_response_instance = UpdateSubscriptionAPIResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionAPIResponse.to_json())

# convert the object into a dict
update_subscription_api_response_dict = update_subscription_api_response_instance.to_dict()
# create an instance of UpdateSubscriptionAPIResponse from a dict
update_subscription_api_response_from_dict = UpdateSubscriptionAPIResponse.from_dict(update_subscription_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


