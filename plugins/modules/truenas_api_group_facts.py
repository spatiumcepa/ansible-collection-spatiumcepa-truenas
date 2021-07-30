from __future__ import (absolute_import, division, print_function)
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasGroup
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils.basic import AnsibleModule
__metaclass__ = type

DOCUMENTATION = """
module: truenas_api_group_facts

short_description: Retrieve TrueNAS group facts

description:
    - Retrieve TrueNAS group facts via REST API

version_added: "2.10"

author:
    - Nicholas Kiraly (@nkiraly)
"""

EXAMPLES = """
  - name: Gather TrueNAS Groups
    connection: spatiumcepa.truenas.truenas_api
    spatiumcepa.truenas.truenas_api_group_facts:
    register: group_facts_result
"""

RETURN = """
# These are examples of possible return values, and in general should use other names for return values.
ansible_facts:
  description: TrueNAS Group Facts
  returned: always
  type: dict
  contains:
    group:
      description: List of groups configured in the system
      type: list
      returned: always
      sample:
        - builtin: false
          gid: 983
          group: syncthing
          id: 46
          id_type_both: false
          local: true
          smb: true
          sudo: false
          sudo_commands: []
          sudo_nopasswd: false
          users:
            - 36
"""


def main():
    module_args = dict()

    result = dict(
        changed=False,
        ansible_facts=dict(),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    group_resource = TruenasGroup(connection, module.check_mode)

    try:
        response = group_resource.read()
        result['ansible_facts'] = {
            'group': response[HTTPResponse.BODY]
        }
        result['response'] = response
        result['failed'] = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK
        module.exit_json(**result)

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
