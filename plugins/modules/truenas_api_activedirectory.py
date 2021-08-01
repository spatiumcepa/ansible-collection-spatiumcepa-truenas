from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasActivedirectory
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
module: truenas_api_activedirectory

short_description: Configure TrueNAS ActiveDirectory settings

description:
  - Configure TrueNAS ActiveDirectory via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  model:
    type: dict
    description: ''
    options:
      allow_dns_updates:
        description: ''
        type: bool
      allow_trusted_doms:
        description: ''
        type: bool
      bindname:
        description: ''
        type: str
      bindpw:
        description: ''
        type: str
      createcomputer:
        description: ''
        type: str
      disable_freenas_cache:
        description: ''
        type: bool
      dns_timeout:
        description: ''
        type: int
      domainname:
        description: ''
        type: str
      enable:
        description: ''
        type: bool
      kerberos_principal:
        description: ''
        type: str
      kerberos_realm:
        description: ''
        type: int
      netbiosalias:
        description: ''
        type: list
      netbiosname:
        description: ''
        type: str
      netbiosname_b:
        description: ''
        type: str
      nss_info:
        choices:
        - SFU
        - SFU20
        - RFC2307
        description: ''
        type: str
      restrict_pam:
        description: ''
        type: bool
      site:
        description: ''
        type: str
      timeout:
        description: ''
        type: int
      use_default_domain:
        description: ''
        type: bool
      verbose_logging:
        description: ''
        type: bool
"""

EXAMPLES = """
  - name: ActiveDirectory Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_api_activedirectory:
      model:
        allow_dns_updates: true
        allow_trusted_doms: false
        bindname: appliance_add
        bindpw: password1
        createcomputer: Spatium Cepa/Machines/Appliances
        disable_freenas_cache: false
        dns_timeout: 10
        domainname: spatium-cepa.com
        enable: true
        netbiosname: "{{ inventory_hostname }}"
        nss_info: RFC2307
        restrict_pam: false
        site: "{{ corporate_site_name }}"
        timeout: 60
        use_default_domain: true
        verbose_logging: true
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
            model=API_ARG_SPECS[TruenasActivedirectory.RESOURCE_API_MODEL]
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    activedirectory_resource = TruenasActivedirectory(connection, module.check_mode)

    try:
        model_param = strip_null_module_params(module.params['model'])
        response = activedirectory_resource.update(model_param)
        module.exit_json(
            changed=activedirectory_resource.resource_changed,
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
