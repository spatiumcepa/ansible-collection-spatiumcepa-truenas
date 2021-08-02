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
module: truenas_api_nfs

short_description: Configure TrueNAS NFS settings

description:
  - Configure TrueNAS NFS settings via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  model:
    type: dict
    description: ''
    options:
      allow_nonroot:
        description: ''
        type: bool
      bindip:
        description: ''
        type: list
      mountd_log:
        description: ''
        type: bool
      mountd_port:
        description: ''
        type: int
      rpclockd_port:
        description: ''
        type: int
      rpcstatd_port:
        description: ''
        type: int
      servers:
        description: ''
        type: int
      statd_lockd_log:
        description: ''
        type: bool
      udp:
        description: ''
        type: bool
      userd_manage_gids:
        description: ''
        type: bool
      v4:
        description: ''
        type: bool
      v4_domain:
        description: ''
        type: str
      v4_krb:
        description: ''
        type: bool
      v4_v3owner:
        description: ''
        type: bool
"""

EXAMPLES = """
  - name: NFS Service Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_api_nfs:
      model:
        v4: true
        v4_v3owner: true
        mountd_log: true
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
            model=API_ARG_SPECS["nfs_update_0"]
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    service_resource = TruenasService(connection, module.check_mode)

    try:
        model_param = strip_null_module_params(module.params['model'])
        response = service_resource.service_settings("nfs", "/nfs", model_param)
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
