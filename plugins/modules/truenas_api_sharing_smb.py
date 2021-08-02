from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasSharingSmb
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
module: truenas_api_sharing_smb

short_description: Manage TrueNAS Groups

description:
  - Manage TrueNAS Groups via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  state:
    type: str
    description: Desired state of the SMB share
    default: present
    choices: [ absent, present ]
  model:
    type: dict
    description: ''
    options:
      aapl_name_mangling:
        description: ''
        type: bool
      abe:
        description: ''
        type: bool
      acl:
        description: ''
        type: bool
      auxsmbconf:
        description: ''
        type: str
      browsable:
        description: ''
        type: bool
      comment:
        description: ''
        type: str
      durablehandle:
        description: ''
        type: bool
      enabled:
        description: ''
        type: bool
      fsrvp:
        description: ''
        type: bool
      guestok:
        description: ''
        type: bool
      home:
        description: ''
        type: bool
      hostsallow:
        description: ''
        type: list
      hostsdeny:
        description: ''
        type: list
      name:
        description: ''
        type: str
      path:
        description: ''
        type: str
      path_suffix:
        description: ''
        type: str
      purpose:
        choices:
        - NO_PRESET
        - DEFAULT_SHARE
        - ENHANCED_TIMEMACHINE
        - MULTI_PROTOCOL_AFP
        - MULTI_PROTOCOL_NFS
        - PRIVATE_DATASETS
        - WORM_DROPBOX
        description: ''
        type: str
      recyclebin:
        description: ''
        type: bool
      ro:
        description: ''
        type: bool
      shadowcopy:
        description: ''
        type: bool
      streams:
        description: ''
        type: bool
      timemachine:
        description: ''
        type: bool
"""

EXAMPLES = """
  - name: Manage Sharing SMB via TrueNAS API
    spatiumcepa.truenas.truenas_api_sharing_smb:
      model:
        path: "/mnt/tank/collab"
        name: collab
        purpose: DEFAULT_SHARE
        acl: true
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
            model=API_ARG_SPECS[TruenasSharingSmb.RESOURCE_API_MODEL],
            state={'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'}
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    sharing_smb_resource = TruenasSharingSmb(connection, module.check_mode)

    try:
        response = None
        model_param = strip_null_module_params(module.params['model'])
        state_param = module.params['state']

        if state_param == 'present':
            response = sharing_smb_resource.update_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK
        elif state_param == 'absent':
            response = sharing_smb_resource.delete_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] not in [HTTPCode.OK, HTTPCode.NOT_FOUND]

        module.exit_json(
            created=sharing_smb_resource.resource_created,
            changed=sharing_smb_resource.resource_changed,
            deleted=sharing_smb_resource.resource_deleted,
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
