# coding: utf-8

"""
    qTest Manager API Version 8.6 - 9.0

    qTest Manager API Version 8.6 - 9.0

    OpenAPI spec version: 8.6 - 9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ProjectApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_project(self, body, **kwargs):
        """
        Creates a Project
        To create a new Project  <strong>qTest Manager version:</strong> 4+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_project(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ProjectResource body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_project_with_http_info(body, **kwargs)
        else:
            (data) = self.create_project_with_http_info(body, **kwargs)
            return data

    def create_project_with_http_info(self, body, **kwargs):
        """
        Creates a Project
        To create a new Project  <strong>qTest Manager version:</strong> 4+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_project_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ProjectResource body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_project`")


        collection_formats = {}

        resource_path = '/api/v3/projects'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_current_profile(self, project_id, **kwargs):
        """
        Gets current user Permissions in a Project
        To retrieve your Permissions in a Project  <strong>qTest Manager version:</strong> 4+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_current_profile(project_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int project_id: ID of the project (required)
        :return: UserProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_current_profile_with_http_info(project_id, **kwargs)
        else:
            (data) = self.get_current_profile_with_http_info(project_id, **kwargs)
            return data

    def get_current_profile_with_http_info(self, project_id, **kwargs):
        """
        Gets current user Permissions in a Project
        To retrieve your Permissions in a Project  <strong>qTest Manager version:</strong> 4+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_current_profile_with_http_info(project_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int project_id: ID of the project (required)
        :return: UserProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_current_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params) or (params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_current_profile`")


        collection_formats = {}

        resource_path = '/api/v3/projects/{projectId}/user-profiles/current'.replace('{format}', 'json')
        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UserProfile',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_project(self, project_id, **kwargs):
        """
        Gets a Project
        To retrieve a specific Project
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_project(project_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int project_id: ID of the project (required)
        :param str expand: <em>expand=userprofile</em> - include the your profile and permissions within the project in the response
        :return: ProjectResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_project_with_http_info(project_id, **kwargs)
        else:
            (data) = self.get_project_with_http_info(project_id, **kwargs)
            return data

    def get_project_with_http_info(self, project_id, **kwargs):
        """
        Gets a Project
        To retrieve a specific Project
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_project_with_http_info(project_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int project_id: ID of the project (required)
        :param str expand: <em>expand=userprofile</em> - include the your profile and permissions within the project in the response
        :return: ProjectResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'expand']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params) or (params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_project`")


        collection_formats = {}

        resource_path = '/api/v3/projects/{projectId}'.replace('{format}', 'json')
        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ProjectResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_projects(self, **kwargs):
        """
        Gets multiple Projects
        To retrieve all Projects which the requested qTest  Manager account can access to  <strong>qTest Manager version:</strong> 4+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_projects(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str expand: <em>expand=userprofile</em> - to include your profile and permissions in each project
        :param bool assigned: <em>assigned=true</em> - default value. Only the projects which the requested user has access to  <em>assigned=false</em> - Users with admin profile can use this value to retrieve all projects, regardless of having access
        :return: list[ProjectResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_projects_with_http_info(**kwargs)
        else:
            (data) = self.get_projects_with_http_info(**kwargs)
            return data

    def get_projects_with_http_info(self, **kwargs):
        """
        Gets multiple Projects
        To retrieve all Projects which the requested qTest  Manager account can access to  <strong>qTest Manager version:</strong> 4+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_projects_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str expand: <em>expand=userprofile</em> - to include your profile and permissions in each project
        :param bool assigned: <em>assigned=true</em> - default value. Only the projects which the requested user has access to  <em>assigned=false</em> - Users with admin profile can use this value to retrieve all projects, regardless of having access
        :return: list[ProjectResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expand', 'assigned']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_projects" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/v3/projects'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'assigned' in params:
            query_params['assigned'] = params['assigned']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ProjectResource]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_users(self, project_id, **kwargs):
        """
        Gets all Users in a Project
        To retrieve all members in a qTest Manager Project  <strong>qTest Manager version:</strong> 8.4.2+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_users(project_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int project_id: ID of the project (required)
        :param bool inactive: <em>inactive=false</em> - default value. Inactive users are excluded from the response  <em>inactive=true</em> - inactive users are included in the response
        :return: list[UserResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_users_with_http_info(project_id, **kwargs)
        else:
            (data) = self.get_users_with_http_info(project_id, **kwargs)
            return data

    def get_users_with_http_info(self, project_id, **kwargs):
        """
        Gets all Users in a Project
        To retrieve all members in a qTest Manager Project  <strong>qTest Manager version:</strong> 8.4.2+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_users_with_http_info(project_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int project_id: ID of the project (required)
        :param bool inactive: <em>inactive=false</em> - default value. Inactive users are excluded from the response  <em>inactive=true</em> - inactive users are included in the response
        :return: list[UserResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'inactive']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params) or (params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_users`")


        collection_formats = {}

        resource_path = '/api/v3/projects/{projectId}/users'.replace('{format}', 'json')
        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']

        query_params = {}
        if 'inactive' in params:
            query_params['inactive'] = params['inactive']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[UserResource]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
