from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse, strip_null_module_params
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasMail
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
module: truenas_api_mail

short_description: Configure TrueNAS mail settings

description:
  - Configure TrueNAS mail settings via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  model:
    type: dict
    description: ''
    options:
      fromemail:
        description: ''
        type: str
      fromname:
        description: ''
        type: str
      oauth:
        description: ''
        suboptions:
          client_id:
            type: str
          client_secret:
            type: str
          refresh_token:
            type: str
        type: dict
      outgoingserver:
        description: ''
        type: str
      pass:
        description: ''
        type: str
      port:
        description: ''
        type: int
      security:
        choices:
        - PLAIN
        - SSL
        - TLS
        description: ''
        type: str
      smtp:
        description: ''
        type: bool
      user:
        description: ''
        type: str
"""

EXAMPLES = """
  - name: Email Configuration via TrueNAS API
    spatiumcepa.truenas.truenas_api_mail:
      model:
        fromemail: "truenas@spatium-cepa.com"
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
            model=API_ARG_SPECS[TruenasMail.RESOURCE_API_MODEL_SPEC]
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    mail_resource = TruenasMail(connection, module.check_mode)

    try:
        model_param = strip_null_module_params(module.params['model'])
        response = mail_resource.update(model_param)
        module.exit_json(
            changed=mail_resource.resource_changed,
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
