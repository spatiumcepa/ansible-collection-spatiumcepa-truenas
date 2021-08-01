from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasSystemAdvanced
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
module: truenas_api_system_advanced

short_description: Configure TrueNAS System Advanced settings

description:
  - Configure TrueNAS System Advanced settings via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  model:
    type: dict
    description: ''
    options:
      advancedmode:
        description: ''
        type: bool
      anonstats:
        description: ''
        type: bool
      autotune:
        description: ''
        type: bool
      boot_scrub:
        description: ''
        type: int
      consolemenu:
        description: ''
        type: bool
      consolemsg:
        description: ''
        type: bool
      debugkernel:
        description: ''
        type: bool
      fqdn_syslog:
        description: ''
        type: bool
      motd:
        description: ''
        type: str
      overprovision:
        description: ''
        type: int
      powerdaemon:
        description: ''
        type: bool
      sed_passwd:
        description: ''
        type: str
      sed_user:
        choices:
        - USER
        - MASTER
        description: ''
        type: str
      serialconsole:
        description: ''
        type: bool
      serialport:
        description: ''
        type: str
      serialspeed:
        choices:
        - '9600'
        - '19200'
        - '38400'
        - '57600'
        - '115200'
        description: ''
        type: str
      swapondrive:
        description: ''
        type: int
      syslog_tls_certificate:
        description: ''
        type: int
      syslog_transport:
        choices:
        - UDP
        - TCP
        - TLS
        description: ''
        type: str
      sysloglevel:
        choices:
        - F_EMERG
        - F_ALERT
        - F_CRIT
        - F_ERR
        - F_WARNING
        - F_NOTICE
        - F_INFO
        - F_DEBUG
        - F_IS_DEBUG
        description: ''
        type: str
      syslogserver:
        description: ''
        type: str
      traceback:
        description: ''
        type: bool
      uploadcrash:
        description: ''
        type: bool
"""

EXAMPLES = """
  - name: System Advanced Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_api_system_advanced:
      model:
        autotune: true
        consolemenu: true
        serialconsole: true
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
            model=API_ARG_SPECS[TruenasSystemAdvanced.RESOURCE_API_MODEL]
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    system_general_resource = TruenasSystemAdvanced(connection, module.check_mode)

    try:
        model_param = strip_null_module_params(module.params['model'])
        response = system_general_resource.update(model_param)
        module.exit_json(
            changed=system_general_resource.resource_changed,
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
