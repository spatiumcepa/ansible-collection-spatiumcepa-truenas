from __future__ import absolute_import, division, print_function
__metaclass__ = type

import copy
from functools import partial

from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPMethod, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse


class TruenasResource(object):

    RESOURCE_API_MODEL = 'RESOURCE_API_MODEL_NOT_SET'
    _RESOURCE_PATH = None
    _RESOURCE_ITEM_PATH = None
    RESOURCE_ITEM_ID_FIELD = 'id'
    RESOURCE_SEARCH_FIELD = 'RESOURCE_SEARCH_FIELD_NOT_SET'

    def __init__(self, conn, check_mode=False):
        self._conn = conn
        self._check_mode = check_mode

        self.resource_changed = False
        self.resource_created = False
        self.resource_deleted = False

    def _send_request(self, http_method, url_path, body_params=None, path_params=None, query_params=None):
        response = self._conn.send_request(
            http_method=http_method,
            url_path=url_path,
            body_params=body_params,
            path_params=path_params,
            query_params=query_params
        )
        return response

    def _send_checked_request(self, existing_model, http_method, url_path, body_params=None, path_params=None, query_params=None):
        # if we are in check_mode, respond with mocked response
        if self._check_mode:
            return self._mocked_response(existing_model)

        return self._send_request(http_method, url_path, body_params, path_params, query_params)

    def _mocked_response(self, existing_model):
        if existing_model is None:
            raise TruenasModelError("Existing model to return for mocked response is null. Bug?")
        return {
            HTTPResponse.STATUS_CODE: HTTPCode.OK,
            HTTPResponse.HEADERS: {'ansible-simulated-response': True},
            HTTPResponse.BODY: existing_model,
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
                # the way role implementers should fix their model definitions is to migrate the fields to their new endpoint model for submission
                raise TruenasModelError("Server did not return model field %s - check API schema arg spec for %s" % (new_key, self.RESOURCE_API_MODEL))
            elif existing_model[new_key] == {} and new_model[new_key] is None:
                # consider existing empty dict and arg spec defaulted dict None equal
                # endpoints return empty complex types as {}
                continue
            elif existing_model[new_key] != new_model[new_key]:
                has_changes = True
        return has_changes

    def create(self, new_model):
        existing_model = new_model
        create_response = self._send_checked_request(existing_model, HTTPMethod.POST, self._RESOURCE_PATH, new_model)
        self.resource_changed = create_response[HTTPResponse.STATUS_CODE] == HTTPCode.OK
        self.resource_created = self.resource_changed
        return create_response

    def read(self):
        return self._send_request(HTTPMethod.GET, self._RESOURCE_PATH)

    def read_item_by_id(self, id):
        if self._RESOURCE_ITEM_PATH is None:
            raise TruenasModelError("resource item path not set. required for read_item() operations")
        return self._send_request(HTTPMethod.GET, self._RESOURCE_ITEM_PATH.format(id=id))

    def find_item(self, model):
        found_item = None
        response = {
            HTTPResponse.STATUS_CODE: HTTPCode.NOT_FOUND,
            HTTPResponse.HEADERS: {'ansible-simulated-response': True},
            HTTPResponse.BODY: None,
        }
        if self.RESOURCE_SEARCH_FIELD not in model.keys():
            raise TruenasModelError(
                "Specified model parameter does not contain RESOURCE_SEARCH_FIELD %s" % (self.RESOURCE_SEARCH_FIELD)
            )
        search_field_value = model[self.RESOURCE_SEARCH_FIELD]
        read_response = self.read()
        item_list = read_response[HTTPResponse.BODY]
        for item in item_list:
            if self.RESOURCE_SEARCH_FIELD not in item.keys():
                raise TruenasModelError(
                    "find item candidate does not have field RESOURCE_SEARCH_FIELD %s" % (self.RESOURCE_SEARCH_FIELD)
                )
            if item[self.RESOURCE_SEARCH_FIELD] == search_field_value:
                if found_item is not None:
                    raise TruenasModelError(
                        "Found more than one item with RESOURCE_SEARCH_FIELD %s having value %s - is the item value for the field unique ?" % (
                            self.RESOURCE_SEARCH_FIELD, search_field_value)
                    )
                found_item = item
                response[HTTPResponse.STATUS_CODE] = HTTPCode.OK
                response[HTTPResponse.BODY] = item
                break
        return response

    def update(self, new_model):
        read_response = self.read()
        existing_model = read_response[HTTPResponse.BODY]
        self.resource_changed = self._model_has_changes(existing_model, new_model)

        # if there are no detected changes,
        # return the read response and skip the API update call
        # this ensures that configuration reloads and service restarts that middlewared does are not invoked unnecessarily
        if not self.resource_changed:
            return read_response

        return self._send_checked_request(existing_model, HTTPMethod.PUT, self._RESOURCE_PATH, new_model)

    def update_item(self, model):
        find_item_response = self.find_item(model)
        if find_item_response[HTTPResponse.STATUS_CODE] == HTTPCode.NOT_FOUND:
            # not found, route to create
            response = self.create(model)
            self.resource_created = response[HTTPResponse.STATUS_CODE] == HTTPCode.OK
            return response

        # upate found item
        found_item = find_item_response[HTTPResponse.BODY]
        found_item_id = found_item[self.RESOURCE_ITEM_ID_FIELD]

        self.resource_changed = self._model_has_changes(found_item, model)
        # if model does not have changes, respond with find repsonse and avoid submitting data with no delta
        if not self.resource_changed:
            return find_item_response

        return self._send_checked_request(found_item, HTTPMethod.PUT, self._RESOURCE_ITEM_PATH.format(id=found_item_id), model)

    def delete_item(self, model):
        find_item_response = self.find_item(model)
        # if it could not be found, it doesn't need deleted
        if find_item_response[HTTPResponse.STATUS_CODE] == HTTPCode.NOT_FOUND:
            return find_item_response

        # delete found item
        # upate found item
        found_item = find_item_response[HTTPResponse.BODY]
        found_item_id = found_item[self.RESOURCE_ITEM_ID_FIELD]

        delete_response = self._send_checked_request({}, HTTPMethod.DELETE, str(self._RESOURCE_ITEM_PATH.format(id=found_item_id)))
        self.resource_changed = delete_response[HTTPResponse.STATUS_CODE] == HTTPCode.OK
        self.resource_deleted = self.resource_changed
        return delete_response


class TruenasGroup(TruenasResource):

    RESOURCE_API_MODEL = 'group_create'
    _RESOURCE_PATH = '/group'
    _RESOURCE_ITEM_PATH = '/group/id/{id}'
    RESOURCE_SEARCH_FIELD = 'gid'

    def _model_has_changes(self, existing_model, new_model):
        has_changes = False
        new_keys = new_model.keys()
        for new_key in new_keys:
            # GET /group schema varies from write operations where group field is the name instead of name field
            # as seen in GET /group #/components/schemas/group_create_0 and PUT /group accepts #/components/schemas/group_update_1
            # where group name is specified by the field name
            if new_key == "name":
                has_changes = has_changes or existing_model["group"] != new_model["name"]
            elif new_key not in existing_model:
                raise TruenasModelError("Server did not return model field %s - check API schema arg spec for %s" % (new_key, self.RESOURCE_API_MODEL))
            elif existing_model[new_key] == {} and new_model[new_key] is None:
                continue
            elif existing_model[new_key] != new_model[new_key]:
                has_changes = True
        return has_changes


class TruenasAlertservice(TruenasResource):

    RESOURCE_API_MODEL = 'alert_service_create'
    _RESOURCE_PATH = '/alertservice'
    _RESOURCE_ITEM_PATH = '/alertservice/id/{id}'
    RESOURCE_SEARCH_FIELD = 'name'


class TruenasInterface(TruenasResource):

    RESOURCE_API_MODEL = 'interface_create'
    _RESOURCE_PATH = '/interface'
    _RESOURCE_ITEM_PATH = '/interface/id/{id}'
    RESOURCE_SEARCH_FIELD = 'name'


class TruenasMail(TruenasResource):

    RESOURCE_API_MODEL = 'mail_update'
    _RESOURCE_PATH = '/mail'


class TruenasNetworkConfiguration(TruenasResource):

    RESOURCE_API_MODEL = 'global_configuration_update'
    _RESOURCE_PATH = '/network/configuration'


class TruenasSystemAdvanced(TruenasResource):

    RESOURCE_API_MODEL = 'system_advanced_update'
    _RESOURCE_PATH = '/system/advanced'


class TruenasSystemGeneral(TruenasResource):

    RESOURCE_API_MODEL = 'general_settings'
    _RESOURCE_PATH = '/system/general'


class TruenasSystemNtpserver(TruenasResource):

    RESOURCE_API_MODEL = 'ntp_create'
    _RESOURCE_PATH = '/system/ntpserver'
    _RESOURCE_ITEM_PATH = '/system/ntpserver/id/{id}'
    RESOURCE_SEARCH_FIELD = 'address'


class TruenasSystemState(TruenasResource):

    RESOURCE_API_MODEL = 'json_string'
    _RESOURCE_PATH = '/system/state'

    def __init__(self, conn, check_mode=False):
        super(TruenasSystemState, self).__init__(
            conn,
            check_mode
        )


class TruenasUser(TruenasResource):

    RESOURCE_API_MODEL = 'user_create'  # /components/schemas/user_update_1 as it supersets #/components/schemas/user_create_0
    _RESOURCE_PATH = '/user'
    _RESOURCE_ITEM_PATH = '/user/id/{id}'
    RESOURCE_SEARCH_FIELD = 'username'

    def _model_has_changes(self, existing_model, new_model):
        has_changes = False
        new_keys = new_model.keys()
        for new_key in new_keys:
            if new_key not in existing_model:
                raise TruenasModelError("Server did not return model field %s - check API schema arg spec for %s" % (new_key, self.RESOURCE_API_MODEL))
            elif existing_model[new_key] == {} and new_model[new_key] is None:
                continue
            elif new_key == "group":
                if "id" in existing_model["group"]:
                    # PUT model group field is the group id integer #/components/schemas/user_update_1
                    # but GET model returns the bsdgrp structure
                    has_changes = int(existing_model["group"]["id"]) != int(new_model["group"])
            elif existing_model[new_key] != new_model[new_key]:
                has_changes = True
        return has_changes

    def update_item(self, model):
        # group_create is in #/components/schemas/user_create_0 but not in #/components/schemas/user_update_1
        update_model = model
        popped = update_model.pop("group_create", None)
        return TruenasResource.update_item(self, update_model)
