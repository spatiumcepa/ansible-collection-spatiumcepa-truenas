class HTTPMethod:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'

class TruenasServerError(Exception):
    def __init__(self, response, code):
        super(TruenasServerError, self).__init__(response)
        self.response = response
        self.code = code

class TruenasModelError(Exception):
    def __init__(self, response, code):
        super(TruenasServerError, self).__init__(response)
        self.response = response
        self.code = code

class TruenasUnexpectedResponse(Exception):
    """Raise when TrueNAS does not respond as expected"""
    pass
