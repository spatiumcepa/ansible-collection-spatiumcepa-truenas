from __future__ import absolute_import, division, print_function
__metaclass__ = type

import collections

""" it is unclear what JSON response is structured as
{
  "0": {
    "entry": [
      "/mnt/tank/storage",
      "/mnt/tank/iocage/jails/syncthing-test1/root/mnt/tank/storage",
      "nullfs",
      "rw",
      "0",
      "0"
    ],
    "type": "USER"
  },
  "1": {
    "entry": [
      "/mnt/tank/otherdata",
      "/mnt/tank/iocage/jails/syncthing-test1/root/mnt/tank/otherdata",
      "nullfs",
      "rw",
      "0",
      "0"
    ],
    "type": "USER"
  }
}
so let's convert it to a structured JSON that we can json_query
"""


def structure_truenas_api_jail_fstab_entry_response(entry_response):
    structured_entries = []

    for entry_key, entry_value in entry_response.items():
        entry_type = entry_value['type']
        entry_source = entry_value['entry'][0]
        entry_destination = entry_value['entry'][1]
        entry_fstype = entry_value['entry'][2]
        entry_fsoptions = entry_value['entry'][3]
        entry_dump = entry_value['entry'][4]
        entry_pass = entry_value['entry'][5]

        structured_entry = {
            'index': entry_key,
            'type': entry_type,
            'source': entry_source,
            'destination': entry_destination,
            'fstype': entry_fstype,
            'fsoptions': entry_fsoptions,
            'dump': entry_dump,
            'pass': entry_pass,
        }
        structured_entries.append(structured_entry)

    return structured_entries


"""
find API group id for group named group_name
GET /api/v2.0/groups JSON looks like this
[
    {
        "builtin": false,
        "gid": 983,
        "group": "syncthing",
        "id": 46,
        "id_type_both": false,
        "local": true,
        "smb": true,
        "sudo": false,
        "sudo_commands": [],
        "sudo_nopasswd": false,
        "users": [
            36
        ]
    }
]
"""


def truenas_group_id_for_name(group_list, group_name):
    for group_item in group_list:
        if group_item["group"] == group_name:
            return group_item["id"]
    return None


class FilterModule(object):
    def filters(self):
        return {
            'structure_truenas_api_jail_fstab_entry_response': structure_truenas_api_jail_fstab_entry_response,
            'truenas_group_id_for_name': truenas_group_id_for_name,
        }
