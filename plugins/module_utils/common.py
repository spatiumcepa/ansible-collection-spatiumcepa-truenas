from __future__ import absolute_import, division, print_function
__metaclass__ = type


class HTTPMethod:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class HTTPCode:
    OK = 200
    NOT_FOUND = 404


class HTTPResponse:
    HTTP_METHOD = 'http_method'
    URL = 'url'
    REQUEST_BODY = 'request_body'
    STATUS_CODE = 'status_code'
    HEADERS = 'headers'
    BODY = 'body'


class TruenasModelError(Exception):
    """Raise when specified TrueNAS model is erroneous"""
    pass


class TruenasServerError(Exception):
    def __init__(self, response, code):
        super(TruenasServerError, self).__init__(response)
        self.response = response
        self.code = code


class TruenasUnexpectedResponse(Exception):
    """Raise when TrueNAS does not respond as expected"""
    pass


def strip_null_module_params(params):
    if params is None:
        raise TruenasModelError("Module params is null. Not expected.")
    return {k: v for k, v in params.items() if v is not None}
