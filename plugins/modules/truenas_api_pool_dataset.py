from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPCode, HTTPResponse, \
    TruenasServerError, TruenasModelError, TruenasUnexpectedResponse
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.resources import TruenasPoolDataset
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
module: truenas_api_pool_dataset

short_description: Manage TrueNAS Groups

description:
  - Manage TrueNAS Groups via REST API

version_added: "0.1"

author: Nicholas Kiraly (@nkiraly)

options:
  state:
    type: str
    description: Desired state of the pool dataset
    default: present
    choices: [ absent, present ]
  model:
    type: dict
    description: ''
    options:
      aclmode:
        choices:
        - PASSTHROUGH
        - RESTRICTED
        description: ''
        type: str
      acltype:
        choices:
        - NOACL
        - NFS4ACL
        - POSIXACL
        description: ''
        type: str
      atime:
        choices:
        - 'ON'
        - 'OFF'
        description: ''
        type: str
      casesensitivity:
        choices:
        - SENSITIVE
        - INSENSITIVE
        - MIXED
        description: ''
        type: str
      comments:
        description: ''
        type: str
      compression:
        choices:
        - 'OFF'
        - LZ4
        - GZIP
        - GZIP-1
        - GZIP-9
        - ZSTD
        - ZSTD-FAST
        - ZLE
        - LZJB
        - ZSTD-1
        - ZSTD-2
        - ZSTD-3
        - ZSTD-4
        - ZSTD-5
        - ZSTD-6
        - ZSTD-7
        - ZSTD-8
        - ZSTD-9
        - ZSTD-10
        - ZSTD-11
        - ZSTD-12
        - ZSTD-13
        - ZSTD-14
        - ZSTD-15
        - ZSTD-16
        - ZSTD-17
        - ZSTD-18
        - ZSTD-19
        - ZSTD-FAST-1
        - ZSTD-FAST-2
        - ZSTD-FAST-3
        - ZSTD-FAST-4
        - ZSTD-FAST-5
        - ZSTD-FAST-6
        - ZSTD-FAST-7
        - ZSTD-FAST-8
        - ZSTD-FAST-9
        - ZSTD-FAST-10
        - ZSTD-FAST-20
        - ZSTD-FAST-30
        - ZSTD-FAST-40
        - ZSTD-FAST-50
        - ZSTD-FAST-60
        - ZSTD-FAST-70
        - ZSTD-FAST-80
        - ZSTD-FAST-90
        - ZSTD-FAST-100
        - ZSTD-FAST-500
        - ZSTD-FAST-1000
        description: ''
        type: str
      copies:
        description: ''
        type: int
      deduplication:
        choices:
        - 'ON'
        - VERIFY
        - 'OFF'
        description: ''
        type: str
      encryption:
        description: ''
        type: bool
      encryption_options:
        description: ''
        suboptions:
          algorithm:
            choices:
            - AES-128-CCM
            - AES-192-CCM
            - AES-256-CCM
            - AES-128-GCM
            - AES-192-GCM
            - AES-256-GCM
            type: str
          generate_key:
            type: bool
          key:
            type: str
          passphrase:
            type: str
          pbkdf2iters:
            type: int
        type: dict
      exec:
        choices:
        - 'ON'
        - 'OFF'
        description: ''
        type: str
      force_size:
        description: ''
        type: bool
      inherit_encryption:
        description: ''
        type: bool
      managedby:
        description: ''
        type: str
      name:
        description: ''
        type: str
      quota:
        description: ''
        type: int
      quota_critical:
        description: ''
        type: int
      quota_warning:
        description: ''
        type: int
      readonly:
        choices:
        - 'ON'
        - 'OFF'
        description: ''
        type: str
      recordsize:
        choices:
        - '512'
        - 1K
        - 2K
        - 4K
        - 8K
        - 16K
        - 32K
        - 64K
        - 128K
        - 256K
        - 512K
        - 1024K
        description: ''
        type: str
      refquota:
        description: ''
        type: int
      refquota_critical:
        description: ''
        type: int
      refquota_warning:
        description: ''
        type: int
      refreservation:
        description: ''
        type: int
      reservation:
        description: ''
        type: int
      share_type:
        choices:
        - GENERIC
        - SMB
        description: ''
        type: str
      snapdir:
        choices:
        - VISIBLE
        - HIDDEN
        description: ''
        type: str
      sparse:
        description: ''
        type: bool
      special_small_block_size:
        description: ''
        type: int
      sync:
        choices:
        - STANDARD
        - ALWAYS
        - DISABLED
        description: ''
        type: str
      type:
        choices:
        - FILESYSTEM
        - VOLUME
        description: ''
        type: str
      volblocksize:
        choices:
        - '512'
        - 1K
        - 2K
        - 4K
        - 8K
        - 16K
        - 32K
        - 64K
        - 128K
        description: ''
        type: str
      volsize:
        description: ''
        type: int
      xattr:
        choices:
        - 'ON'
        - SA
        description: ''
        type: str
"""

EXAMPLES = """
  - name: Manage Pool Dataset via TrueNAS API
    spatiumcepa.truenas.truenas_api_pool_dataset:
      model:
        name: tank/home
        aclmode: PASSTHROUGH
        copies: 1
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
            # TODO: solve pool_dataset_create_0 vs pool_dataset_update_1 model arg spec conflicts
            model=API_ARG_SPECS[TruenasPoolDataset.RESOURCE_API_MODEL],
            state={'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'}
        ),
        supports_check_mode=True,
    )

    connection = Connection(module._socket_path)
    dataset_resource = TruenasPoolDataset(connection, module.check_mode)

    try:
        response = None
        model_param = strip_null_module_params(module.params['model'])
        state_param = module.params['state']

        if state_param == 'present':
            response = dataset_resource.update_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] != HTTPCode.OK
        elif state_param == 'absent':
            response = dataset_resource.delete_item(model_param)
            failed = response[HTTPResponse.STATUS_CODE] not in [HTTPCode.OK, HTTPCode.NOT_FOUND]

        module.exit_json(
            created=dataset_resource.resource_created,
            changed=dataset_resource.resource_changed,
            deleted=dataset_resource.resource_deleted,
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
