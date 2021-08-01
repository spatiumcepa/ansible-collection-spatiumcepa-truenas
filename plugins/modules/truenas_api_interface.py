from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasInterface
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
module: truenas_api_interface

short_description: Manage TrueNAS Interfaces

description:
  - Manage TrueNAS Interfaces via REST API

version_added: "2.10"

author: Nicholas Kiraly (@nkiraly)

options:
  model:
    type: dict
    description: ''
    options:
      aliases:
        description: ''
        type: list
      bridge_members:
        description: ''
        type: list
      description:
        description: ''
        type: str
      disable_offload_capabilities:
        description: ''
        type: bool
      failover_aliases:
        description: ''
        type: list
      failover_critical:
        description: ''
        type: bool
      failover_group:
        description: ''
        type: int
      failover_vhid:
        description: ''
        type: int
      failover_virtual_aliases:
        description: ''
        type: list
      ipv4_dhcp:
        description: ''
        type: bool
      ipv6_auto:
        description: ''
        type: bool
      lag_ports:
        description: ''
        type: list
      lag_protocol:
        choices:
        - LACP
        - FAILOVER
        - LOADBALANCE
        - ROUNDROBIN
        - NONE
        description: ''
        type: str
      mtu:
        description: ''
        type: int
      name:
        description: ''
        type: str
      options:
        description: ''
        type: str
      vlan_parent_interface:
        description: ''
        type: str
      vlan_pcp:
        description: ''
        type: int
      vlan_tag:
        description: ''
        type: int
"""

EXAMPLES = """
  - name: Interface Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_api_interface:
      model:
        name: lagg0
        aliases:
          - type: INET
            address: 172.16.13.41
            netmask: 23
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
            model=API_ARG_SPECS[TruenasInterface.RESOURCE_API_MODEL]
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    interface_resource = TruenasInterface(connection, module.check_mode)

    try:
        response = None
        model_param = strip_null_module_params(module.params['model'])
        state_param = module.params['state']

        if state_param == 'present':
            response = interface_resource.update_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK
        elif state_param == 'absent':
            response = interface_resource.delete_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] not in [HTTPCode.OK, HTTPCode.NOT_FOUND]

        module.exit_json(
            created=interface_resource.resource_created,
            changed=interface_resource.resource_changed,
            deleted=interface_resource.resource_deleted,
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
