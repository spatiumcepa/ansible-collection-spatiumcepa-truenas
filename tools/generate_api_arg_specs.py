# process TrueNAS API v2.0 OpenAPI Spec 3.0 definition
# turn it into ansible module spec objects map
#
from __future__ import absolute_import, division, print_function
__metaclass__ = type

import sys
import json

# list of API schema IDs we care about generating for plugins/module_utils/arg_specs.py
schema_id_white_list = [
    "activedirectory_update_0",
    "alertservice_create_0",
    "alertservice_update_1",
    "cronjob_create_0",
    "cronjob_update_1",
    "group_create_0",
    "group_update_1",
    "idmap_create_0",
    "idmap_update_1",
    "interface_create_0",
    "interface_update_1",
    "mail_update_0",
    "network_configuration_update_0",
    "nfs_update_0",
    "pool_dataset_create_0",
    "pool_dataset_update_1",
    "pool_snapshottask_create_0",
    "pool_snapshottask_update_1",
    "replication_create_0",
    "replication_update_1",
    "rsynctask_create_0",
    "rsynctask_update_1",
    "sharing_nfs_create_0",
    "sharing_nfs_update_1",
    "sharing_smb_create_0",
    "sharing_smb_update_1",
    "smb_update_0",
    "ssh_update_0",
    "system_advanced_update_0",
    "system_general_update_0",
    "system_ntpserver_create_0",
    "system_ntpserver_update_1",
    "system_reboot_0",
    "user_create_0",
    "user_update_1",
    "update_update_0"
]


oas = json.load(sys.stdin)

schemas = oas["components"]["schemas"]


def schema_name_filter(schema_id, schema):
    name = schema_id
    if "title" in schema:
        name = schema["title"]
    return name


def schema_to_spec(schema_id, schema, options_name='options'):
    spec = {}

    schema_type = None
    # check any of types, if they are multiple, use string
    if "anyOf" in schema:
        for aoi in schema["anyOf"]:
            if schema_type is None:
                schema_type = aoi["type"]
            elif schema_type != aoi["type"]:
                schema_type = "string"
    else:
        schema_type = schema["type"]

    if schema_type == "boolean":
        spec["type"] = "bool"
    elif schema_type == "integer":
        spec["type"] = "int"
    elif schema_type == "array":
        spec["type"] = "list"
    elif schema_type == "object":
        spec["type"] = "dict"
        options = {}
        for property_name, property_schema in schema["properties"].items():
            option_name = schema_name_filter(property_name, property_schema)
            options[option_name] = schema_to_spec(property_name, property_schema, 'suboptions')
        spec[options_name] = options
    elif schema_type == "string":
        spec["type"] = "str"
        if "enum" in schema:
            spec["choices"] = schema["enum"]
    else:
        raise ValueError("unknown schema type {} for schema_id {}".format(schema_type, schema_id))

    return spec


arg_specs = {}

if len(sys.argv) > 1 is not None:
    schema_id_white_list = [
        sys.argv[1]
    ]

for schema_id, schema in schemas.items():
    # print(json.dumps(schema))
    if schema_id in schema_id_white_list:
        # arg spec names are the ID or the title name if specified
        schema_name = schema_name_filter(schema_id, schema)
        schema_arg_spec = schema_to_spec(schema_id, schema)
        # print(schema_arg_spec)
        arg_specs[schema_id] = schema_arg_spec

sys.stdout.write(json.dumps(arg_specs))
