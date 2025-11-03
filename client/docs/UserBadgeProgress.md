# UserBadgeProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**user_id** | **str** |  | 
**first_comment_id** | **str** |  | 
**first_comment_date** | **datetime** |  | 
**auto_trust_factor** | **float** |  | [optional] 
**manual_trust_factor** | **float** |  | [optional] 
**progress** | **Dict[str, float]** | Construct a type with a set of properties K of type T | 

## Example

```python
from generated.models.user_badge_progress import UserBadgeProgress

# TODO update the JSON string below
json = "{}"
# create an instance of UserBadgeProgress from a JSON string
user_badge_progress_instance = UserBadgeProgress.from_json(json)
# print the JSON string representation of the object
print(UserBadgeProgress.to_json())

# convert the object into a dict
user_badge_progress_dict = user_badge_progress_instance.to_dict()
# create an instance of UserBadgeProgress from a dict
user_badge_progress_from_dict = UserBadgeProgress.from_dict(user_badge_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


