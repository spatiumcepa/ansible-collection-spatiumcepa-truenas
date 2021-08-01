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
module: truenas_api_smb

short_description: Configure TrueNAS SMB settings

description:
  - Configure TrueNAS SMB settings via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  model:
    type: dict
    description: ''
    options:
      aapl_extensions:
        description: ''
        type: bool
      admin_group:
        description: ''
        type: str
      bindip:
        description: ''
        type: list
      description:
        description: ''
        type: str
      dirmask:
        description: ''
        type: str
      enable_smb1:
        description: ''
        type: bool
      filemask:
        description: ''
        type: str
      guest:
        description: ''
        type: str
      localmaster:
        description: ''
        type: bool
      loglevel:
        choices:
        - NONE
        - MINIMUM
        - NORMAL
        - FULL
        - DEBUG
        description: ''
        type: str
      netbiosalias:
        description: ''
        type: list
      netbiosname:
        description: ''
        type: str
      netbiosname_b:
        description: ''
        type: str
      ntlmv1_auth:
        description: ''
        type: bool
      smb_options:
        description: ''
        type: str
      syslog:
        description: ''
        type: bool
      unixcharset:
        description: ''
        type: str
      workgroup:
        description: ''
        type: str
"""

EXAMPLES = """
  - name: Eservice Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_api_smb:
      model:
        netbiosname: "{{ inventory_hostname }}"
        workgroup: REDCEPA
        enable_smb1: false
        localmaster: true
        guest: nobody
        aapl_extensions: true
        ntlmv1_auth: false
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
            model=API_ARG_SPECS["smb_update"]
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    service_resource = TruenasService(connection, module.check_mode)

    try:
        model_param = strip_null_module_params(module.params['model'])
        response = service_resource.service_settings("cifs", "/smb", model_param)
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
