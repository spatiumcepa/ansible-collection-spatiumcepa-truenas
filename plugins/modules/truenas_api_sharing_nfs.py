from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse, strip_null_module_params
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasSharingNfs
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
module: truenas_api_sharing_nfs

short_description: Manage TrueNAS NFS Share

description:
  - Manage TrueNAS NFS Share via REST API

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
      alldirs:
        description: ''
        type: bool
      comment:
        description: ''
        type: str
      enabled:
        description: ''
        type: bool
      hosts:
        description: ''
        type: list
      mapall_group:
        description: ''
        type: str
      mapall_user:
        description: ''
        type: str
      maproot_group:
        description: ''
        type: str
      maproot_user:
        description: ''
        type: str
      networks:
        description: ''
        type: list
      paths:
        description: ''
        type: list
      quiet:
        description: ''
        type: bool
      ro:
        description: ''
        type: bool
      security:
        description: ''
        type: list
"""

EXAMPLES = """
  - name: Manage Sharing NFS via TrueNAS API
    spatiumcepa.truenas.truenas_api_sharing_nfs:
      model:
        paths:
          - "/mnt/tank/home"
        enabled: true
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
            model=API_ARG_SPECS[TruenasSharingNfs.RESOURCE_API_MODEL_SPEC],
            state={'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'}
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    sharing_nfs_resource = TruenasSharingNfs(connection, module.check_mode)

    try:
        response = None
        model_param = strip_null_module_params(module.params['model'])
        state_param = module.params['state']

        if state_param == 'present':
            response = sharing_nfs_resource.update_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK
        elif state_param == 'absent':
            response = sharing_nfs_resource.delete_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] not in [HTTPCode.OK, HTTPCode.NOT_FOUND]

        module.exit_json(
            created=sharing_nfs_resource.resource_created,
            changed=sharing_nfs_resource.resource_changed,
            deleted=sharing_nfs_resource.resource_deleted,
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
