from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasReplication
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
module: truenas_api_replication

short_description: Manage TrueNAS ZFS Replication

description:
  - Manage TrueNAS ZFS Replication via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  state:
    type: str
    description: Desired state of the ZFS Replication Task
    default: present
    choices: [ absent, present ]
  model:
    type: dict
    description: ''
    options:
      allow_from_scratch:
        description: ''
        type: bool
      also_include_naming_schema:
        description: ''
        type: list
      auto:
        description: ''
        type: bool
      compressed:
        description: ''
        type: bool
      compression:
        choices:
        - LZ4
        - PIGZ
        - PLZIP
        description: ''
        type: str
      direction:
        choices:
        - PUSH
        - PULL
        description: ''
        type: str
      embed:
        description: ''
        type: bool
      enabled:
        description: ''
        type: bool
      encryption:
        description: ''
        type: bool
      encryption_key:
        description: ''
        type: str
      encryption_key_format:
        choices:
        - HEX
        - PASSPHRASE
        description: ''
        type: str
      encryption_key_location:
        description: ''
        type: str
      exclude:
        description: ''
        type: list
      hold_pending_snapshots:
        description: ''
        type: bool
      large_block:
        description: ''
        type: bool
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
      logging_level:
        choices:
        - DEBUG
        - INFO
        - WARNING
        - ERROR
        description: ''
        type: str
      name:
        description: ''
        type: str
      naming_schema:
        description: ''
        type: list
      netcat_active_side:
        choices:
        - LOCAL
        - REMOTE
        description: ''
        type: str
      netcat_active_side_listen_address:
        description: ''
        type: str
      netcat_active_side_port_max:
        description: ''
        type: int
      netcat_active_side_port_min:
        description: ''
        type: int
      netcat_passive_side_connect_address:
        description: ''
        type: str
      only_matching_schedule:
        description: ''
        type: bool
      periodic_snapshot_tasks:
        description: ''
        type: list
      properties:
        description: ''
        type: bool
      properties_exclude:
        description: ''
        type: list
      readonly:
        choices:
        - SET
        - REQUIRE
        - IGNORE
        description: ''
        type: str
      recursive:
        description: ''
        type: bool
      replicate:
        description: ''
        type: bool
      restrict_schedule:
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
      retention_policy:
        choices:
        - SOURCE
        - CUSTOM
        - NONE
        description: ''
        type: str
      retries:
        description: ''
        type: int
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
      source_datasets:
        description: ''
        type: list
      speed_limit:
        description: ''
        type: int
      ssh_credentials:
        description: ''
        type: int
      target_dataset:
        description: ''
        type: str
      transport:
        choices:
        - SSH
        - SSH+NETCAT
        - LOCAL
        description: ''
        type: str
"""

EXAMPLES = """
  - name: Manage ZFS Home Replication Task via TrueNAS API
    spatiumcepa.truenas.truenas_api_replication:
      model:
        name: "Home - Site 1 to Site 2"
        source_datasets:
          - tank/home
        target_dataset: tank/home
        transport: SSH
        ssh_credentials: 1
        direction: PUSH
        readonly: SET
        retention_policy: SOURCE
        auto: true
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
            model=API_ARG_SPECS[TruenasReplication.RESOURCE_API_MODEL_SPEC],
            state={'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'}
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    replication_resource = TruenasReplication(connection, module.check_mode)

    try:
        response = None
        model_param = strip_null_module_params(module.params['model'])
        state_param = module.params['state']

        if state_param == 'present':
            response = replication_resource.update_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK
        elif state_param == 'absent':
            response = replication_resource.delete_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] not in [HTTPCode.OK, HTTPCode.NOT_FOUND]

        module.exit_json(
            created=replication_resource.resource_created,
            changed=replication_resource.resource_changed,
            deleted=replication_resource.resource_deleted,
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
