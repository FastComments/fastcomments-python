# QuestionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**url_id** | **str** |  | 
**anon_user_id** | **str** |  | 
**user_id** | **str** |  | 
**created_at** | **datetime** |  | 
**value** | **int** |  | 
**comment_id** | **str** |  | [optional] 
**question_id** | **str** |  | 
**meta** | [**List[MetaItem]**](MetaItem.md) |  | [optional] 
**ip_hash** | **str** |  | 

## Example

```python
from generated.models.question_result import QuestionResult

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionResult from a JSON string
question_result_instance = QuestionResult.from_json(json)
# print the JSON string representation of the object
print(QuestionResult.to_json())

# convert the object into a dict
question_result_dict = question_result_instance.to_dict()
# create an instance of QuestionResult from a dict
question_result_from_dict = QuestionResult.from_dict(question_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


