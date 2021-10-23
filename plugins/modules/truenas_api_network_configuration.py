from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse, strip_null_module_params
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasNetworkConfiguration
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
module: truenas_api_network_configuration

short_description: Configure TrueNAS Network Configuration settings

description:
  - Configure TrueNAS Network Configuration settings via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  model:
    type: dict
    description: ''
    options:
      domain:
        description: ''
        type: str
      domains:
        description: ''
        type: list
      hostname:
        description: ''
        type: str
      hostname_b:
        description: ''
        type: str
      hostname_virtual:
        description: ''
        type: str
      hosts:
        description: ''
        type: str
      httpproxy:
        description: ''
        type: str
      ipv4gateway:
        description: ''
        type: str
      ipv6gateway:
        description: ''
        type: str
      nameserver1:
        description: ''
        type: str
      nameserver2:
        description: ''
        type: str
      nameserver3:
        description: ''
        type: str
      netwait_enabled:
        description: ''
        type: bool
      netwait_ip:
        description: ''
        type: list
      service_announcement:
        description: ''
        suboptions:
          mdns:
            type: bool
          netbios:
            type: bool
          wsd:
            type: bool
        type: dict
"""

EXAMPLES = """
  - name: System Network Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_api_network_configuration:
      model:
        hostname: truenas01
        domain: spatium-cepa.com
        ipv4gateway: 172.16.13.1
        nameserver1: 172.16.13.7
        nameserver2: 172.16.17.7
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
            model=API_ARG_SPECS[TruenasNetworkConfiguration.RESOURCE_API_MODEL_SPEC]
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    network_configuration_resource = TruenasNetworkConfiguration(connection, module.check_mode)

    try:
        model_param = strip_null_module_params(module.params['model'])
        response = network_configuration_resource.update(model_param)
        module.exit_json(
            changed=network_configuration_resource.resource_changed,
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
