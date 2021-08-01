from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasSystemNtpserver
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
module: truenas_api_system_ntpserver

short_description: Manage TrueNAS Groups

description:
  - Manage TrueNAS Groups via REST API

version_added: "2.10"

author: Nicholas Kiraly (@nkiraly)

options:
  state:
    type: str
    description: Desired state of the group
    default: present
    choices: [ absent, present ]
  model:
    type: dict
    description: ''
    options:
      attributes:
        description: ''
        suboptions: {}
        type: dict
      email:
        description: ''
        type: str
      full_name:
        description: ''
        type: str
      group:
        description: ''
        type: int
      groups:
        description: ''
        type: list
      home:
        description: ''
        type: str
      home_mode:
        description: ''
        type: str
      locked:
        description: ''
        type: bool
      microsoft_account:
        description: ''
        type: bool
      password:
        description: ''
        type: str
      password_disabled:
        description: ''
        type: bool
      shell:
        description: ''
        type: str
      smb:
        description: ''
        type: bool
      sshpubkey:
        description: ''
        type: str
      sudo:
        description: ''
        type: bool
      sudo_commands:
        description: ''
        type: list
      sudo_nopasswd:
        description: ''
        type: bool
      uid:
        description: ''
        type: int
      username:
        description: ''
        type: str
"""

EXAMPLES = """
  - name: Manage Group via TrueNAS API
    spatiumcepa.truenas.truenas_api_system_ntpserver:
      model:
        address: hq2-dc01.corp.vicarious.com
        prefer: true
      state: present
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
            model=API_ARG_SPECS[TruenasSystemNtpserver.RESOURCE_API_MODEL],
            state={'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'}
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    ntpserver_resource = TruenasSystemNtpserver(connection, module.check_mode)

    try:
        response = None
        model_param = strip_null_module_params(module.params['model'])
        state_param = module.params['state']

        if state_param == 'present':
            response = ntpserver_resource.update_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK
        elif state_param == 'absent':
            response = ntpserver_resource.delete_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] not in [HTTPCode.OK, HTTPCode.NOT_FOUND]

        module.exit_json(
            created=ntpserver_resource.resource_created,
            changed=ntpserver_resource.resource_changed,
            deleted=ntpserver_resource.resource_deleted,
            failed=failed,
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
