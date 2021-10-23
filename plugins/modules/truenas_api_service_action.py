from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse, strip_null_module_params
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasService
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
module: truenas_api_action

short_description: TrueNAS Service Action

description:
  - TrueNAS Service Action via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  name:
    description: Name of service to manage
    required: true
    type: str
  action:
    description: Service action to initiate
    type: str
    choices:
      - reload
      - restart
      - start
      - stop
"""

EXAMPLES = """
  - name: Service Action Execution via TrueNAS API
    spatiumcepa.truenas.truenas_api_service:
      name: ssh
      action: reload
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
            name={'type': 'str', 'required': True},
            action={'type': 'str', 'required': True, 'choices': ['reload', 'restart', 'start', 'stop']}
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    service_resource = TruenasService(connection, module.check_mode)

    try:
        response = None
        name = module.params['name']
        action = module.params['action']

        response = service_resource.service_action(name, action)
        failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK

        module.exit_json(
            changed=service_resource.resource_changed,
            failed=failed,
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
