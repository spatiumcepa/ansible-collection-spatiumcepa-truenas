from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasService
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
module: truenas_api_ssh

short_description: Configure TrueNAS SSH settings

description:
  - Configure TrueNAS SSH settings via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  model:
    type: dict
    description: ''
    options:
      bindiface:
        description: ''
        type: list
      compression:
        description: ''
        type: bool
      kerberosauth:
        description: ''
        type: bool
      options:
        description: ''
        type: str
      passwordauth:
        description: ''
        type: bool
      rootlogin:
        description: ''
        type: bool
      sftp_log_facility:
        choices:
        - ''
        - DAEMON
        - USER
        - AUTH
        - LOCAL0
        - LOCAL1
        - LOCAL2
        - LOCAL3
        - LOCAL4
        - LOCAL5
        - LOCAL6
        - LOCAL7
        description: ''
        type: str
      sftp_log_level:
        choices:
        - ''
        - QUIET
        - FATAL
        - ERROR
        - INFO
        - VERBOSE
        - DEBUG
        - DEBUG2
        - DEBUG3
        description: ''
        type: str
      tcpfwd:
        description: ''
        type: bool
      tcpport:
        description: ''
        type: int
      weak_ciphers:
        description: ''
        type: list
"""

EXAMPLES = """
  - name: Eservice Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_api_ssh:
      model:
        kerberosauth: false
        passwordauth: true
        tcpfwd: false
        rootlogin: true
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
            model=API_ARG_SPECS["ssh_update"]
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    service_resource = TruenasService(connection, module.check_mode)

    try:
        model_param = strip_null_module_params(module.params['model'])
        response = service_resource.service_settings("ssh", "/ssh", model_param)
        module.exit_json(
            changed=service_resource.resource_changed,
            failed=response[HTTPResponse.STATUS_CODE] != HTTPCode.OK,
            response=response,
            submitted_model=model_param,
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
