# client.ModerationApi

All URIs are relative to *https://fastcomments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_moderation_vote**](ModerationApi.md#delete_moderation_vote) | **DELETE** /auth/my-account/moderate-comments/vote/{commentId}/{voteId} | 
[**get_api_comments**](ModerationApi.md#get_api_comments) | **GET** /auth/my-account/moderate-comments/api/comments | 
[**get_api_export_status**](ModerationApi.md#get_api_export_status) | **GET** /auth/my-account/moderate-comments/api/export/status | 
[**get_api_ids**](ModerationApi.md#get_api_ids) | **GET** /auth/my-account/moderate-comments/api/ids | 
[**get_ban_users_from_comment**](ModerationApi.md#get_ban_users_from_comment) | **GET** /auth/my-account/moderate-comments/ban-users/from-comment/{commentId} | 
[**get_comment_ban_status**](ModerationApi.md#get_comment_ban_status) | **GET** /auth/my-account/moderate-comments/get-comment-ban-status/{commentId} | 
[**get_comment_children**](ModerationApi.md#get_comment_children) | **GET** /auth/my-account/moderate-comments/comment-children/{commentId} | 
[**get_count**](ModerationApi.md#get_count) | **GET** /auth/my-account/moderate-comments/count | 
[**get_counts**](ModerationApi.md#get_counts) | **GET** /auth/my-account/moderate-comments/banned-users/counts | 
[**get_logs**](ModerationApi.md#get_logs) | **GET** /auth/my-account/moderate-comments/logs/{commentId} | 
[**get_manual_badges**](ModerationApi.md#get_manual_badges) | **GET** /auth/my-account/moderate-comments/get-manual-badges | 
[**get_manual_badges_for_user**](ModerationApi.md#get_manual_badges_for_user) | **GET** /auth/my-account/moderate-comments/get-manual-badges-for-user | 
[**get_moderation_comment**](ModerationApi.md#get_moderation_comment) | **GET** /auth/my-account/moderate-comments/comment/{commentId} | 
[**get_moderation_comment_text**](ModerationApi.md#get_moderation_comment_text) | **GET** /auth/my-account/moderate-comments/get-comment-text/{commentId} | 
[**get_pre_ban_summary**](ModerationApi.md#get_pre_ban_summary) | **GET** /auth/my-account/moderate-comments/pre-ban-summary/{commentId} | 
[**get_search_comments_summary**](ModerationApi.md#get_search_comments_summary) | **GET** /auth/my-account/moderate-comments/search/comments/summary | 
[**get_search_pages**](ModerationApi.md#get_search_pages) | **GET** /auth/my-account/moderate-comments/search/pages | 
[**get_search_sites**](ModerationApi.md#get_search_sites) | **GET** /auth/my-account/moderate-comments/search/sites | 
[**get_search_suggest**](ModerationApi.md#get_search_suggest) | **GET** /auth/my-account/moderate-comments/search/suggest | 
[**get_search_users**](ModerationApi.md#get_search_users) | **GET** /auth/my-account/moderate-comments/search/users | 
[**get_trust_factor**](ModerationApi.md#get_trust_factor) | **GET** /auth/my-account/moderate-comments/get-trust-factor | 
[**get_user_ban_preference**](ModerationApi.md#get_user_ban_preference) | **GET** /auth/my-account/moderate-comments/user-ban-preference | 
[**get_user_internal_profile**](ModerationApi.md#get_user_internal_profile) | **GET** /auth/my-account/moderate-comments/get-user-internal-profile | 
[**post_adjust_comment_votes**](ModerationApi.md#post_adjust_comment_votes) | **POST** /auth/my-account/moderate-comments/adjust-comment-votes/{commentId} | 
[**post_api_export**](ModerationApi.md#post_api_export) | **POST** /auth/my-account/moderate-comments/api/export | 
[**post_ban_user_from_comment**](ModerationApi.md#post_ban_user_from_comment) | **POST** /auth/my-account/moderate-comments/ban-user/from-comment/{commentId} | 
[**post_ban_user_undo**](ModerationApi.md#post_ban_user_undo) | **POST** /auth/my-account/moderate-comments/ban-user/undo | 
[**post_bulk_pre_ban_summary**](ModerationApi.md#post_bulk_pre_ban_summary) | **POST** /auth/my-account/moderate-comments/bulk-pre-ban-summary | 
[**post_comments_by_ids**](ModerationApi.md#post_comments_by_ids) | **POST** /auth/my-account/moderate-comments/comments-by-ids | 
[**post_flag_comment**](ModerationApi.md#post_flag_comment) | **POST** /auth/my-account/moderate-comments/flag-comment/{commentId} | 
[**post_remove_comment**](ModerationApi.md#post_remove_comment) | **POST** /auth/my-account/moderate-comments/remove-comment/{commentId} | 
[**post_restore_deleted_comment**](ModerationApi.md#post_restore_deleted_comment) | **POST** /auth/my-account/moderate-comments/restore-deleted-comment/{commentId} | 
[**post_set_comment_approval_status**](ModerationApi.md#post_set_comment_approval_status) | **POST** /auth/my-account/moderate-comments/set-comment-approval-status/{commentId} | 
[**post_set_comment_review_status**](ModerationApi.md#post_set_comment_review_status) | **POST** /auth/my-account/moderate-comments/set-comment-review-status/{commentId} | 
[**post_set_comment_spam_status**](ModerationApi.md#post_set_comment_spam_status) | **POST** /auth/my-account/moderate-comments/set-comment-spam-status/{commentId} | 
[**post_set_comment_text**](ModerationApi.md#post_set_comment_text) | **POST** /auth/my-account/moderate-comments/set-comment-text/{commentId} | 
[**post_un_flag_comment**](ModerationApi.md#post_un_flag_comment) | **POST** /auth/my-account/moderate-comments/un-flag-comment/{commentId} | 
[**post_vote**](ModerationApi.md#post_vote) | **POST** /auth/my-account/moderate-comments/vote/{commentId} | 
[**put_award_badge**](ModerationApi.md#put_award_badge) | **PUT** /auth/my-account/moderate-comments/award-badge | 
[**put_close_thread**](ModerationApi.md#put_close_thread) | **PUT** /auth/my-account/moderate-comments/close-thread | 
[**put_remove_badge**](ModerationApi.md#put_remove_badge) | **PUT** /auth/my-account/moderate-comments/remove-badge | 
[**put_reopen_thread**](ModerationApi.md#put_reopen_thread) | **PUT** /auth/my-account/moderate-comments/reopen-thread | 
[**set_trust_factor**](ModerationApi.md#set_trust_factor) | **PUT** /auth/my-account/moderate-comments/set-trust-factor | 


# **delete_moderation_vote**
> DeleteModerationVoteResponse delete_moderation_vote(comment_id, vote_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.delete_moderation_vote_response import DeleteModerationVoteResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    vote_id = 'vote_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.delete_moderation_vote(comment_id, vote_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->delete_moderation_vote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->delete_moderation_vote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **vote_id** | **str**|  | 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**DeleteModerationVoteResponse**](DeleteModerationVoteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_comments**
> GetApiCommentsResponse get_api_comments(page=page, count=count, text_search=text_search, by_ip_from_comment=by_ip_from_comment, filters=filters, search_filters=search_filters, sorts=sorts, demo=demo, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_api_comments_response import GetApiCommentsResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    page = 3.4 # float |  (optional)
    count = 3.4 # float |  (optional)
    text_search = 'text_search_example' # str |  (optional)
    by_ip_from_comment = 'by_ip_from_comment_example' # str |  (optional)
    filters = 'filters_example' # str |  (optional)
    search_filters = 'search_filters_example' # str |  (optional)
    sorts = 'sorts_example' # str |  (optional)
    demo = True # bool |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_api_comments(page=page, count=count, text_search=text_search, by_ip_from_comment=by_ip_from_comment, filters=filters, search_filters=search_filters, sorts=sorts, demo=demo, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_api_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_api_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] 
 **count** | **float**|  | [optional] 
 **text_search** | **str**|  | [optional] 
 **by_ip_from_comment** | **str**|  | [optional] 
 **filters** | **str**|  | [optional] 
 **search_filters** | **str**|  | [optional] 
 **sorts** | **str**|  | [optional] 
 **demo** | **bool**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetApiCommentsResponse**](GetApiCommentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_export_status**
> GetApiExportStatusResponse get_api_export_status(batch_job_id=batch_job_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_api_export_status_response import GetApiExportStatusResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    batch_job_id = 'batch_job_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_api_export_status(batch_job_id=batch_job_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_api_export_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_api_export_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_job_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetApiExportStatusResponse**](GetApiExportStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_ids**
> GetApiIdsResponse get_api_ids(text_search=text_search, by_ip_from_comment=by_ip_from_comment, filters=filters, search_filters=search_filters, after_id=after_id, demo=demo, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_api_ids_response import GetApiIdsResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    text_search = 'text_search_example' # str |  (optional)
    by_ip_from_comment = 'by_ip_from_comment_example' # str |  (optional)
    filters = 'filters_example' # str |  (optional)
    search_filters = 'search_filters_example' # str |  (optional)
    after_id = 'after_id_example' # str |  (optional)
    demo = True # bool |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_api_ids(text_search=text_search, by_ip_from_comment=by_ip_from_comment, filters=filters, search_filters=search_filters, after_id=after_id, demo=demo, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_api_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_api_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_search** | **str**|  | [optional] 
 **by_ip_from_comment** | **str**|  | [optional] 
 **filters** | **str**|  | [optional] 
 **search_filters** | **str**|  | [optional] 
 **after_id** | **str**|  | [optional] 
 **demo** | **bool**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetApiIdsResponse**](GetApiIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ban_users_from_comment**
> GetBanUsersFromCommentResponse get_ban_users_from_comment(comment_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_ban_users_from_comment_response import GetBanUsersFromCommentResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_ban_users_from_comment(comment_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_ban_users_from_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_ban_users_from_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetBanUsersFromCommentResponse**](GetBanUsersFromCommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_ban_status**
> GetCommentBanStatusResponse1 get_comment_ban_status(comment_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_comment_ban_status_response1 import GetCommentBanStatusResponse1
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_comment_ban_status(comment_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_comment_ban_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_comment_ban_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetCommentBanStatusResponse1**](GetCommentBanStatusResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_children**
> GetCommentChildrenResponse get_comment_children(comment_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_comment_children_response import GetCommentChildrenResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_comment_children(comment_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_comment_children:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_comment_children: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetCommentChildrenResponse**](GetCommentChildrenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count**
> GetCountResponse get_count(text_search=text_search, by_ip_from_comment=by_ip_from_comment, filter=filter, search_filters=search_filters, demo=demo, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_count_response import GetCountResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    text_search = 'text_search_example' # str |  (optional)
    by_ip_from_comment = 'by_ip_from_comment_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    search_filters = 'search_filters_example' # str |  (optional)
    demo = True # bool |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_count(text_search=text_search, by_ip_from_comment=by_ip_from_comment, filter=filter, search_filters=search_filters, demo=demo, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_search** | **str**|  | [optional] 
 **by_ip_from_comment** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **search_filters** | **str**|  | [optional] 
 **demo** | **bool**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetCountResponse**](GetCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_counts**
> GetCountsResponse get_counts(tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_counts_response import GetCountsResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_counts(tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_counts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_counts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetCountsResponse**](GetCountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> GetLogsResponse get_logs(comment_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_logs_response import GetLogsResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_logs(comment_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetLogsResponse**](GetLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_badges**
> GetManualBadgesResponse get_manual_badges(tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_manual_badges_response import GetManualBadgesResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_manual_badges(tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_manual_badges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_manual_badges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetManualBadgesResponse**](GetManualBadgesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_badges_for_user**
> GetManualBadgesForUserResponse get_manual_badges_for_user(badges_user_id=badges_user_id, comment_id=comment_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_manual_badges_for_user_response import GetManualBadgesForUserResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    badges_user_id = 'badges_user_id_example' # str |  (optional)
    comment_id = 'comment_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_manual_badges_for_user(badges_user_id=badges_user_id, comment_id=comment_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_manual_badges_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_manual_badges_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **badges_user_id** | **str**|  | [optional] 
 **comment_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetManualBadgesForUserResponse**](GetManualBadgesForUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_moderation_comment**
> GetModerationCommentResponse get_moderation_comment(comment_id, include_email=include_email, include_ip=include_ip, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_moderation_comment_response import GetModerationCommentResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    include_email = True # bool |  (optional)
    include_ip = True # bool |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_moderation_comment(comment_id, include_email=include_email, include_ip=include_ip, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_moderation_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_moderation_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **include_email** | **bool**|  | [optional] 
 **include_ip** | **bool**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetModerationCommentResponse**](GetModerationCommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_moderation_comment_text**
> GetModerationCommentTextResponse get_moderation_comment_text(comment_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_moderation_comment_text_response import GetModerationCommentTextResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_moderation_comment_text(comment_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_moderation_comment_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_moderation_comment_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetModerationCommentTextResponse**](GetModerationCommentTextResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pre_ban_summary**
> GetPreBanSummaryResponse get_pre_ban_summary(comment_id, include_by_user_id_and_email=include_by_user_id_and_email, include_by_ip=include_by_ip, include_by_email_domain=include_by_email_domain, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_pre_ban_summary_response import GetPreBanSummaryResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    include_by_user_id_and_email = True # bool |  (optional)
    include_by_ip = True # bool |  (optional)
    include_by_email_domain = True # bool |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_pre_ban_summary(comment_id, include_by_user_id_and_email=include_by_user_id_and_email, include_by_ip=include_by_ip, include_by_email_domain=include_by_email_domain, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_pre_ban_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_pre_ban_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **include_by_user_id_and_email** | **bool**|  | [optional] 
 **include_by_ip** | **bool**|  | [optional] 
 **include_by_email_domain** | **bool**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetPreBanSummaryResponse**](GetPreBanSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_comments_summary**
> GetSearchCommentsSummaryResponse get_search_comments_summary(value=value, filters=filters, search_filters=search_filters, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_search_comments_summary_response import GetSearchCommentsSummaryResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    value = 'value_example' # str |  (optional)
    filters = 'filters_example' # str |  (optional)
    search_filters = 'search_filters_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_search_comments_summary(value=value, filters=filters, search_filters=search_filters, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_search_comments_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_search_comments_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | [optional] 
 **filters** | **str**|  | [optional] 
 **search_filters** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetSearchCommentsSummaryResponse**](GetSearchCommentsSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_pages**
> GetSearchPagesResponse get_search_pages(value=value, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_search_pages_response import GetSearchPagesResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    value = 'value_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_search_pages(value=value, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_search_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_search_pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetSearchPagesResponse**](GetSearchPagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_sites**
> GetSearchSitesResponse get_search_sites(value=value, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_search_sites_response import GetSearchSitesResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    value = 'value_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_search_sites(value=value, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_search_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_search_sites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetSearchSitesResponse**](GetSearchSitesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_suggest**
> GetSearchSuggestResponse get_search_suggest(text_search=text_search, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_search_suggest_response import GetSearchSuggestResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    text_search = 'text_search_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_search_suggest(text_search=text_search, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_search_suggest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_search_suggest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_search** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetSearchSuggestResponse**](GetSearchSuggestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_users**
> GetSearchUsersResponse get_search_users(value=value, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_search_users_response import GetSearchUsersResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    value = 'value_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_search_users(value=value, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_search_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_search_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetSearchUsersResponse**](GetSearchUsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trust_factor**
> GetTrustFactorResponse get_trust_factor(user_id=user_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_trust_factor_response import GetTrustFactorResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    user_id = 'user_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_trust_factor(user_id=user_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_trust_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_trust_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetTrustFactorResponse**](GetTrustFactorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ban_preference**
> GetUserBanPreferenceResponse get_user_ban_preference(tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_user_ban_preference_response import GetUserBanPreferenceResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_user_ban_preference(tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_user_ban_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_user_ban_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetUserBanPreferenceResponse**](GetUserBanPreferenceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_internal_profile**
> GetUserInternalProfileResponse1 get_user_internal_profile(comment_id=comment_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.get_user_internal_profile_response1 import GetUserInternalProfileResponse1
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_user_internal_profile(comment_id=comment_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->get_user_internal_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_user_internal_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetUserInternalProfileResponse1**](GetUserInternalProfileResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_adjust_comment_votes**
> PostAdjustCommentVotesResponse post_adjust_comment_votes(comment_id, adjust_comment_votes_params, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.adjust_comment_votes_params import AdjustCommentVotesParams
from client.models.post_adjust_comment_votes_response import PostAdjustCommentVotesResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    adjust_comment_votes_params = client.AdjustCommentVotesParams() # AdjustCommentVotesParams | 
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_adjust_comment_votes(comment_id, adjust_comment_votes_params, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_adjust_comment_votes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_adjust_comment_votes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **adjust_comment_votes_params** | [**AdjustCommentVotesParams**](AdjustCommentVotesParams.md)|  | 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostAdjustCommentVotesResponse**](PostAdjustCommentVotesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_export**
> PostApiExportResponse post_api_export(text_search=text_search, by_ip_from_comment=by_ip_from_comment, filters=filters, search_filters=search_filters, sorts=sorts, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_api_export_response import PostApiExportResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    text_search = 'text_search_example' # str |  (optional)
    by_ip_from_comment = 'by_ip_from_comment_example' # str |  (optional)
    filters = 'filters_example' # str |  (optional)
    search_filters = 'search_filters_example' # str |  (optional)
    sorts = 'sorts_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_api_export(text_search=text_search, by_ip_from_comment=by_ip_from_comment, filters=filters, search_filters=search_filters, sorts=sorts, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_api_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_api_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_search** | **str**|  | [optional] 
 **by_ip_from_comment** | **str**|  | [optional] 
 **filters** | **str**|  | [optional] 
 **search_filters** | **str**|  | [optional] 
 **sorts** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostApiExportResponse**](PostApiExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ban_user_from_comment**
> PostBanUserFromCommentResponse post_ban_user_from_comment(comment_id, ban_email=ban_email, ban_email_domain=ban_email_domain, ban_ip=ban_ip, delete_all_users_comments=delete_all_users_comments, banned_until=banned_until, is_shadow_ban=is_shadow_ban, update_id=update_id, ban_reason=ban_reason, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_ban_user_from_comment_response import PostBanUserFromCommentResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    ban_email = True # bool |  (optional)
    ban_email_domain = True # bool |  (optional)
    ban_ip = True # bool |  (optional)
    delete_all_users_comments = True # bool |  (optional)
    banned_until = 'banned_until_example' # str |  (optional)
    is_shadow_ban = True # bool |  (optional)
    update_id = 'update_id_example' # str |  (optional)
    ban_reason = 'ban_reason_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_ban_user_from_comment(comment_id, ban_email=ban_email, ban_email_domain=ban_email_domain, ban_ip=ban_ip, delete_all_users_comments=delete_all_users_comments, banned_until=banned_until, is_shadow_ban=is_shadow_ban, update_id=update_id, ban_reason=ban_reason, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_ban_user_from_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_ban_user_from_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **ban_email** | **bool**|  | [optional] 
 **ban_email_domain** | **bool**|  | [optional] 
 **ban_ip** | **bool**|  | [optional] 
 **delete_all_users_comments** | **bool**|  | [optional] 
 **banned_until** | **str**|  | [optional] 
 **is_shadow_ban** | **bool**|  | [optional] 
 **update_id** | **str**|  | [optional] 
 **ban_reason** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostBanUserFromCommentResponse**](PostBanUserFromCommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ban_user_undo**
> PostBanUserUndoResponse post_ban_user_undo(ban_user_undo_params, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.ban_user_undo_params import BanUserUndoParams
from client.models.post_ban_user_undo_response import PostBanUserUndoResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    ban_user_undo_params = client.BanUserUndoParams() # BanUserUndoParams | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_ban_user_undo(ban_user_undo_params, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_ban_user_undo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_ban_user_undo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ban_user_undo_params** | [**BanUserUndoParams**](BanUserUndoParams.md)|  | 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostBanUserUndoResponse**](PostBanUserUndoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bulk_pre_ban_summary**
> PostBulkPreBanSummaryResponse post_bulk_pre_ban_summary(bulk_pre_ban_params, include_by_user_id_and_email=include_by_user_id_and_email, include_by_ip=include_by_ip, include_by_email_domain=include_by_email_domain, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.bulk_pre_ban_params import BulkPreBanParams
from client.models.post_bulk_pre_ban_summary_response import PostBulkPreBanSummaryResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    bulk_pre_ban_params = client.BulkPreBanParams() # BulkPreBanParams | 
    include_by_user_id_and_email = True # bool |  (optional)
    include_by_ip = True # bool |  (optional)
    include_by_email_domain = True # bool |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_bulk_pre_ban_summary(bulk_pre_ban_params, include_by_user_id_and_email=include_by_user_id_and_email, include_by_ip=include_by_ip, include_by_email_domain=include_by_email_domain, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_bulk_pre_ban_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_bulk_pre_ban_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_pre_ban_params** | [**BulkPreBanParams**](BulkPreBanParams.md)|  | 
 **include_by_user_id_and_email** | **bool**|  | [optional] 
 **include_by_ip** | **bool**|  | [optional] 
 **include_by_email_domain** | **bool**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostBulkPreBanSummaryResponse**](PostBulkPreBanSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_comments_by_ids**
> PostCommentsByIdsResponse post_comments_by_ids(comments_by_ids_params, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.comments_by_ids_params import CommentsByIdsParams
from client.models.post_comments_by_ids_response import PostCommentsByIdsResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comments_by_ids_params = client.CommentsByIdsParams() # CommentsByIdsParams | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_comments_by_ids(comments_by_ids_params, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_comments_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_comments_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_by_ids_params** | [**CommentsByIdsParams**](CommentsByIdsParams.md)|  | 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostCommentsByIdsResponse**](PostCommentsByIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_flag_comment**
> PostFlagCommentResponse post_flag_comment(comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_flag_comment_response import PostFlagCommentResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_flag_comment(comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_flag_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_flag_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostFlagCommentResponse**](PostFlagCommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_remove_comment**
> PostRemoveCommentResponse post_remove_comment(comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_remove_comment_response import PostRemoveCommentResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_remove_comment(comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_remove_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_remove_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostRemoveCommentResponse**](PostRemoveCommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_restore_deleted_comment**
> PostRestoreDeletedCommentResponse post_restore_deleted_comment(comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_restore_deleted_comment_response import PostRestoreDeletedCommentResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_restore_deleted_comment(comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_restore_deleted_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_restore_deleted_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostRestoreDeletedCommentResponse**](PostRestoreDeletedCommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_set_comment_approval_status**
> PostSetCommentApprovalStatusResponse post_set_comment_approval_status(comment_id, approved=approved, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_set_comment_approval_status_response import PostSetCommentApprovalStatusResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    approved = True # bool |  (optional)
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_set_comment_approval_status(comment_id, approved=approved, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_set_comment_approval_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_set_comment_approval_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **approved** | **bool**|  | [optional] 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostSetCommentApprovalStatusResponse**](PostSetCommentApprovalStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_set_comment_review_status**
> PostSetCommentReviewStatusResponse post_set_comment_review_status(comment_id, reviewed=reviewed, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_set_comment_review_status_response import PostSetCommentReviewStatusResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    reviewed = True # bool |  (optional)
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_set_comment_review_status(comment_id, reviewed=reviewed, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_set_comment_review_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_set_comment_review_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **reviewed** | **bool**|  | [optional] 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostSetCommentReviewStatusResponse**](PostSetCommentReviewStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_set_comment_spam_status**
> PostSetCommentSpamStatusResponse post_set_comment_spam_status(comment_id, spam=spam, perm_not_spam=perm_not_spam, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_set_comment_spam_status_response import PostSetCommentSpamStatusResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    spam = True # bool |  (optional)
    perm_not_spam = True # bool |  (optional)
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_set_comment_spam_status(comment_id, spam=spam, perm_not_spam=perm_not_spam, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_set_comment_spam_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_set_comment_spam_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **spam** | **bool**|  | [optional] 
 **perm_not_spam** | **bool**|  | [optional] 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostSetCommentSpamStatusResponse**](PostSetCommentSpamStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_set_comment_text**
> PostSetCommentTextResponse post_set_comment_text(comment_id, set_comment_text_params, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_set_comment_text_response import PostSetCommentTextResponse
from client.models.set_comment_text_params import SetCommentTextParams
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    set_comment_text_params = client.SetCommentTextParams() # SetCommentTextParams | 
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_set_comment_text(comment_id, set_comment_text_params, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_set_comment_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_set_comment_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **set_comment_text_params** | [**SetCommentTextParams**](SetCommentTextParams.md)|  | 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostSetCommentTextResponse**](PostSetCommentTextResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_un_flag_comment**
> PostUnFlagCommentResponse post_un_flag_comment(comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_un_flag_comment_response import PostUnFlagCommentResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_un_flag_comment(comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_un_flag_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_un_flag_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostUnFlagCommentResponse**](PostUnFlagCommentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_vote**
> PostVoteResponse post_vote(comment_id, direction=direction, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.post_vote_response import PostVoteResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    comment_id = 'comment_id_example' # str | 
    direction = 'direction_example' # str |  (optional)
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.post_vote(comment_id, direction=direction, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->post_vote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->post_vote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **direction** | **str**|  | [optional] 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PostVoteResponse**](PostVoteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_award_badge**
> PutAwardBadgeResponse put_award_badge(badge_id, user_id=user_id, comment_id=comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.put_award_badge_response import PutAwardBadgeResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    badge_id = 'badge_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    comment_id = 'comment_id_example' # str |  (optional)
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.put_award_badge(badge_id, user_id=user_id, comment_id=comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->put_award_badge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->put_award_badge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **badge_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **comment_id** | **str**|  | [optional] 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PutAwardBadgeResponse**](PutAwardBadgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_close_thread**
> PutCloseThreadResponse put_close_thread(url_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.put_close_thread_response import PutCloseThreadResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    url_id = 'url_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.put_close_thread(url_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->put_close_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->put_close_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PutCloseThreadResponse**](PutCloseThreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_remove_badge**
> PutRemoveBadgeResponse put_remove_badge(badge_id, user_id=user_id, comment_id=comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.put_remove_badge_response import PutRemoveBadgeResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    badge_id = 'badge_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    comment_id = 'comment_id_example' # str |  (optional)
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.put_remove_badge(badge_id, user_id=user_id, comment_id=comment_id, broadcast_id=broadcast_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->put_remove_badge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->put_remove_badge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **badge_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **comment_id** | **str**|  | [optional] 
 **broadcast_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PutRemoveBadgeResponse**](PutRemoveBadgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reopen_thread**
> PutReopenThreadResponse put_reopen_thread(url_id, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.put_reopen_thread_response import PutReopenThreadResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    url_id = 'url_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.put_reopen_thread(url_id, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->put_reopen_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->put_reopen_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**PutReopenThreadResponse**](PutReopenThreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_trust_factor**
> SetTrustFactorResponse set_trust_factor(user_id=user_id, trust_factor=trust_factor, tenant_id=tenant_id, sso=sso)



### Example


```python
import client
from client.models.set_trust_factor_response import SetTrustFactorResponse
from client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = client.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client.ModerationApi(api_client)
    user_id = 'user_id_example' # str |  (optional)
    trust_factor = 'trust_factor_example' # str |  (optional)
    tenant_id = 'tenant_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.set_trust_factor(user_id=user_id, trust_factor=trust_factor, tenant_id=tenant_id, sso=sso)
        print("The response of ModerationApi->set_trust_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->set_trust_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
 **trust_factor** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**SetTrustFactorResponse**](SetTrustFactorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

