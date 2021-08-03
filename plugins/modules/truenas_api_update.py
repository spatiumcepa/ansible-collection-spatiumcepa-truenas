from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasUpdate
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.arg_specs import API_ARG_SPECS, strip_null_module_params
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils.basic import AnsibleModule
__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community"
}

DOCUMENTATION = """
module: truenas_api_update

short_description: Check for and perform updates on a TrueNAS System

description:
  - Check for and perform updates on a TrueNAS System via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  options:
    action:
      choices:
        - check_available
        - download
        - get_auto_download
        - get_pending
        - get_trains
        - manual
        - set_auto_download
        - set_train
        - update
      description: 'Update action to execute'
      required = true
      type: str
    model:
      type: dict
      default: {}
"""

EXAMPLES = """
  - name: System General Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_api_update:
      model:
        ui_address: ['0.0.0.0']
        ui_httpsredirect: true
"""

RETURN = """
response:
  description: HTTP response returned from the API call
  returned: success
  type: dict
"""


def main():
    module = AnsibleModule(
        argument_spec=dict(
            action={
                'type': 'str',
                'choices': ['check_available', 'download', 'get_auto_download', 'get_pending', 'get_trains', 'manual', 'set_auto_download', 'set_train', 'update'],
                'required': True
            },
            model={'type': 'dict', 'default': {}}
        ),
        supports_check_mode=False,
    )

    connection = Connection(module._socket_path)
    update_resource = TruenasUpdate(connection, module.check_mode)

    try:
        action_param = module.params['action']
        model_param = module.params['model']
        response = update_resource.action(action_param, model_param)
        module.exit_json(
            changed=update_resource.resource_changed,
            failed=response[HTTPResponse.STATUS_CODE] != HTTPCode.OK,
            response=response,
            action_result=update_resource.action_result,
        )

    except TruenasServerError as e:
        module.fail_json(msg='Server returned an error, satus code: %s. '
                             'Server response: %s' % (e.code, e.response))

    except TruenasModelError as e:
        module.fail_json(msg='Data model error: %s' % (e.args[0]))

    except TruenasUnexpectedResponse as e:
        module.fail_json(msg=e.args[0])

    except ConnectionError as e:
        module.fail_json(msg=e.args[0])


if __name__ == '__main__':
    main()
