# UserBadge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**badge_id** | **str** |  | 
**from_tenant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**type** | **int** |  | 
**threshold** | **int** |  | 
**description** | **str** |  | 
**display_label** | **str** |  | 
**display_src** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**border_color** | **str** |  | [optional] 
**text_color** | **str** |  | [optional] 
**css_class** | **str** |  | [optional] 
**veteran_user_threshold_millis** | **int** |  | 
**displayed_on_comments** | **bool** |  | 
**received_at** | **datetime** |  | 
**order** | **int** |  | [optional] 

## Example

```python
from client.models.user_badge import UserBadge

# TODO update the JSON string below
json = "{}"
# create an instance of UserBadge from a JSON string
user_badge_instance = UserBadge.from_json(json)
# print the JSON string representation of the object
print(UserBadge.to_json())

# convert the object into a dict
user_badge_dict = user_badge_instance.to_dict()
# create an instance of UserBadge from a dict
user_badge_from_dict = UserBadge.from_dict(user_badge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


