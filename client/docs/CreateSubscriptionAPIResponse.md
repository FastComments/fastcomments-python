# CreateSubscriptionAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**subscription** | [**APIUserSubscription**](APIUserSubscription.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from client.models.create_subscription_api_response import CreateSubscriptionAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionAPIResponse from a JSON string
create_subscription_api_response_instance = CreateSubscriptionAPIResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionAPIResponse.to_json())

# convert the object into a dict
create_subscription_api_response_dict = create_subscription_api_response_instance.to_dict()
# create an instance of CreateSubscriptionAPIResponse from a dict
create_subscription_api_response_from_dict = CreateSubscriptionAPIResponse.from_dict(create_subscription_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


