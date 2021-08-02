from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasPoolSnapshottask
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
module: truenas_api_pool_snapshottask

short_description: Manage TrueNAS Pool Snapshottasks

description:
  - Manage TrueNAS Pool Snapshottasks via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  state:
    type: str
    description: Desired state of the snapshot task
    default: present
    choices: [ absent, present ]
  model:
    type: dict
    description: ''
    options:
      allow_empty:
        description: ''
        type: bool
      dataset:
        description: ''
        type: str
      enabled:
        description: ''
        type: bool
      exclude:
        description: ''
        type: list
      lifetime_unit:
        choices:
        - HOUR
        - DAY
        - WEEK
        - MONTH
        - YEAR
        description: ''
        type: str
      lifetime_value:
        description: ''
        type: int
      naming_schema:
        description: ''
        type: str
      recursive:
        description: ''
        type: bool
      schedule:
        description: ''
        suboptions:
          begin:
            type: str
          dom:
            type: str
          dow:
            type: str
          end:
            type: str
          hour:
            type: str
          minute:
            type: str
          month:
            type: str
        type: dict
"""

EXAMPLES = """
  - name: Manage Pool Snapshottask via TrueNAS API
    spatiumcepa.truenas.truenas_api_pool_snapshottask:
      model:
        dataset: tank/storage
        recursive: true
        exclude: []
        lifetime_value: 2
        lifetime_unit: WEEK
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
            model=API_ARG_SPECS[TruenasPoolSnapshottask.RESOURCE_API_MODEL],
            state={'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'}
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    snapshottask_resource = TruenasPoolSnapshottask(connection, module.check_mode)

    try:
        response = None
        model_param = strip_null_module_params(module.params['model'])
        state_param = module.params['state']

        if state_param == 'present':
            response = snapshottask_resource.update_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK
        elif state_param == 'absent':
            response = snapshottask_resource.delete_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] not in [HTTPCode.OK, HTTPCode.NOT_FOUND]

        module.exit_json(
            created=snapshottask_resource.resource_created,
            changed=snapshottask_resource.resource_changed,
            deleted=snapshottask_resource.resource_deleted,
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
