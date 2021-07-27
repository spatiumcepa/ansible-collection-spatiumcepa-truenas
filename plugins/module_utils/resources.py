from __future__ import absolute_import, division, print_function
__metaclass__ = type

import copy
from functools import partial

from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPMethod, TruenasServerError, TruenasModelError, TruenasUnexpectedResponse


CHECKED_REQUEST_SUCCESS_CODE = 200


class TruenasResource(object):

    def __init__(self, conn, resource_path, resource_api_model, check_mode=False):
        self._conn = conn
        self._resource_path = resource_path
        self._resource_api_model = resource_api_model
        self._check_mode = check_mode

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
        if self._check_mode:
            return CHECKED_REQUEST_SUCCESS_CODE, {}, body_params
        return self._send_request(url_path, http_method, body_params, path_params, query_params)

    def _model_has_changes(self, existing_model, new_model):
        print("entered _model_has_changes")
        print(existing_model)
        print(new_model)
        exit(1)
        has_changes = False
        new_keys = new_model.keys()
        for new_key in new_keys:
            if new_key not in existing_model:
                raise TruenasModelError("Unknown model property %s" % (new_key))
            if existing_model[new_key] != new_model[new_key]:
                has_changes = True
        return has_changes

    def read(self):
        return self._send_request(HTTPMethod.GET, self._resource_path)

    def read_by_id(self, id):
        raise TruenasUnexpectedResponse("TODO : read_by_id()")

    def update(self, new_model):
        read_status, read_headers, read_data = self.read()
        existing_model = read_data
        self.resource_changed = self._model_has_changes(existing_model, new_model)

        response = self._send_checked_request(HTTPMethod.PUT, self._resource_path, new_model)
        return response

    def update_by_id(self, id):
        raise TruenasUnexpectedResponse("TODO : update_by_id()")


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
