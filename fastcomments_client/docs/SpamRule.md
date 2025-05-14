# SpamRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **List[str]** |  | 
**comment_contains** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.spam_rule import SpamRule

# TODO update the JSON string below
json = "{}"
# create an instance of SpamRule from a JSON string
spam_rule_instance = SpamRule.from_json(json)
# print the JSON string representation of the object
print(SpamRule.to_json())

# convert the object into a dict
spam_rule_dict = spam_rule_instance.to_dict()
# create an instance of SpamRule from a dict
spam_rule_from_dict = SpamRule.from_dict(spam_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


