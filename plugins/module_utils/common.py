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
