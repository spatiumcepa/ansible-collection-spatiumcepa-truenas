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

        # update found item
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
        # update found item
        found_item = find_item_response[HTTPResponse.BODY]
        found_item_id = found_item[self.RESOURCE_ITEM_ID_FIELD]

        delete_response = self._send_checked_request({}, HTTPMethod.DELETE, str(self._RESOURCE_ITEM_PATH.format(id=found_item_id)))
        self.resource_changed = delete_response[HTTPResponse.STATUS_CODE] == HTTPCode.OK
        self.resource_deleted = self.resource_changed
        return delete_response


class TruenasActivedirectory(TruenasResource):

    RESOURCE_API_MODEL = 'activedirectory_update_0'
    _RESOURCE_PATH = '/activedirectory'

    def update(self, new_model):
        config_model = new_model.copy()
        enable_model = {
            'enable': config_model.pop('enable', False)
        }
        if 'bindname' in config_model:
            enable_model['bindname'] = config_model.pop('bindname')
        if 'bindpw' in config_model:
            enable_model['bindpw'] = config_model.pop('bindpw')

        existing_response = self.read()
        existing_model = existing_response[HTTPResponse.BODY]
        self.resource_changed = self._model_has_changes(existing_model, config_model)
        if existing_model['enable'] != new_model['enable']:
            self.resource_changed = True

        # if there are no detected changes,
        # return the existing response and skip the API update call
        # this ensures that configuration reloads and service restarts that middlewared does are not invoked unnecessarily
        if not self.resource_changed:
            return existing_response

        response = None
        if self._model_has_changes(existing_model, config_model):
            response = self._send_checked_request(existing_model, HTTPMethod.PUT, self._RESOURCE_PATH, config_model)
        if existing_model['enable'] != new_model['enable']:
            response = self._send_checked_request(existing_model, HTTPMethod.PUT, self._RESOURCE_PATH, enable_model)
        return response


class TruenasAlertservice(TruenasResource):

    RESOURCE_API_MODEL = 'alertservice_update_1'
    _RESOURCE_PATH = '/alertservice'
    _RESOURCE_ITEM_PATH = '/alertservice/id/{id}'
    RESOURCE_SEARCH_FIELD = 'name'


class TruenasCronjob(TruenasResource):

    RESOURCE_API_MODEL = 'cronjob_update_1'
    _RESOURCE_PATH = '/cronjob'
    _RESOURCE_ITEM_PATH = '/cronjob/id/{id}'
    RESOURCE_SEARCH_FIELD = 'description'


class TruenasGroup(TruenasResource):

    RESOURCE_API_MODEL = 'group_update_1'
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


class TruenasIdmap(TruenasResource):

    RESOURCE_API_MODEL = 'idmap_update_1'
    _RESOURCE_PATH = '/idmap'
    _RESOURCE_ITEM_PATH = '/idmap/id/{id}'
    RESOURCE_SEARCH_FIELD = 'name'


class TruenasInterface(TruenasResource):

    RESOURCE_API_MODEL = 'interface_update_1'
    _RESOURCE_PATH = '/interface'
    _RESOURCE_ITEM_PATH = '/interface/id/{id}'
    RESOURCE_SEARCH_FIELD = 'name'


class TruenasMail(TruenasResource):

    RESOURCE_API_MODEL = 'mail_update_0'
    _RESOURCE_PATH = '/mail'


class TruenasNetworkConfiguration(TruenasResource):

    RESOURCE_API_MODEL = 'network_configuration_update_0'
    _RESOURCE_PATH = '/network/configuration'


class TruenasPoolDataset(TruenasResource):

    RESOURCE_API_MODEL = 'pool_dataset_create_0'
    _RESOURCE_PATH = '/pool/dataset'
    _RESOURCE_ITEM_PATH = '/pool/dataset/id/{id}'
    RESOURCE_SEARCH_FIELD = 'name'

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

            # unlike most of the API, returned dataset details have raw and parsed values for their fields
            existing_rawvalue = existing_model[new_key]['rawvalue']
            existing_value = existing_model[new_key]['value']
            new_value = new_model[new_key]
            # so for detetcing changes in new values
            # first compare to rawvalue as that is what would have been submitted during initial creation
            # second compare to value as the composite value will be considered valid input for ansible change calculation
            # third compare raw with new after casting to string
            if existing_rawvalue != new_value:
                if existing_value != new_value:
                    if str(existing_rawvalue) != str(new_value):
                        has_changes = True

        return has_changes

    def update_item(self, model):
        find_item_response = self._send_request(HTTPMethod.GET, self._RESOURCE_PATH + "?name=" + model["name"])
        # URL query by name responses with a list of matches, check it actually returned one
        if find_item_response[HTTPResponse.STATUS_CODE] == HTTPCode.NOT_FOUND or len(find_item_response[HTTPResponse.BODY]) == 0:
            # not found, route to create
            response = self.create(model)
            self.resource_created = response[HTTPResponse.STATUS_CODE] == HTTPCode.OK
            return response

        # remove name from update model, it is read only
        update_model = model.copy()
        hasno = update_model.pop("name")

        # update found item
        # URL query by name responses with a list of matches, use the first match
        found_item = find_item_response[HTTPResponse.BODY][0]
        found_item_id = found_item[self.RESOURCE_ITEM_ID_FIELD]

        self.resource_changed = self._model_has_changes(found_item, update_model)
        # if model does not have changes, respond with find repsonse and avoid submitting data with no delta
        if not self.resource_changed:
            return find_item_response

        return self._send_checked_request(found_item, HTTPMethod.PUT, self._RESOURCE_ITEM_PATH.format(id=found_item_id.replace('/', '%2F')), update_model)

    def delete_item(self, model):
        find_item_response = self._send_request(HTTPMethod.GET, self._RESOURCE_PATH + "?name=" + model["name"])
        # URL query by name responses with a list of matches, check it actually returned one
        # if it could not be found, it doesn't need deleted
        if find_item_response[HTTPResponse.STATUS_CODE] == HTTPCode.NOT_FOUND or len(find_item_response[HTTPResponse.BODY]) == 0:
            return find_item_response

        # delete found item
        # URL query by name responses with a list of matches, use the first match
        found_item = find_item_response[HTTPResponse.BODY][0]
        found_item_id = found_item[self.RESOURCE_ITEM_ID_FIELD]

        delete_response = self._send_checked_request({}, HTTPMethod.DELETE, self._RESOURCE_ITEM_PATH.format(id=found_item_id.replace('/', '%2F')))
        self.resource_changed = delete_response[HTTPResponse.STATUS_CODE] == HTTPCode.OK
        self.resource_deleted = self.resource_changed
        return delete_response


class TruenasPoolSnapshottask(TruenasResource):

    RESOURCE_API_MODEL = 'pool_snapshottask_update_1'
    _RESOURCE_PATH = '/pool/snapshottask'
    _RESOURCE_ITEM_PATH = '/pool/snapshottask/id/{id}'
    RESOURCE_SEARCH_FIELD = 'dataset'


class TruenasService(TruenasResource):

    RESOURCE_API_MODEL = None
    _RESOURCE_PATH = '/service'
    _RESOURCE_ITEM_PATH = '/service/id/{id}'
    RESOURCE_SEARCH_FIELD = 'service'

    def service_action(self, name, action):
        find_service_response = self.find_item({'service': name})
        if find_service_response[HTTPResponse.STATUS_CODE] == HTTPCode.NOT_FOUND:
            # not found, return not found response
            self.resource_changed = False
            return find_service_response

        found_item = find_service_response[HTTPResponse.BODY]
        self.resource_changed = False
        if action == 'reload':
            self.resource_changed = True
        elif action == 'restart':
            self.resource_changed = True
        elif action == 'start':
            if found_item['state'] == 'STOPPED':
                self.resource_changed = True
        elif action == 'stop':
            if found_item['state'] == 'RUNNING':
                self.resource_changed = True
        else:
            raise TruenasModelError("Unknown action specified: %s" % (action))

        # if there are no detected changes,
        # return the found item response and skip the API action call
        # this ensures that configuration reloads and service restarts that middlewared does are not invoked unnecessarily
        if not self.resource_changed:
            return find_service_response

        return self._send_checked_request(found_item, HTTPMethod.POST, self._RESOURCE_PATH + '/' + action, {'service': name})

    def service_state(self, name, enable, running):
        find_service_response = self.find_item({'service': name})
        if find_service_response[HTTPResponse.STATUS_CODE] == HTTPCode.NOT_FOUND:
            # not found, return not found response
            self.resource_changed = False
            return find_service_response

        found_item = find_service_response[HTTPResponse.BODY]
        found_item_id = found_item['id']
        found_item_is_running = found_item['state'] == 'RUNNING'
        self.resource_changed = False
        if found_item['enable'] != enable:
            self.resource_changed = True
        if found_item_is_running != running:
            self.resource_changed = True
        # if there are no detected changes,
        # return the found item response and skip the API update call
        # this ensures that configuration reloads and service restarts that middlewared does are not invoked unnecessarily
        if not self.resource_changed:
            return find_service_response

        response = None
        if found_item['enable'] != enable:
            response = self._send_checked_request(found_item, HTTPMethod.PUT, self._RESOURCE_ITEM_PATH.format(id=found_item_id), {'enable': enable})
        if running and not found_item_is_running:
            response = self._send_checked_request(found_item, HTTPMethod.POST, self._RESOURCE_PATH + '/start', {'service': name})
        if not running and found_item_is_running:
            response = self._send_checked_request(found_item, HTTPMethod.POST, self._RESOURCE_PATH + '/stop', {'service': name})
        return response

    def service_settings(self, name, service_url, settings):
        find_service_response = self.find_item({'service': name})
        if find_service_response[HTTPResponse.STATUS_CODE] == HTTPCode.NOT_FOUND:
            # not found, return not found response
            self.resource_changed = False
            return find_service_response

        existing_settings_response = self._send_request(HTTPMethod.GET, service_url)
        existing_settings = existing_settings_response[HTTPResponse.BODY]
        self.resource_changed = self._model_has_changes(existing_settings, settings)

        # if there are no detected changes,
        # return the existing settings response and skip the API update call
        # this ensures that configuration reloads and service restarts that middlewared does are not invoked unnecessarily
        if not self.resource_changed:
            return existing_settings_response

        return self._send_checked_request(existing_settings, HTTPMethod.PUT, service_url, settings)


class TruenasSharingNfs(TruenasResource):

    RESOURCE_API_MODEL = 'sharing_nfs_update_1'
    _RESOURCE_PATH = '/sharing/nfs'
    _RESOURCE_ITEM_PATH = '/sharing/nfs/id/{id}'
    RESOURCE_SEARCH_FIELD = 'comment'

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
        # find NFS share by paths + comment
        search_field_value = model[self.RESOURCE_SEARCH_FIELD]
        search_paths_value = model['paths']
        read_response = self.read()
        item_list = read_response[HTTPResponse.BODY]
        for item in item_list:
            if self.RESOURCE_SEARCH_FIELD not in item.keys():
                raise TruenasModelError(
                    "find item candidate does not have field RESOURCE_SEARCH_FIELD %s" % (self.RESOURCE_SEARCH_FIELD)
                )
            if item[self.RESOURCE_SEARCH_FIELD] == search_field_value and item["paths"].sort() == search_paths_value.sort():
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


class TruenasSharingSmb(TruenasResource):

    RESOURCE_API_MODEL = 'sharing_smb_update_1'
    _RESOURCE_PATH = '/sharing/smb'
    _RESOURCE_ITEM_PATH = '/sharing/smb/id/{id}'
    RESOURCE_SEARCH_FIELD = 'name'


class TruenasSystemAdvanced(TruenasResource):

    RESOURCE_API_MODEL = 'system_advanced_update_0'
    _RESOURCE_PATH = '/system/advanced'


class TruenasSystemGeneral(TruenasResource):

    RESOURCE_API_MODEL = 'system_general_update_0'
    _RESOURCE_PATH = '/system/general'


class TruenasSystemNtpserver(TruenasResource):

    RESOURCE_API_MODEL = 'system_ntpserver_update_1'
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

    RESOURCE_API_MODEL = 'user_create_0'
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
