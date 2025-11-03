# DeleteSubscriptionAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from client.models.delete_subscription_api_response import DeleteSubscriptionAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSubscriptionAPIResponse from a JSON string
delete_subscription_api_response_instance = DeleteSubscriptionAPIResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteSubscriptionAPIResponse.to_json())

# convert the object into a dict
delete_subscription_api_response_dict = delete_subscription_api_response_instance.to_dict()
# create an instance of DeleteSubscriptionAPIResponse from a dict
delete_subscription_api_response_from_dict = DeleteSubscriptionAPIResponse.from_dict(delete_subscription_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


