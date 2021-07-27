from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: truenas_api_system_state_facts

short_description: Retrieve TrueNAS system state

version_added: 2.10

description: Retrieve TrueNAS system state facts

author:
    - Nicholas Kiraly (@nkiraly)
'''

EXAMPLES = """
- name: Gather TrueNAS System State Facts
  connection: connection: spatiumcepa.truenas.truenas_api
  spatiumcepa.truenas.truenas_api_system_state_facts:
  register: system_state_task_result
"""

RETURN = """
# These are examples of possible return values, and in general should use other names for return values.
ansible_facts:
  description: TrueNAS System State Facts
  returned: always
  type: dict
  contains:
    system_state:
      description: System State - one of BOOTING, READY, SHUTTING_DOWN
      type: str
      returned: If /system/state RESTful API is responding
      sample: 'READY'
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection, ConnectionError
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasSystemState
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import TruenasServerError, TruenasModelError, TruenasUnexpectedResponse


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
    system_state_resource = TruenasSystemState(connection, module.check_mode)

    try:
        response_status, response_headers, response_data = system_state_resource.read()
        system_state = response_data
        result['ansible_facts'] = {
            'system_state': system_state
        }
        module.exit_json(**result)

    except TruenasServerError as e:
        module.fail_json(msg='Server returned an error, satus code: %s. '
                             'Server response: %s' % (e.code, e.response))
    except TruenasModelError as e:
        module.fail_json(msg='Data model error: %s' % (e.code, e.response))
                             
    except TruenasUnexpectedResponse as e:
        module.fail_json(msg=e.args[0])

    except ConnectionError as e:
        module.fail_json(msg=e.args[0])

if __name__ == '__main__':
    main()
