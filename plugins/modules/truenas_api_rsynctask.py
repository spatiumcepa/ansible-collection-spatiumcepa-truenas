from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse, strip_null_module_params
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasRsynctask
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
module: truenas_api_rsynctask

short_description: Manage TrueNAS rsync tasks

description:
  - Manage TrueNAS rsync tasks via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  archive:
    description: ''
    type: bool
  compress:
    description: ''
    type: bool
  delayupdates:
    description: ''
    type: bool
  delete:
    description: ''
    type: bool
  desc:
    description: ''
    type: str
  direction:
    choices:
    - PULL
    - PUSH
    description: ''
    type: str
  enabled:
    description: ''
    type: bool
  extra:
    description: ''
    type: list
  mode:
    choices:
    - MODULE
    - SSH
    description: ''
    type: str
  path:
    description: ''
    type: str
  preserveattr:
    description: ''
    type: bool
  preserveperm:
    description: ''
    type: bool
  quiet:
    description: ''
    type: bool
  recursive:
    description: ''
    type: bool
  remotehost:
    description: ''
    type: str
  remotemodule:
    description: ''
    type: str
  remotepath:
    description: ''
    type: str
  remoteport:
    description: ''
    type: int
  schedule:
    description: ''
    suboptions:
      dom:
        type: str
      dow:
        type: str
      hour:
        type: str
      minute:
        type: str
      month:
        type: str
    type: dict
  times:
    description: ''
    type: bool
  user:
    description: ''
    type: str
  validate_rpath:
    description: ''
    type: bool
type: dict
"""

EXAMPLES = """
  - name: Manage rsync task via TrueNAS API
    spatiumcepa.truenas.truenas_api_rsynctask:
      model:
        archive: true
        compress: true
        delayupdates: false
        delete: false
        desc: Site 1 research to Site 2 every 4 hours
        direction: PUSH
        enabled: true
        mode: SSH
        path: /mnt/tank/home
        preserveattr: true
        preserveperm: true
        quiet: false
        recursive: true
        remotehost: site2-truenas1
        remotemodule: ""
        remotepath: /mnt/tank/research
        remoteport: 22
        schedule:
          dom: '*'
          dow: '*'
          hour: '*/4'
          minute: "0"
          month: '*'
        times: true
        user: root
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
            model=API_ARG_SPECS[TruenasRsynctask.RESOURCE_API_MODEL_SPEC],
            state={'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'}
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    rsynctask_resource = TruenasRsynctask(connection, module.check_mode)

    try:
        response = None
        model_param = strip_null_module_params(module.params['model'])
        state_param = module.params['state']

        if state_param == 'present':
            response = rsynctask_resource.update_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK
        elif state_param == 'absent':
            response = rsynctask_resource.delete_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] not in [HTTPCode.OK, HTTPCode.NOT_FOUND]

        module.exit_json(
            created=rsynctask_resource.resource_created,
            changed=rsynctask_resource.resource_changed,
            deleted=rsynctask_resource.resource_deleted,
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
