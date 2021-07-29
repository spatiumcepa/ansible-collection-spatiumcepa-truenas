from __future__ import absolute_import, division, print_function
__metaclass__ = type

import copy
from functools import partial

from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPMethod, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse


CHECKED_REQUEST_SUCCESS_CODE = 200


class TruenasResource(object):

    RESOURCE_API_MODEL = 'model_name_not_defined'

    def __init__(self, conn, resource_path, resource_api_model, check_mode=False):
        self._conn = conn
        self._resource_path = resource_path
        self._resource_api_model = resource_api_model
        self._check_mode = check_mode

        self._existing_model = None

        self.resource_changed = False

    def _send_request(self, http_method, url_path, body_params=None, path_params=None, query_params=None):
        return self._conn.send_request(
            http_method=http_method,
            url_path=url_path,
            body_params=body_params,
            path_params=path_params,
            query_params=query_params
        )

    def _send_checked_request(self, http_method, url_path, body_params=None, path_params=None, query_params=None):
        # if we are in check_mode, respond with mocked response
        if self._check_mode:
            return self._mocked_response()

        return self._send_request(http_method, url_path, body_params, path_params, query_params)

    def _mocked_response(self):
        if self._existing_model is None:
            raise TruenasModelError("No existing model to return for mocked response. Code branching bug?")
        return {
            HTTPResponse.STATUS_CODE: CHECKED_REQUEST_SUCCESS_CODE,
            HTTPResponse.HEADERS: {'truenas-api-mocked-response': True},
            HTTPResponse.BODY: self._existing_model,
        }

    def _model_has_changes(self, existing_model, new_model):
        has_changes = False
        new_keys = new_model.keys()
        for new_key in new_keys:
            if new_key not in existing_model:
                # some fields defined in an API schema are not returned to spec
                # I infer this happens for fields that were moved to a different endpoint
                # complain via exception: the resolution is to move the field to the "current" endpoint that does expect and return the field
                # examples of this are sysloglevel and syslogserver seem to have moved to system/advanced
                # and as of 12.0 API are in both system_general_update_0 and system_advanced_update_0 OAS specs
                # the way role implementers should fix their model definitions is to migrate the properties that moved to their new endpoint model for submission there
                raise TruenasModelError("Server did not return model property %s - check API schema %s" % (new_key, self.RESOURCE_API_MODEL))
            elif existing_model[new_key] == {} and new_model[new_key] is None:
                # consider existing empty dict and arg spec defaulted dict None equal
                # endpoints return empty complex types as {}
                pass
            elif existing_model[new_key] != new_model[new_key]:
                has_changes = True
        return has_changes

    def read(self):
        return self._send_request(HTTPMethod.GET, self._resource_path)

    def read_by_id(self, id):
        raise TruenasUnexpectedResponse("TODO : read_by_id()")

    def update(self, new_model):
        read_response = self.read()
        self._existing_model = read_response[HTTPResponse.BODY]
        self.resource_changed = self._model_has_changes(self._existing_model, new_model)

        # if there are no detected changes,
        # return the read response and skip the API update call
        # this ensures that configuration reloads and service restarts that middlewared enforces are not invoked unnecessarily
        if not self.resource_changed:
            return read_response

        return self._send_checked_request(HTTPMethod.PUT, self._resource_path, new_model)

    def update_by_id(self, id):
        raise TruenasUnexpectedResponse("TODO : update_by_id()")


class TruenasMail(TruenasResource):

    RESOURCE_PATH = '/mail'
    RESOURCE_API_MODEL = 'mail_update'

    def __init__(self, conn, check_mode=False):
        super(TruenasMail, self).__init__(
            conn,
            self.RESOURCE_PATH,
            self.RESOURCE_API_MODEL,
            check_mode
        )


class TruenasSystemGeneral(TruenasResource):

    RESOURCE_PATH = '/system/general'
    RESOURCE_API_MODEL = 'general_settings'

    def __init__(self, conn, check_mode=False):
        super(TruenasSystemGeneral, self).__init__(
            conn,
            self.RESOURCE_PATH,
            self.RESOURCE_API_MODEL,
            check_mode
        )


class TruenasSystemAdvanced(TruenasResource):

    RESOURCE_PATH = '/system/advanced'
    RESOURCE_API_MODEL = 'system_advanced_update'

    def __init__(self, conn, check_mode=False):
        super(TruenasSystemAdvanced, self).__init__(
            conn,
            self.RESOURCE_PATH,
            self.RESOURCE_API_MODEL,
            check_mode
        )


class TruenasSystemState(TruenasResource):

    RESOURCE_PATH = '/system/state'
    RESOURCE_API_MODEL = 'json_string'

    def __init__(self, conn, check_mode=False):
        super(TruenasSystemState, self).__init__(
            conn,
            self.RESOURCE_PATH,
            self.RESOURCE_API_MODEL,
            check_mode
        )
