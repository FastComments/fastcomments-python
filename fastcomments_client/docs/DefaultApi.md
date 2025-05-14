# openapi_client.DefaultApi

All URIs are relative to *https://fastcomments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain_config**](DefaultApi.md#add_domain_config) | **POST** /api/v1/domain-configs | 
[**aggregate**](DefaultApi.md#aggregate) | **POST** /api/v1/aggregate | 
[**aggregate_question_results**](DefaultApi.md#aggregate_question_results) | **GET** /api/v1/question-results-aggregation | 
[**block_user_from_comment**](DefaultApi.md#block_user_from_comment) | **POST** /api/v1/comments/{id}/block | 
[**bulk_aggregate_question_results**](DefaultApi.md#bulk_aggregate_question_results) | **POST** /api/v1/question-results-aggregation/bulk | 
[**combine_comments_with_question_results**](DefaultApi.md#combine_comments_with_question_results) | **GET** /api/v1/question-results-aggregation/combine/comments | 
[**create_feed_post**](DefaultApi.md#create_feed_post) | **POST** /api/v1/feed-posts | 
[**delete_comment**](DefaultApi.md#delete_comment) | **DELETE** /api/v1/comments/{id} | 
[**delete_domain_config**](DefaultApi.md#delete_domain_config) | **DELETE** /api/v1/domain-configs/{domain} | 
[**flag_comment**](DefaultApi.md#flag_comment) | **POST** /api/v1/comments/{id}/flag | 
[**get_audit_logs**](DefaultApi.md#get_audit_logs) | **GET** /api/v1/audit-logs | 
[**get_comment**](DefaultApi.md#get_comment) | **GET** /api/v1/comments/{id} | 
[**get_comments**](DefaultApi.md#get_comments) | **GET** /api/v1/comments | 
[**get_domain_config**](DefaultApi.md#get_domain_config) | **GET** /api/v1/domain-configs/{domain} | 
[**get_domain_configs**](DefaultApi.md#get_domain_configs) | **GET** /api/v1/domain-configs | 
[**get_feed_posts**](DefaultApi.md#get_feed_posts) | **GET** /api/v1/feed-posts | 
[**patch_domain_config**](DefaultApi.md#patch_domain_config) | **PATCH** /api/v1/domain-configs/{domainToUpdate} | 
[**put_domain_config**](DefaultApi.md#put_domain_config) | **PUT** /api/v1/domain-configs/{domainToUpdate} | 
[**save_comment**](DefaultApi.md#save_comment) | **POST** /api/v1/comments | 
[**un_block_user_from_comment**](DefaultApi.md#un_block_user_from_comment) | **POST** /api/v1/comments/{id}/un-block | 
[**un_flag_comment**](DefaultApi.md#un_flag_comment) | **POST** /api/v1/comments/{id}/un-flag | 
[**update_comment**](DefaultApi.md#update_comment) | **PATCH** /api/v1/comments/{id} | 
[**update_feed_post**](DefaultApi.md#update_feed_post) | **PATCH** /api/v1/feed-posts/{id} | 


# **add_domain_config**
> AddDomainConfig200Response add_domain_config(tenant_id, add_domain_config_params)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.add_domain_config200_response import AddDomainConfig200Response
from openapi_client.models.add_domain_config_params import AddDomainConfigParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    add_domain_config_params = openapi_client.AddDomainConfigParams() # AddDomainConfigParams | 

    try:
        api_response = api_instance.add_domain_config(tenant_id, add_domain_config_params)
        print("The response of DefaultApi->add_domain_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_domain_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **add_domain_config_params** | [**AddDomainConfigParams**](AddDomainConfigParams.md)|  | 

### Return type

[**AddDomainConfig200Response**](AddDomainConfig200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate**
> AggregationResponse aggregate(tenant_id, aggregation_request, parent_tenant_id=parent_tenant_id, include_stats=include_stats)

Aggregates documents by grouping them (if groupBy is provided) and applying multiple operations.
Different operations (e.g. sum, countDistinct, avg, etc.) are supported.

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.aggregation_request import AggregationRequest
from openapi_client.models.aggregation_response import AggregationResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    aggregation_request = openapi_client.AggregationRequest() # AggregationRequest | 
    parent_tenant_id = 'parent_tenant_id_example' # str |  (optional)
    include_stats = True # bool |  (optional)

    try:
        api_response = api_instance.aggregate(tenant_id, aggregation_request, parent_tenant_id=parent_tenant_id, include_stats=include_stats)
        print("The response of DefaultApi->aggregate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->aggregate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)|  | 
 **parent_tenant_id** | **str**|  | [optional] 
 **include_stats** | **bool**|  | [optional] 

### Return type

[**AggregationResponse**](AggregationResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_question_results**
> AggregateQuestionResults200Response aggregate_question_results(tenant_id, question_id=question_id, question_ids=question_ids, url_id=url_id, time_bucket=time_bucket, start_date=start_date, force_recalculate=force_recalculate)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.aggregate_question_results200_response import AggregateQuestionResults200Response
from openapi_client.models.aggregate_time_bucket import AggregateTimeBucket
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    question_id = 'question_id_example' # str |  (optional)
    question_ids = ['question_ids_example'] # List[str] |  (optional)
    url_id = 'url_id_example' # str |  (optional)
    time_bucket = openapi_client.AggregateTimeBucket() # AggregateTimeBucket |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    force_recalculate = True # bool |  (optional)

    try:
        api_response = api_instance.aggregate_question_results(tenant_id, question_id=question_id, question_ids=question_ids, url_id=url_id, time_bucket=time_bucket, start_date=start_date, force_recalculate=force_recalculate)
        print("The response of DefaultApi->aggregate_question_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->aggregate_question_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **question_id** | **str**|  | [optional] 
 **question_ids** | [**List[str]**](str.md)|  | [optional] 
 **url_id** | **str**|  | [optional] 
 **time_bucket** | [**AggregateTimeBucket**](.md)|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **force_recalculate** | **bool**|  | [optional] 

### Return type

[**AggregateQuestionResults200Response**](AggregateQuestionResults200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_user_from_comment**
> BlockFromCommentPublic200Response block_user_from_comment(tenant_id, id, block_from_comment_params, user_id=user_id, anon_user_id=anon_user_id)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.block_from_comment_params import BlockFromCommentParams
from openapi_client.models.block_from_comment_public200_response import BlockFromCommentPublic200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    block_from_comment_params = openapi_client.BlockFromCommentParams() # BlockFromCommentParams | 
    user_id = 'user_id_example' # str |  (optional)
    anon_user_id = 'anon_user_id_example' # str |  (optional)

    try:
        api_response = api_instance.block_user_from_comment(tenant_id, id, block_from_comment_params, user_id=user_id, anon_user_id=anon_user_id)
        print("The response of DefaultApi->block_user_from_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->block_user_from_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **block_from_comment_params** | [**BlockFromCommentParams**](BlockFromCommentParams.md)|  | 
 **user_id** | **str**|  | [optional] 
 **anon_user_id** | **str**|  | [optional] 

### Return type

[**BlockFromCommentPublic200Response**](BlockFromCommentPublic200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_aggregate_question_results**
> BulkAggregateQuestionResults200Response bulk_aggregate_question_results(tenant_id, bulk_aggregate_question_results_request, force_recalculate=force_recalculate)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.bulk_aggregate_question_results200_response import BulkAggregateQuestionResults200Response
from openapi_client.models.bulk_aggregate_question_results_request import BulkAggregateQuestionResultsRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bulk_aggregate_question_results_request = openapi_client.BulkAggregateQuestionResultsRequest() # BulkAggregateQuestionResultsRequest | 
    force_recalculate = True # bool |  (optional)

    try:
        api_response = api_instance.bulk_aggregate_question_results(tenant_id, bulk_aggregate_question_results_request, force_recalculate=force_recalculate)
        print("The response of DefaultApi->bulk_aggregate_question_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_aggregate_question_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bulk_aggregate_question_results_request** | [**BulkAggregateQuestionResultsRequest**](BulkAggregateQuestionResultsRequest.md)|  | 
 **force_recalculate** | **bool**|  | [optional] 

### Return type

[**BulkAggregateQuestionResults200Response**](BulkAggregateQuestionResults200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combine_comments_with_question_results**
> CombineCommentsWithQuestionResults200Response combine_comments_with_question_results(tenant_id, question_id=question_id, question_ids=question_ids, url_id=url_id, start_date=start_date, force_recalculate=force_recalculate, min_value=min_value, max_value=max_value, limit=limit)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.combine_comments_with_question_results200_response import CombineCommentsWithQuestionResults200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    question_id = 'question_id_example' # str |  (optional)
    question_ids = ['question_ids_example'] # List[str] |  (optional)
    url_id = 'url_id_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    force_recalculate = True # bool |  (optional)
    min_value = 3.4 # float |  (optional)
    max_value = 3.4 # float |  (optional)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.combine_comments_with_question_results(tenant_id, question_id=question_id, question_ids=question_ids, url_id=url_id, start_date=start_date, force_recalculate=force_recalculate, min_value=min_value, max_value=max_value, limit=limit)
        print("The response of DefaultApi->combine_comments_with_question_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->combine_comments_with_question_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **question_id** | **str**|  | [optional] 
 **question_ids** | [**List[str]**](str.md)|  | [optional] 
 **url_id** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **force_recalculate** | **bool**|  | [optional] 
 **min_value** | **float**|  | [optional] 
 **max_value** | **float**|  | [optional] 
 **limit** | **float**|  | [optional] 

### Return type

[**CombineCommentsWithQuestionResults200Response**](CombineCommentsWithQuestionResults200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_feed_post**
> CreateFeedPost200Response create_feed_post(tenant_id, feed_post)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.create_feed_post200_response import CreateFeedPost200Response
from openapi_client.models.feed_post import FeedPost
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    feed_post = openapi_client.FeedPost() # FeedPost | 

    try:
        api_response = api_instance.create_feed_post(tenant_id, feed_post)
        print("The response of DefaultApi->create_feed_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_feed_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **feed_post** | [**FeedPost**](FeedPost.md)|  | 

### Return type

[**CreateFeedPost200Response**](CreateFeedPost200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> DeleteComment200Response delete_comment(tenant_id, id, context_user_id=context_user_id, is_live=is_live)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.delete_comment200_response import DeleteComment200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    context_user_id = 'context_user_id_example' # str |  (optional)
    is_live = True # bool |  (optional)

    try:
        api_response = api_instance.delete_comment(tenant_id, id, context_user_id=context_user_id, is_live=is_live)
        print("The response of DefaultApi->delete_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **context_user_id** | **str**|  | [optional] 
 **is_live** | **bool**|  | [optional] 

### Return type

[**DeleteComment200Response**](DeleteComment200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_config**
> DeleteDomainConfig200Response delete_domain_config(tenant_id, domain)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.delete_domain_config200_response import DeleteDomainConfig200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    domain = 'domain_example' # str | 

    try:
        api_response = api_instance.delete_domain_config(tenant_id, domain)
        print("The response of DefaultApi->delete_domain_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_domain_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **domain** | **str**|  | 

### Return type

[**DeleteDomainConfig200Response**](DeleteDomainConfig200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flag_comment**
> FlagComment200Response flag_comment(tenant_id, id, user_id=user_id, anon_user_id=anon_user_id)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.flag_comment200_response import FlagComment200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    anon_user_id = 'anon_user_id_example' # str |  (optional)

    try:
        api_response = api_instance.flag_comment(tenant_id, id, user_id=user_id, anon_user_id=anon_user_id)
        print("The response of DefaultApi->flag_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->flag_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **anon_user_id** | **str**|  | [optional] 

### Return type

[**FlagComment200Response**](FlagComment200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs**
> GetAuditLogs200Response get_audit_logs(tenant_id, limit=limit, skip=skip, order=order, after=after, before=before)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.get_audit_logs200_response import GetAuditLogs200Response
from openapi_client.models.sortdir import SORTDIR
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    limit = 3.4 # float |  (optional)
    skip = 3.4 # float |  (optional)
    order = openapi_client.SORTDIR() # SORTDIR |  (optional)
    after = 3.4 # float |  (optional)
    before = 3.4 # float |  (optional)

    try:
        api_response = api_instance.get_audit_logs(tenant_id, limit=limit, skip=skip, order=order, after=after, before=before)
        print("The response of DefaultApi->get_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **limit** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 
 **order** | [**SORTDIR**](.md)|  | [optional] 
 **after** | **float**|  | [optional] 
 **before** | **float**|  | [optional] 

### Return type

[**GetAuditLogs200Response**](GetAuditLogs200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> GetComment200Response get_comment(tenant_id, id)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.get_comment200_response import GetComment200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_comment(tenant_id, id)
        print("The response of DefaultApi->get_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GetComment200Response**](GetComment200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> GetComments200Response get_comments(tenant_id, page=page, limit=limit, skip=skip, as_tree=as_tree, skip_children=skip_children, limit_children=limit_children, max_tree_depth=max_tree_depth, url_id=url_id, user_id=user_id, anon_user_id=anon_user_id, context_user_id=context_user_id, hash_tag=hash_tag, parent_id=parent_id, direction=direction)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.get_comments200_response import GetComments200Response
from openapi_client.models.sort_directions import SortDirections
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    page = 3.4 # float |  (optional)
    limit = 3.4 # float |  (optional)
    skip = 3.4 # float |  (optional)
    as_tree = True # bool |  (optional)
    skip_children = 3.4 # float |  (optional)
    limit_children = 3.4 # float |  (optional)
    max_tree_depth = 3.4 # float |  (optional)
    url_id = 'url_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    anon_user_id = 'anon_user_id_example' # str |  (optional)
    context_user_id = 'context_user_id_example' # str |  (optional)
    hash_tag = 'hash_tag_example' # str |  (optional)
    parent_id = 'parent_id_example' # str |  (optional)
    direction = openapi_client.SortDirections() # SortDirections |  (optional)

    try:
        api_response = api_instance.get_comments(tenant_id, page=page, limit=limit, skip=skip, as_tree=as_tree, skip_children=skip_children, limit_children=limit_children, max_tree_depth=max_tree_depth, url_id=url_id, user_id=user_id, anon_user_id=anon_user_id, context_user_id=context_user_id, hash_tag=hash_tag, parent_id=parent_id, direction=direction)
        print("The response of DefaultApi->get_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **page** | **float**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 
 **as_tree** | **bool**|  | [optional] 
 **skip_children** | **float**|  | [optional] 
 **limit_children** | **float**|  | [optional] 
 **max_tree_depth** | **float**|  | [optional] 
 **url_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **anon_user_id** | **str**|  | [optional] 
 **context_user_id** | **str**|  | [optional] 
 **hash_tag** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 
 **direction** | [**SortDirections**](.md)|  | [optional] 

### Return type

[**GetComments200Response**](GetComments200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_config**
> GetDomainConfig200Response get_domain_config(tenant_id, domain)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.get_domain_config200_response import GetDomainConfig200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    domain = 'domain_example' # str | 

    try:
        api_response = api_instance.get_domain_config(tenant_id, domain)
        print("The response of DefaultApi->get_domain_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_domain_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **domain** | **str**|  | 

### Return type

[**GetDomainConfig200Response**](GetDomainConfig200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_configs**
> GetDomainConfigs200Response get_domain_configs(tenant_id)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.get_domain_configs200_response import GetDomainConfigs200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.get_domain_configs(tenant_id)
        print("The response of DefaultApi->get_domain_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_domain_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GetDomainConfigs200Response**](GetDomainConfigs200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_posts**
> GetFeedPosts200Response get_feed_posts(tenant_id, after_id=after_id, limit=limit, tags=tags)


req
tenantId
afterId

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.get_feed_posts200_response import GetFeedPosts200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    after_id = 'after_id_example' # str |  (optional)
    limit = 56 # int |  (optional)
    tags = ['tags_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.get_feed_posts(tenant_id, after_id=after_id, limit=limit, tags=tags)
        print("The response of DefaultApi->get_feed_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_feed_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **after_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **tags** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**GetFeedPosts200Response**](GetFeedPosts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_domain_config**
> GetDomainConfig200Response patch_domain_config(tenant_id, domain_to_update, patch_domain_config_params)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.get_domain_config200_response import GetDomainConfig200Response
from openapi_client.models.patch_domain_config_params import PatchDomainConfigParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    domain_to_update = 'domain_to_update_example' # str | 
    patch_domain_config_params = openapi_client.PatchDomainConfigParams() # PatchDomainConfigParams | 

    try:
        api_response = api_instance.patch_domain_config(tenant_id, domain_to_update, patch_domain_config_params)
        print("The response of DefaultApi->patch_domain_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_domain_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **domain_to_update** | **str**|  | 
 **patch_domain_config_params** | [**PatchDomainConfigParams**](PatchDomainConfigParams.md)|  | 

### Return type

[**GetDomainConfig200Response**](GetDomainConfig200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_domain_config**
> GetDomainConfig200Response put_domain_config(tenant_id, domain_to_update, update_domain_config_params)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.get_domain_config200_response import GetDomainConfig200Response
from openapi_client.models.update_domain_config_params import UpdateDomainConfigParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    domain_to_update = 'domain_to_update_example' # str | 
    update_domain_config_params = openapi_client.UpdateDomainConfigParams() # UpdateDomainConfigParams | 

    try:
        api_response = api_instance.put_domain_config(tenant_id, domain_to_update, update_domain_config_params)
        print("The response of DefaultApi->put_domain_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->put_domain_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **domain_to_update** | **str**|  | 
 **update_domain_config_params** | [**UpdateDomainConfigParams**](UpdateDomainConfigParams.md)|  | 

### Return type

[**GetDomainConfig200Response**](GetDomainConfig200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_comment**
> SaveComment200Response save_comment(tenant_id, create_comment_params, is_live=is_live, do_spam_check=do_spam_check, send_emails=send_emails, populate_notifications=populate_notifications)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.create_comment_params import CreateCommentParams
from openapi_client.models.save_comment200_response import SaveComment200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    create_comment_params = openapi_client.CreateCommentParams() # CreateCommentParams | 
    is_live = True # bool |  (optional)
    do_spam_check = True # bool |  (optional)
    send_emails = True # bool |  (optional)
    populate_notifications = True # bool |  (optional)

    try:
        api_response = api_instance.save_comment(tenant_id, create_comment_params, is_live=is_live, do_spam_check=do_spam_check, send_emails=send_emails, populate_notifications=populate_notifications)
        print("The response of DefaultApi->save_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->save_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **create_comment_params** | [**CreateCommentParams**](CreateCommentParams.md)|  | 
 **is_live** | **bool**|  | [optional] 
 **do_spam_check** | **bool**|  | [optional] 
 **send_emails** | **bool**|  | [optional] 
 **populate_notifications** | **bool**|  | [optional] 

### Return type

[**SaveComment200Response**](SaveComment200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_block_user_from_comment**
> UnBlockCommentPublic200Response un_block_user_from_comment(tenant_id, id, un_block_from_comment_params, user_id=user_id, anon_user_id=anon_user_id)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.un_block_comment_public200_response import UnBlockCommentPublic200Response
from openapi_client.models.un_block_from_comment_params import UnBlockFromCommentParams
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    un_block_from_comment_params = openapi_client.UnBlockFromCommentParams() # UnBlockFromCommentParams | 
    user_id = 'user_id_example' # str |  (optional)
    anon_user_id = 'anon_user_id_example' # str |  (optional)

    try:
        api_response = api_instance.un_block_user_from_comment(tenant_id, id, un_block_from_comment_params, user_id=user_id, anon_user_id=anon_user_id)
        print("The response of DefaultApi->un_block_user_from_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->un_block_user_from_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **un_block_from_comment_params** | [**UnBlockFromCommentParams**](UnBlockFromCommentParams.md)|  | 
 **user_id** | **str**|  | [optional] 
 **anon_user_id** | **str**|  | [optional] 

### Return type

[**UnBlockCommentPublic200Response**](UnBlockCommentPublic200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_flag_comment**
> FlagComment200Response un_flag_comment(tenant_id, id, user_id=user_id, anon_user_id=anon_user_id)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.flag_comment200_response import FlagComment200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    anon_user_id = 'anon_user_id_example' # str |  (optional)

    try:
        api_response = api_instance.un_flag_comment(tenant_id, id, user_id=user_id, anon_user_id=anon_user_id)
        print("The response of DefaultApi->un_flag_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->un_flag_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **anon_user_id** | **str**|  | [optional] 

### Return type

[**FlagComment200Response**](FlagComment200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> FlagCommentPublic200Response update_comment(tenant_id, id, body, context_user_id=context_user_id, do_spam_check=do_spam_check, is_live=is_live)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.flag_comment_public200_response import FlagCommentPublic200Response
from openapi_client.models.pick_api_comment_updatable_comment_fields import PickAPICommentUpdatableCommentFields
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    body = openapi_client.PickAPICommentUpdatableCommentFields() # PickAPICommentUpdatableCommentFields | 
    context_user_id = 'context_user_id_example' # str |  (optional)
    do_spam_check = True # bool |  (optional)
    is_live = True # bool |  (optional)

    try:
        api_response = api_instance.update_comment(tenant_id, id, body, context_user_id=context_user_id, do_spam_check=do_spam_check, is_live=is_live)
        print("The response of DefaultApi->update_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **body** | **PickAPICommentUpdatableCommentFields**|  | 
 **context_user_id** | **str**|  | [optional] 
 **do_spam_check** | **bool**|  | [optional] 
 **is_live** | **bool**|  | [optional] 

### Return type

[**FlagCommentPublic200Response**](FlagCommentPublic200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feed_post**
> FlagCommentPublic200Response update_feed_post(tenant_id, id, feed_post)

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.feed_post import FeedPost
from openapi_client.models.flag_comment_public200_response import FlagCommentPublic200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://fastcomments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    feed_post = openapi_client.FeedPost() # FeedPost | 

    try:
        api_response = api_instance.update_feed_post(tenant_id, id, feed_post)
        print("The response of DefaultApi->update_feed_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_feed_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **feed_post** | [**FeedPost**](FeedPost.md)|  | 

### Return type

[**FlagCommentPublic200Response**](FlagCommentPublic200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

