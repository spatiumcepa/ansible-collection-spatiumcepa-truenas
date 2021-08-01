from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasIdmap
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

short_description: Manage TrueNAS IDMaps

description:
  - Manage TrueNAS IDMaps via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  model:
    type: dict
    description: ''
    options:
      certificate:
        description: ''
        type: int
      dns_domain_name:
        description: ''
        type: str
      idmap_backend:
        choices:
        - AD
        - AUTORID
        - LDAP
        - NSS
        - RFC2307
        - RID
        - TDB
        description: ''
        type: str
      name:
        description: ''
        type: str
      options:
        description: ''
        suboptions:
          bind_path_group:
            description: ''
            type: str
          bind_path_user:
            description: ''
            type: str
          cn_realm:
            description: ''
            type: str
          description: ''
          ignore_builtin:
            description: ''
            type: bool
          ldap_base_dn:
            description: ''
            type: str
          ldap_domain:
            description: ''
            type: str
          ldap_realm:
            description: ''
            type: bool
          ldap_server:
            description: ''
            type: str
          ldap_url:
            description: ''
            type: str
          ldap_user_dn:
            description: ''
            type: str
          ldap_user_dn_password:
            description: ''
            type: str
          linked_service:
            choices:
            - LOCAL_ACCOUNT
            - LDAP
            - NIS
            description: ''
            type: str
          rangesize:
            description: ''
            type: int
          readonly:
            description: ''
            type: bool
          schema_mode:
            choices:
            - RFC2307
            - SFU
            - SFU20
            description: ''
            type: str
          ssl:
            choices:
            - 'OFF'
            - 'ON'
            - START_TLS
            description: ''
            type: str
          sssd_compat:
            description: ''
            type: bool
          unix_nss_info:
            description: ''
            type: bool
          unix_primary_group:
            description: ''
            type: bool
          user_cn:
            description: ''
            type: bool
        type: dict
      range_high:
        description: ''
        type: int
      range_low:
        description: ''
        type: int
"""

EXAMPLES = """
  - name: Interface Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_api_interface:
      model:
        name: DS_TYPE_ACTIVEDIRECTORY
        options:
          schema_mode: RFC2307
          unix_nss_info: true
          unix_primary_group: true
        range_high: 9000000
        range_low: 2000
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
            model=API_ARG_SPECS[TruenasIdmap.RESOURCE_API_MODEL],
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    idmap_resource = TruenasIdmap(connection, module.check_mode)

    try:
        response = None
        model_param = strip_null_module_params(module.params['model'])

        response = idmap_resource.update_item(model_param)
        failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK

        module.exit_json(
            changed=idmap_resource.resource_changed,
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
