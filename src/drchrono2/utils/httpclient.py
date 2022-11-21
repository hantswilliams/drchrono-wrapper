#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from . import exceptions


class HttpRequestBuilder:

    URL_TEMPLATE_WITHOUT_SUBDOMAINS = '{}://{}/{}'

    """
    A stateful HTTP URL, params and headers builder with a fluent interface
    """
    def __init__(self, root_uri_token, api_key):
        assert isinstance(root_uri_token, str)
        self.root = root_uri_token
        assert isinstance(api_key, str)
        self.api_key = api_key
        self.schema = None
        self.path = None
        self.params = {}
        self.headers = {}
        self._set_schema()

    def _set_schema(self):
        self.schema = 'https' 

    def with_path(self, path_uri_token):
        assert isinstance(path_uri_token, str)
        self.path = path_uri_token
        return self

    def with_headers(self, headers):
        assert isinstance(headers, dict)
        self.headers.update(headers)
        return self

    def with_header(self, key, value):
        assert isinstance(key, str)
        try:
            json.dumps(value)
        except TypeError:
            raise ValueError('Header value is not JSON serializable')
        self.headers.update({key: value})
        return self

    def with_query_params(self, query_params):
        assert isinstance(query_params, dict)
        self.params.update(query_params)
        return self

    def with_api_key(self):
        self.params['APPID'] = self.api_key
        return self

    def build(self):   
        return self.URL_TEMPLATE_WITHOUT_SUBDOMAINS.format(self.schema, self.root, self.path), \
                self.params

    def __repr__(self):
        return "<%s.%s>" % (__name__, self.__class__.__name__)


class HttpClient:

    """
    An HTTP client encapsulating some config data and abstarcting away data raw retrieval
    :param api_key: the OWM API key
    :type api_key: str
    :param root_uri: the root URI of the API endpoint
    :type root_uri: str
    """

    def __init__(self, api_key, root_uri):
        assert isinstance(api_key, str)
        self.api_key = api_key
        assert isinstance(root_uri, str)
        self.root_uri = root_uri        
        self.http = requests


    def get_json(self, path, params=None, headers=None):
        builder = HttpRequestBuilder(self.root_uri, self.api_key)\
            .with_path(path)\
            .with_api_key()\
            .with_query_params(params if params is not None else dict())\
            .with_headers(headers if headers is not None else dict())
        url, params, headers = builder.build()
        try:
            resp = self.http.get(url, params=params, headers=headers)
        except requests.exceptions.SSLError as e:
            raise exceptions.InvalidSSLCertificateError(str(e))
        except requests.exceptions.ConnectionError as e:
            raise exceptions.InvalidSSLCertificateError(str(e))
        except requests.exceptions.Timeout:
            raise exceptions.TimeoutError('API call timeouted')
        HttpClient.check_status_code(resp.status_code, resp.text)
        try:
            return resp.status_code, resp.json()
        except:
            raise exceptions.ParseAPIResponseError('Impossible to parse API response data')

    def post(self, path, params=None, data=None, headers=None):
        builder = HttpRequestBuilder(self.root_uri, self.api_key)\
            .with_path(path)\
            .with_api_key()\
            .with_query_params(params if params is not None else dict())\
            .with_headers(headers if headers is not None else dict())
        url, params, headers = builder.build()
        try:
            resp = self.http.post(url, params=params, json=data, headers=headers)
        except requests.exceptions.SSLError as e:
            raise exceptions.InvalidSSLCertificateError(str(e))
        except requests.exceptions.ConnectionError as e:
            raise exceptions.InvalidSSLCertificateError(str(e))
        except requests.exceptions.Timeout:
            raise exceptions.TimeoutError('API call timeouted')
        HttpClient.check_status_code(resp.status_code, resp.text)
        # this is a defense against OWM API responses containing an empty body!
        try:
            json_data = resp.json()
        except:
            json_data = {}
        return resp.status_code, json_data

    def put(self, path, params=None, data=None, headers=None):
        builder = HttpRequestBuilder(self.root_uri, self.api_key)\
            .with_path(path)\
            .with_api_key()\
            .with_query_params(params if params is not None else dict())\
            .with_headers(headers if headers is not None else dict())
        url, params, headers = builder.build()
        try:
            resp = self.http.put(url, params=params, json=data, headers=headers)
        except requests.exceptions.SSLError as e:
            raise exceptions.InvalidSSLCertificateError(str(e))
        except requests.exceptions.ConnectionError as e:
            raise exceptions.InvalidSSLCertificateError(str(e))
        except requests.exceptions.Timeout:
            raise exceptions.TimeoutError('API call timeouted')
        HttpClient.check_status_code(resp.status_code, resp.text)
        # this is a defense against OWM API responses containing an empty body!
        try:
            json_data = resp.json()
        except:
            json_data = {}
        return resp.status_code, json_data

    def delete(self, path, params=None, data=None, headers=None):
        builder = HttpRequestBuilder(self.root_uri, self.api_key)\
            .with_path(path)\
            .with_api_key()\
            .with_query_params(params if params is not None else dict())\
            .with_headers(headers if headers is not None else dict())
        url, params, headers = builder.build()
        try:
            resp = self.http.delete(url, params=params, json=data, headers=headers)
        except requests.exceptions.SSLError as e:
            raise exceptions.InvalidSSLCertificateError(str(e))
        except requests.exceptions.ConnectionError as e:
            raise exceptions.InvalidSSLCertificateError(str(e))
        except requests.exceptions.Timeout:
            raise exceptions.TimeoutError('API call timeouted')
        HttpClient.check_status_code(resp.status_code, resp.text)
        # this is a defense against OWM API responses containing an empty body!
        try:
            json_data = resp.json()
        except:
            json_data = None
        return resp.status_code, json_data

    @classmethod
    def check_status_code(cls, status_code, payload):
        if status_code < 400:
            return
        if status_code == 400 or status_code not in [401, 404, 502]:
            raise exceptions.APIRequestError(payload)
        elif status_code == 401:
            raise exceptions.UnauthorizedError('Invalid API Key provided')
        elif status_code == 404:
            raise exceptions.NotFoundError('Unable to find the resource')
        else:
            raise exceptions.BadGatewayError('Unable to contact the upstream server')

    def __repr__(self):
        return "<%s.%s - root: %s>" % (__name__, self.__class__.__name__, self.root_uri)