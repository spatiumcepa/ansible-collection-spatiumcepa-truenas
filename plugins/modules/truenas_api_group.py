from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse, strip_null_module_params
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasGroup
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
module: truenas_api_group

short_description: Manage TrueNAS Groups

description:
  - Manage TrueNAS Groups via REST API

version_added: "0.1"

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
      allow_duplicate_gid:
        description: ''
        type: bool
      gid:
        description: ''
        type: int
      name:
        description: ''
        type: str
      smb:
        description: ''
        type: bool
      sudo:
        description: ''
        type: bool
      sudo_commands:
        description: ''
        type: list
      sudo_nopasswd:
        description: ''
        type: bool
      users:
        description: ''
        type: list
"""

EXAMPLES = """
  - name: Manage Group via TrueNAS API
    spatiumcepa.truenas.truenas_api_group:
      model:
        gid: 983
        name: syncthing
        sudo: false
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
            model=API_ARG_SPECS[TruenasGroup.RESOURCE_API_MODEL_SPEC],
            state={'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'}
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    group_resource = TruenasGroup(connection, module.check_mode)

    try:
        response = None
        model_param = strip_null_module_params(module.params['model'])
        state_param = module.params['state']

        if state_param == 'present':
            response = group_resource.update_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK
        elif state_param == 'absent':
            response = group_resource.delete_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] not in [HTTPCode.OK, HTTPCode.NOT_FOUND]

        module.exit_json(
            created=group_resource.resource_created,
            changed=group_resource.resource_changed,
            deleted=group_resource.resource_deleted,
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
