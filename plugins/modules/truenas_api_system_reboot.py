from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse, strip_null_module_params
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasSystemReboot
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.arg_specs import API_ARG_SPECS
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

short_description: Reboot a TrueNAS System

description:
  - Reboot a TrueNAS System via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  options:
    model:
      delay:
        description: ''
        type: int
"""

EXAMPLES = """
  - name: System General Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_reboot:
      model:
        delay: 10
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
            model=API_ARG_SPECS[TruenasSystemReboot.RESOURCE_API_MODEL_SPEC],
        ),
        supports_check_mode=False,
    )

    connection = Connection(module._socket_path)
    update_resource = TruenasSystemReboot(connection, module.check_mode)

    try:
        model_param = module.params['model']
        response = update_resource.reboot(model_param)
        module.exit_json(
            changed=update_resource.resource_changed,
            failed=response[HTTPResponse.STATUS_CODE] != HTTPCode.OK,
            response=response,
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
