# QuestionDatum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v** | **Dict[str, float]** | Construct a type with a set of properties K of type T | 
**total** | **int** |  | 

## Example

```python
from generated.models.question_datum import QuestionDatum

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionDatum from a JSON string
question_datum_instance = QuestionDatum.from_json(json)
# print the JSON string representation of the object
print(QuestionDatum.to_json())

# convert the object into a dict
question_datum_dict = question_datum_instance.to_dict()
# create an instance of QuestionDatum from a dict
question_datum_from_dict = QuestionDatum.from_dict(question_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


