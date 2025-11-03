# QueryPredicate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | [**QueryPredicateValue**](QueryPredicateValue.md) |  | 
**operator** | **str** |  | 

## Example

```python
from generated.models.query_predicate import QueryPredicate

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPredicate from a JSON string
query_predicate_instance = QueryPredicate.from_json(json)
# print the JSON string representation of the object
print(QueryPredicate.to_json())

# convert the object into a dict
query_predicate_dict = query_predicate_instance.to_dict()
# create an instance of QueryPredicate from a dict
query_predicate_from_dict = QueryPredicate.from_dict(query_predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


