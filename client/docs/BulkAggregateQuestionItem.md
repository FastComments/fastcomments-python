# BulkAggregateQuestionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agg_id** | **str** |  | 
**question_id** | **str** |  | [optional] 
**question_ids** | **List[str]** |  | [optional] 
**url_id** | **str** |  | [optional] 
**time_bucket** | [**AggregateTimeBucket**](AggregateTimeBucket.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.bulk_aggregate_question_item import BulkAggregateQuestionItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAggregateQuestionItem from a JSON string
bulk_aggregate_question_item_instance = BulkAggregateQuestionItem.from_json(json)
# print the JSON string representation of the object
print(BulkAggregateQuestionItem.to_json())

# convert the object into a dict
bulk_aggregate_question_item_dict = bulk_aggregate_question_item_instance.to_dict()
# create an instance of BulkAggregateQuestionItem from a dict
bulk_aggregate_question_item_from_dict = BulkAggregateQuestionItem.from_dict(bulk_aggregate_question_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


