from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import TruenasModelError
__metaclass__ = type

# truenas_api_* module argument specs map
# derived from TrueNAS API v2.0 OpenAPI Spec 3.0 definition
# generated using tools/generate_api_arg_specs.py
API_ARG_SPECS = {
  "cronjob_create_0": {
    "type": "dict",
    "options": {
      "description": {
        "type": "str"
      },
      "stdout": {
        "type": "bool"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "dom": {
            "type": "str"
          },
          "minute": {
            "type": "str"
          },
          "dow": {
            "type": "str"
          },
          "hour": {
            "type": "str"
          },
          "month": {
            "type": "str"
          }
        }
      },
      "enabled": {
        "type": "bool"
      },
      "command": {
        "type": "str"
      },
      "user": {
        "type": "str"
      },
      "stderr": {
        "type": "bool"
      }
    }
  },
  "idmap_create_0": {
    "type": "dict",
    "options": {
      "range_high": {
        "type": "int"
      },
      "name": {
        "type": "str"
      },
      "certificate": {
        "type": "int"
      },
      "dns_domain_name": {
        "type": "str"
      },
      "idmap_backend": {
        "type": "str",
        "choices": [
          "AD",
          "AUTORID",
          "LDAP",
          "NSS",
          "RFC2307",
          "RID",
          "TDB"
        ]
      },
      "options": {
        "type": "dict",
        "suboptions": {
          "unix_nss_info": {
            "type": "bool"
          },
          "linked_service": {
            "type": "str",
            "choices": [
              "LOCAL_ACCOUNT",
              "LDAP",
              "NIS"
            ]
          },
          "ldap_user_dn": {
            "type": "str"
          },
          "ldap_url": {
            "type": "str"
          },
          "ignore_builtin": {
            "type": "bool"
          },
          "ldap_user_dn_password": {
            "type": "str"
          },
          "ldap_server": {
            "type": "str"
          },
          "unix_primary_group": {
            "type": "bool"
          },
          "ldap_base_dn": {
            "type": "str"
          },
          "bind_path_user": {
            "type": "str"
          },
          "ssl": {
            "type": "str",
            "choices": [
              "OFF",
              "ON",
              "START_TLS"
            ]
          },
          "readonly": {
            "type": "bool"
          },
          "ldap_realm": {
            "type": "bool"
          },
          "schema_mode": {
            "type": "str",
            "choices": [
              "RFC2307",
              "SFU",
              "SFU20"
            ]
          },
          "ldap_domain": {
            "type": "str"
          },
          "cn_realm": {
            "type": "str"
          },
          "user_cn": {
            "type": "bool"
          },
          "rangesize": {
            "type": "int"
          },
          "bind_path_group": {
            "type": "str"
          },
          "sssd_compat": {
            "type": "bool"
          }
        }
      },
      "range_low": {
        "type": "int"
      }
    }
  },
  "sharing_nfs_create_0": {
    "type": "dict",
    "options": {
      "comment": {
        "type": "str"
      },
      "paths": {
        "type": "list"
      },
      "alldirs": {
        "type": "bool"
      },
      "maproot_group": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      },
      "quiet": {
        "type": "bool"
      },
      "mapall_user": {
        "type": "str"
      },
      "maproot_user": {
        "type": "str"
      },
      "hosts": {
        "type": "list"
      },
      "mapall_group": {
        "type": "str"
      },
      "security": {
        "type": "list"
      },
      "ro": {
        "type": "bool"
      },
      "networks": {
        "type": "list"
      }
    }
  },
  "system_advanced_update_0": {
    "type": "dict",
    "options": {
      "sysloglevel": {
        "type": "str",
        "choices": [
          "F_EMERG",
          "F_ALERT",
          "F_CRIT",
          "F_ERR",
          "F_WARNING",
          "F_NOTICE",
          "F_INFO",
          "F_DEBUG",
          "F_IS_DEBUG"
        ]
      },
      "serialport": {
        "type": "str"
      },
      "consolemsg": {
        "type": "bool"
      },
      "motd": {
        "type": "str"
      },
      "swapondrive": {
        "type": "int"
      },
      "sed_user": {
        "type": "str",
        "choices": [
          "USER",
          "MASTER"
        ]
      },
      "syslog_transport": {
        "type": "str",
        "choices": [
          "UDP",
          "TCP",
          "TLS"
        ]
      },
      "sed_passwd": {
        "type": "str"
      },
      "advancedmode": {
        "type": "bool"
      },
      "syslogserver": {
        "type": "str"
      },
      "serialspeed": {
        "type": "str",
        "choices": [
          "9600",
          "19200",
          "38400",
          "57600",
          "115200"
        ]
      },
      "consolemenu": {
        "type": "bool"
      },
      "anonstats": {
        "type": "bool"
      },
      "uploadcrash": {
        "type": "bool"
      },
      "serialconsole": {
        "type": "bool"
      },
      "fqdn_syslog": {
        "type": "bool"
      },
      "powerdaemon": {
        "type": "bool"
      },
      "debugkernel": {
        "type": "bool"
      },
      "boot_scrub": {
        "type": "int"
      },
      "traceback": {
        "type": "bool"
      },
      "overprovision": {
        "type": "int"
      },
      "autotune": {
        "type": "bool"
      },
      "syslog_tls_certificate": {
        "type": "int"
      }
    }
  },
  "update_update_0": {
    "type": "dict",
    "options": {
      "train": {
        "type": "str"
      },
      "reboot": {
        "type": "bool"
      }
    }
  },
  "sharing_nfs_update_1": {
    "type": "dict",
    "options": {
      "comment": {
        "type": "str"
      },
      "paths": {
        "type": "list"
      },
      "alldirs": {
        "type": "bool"
      },
      "maproot_group": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      },
      "quiet": {
        "type": "bool"
      },
      "mapall_user": {
        "type": "str"
      },
      "maproot_user": {
        "type": "str"
      },
      "hosts": {
        "type": "list"
      },
      "mapall_group": {
        "type": "str"
      },
      "security": {
        "type": "list"
      },
      "ro": {
        "type": "bool"
      },
      "networks": {
        "type": "list"
      }
    }
  },
  "nfs_update_0": {
    "type": "dict",
    "options": {
      "v4_domain": {
        "type": "str"
      },
      "mountd_log": {
        "type": "bool"
      },
      "udp": {
        "type": "bool"
      },
      "v4_krb": {
        "type": "bool"
      },
      "v4_v3owner": {
        "type": "bool"
      },
      "bindip": {
        "type": "list"
      },
      "rpcstatd_port": {
        "type": "int"
      },
      "allow_nonroot": {
        "type": "bool"
      },
      "servers": {
        "type": "int"
      },
      "v4": {
        "type": "bool"
      },
      "mountd_port": {
        "type": "int"
      },
      "statd_lockd_log": {
        "type": "bool"
      },
      "userd_manage_gids": {
        "type": "bool"
      },
      "rpclockd_port": {
        "type": "int"
      }
    }
  },
  "sharing_smb_create_0": {
    "type": "dict",
    "options": {
      "comment": {
        "type": "str"
      },
      "guestok": {
        "type": "bool"
      },
      "home": {
        "type": "bool"
      },
      "fsrvp": {
        "type": "bool"
      },
      "timemachine": {
        "type": "bool"
      },
      "path_suffix": {
        "type": "str"
      },
      "abe": {
        "type": "bool"
      },
      "auxsmbconf": {
        "type": "str"
      },
      "recyclebin": {
        "type": "bool"
      },
      "ro": {
        "type": "bool"
      },
      "browsable": {
        "type": "bool"
      },
      "hostsallow": {
        "type": "list"
      },
      "durablehandle": {
        "type": "bool"
      },
      "purpose": {
        "type": "str",
        "choices": [
          "NO_PRESET",
          "DEFAULT_SHARE",
          "ENHANCED_TIMEMACHINE",
          "MULTI_PROTOCOL_AFP",
          "MULTI_PROTOCOL_NFS",
          "PRIVATE_DATASETS",
          "WORM_DROPBOX"
        ]
      },
      "path": {
        "type": "str"
      },
      "name": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      },
      "acl": {
        "type": "bool"
      },
      "aapl_name_mangling": {
        "type": "bool"
      },
      "streams": {
        "type": "bool"
      },
      "shadowcopy": {
        "type": "bool"
      },
      "hostsdeny": {
        "type": "list"
      }
    }
  },
  "pool_dataset_update_1": {
    "type": "dict",
    "options": {
      "acltype": {
        "type": "str",
        "choices": [
          "NOACL",
          "NFS4ACL",
          "POSIXACL"
        ]
      },
      "sync": {
        "type": "str",
        "choices": [
          "STANDARD",
          "ALWAYS",
          "DISABLED",
          "INHERIT"
        ]
      },
      "quota_critical": {
        "type": "str"
      },
      "refquota_warning": {
        "type": "str"
      },
      "xattr": {
        "type": "str",
        "choices": [
          "ON",
          "SA"
        ]
      },
      "compression": {
        "type": "str",
        "choices": [
          "OFF",
          "LZ4",
          "GZIP",
          "GZIP-1",
          "GZIP-9",
          "ZSTD",
          "ZSTD-FAST",
          "ZLE",
          "LZJB",
          "ZSTD-1",
          "ZSTD-2",
          "ZSTD-3",
          "ZSTD-4",
          "ZSTD-5",
          "ZSTD-6",
          "ZSTD-7",
          "ZSTD-8",
          "ZSTD-9",
          "ZSTD-10",
          "ZSTD-11",
          "ZSTD-12",
          "ZSTD-13",
          "ZSTD-14",
          "ZSTD-15",
          "ZSTD-16",
          "ZSTD-17",
          "ZSTD-18",
          "ZSTD-19",
          "ZSTD-FAST-1",
          "ZSTD-FAST-2",
          "ZSTD-FAST-3",
          "ZSTD-FAST-4",
          "ZSTD-FAST-5",
          "ZSTD-FAST-6",
          "ZSTD-FAST-7",
          "ZSTD-FAST-8",
          "ZSTD-FAST-9",
          "ZSTD-FAST-10",
          "ZSTD-FAST-20",
          "ZSTD-FAST-30",
          "ZSTD-FAST-40",
          "ZSTD-FAST-50",
          "ZSTD-FAST-60",
          "ZSTD-FAST-70",
          "ZSTD-FAST-80",
          "ZSTD-FAST-90",
          "ZSTD-FAST-100",
          "ZSTD-FAST-500",
          "ZSTD-FAST-1000",
          "INHERIT"
        ]
      },
      "deduplication": {
        "type": "str",
        "choices": [
          "ON",
          "VERIFY",
          "OFF",
          "INHERIT"
        ]
      },
      "aclmode": {
        "type": "str",
        "choices": [
          "PASSTHROUGH",
          "RESTRICTED"
        ]
      },
      "copies": {
        "type": "int"
      },
      "comments": {
        "type": "str"
      },
      "managedby": {
        "type": "str"
      },
      "readonly": {
        "type": "str",
        "choices": [
          "ON",
          "OFF",
          "INHERIT"
        ]
      },
      "quota_warning": {
        "type": "str"
      },
      "exec": {
        "type": "str",
        "choices": [
          "ON",
          "OFF",
          "INHERIT"
        ]
      },
      "refquota": {
        "type": "int"
      },
      "quota": {
        "type": "int"
      },
      "refquota_critical": {
        "type": "str"
      },
      "volsize": {
        "type": "int"
      },
      "reservation": {
        "type": "int"
      },
      "atime": {
        "type": "str",
        "choices": [
          "ON",
          "OFF",
          "INHERIT"
        ]
      },
      "recordsize": {
        "type": "str",
        "choices": [
          "512",
          "1K",
          "2K",
          "4K",
          "8K",
          "16K",
          "32K",
          "64K",
          "128K",
          "256K",
          "512K",
          "1024K",
          "INHERIT"
        ]
      },
      "force_size": {
        "type": "bool"
      },
      "special_small_block_size": {
        "type": "int"
      },
      "checksum": {
        "type": "str",
        "choices": [
          "ON",
          "OFF",
          "FLETCHER2",
          "FLETCHER4",
          "SHA256",
          "SHA512",
          "SKEIN",
          "INHERIT"
        ]
      },
      "refreservation": {
        "type": "int"
      },
      "snapdir": {
        "type": "str",
        "choices": [
          "VISIBLE",
          "HIDDEN",
          "INHERIT"
        ]
      }
    }
  },
  "system_general_update_0": {
    "type": "dict",
    "options": {
      "ui_httpsport": {
        "type": "int"
      },
      "sysloglevel": {
        "type": "str",
        "choices": [
          "F_EMERG",
          "F_ALERT",
          "F_CRIT",
          "F_ERR",
          "F_WARNING",
          "F_NOTICE",
          "F_INFO",
          "F_DEBUG",
          "F_IS_DEBUG"
        ]
      },
      "language": {
        "type": "str"
      },
      "ui_port": {
        "type": "int"
      },
      "ui_certificate": {
        "type": "int"
      },
      "ui_httpsprotocols": {
        "type": "list"
      },
      "kbdmap": {
        "type": "str"
      },
      "crash_reporting": {
        "type": "bool"
      },
      "ui_v6address": {
        "type": "list"
      },
      "timezone": {
        "type": "str"
      },
      "syslogserver": {
        "type": "str"
      },
      "ui_httpsredirect": {
        "type": "bool"
      },
      "ui_address": {
        "type": "list"
      },
      "usage_collection": {
        "type": "bool"
      }
    }
  },
  "interface_update_1": {
    "type": "dict",
    "options": {
      "aliases": {
        "type": "list"
      },
      "failover_aliases": {
        "type": "list"
      },
      "vlan_parent_interface": {
        "type": "str"
      },
      "description": {
        "type": "str"
      },
      "ipv4_dhcp": {
        "type": "bool"
      },
      "lag_protocol": {
        "type": "str",
        "choices": [
          "LACP",
          "FAILOVER",
          "LOADBALANCE",
          "ROUNDROBIN",
          "NONE"
        ]
      },
      "failover_critical": {
        "type": "bool"
      },
      "failover_group": {
        "type": "int"
      },
      "failover_virtual_aliases": {
        "type": "list"
      },
      "failover_vhid": {
        "type": "int"
      },
      "ipv6_auto": {
        "type": "bool"
      },
      "disable_offload_capabilities": {
        "type": "bool"
      },
      "vlan_pcp": {
        "type": "int"
      },
      "bridge_members": {
        "type": "list"
      },
      "vlan_tag": {
        "type": "int"
      },
      "mtu": {
        "type": "int"
      },
      "lag_ports": {
        "type": "list"
      },
      "options": {
        "type": "str"
      },
      "name": {
        "type": "str"
      }
    }
  },
  "mail_update_0": {
    "type": "dict",
    "options": {
      "fromname": {
        "type": "str"
      },
      "smtp": {
        "type": "bool"
      },
      "outgoingserver": {
        "type": "str"
      },
      "fromemail": {
        "type": "str"
      },
      "user": {
        "type": "str"
      },
      "pass": {
        "type": "str"
      },
      "oauth": {
        "type": "dict",
        "suboptions": {
          "client_secret": {
            "type": "str"
          },
          "client_id": {
            "type": "str"
          },
          "refresh_token": {
            "type": "str"
          }
        }
      },
      "security": {
        "type": "str",
        "choices": [
          "PLAIN",
          "SSL",
          "TLS"
        ]
      },
      "port": {
        "type": "int"
      }
    }
  },
  "pool_snapshottask_update_1": {
    "type": "dict",
    "options": {
      "lifetime_value": {
        "type": "int"
      },
      "lifetime_unit": {
        "type": "str",
        "choices": [
          "HOUR",
          "DAY",
          "WEEK",
          "MONTH",
          "YEAR"
        ]
      },
      "recursive": {
        "type": "bool"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          },
          "hour": {
            "type": "str"
          },
          "dom": {
            "type": "str"
          },
          "month": {
            "type": "str"
          },
          "dow": {
            "type": "str"
          },
          "minute": {
            "type": "str"
          }
        }
      },
      "naming_schema": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      },
      "dataset": {
        "type": "str"
      },
      "allow_empty": {
        "type": "bool"
      },
      "exclude": {
        "type": "list"
      }
    }
  },
  "sharing_smb_update_1": {
    "type": "dict",
    "options": {
      "comment": {
        "type": "str"
      },
      "guestok": {
        "type": "bool"
      },
      "home": {
        "type": "bool"
      },
      "fsrvp": {
        "type": "bool"
      },
      "timemachine": {
        "type": "bool"
      },
      "path_suffix": {
        "type": "str"
      },
      "abe": {
        "type": "bool"
      },
      "auxsmbconf": {
        "type": "str"
      },
      "recyclebin": {
        "type": "bool"
      },
      "ro": {
        "type": "bool"
      },
      "browsable": {
        "type": "bool"
      },
      "hostsallow": {
        "type": "list"
      },
      "durablehandle": {
        "type": "bool"
      },
      "purpose": {
        "type": "str",
        "choices": [
          "NO_PRESET",
          "DEFAULT_SHARE",
          "ENHANCED_TIMEMACHINE",
          "MULTI_PROTOCOL_AFP",
          "MULTI_PROTOCOL_NFS",
          "PRIVATE_DATASETS",
          "WORM_DROPBOX"
        ]
      },
      "path": {
        "type": "str"
      },
      "name": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      },
      "acl": {
        "type": "bool"
      },
      "aapl_name_mangling": {
        "type": "bool"
      },
      "streams": {
        "type": "bool"
      },
      "shadowcopy": {
        "type": "bool"
      },
      "hostsdeny": {
        "type": "list"
      }
    }
  },
  "user_update_1": {
    "type": "dict",
    "options": {
      "username": {
        "type": "str"
      },
      "sshpubkey": {
        "type": "str"
      },
      "password": {
        "type": "str"
      },
      "shell": {
        "type": "str"
      },
      "group": {
        "type": "int"
      },
      "uid": {
        "type": "int"
      },
      "microsoft_account": {
        "type": "bool"
      },
      "home": {
        "type": "str"
      },
      "sudo": {
        "type": "bool"
      },
      "full_name": {
        "type": "str"
      },
      "email": {
        "type": "str"
      },
      "home_mode": {
        "type": "str"
      },
      "sudo_nopasswd": {
        "type": "bool"
      },
      "groups": {
        "type": "list"
      },
      "sudo_commands": {
        "type": "list"
      },
      "locked": {
        "type": "bool"
      },
      "attributes": {
        "type": "dict",
        "suboptions": {}
      },
      "smb": {
        "type": "bool"
      },
      "password_disabled": {
        "type": "bool"
      }
    }
  },
  "system_reboot_0": {
    "type": "dict",
    "options": {
      "delay": {
        "type": "int"
      }
    }
  },
  "alertservice_create_0": {
    "type": "dict",
    "options": {
      "attributes": {
        "type": "dict",
        "suboptions": {}
      },
      "type": {
        "type": "str"
      },
      "name": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      },
      "level": {
        "type": "str",
        "choices": [
          "INFO",
          "NOTICE",
          "WARNING",
          "ERROR",
          "CRITICAL",
          "ALERT",
          "EMERGENCY"
        ]
      }
    }
  },
  "alertservice_update_1": {
    "type": "dict",
    "options": {
      "attributes": {
        "type": "dict",
        "suboptions": {}
      },
      "type": {
        "type": "str"
      },
      "name": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      },
      "level": {
        "type": "str",
        "choices": [
          "INFO",
          "NOTICE",
          "WARNING",
          "ERROR",
          "CRITICAL",
          "ALERT",
          "EMERGENCY"
        ]
      }
    }
  },
  "group_create_0": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "sudo": {
        "type": "bool"
      },
      "gid": {
        "type": "int"
      },
      "sudo_nopasswd": {
        "type": "bool"
      },
      "allow_duplicate_gid": {
        "type": "bool"
      },
      "sudo_commands": {
        "type": "list"
      },
      "smb": {
        "type": "bool"
      },
      "users": {
        "type": "list"
      }
    }
  },
  "cronjob_update_1": {
    "type": "dict",
    "options": {
      "description": {
        "type": "str"
      },
      "stdout": {
        "type": "bool"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "dom": {
            "type": "str"
          },
          "minute": {
            "type": "str"
          },
          "dow": {
            "type": "str"
          },
          "hour": {
            "type": "str"
          },
          "month": {
            "type": "str"
          }
        }
      },
      "enabled": {
        "type": "bool"
      },
      "command": {
        "type": "str"
      },
      "user": {
        "type": "str"
      },
      "stderr": {
        "type": "bool"
      }
    }
  },
  "replication_create_0": {
    "type": "dict",
    "options": {
      "target_dataset": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      },
      "naming_schema": {
        "type": "list"
      },
      "netcat_passive_side_connect_address": {
        "type": "str"
      },
      "netcat_active_side_listen_address": {
        "type": "str"
      },
      "exclude": {
        "type": "list"
      },
      "transport": {
        "type": "str",
        "choices": [
          "SSH",
          "SSH+NETCAT",
          "LOCAL"
        ]
      },
      "netcat_active_side_port_min": {
        "type": "int"
      },
      "recursive": {
        "type": "bool"
      },
      "encryption": {
        "type": "bool"
      },
      "properties_exclude": {
        "type": "list"
      },
      "large_block": {
        "type": "bool"
      },
      "readonly": {
        "type": "str",
        "choices": [
          "SET",
          "REQUIRE",
          "IGNORE"
        ]
      },
      "lifetime_value": {
        "type": "int"
      },
      "replicate": {
        "type": "bool"
      },
      "logging_level": {
        "type": "str",
        "choices": [
          "DEBUG",
          "INFO",
          "WARNING",
          "ERROR"
        ]
      },
      "allow_from_scratch": {
        "type": "bool"
      },
      "direction": {
        "type": "str",
        "choices": [
          "PUSH",
          "PULL"
        ]
      },
      "retention_policy": {
        "type": "str",
        "choices": [
          "SOURCE",
          "CUSTOM",
          "NONE"
        ]
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          },
          "hour": {
            "type": "str"
          },
          "dom": {
            "type": "str"
          },
          "month": {
            "type": "str"
          },
          "dow": {
            "type": "str"
          },
          "minute": {
            "type": "str"
          }
        }
      },
      "auto": {
        "type": "bool"
      },
      "encryption_key_location": {
        "type": "str"
      },
      "encryption_key": {
        "type": "str"
      },
      "also_include_naming_schema": {
        "type": "list"
      },
      "compressed": {
        "type": "bool"
      },
      "source_datasets": {
        "type": "list"
      },
      "netcat_active_side_port_max": {
        "type": "int"
      },
      "properties": {
        "type": "bool"
      },
      "compression": {
        "type": "str",
        "choices": [
          "LZ4",
          "PIGZ",
          "PLZIP"
        ]
      },
      "retries": {
        "type": "int"
      },
      "only_matching_schedule": {
        "type": "bool"
      },
      "lifetime_unit": {
        "type": "str",
        "choices": [
          "HOUR",
          "DAY",
          "WEEK",
          "MONTH",
          "YEAR"
        ]
      },
      "name": {
        "type": "str"
      },
      "hold_pending_snapshots": {
        "type": "bool"
      },
      "speed_limit": {
        "type": "int"
      },
      "netcat_active_side": {
        "type": "str",
        "choices": [
          "LOCAL",
          "REMOTE"
        ]
      },
      "periodic_snapshot_tasks": {
        "type": "list"
      },
      "ssh_credentials": {
        "type": "int"
      },
      "restrict_schedule": {
        "type": "dict",
        "suboptions": {
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          },
          "hour": {
            "type": "str"
          },
          "dom": {
            "type": "str"
          },
          "month": {
            "type": "str"
          },
          "dow": {
            "type": "str"
          },
          "minute": {
            "type": "str"
          }
        }
      },
      "embed": {
        "type": "bool"
      },
      "encryption_key_format": {
        "type": "str",
        "choices": [
          "HEX",
          "PASSPHRASE"
        ]
      }
    }
  },
  "idmap_update_1": {
    "type": "dict",
    "options": {
      "range_high": {
        "type": "int"
      },
      "name": {
        "type": "str"
      },
      "certificate": {
        "type": "int"
      },
      "dns_domain_name": {
        "type": "str"
      },
      "idmap_backend": {
        "type": "str",
        "choices": [
          "AD",
          "AUTORID",
          "LDAP",
          "NSS",
          "RFC2307",
          "RID",
          "TDB"
        ]
      },
      "options": {
        "type": "dict",
        "suboptions": {
          "unix_nss_info": {
            "type": "bool"
          },
          "linked_service": {
            "type": "str",
            "choices": [
              "LOCAL_ACCOUNT",
              "LDAP",
              "NIS"
            ]
          },
          "ldap_user_dn": {
            "type": "str"
          },
          "ldap_url": {
            "type": "str"
          },
          "ignore_builtin": {
            "type": "bool"
          },
          "ldap_user_dn_password": {
            "type": "str"
          },
          "ldap_server": {
            "type": "str"
          },
          "unix_primary_group": {
            "type": "bool"
          },
          "ldap_base_dn": {
            "type": "str"
          },
          "bind_path_user": {
            "type": "str"
          },
          "ssl": {
            "type": "str",
            "choices": [
              "OFF",
              "ON",
              "START_TLS"
            ]
          },
          "readonly": {
            "type": "bool"
          },
          "ldap_realm": {
            "type": "bool"
          },
          "schema_mode": {
            "type": "str",
            "choices": [
              "RFC2307",
              "SFU",
              "SFU20"
            ]
          },
          "ldap_domain": {
            "type": "str"
          },
          "cn_realm": {
            "type": "str"
          },
          "user_cn": {
            "type": "bool"
          },
          "rangesize": {
            "type": "int"
          },
          "bind_path_group": {
            "type": "str"
          },
          "sssd_compat": {
            "type": "bool"
          }
        }
      },
      "range_low": {
        "type": "int"
      }
    }
  },
  "system_ntpserver_create_0": {
    "type": "dict",
    "options": {
      "maxpoll": {
        "type": "int"
      },
      "force": {
        "type": "bool"
      },
      "burst": {
        "type": "bool"
      },
      "prefer": {
        "type": "bool"
      },
      "iburst": {
        "type": "bool"
      },
      "address": {
        "type": "str"
      },
      "minpoll": {
        "type": "int"
      }
    }
  },
  "pool_snapshottask_create_0": {
    "type": "dict",
    "options": {
      "lifetime_value": {
        "type": "int"
      },
      "lifetime_unit": {
        "type": "str",
        "choices": [
          "HOUR",
          "DAY",
          "WEEK",
          "MONTH",
          "YEAR"
        ]
      },
      "recursive": {
        "type": "bool"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          },
          "hour": {
            "type": "str"
          },
          "dom": {
            "type": "str"
          },
          "month": {
            "type": "str"
          },
          "dow": {
            "type": "str"
          },
          "minute": {
            "type": "str"
          }
        }
      },
      "naming_schema": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      },
      "dataset": {
        "type": "str"
      },
      "allow_empty": {
        "type": "bool"
      },
      "exclude": {
        "type": "list"
      }
    }
  },
  "smb_update_0": {
    "type": "dict",
    "options": {
      "unixcharset": {
        "type": "str"
      },
      "netbiosname": {
        "type": "str"
      },
      "aapl_extensions": {
        "type": "bool"
      },
      "workgroup": {
        "type": "str"
      },
      "ntlmv1_auth": {
        "type": "bool"
      },
      "loglevel": {
        "type": "str",
        "choices": [
          "NONE",
          "MINIMUM",
          "NORMAL",
          "FULL",
          "DEBUG"
        ]
      },
      "filemask": {
        "type": "str"
      },
      "description": {
        "type": "str"
      },
      "admin_group": {
        "type": "str"
      },
      "enable_smb1": {
        "type": "bool"
      },
      "syslog": {
        "type": "bool"
      },
      "smb_options": {
        "type": "str"
      },
      "netbiosalias": {
        "type": "list"
      },
      "dirmask": {
        "type": "str"
      },
      "localmaster": {
        "type": "bool"
      },
      "bindip": {
        "type": "list"
      },
      "netbiosname_b": {
        "type": "str"
      },
      "guest": {
        "type": "str"
      }
    }
  },
  "network_configuration_update_0": {
    "type": "dict",
    "options": {
      "netwait_ip": {
        "type": "list"
      },
      "domain": {
        "type": "str"
      },
      "nameserver3": {
        "type": "str"
      },
      "nameserver2": {
        "type": "str"
      },
      "hostname_b": {
        "type": "str"
      },
      "hostname": {
        "type": "str"
      },
      "service_announcement": {
        "type": "dict",
        "suboptions": {
          "mdns": {
            "type": "bool"
          },
          "wsd": {
            "type": "bool"
          },
          "netbios": {
            "type": "bool"
          }
        }
      },
      "hostname_virtual": {
        "type": "str"
      },
      "hosts": {
        "type": "str"
      },
      "domains": {
        "type": "list"
      },
      "httpproxy": {
        "type": "str"
      },
      "ipv4gateway": {
        "type": "str"
      },
      "netwait_enabled": {
        "type": "bool"
      },
      "ipv6gateway": {
        "type": "str"
      },
      "nameserver1": {
        "type": "str"
      }
    }
  },
  "group_update_1": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "sudo": {
        "type": "bool"
      },
      "gid": {
        "type": "int"
      },
      "sudo_nopasswd": {
        "type": "bool"
      },
      "allow_duplicate_gid": {
        "type": "bool"
      },
      "sudo_commands": {
        "type": "list"
      },
      "smb": {
        "type": "bool"
      },
      "users": {
        "type": "list"
      }
    }
  },
  "replication_update_1": {
    "type": "dict",
    "options": {
      "target_dataset": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      },
      "naming_schema": {
        "type": "list"
      },
      "netcat_passive_side_connect_address": {
        "type": "str"
      },
      "netcat_active_side_listen_address": {
        "type": "str"
      },
      "exclude": {
        "type": "list"
      },
      "transport": {
        "type": "str",
        "choices": [
          "SSH",
          "SSH+NETCAT",
          "LOCAL"
        ]
      },
      "netcat_active_side_port_min": {
        "type": "int"
      },
      "recursive": {
        "type": "bool"
      },
      "encryption": {
        "type": "bool"
      },
      "properties_exclude": {
        "type": "list"
      },
      "large_block": {
        "type": "bool"
      },
      "readonly": {
        "type": "str",
        "choices": [
          "SET",
          "REQUIRE",
          "IGNORE"
        ]
      },
      "lifetime_value": {
        "type": "int"
      },
      "replicate": {
        "type": "bool"
      },
      "logging_level": {
        "type": "str",
        "choices": [
          "DEBUG",
          "INFO",
          "WARNING",
          "ERROR"
        ]
      },
      "allow_from_scratch": {
        "type": "bool"
      },
      "direction": {
        "type": "str",
        "choices": [
          "PUSH",
          "PULL"
        ]
      },
      "retention_policy": {
        "type": "str",
        "choices": [
          "SOURCE",
          "CUSTOM",
          "NONE"
        ]
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          },
          "hour": {
            "type": "str"
          },
          "dom": {
            "type": "str"
          },
          "month": {
            "type": "str"
          },
          "dow": {
            "type": "str"
          },
          "minute": {
            "type": "str"
          }
        }
      },
      "auto": {
        "type": "bool"
      },
      "encryption_key_location": {
        "type": "str"
      },
      "encryption_key": {
        "type": "str"
      },
      "also_include_naming_schema": {
        "type": "list"
      },
      "compressed": {
        "type": "bool"
      },
      "source_datasets": {
        "type": "list"
      },
      "netcat_active_side_port_max": {
        "type": "int"
      },
      "properties": {
        "type": "bool"
      },
      "compression": {
        "type": "str",
        "choices": [
          "LZ4",
          "PIGZ",
          "PLZIP"
        ]
      },
      "retries": {
        "type": "int"
      },
      "only_matching_schedule": {
        "type": "bool"
      },
      "lifetime_unit": {
        "type": "str",
        "choices": [
          "HOUR",
          "DAY",
          "WEEK",
          "MONTH",
          "YEAR"
        ]
      },
      "name": {
        "type": "str"
      },
      "hold_pending_snapshots": {
        "type": "bool"
      },
      "speed_limit": {
        "type": "int"
      },
      "netcat_active_side": {
        "type": "str",
        "choices": [
          "LOCAL",
          "REMOTE"
        ]
      },
      "periodic_snapshot_tasks": {
        "type": "list"
      },
      "ssh_credentials": {
        "type": "int"
      },
      "restrict_schedule": {
        "type": "dict",
        "suboptions": {
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          },
          "hour": {
            "type": "str"
          },
          "dom": {
            "type": "str"
          },
          "month": {
            "type": "str"
          },
          "dow": {
            "type": "str"
          },
          "minute": {
            "type": "str"
          }
        }
      },
      "embed": {
        "type": "bool"
      },
      "encryption_key_format": {
        "type": "str",
        "choices": [
          "HEX",
          "PASSPHRASE"
        ]
      }
    }
  },
  "activedirectory_update_0": {
    "type": "dict",
    "options": {
      "use_default_domain": {
        "type": "bool"
      },
      "kerberos_realm": {
        "type": "int"
      },
      "verbose_logging": {
        "type": "bool"
      },
      "bindname": {
        "type": "str"
      },
      "timeout": {
        "type": "int"
      },
      "allow_trusted_doms": {
        "type": "bool"
      },
      "enable": {
        "type": "bool"
      },
      "domainname": {
        "type": "str"
      },
      "site": {
        "type": "str"
      },
      "nss_info": {
        "type": "str",
        "choices": [
          "SFU",
          "SFU20",
          "RFC2307"
        ]
      },
      "netbiosalias": {
        "type": "list"
      },
      "createcomputer": {
        "type": "str"
      },
      "netbiosname": {
        "type": "str"
      },
      "netbiosname_b": {
        "type": "str"
      },
      "bindpw": {
        "type": "str"
      },
      "allow_dns_updates": {
        "type": "bool"
      },
      "disable_freenas_cache": {
        "type": "bool"
      },
      "dns_timeout": {
        "type": "int"
      },
      "restrict_pam": {
        "type": "bool"
      },
      "kerberos_principal": {
        "type": "str"
      }
    }
  },
  "system_ntpserver_update_1": {
    "type": "dict",
    "options": {
      "maxpoll": {
        "type": "int"
      },
      "force": {
        "type": "bool"
      },
      "burst": {
        "type": "bool"
      },
      "prefer": {
        "type": "bool"
      },
      "iburst": {
        "type": "bool"
      },
      "address": {
        "type": "str"
      },
      "minpoll": {
        "type": "int"
      }
    }
  },
  "interface_create_0": {
    "type": "dict",
    "options": {
      "aliases": {
        "type": "list"
      },
      "failover_aliases": {
        "type": "list"
      },
      "vlan_parent_interface": {
        "type": "str"
      },
      "name": {
        "type": "str"
      },
      "ipv4_dhcp": {
        "type": "bool"
      },
      "type": {
        "type": "str",
        "choices": [
          "BRIDGE",
          "LINK_AGGREGATION",
          "VLAN"
        ]
      },
      "description": {
        "type": "str"
      },
      "vlan_pcp": {
        "type": "int"
      },
      "failover_critical": {
        "type": "bool"
      },
      "failover_group": {
        "type": "int"
      },
      "failover_virtual_aliases": {
        "type": "list"
      },
      "lag_protocol": {
        "type": "str",
        "choices": [
          "LACP",
          "FAILOVER",
          "LOADBALANCE",
          "ROUNDROBIN",
          "NONE"
        ]
      },
      "ipv6_auto": {
        "type": "bool"
      },
      "disable_offload_capabilities": {
        "type": "bool"
      },
      "bridge_members": {
        "type": "list"
      },
      "vlan_tag": {
        "type": "int"
      },
      "mtu": {
        "type": "int"
      },
      "lag_ports": {
        "type": "list"
      },
      "options": {
        "type": "str"
      },
      "failover_vhid": {
        "type": "int"
      }
    }
  },
  "user_create_0": {
    "type": "dict",
    "options": {
      "username": {
        "type": "str"
      },
      "sshpubkey": {
        "type": "str"
      },
      "password": {
        "type": "str"
      },
      "shell": {
        "type": "str"
      },
      "group": {
        "type": "int"
      },
      "uid": {
        "type": "int"
      },
      "microsoft_account": {
        "type": "bool"
      },
      "home": {
        "type": "str"
      },
      "sudo": {
        "type": "bool"
      },
      "group_create": {
        "type": "bool"
      },
      "full_name": {
        "type": "str"
      },
      "email": {
        "type": "str"
      },
      "home_mode": {
        "type": "str"
      },
      "sudo_nopasswd": {
        "type": "bool"
      },
      "groups": {
        "type": "list"
      },
      "sudo_commands": {
        "type": "list"
      },
      "locked": {
        "type": "bool"
      },
      "attributes": {
        "type": "dict",
        "suboptions": {}
      },
      "smb": {
        "type": "bool"
      },
      "password_disabled": {
        "type": "bool"
      }
    }
  },
  "ssh_update_0": {
    "type": "dict",
    "options": {
      "sftp_log_facility": {
        "type": "str",
        "choices": [
          "",
          "DAEMON",
          "USER",
          "AUTH",
          "LOCAL0",
          "LOCAL1",
          "LOCAL2",
          "LOCAL3",
          "LOCAL4",
          "LOCAL5",
          "LOCAL6",
          "LOCAL7"
        ]
      },
      "compression": {
        "type": "bool"
      },
      "bindiface": {
        "type": "list"
      },
      "sftp_log_level": {
        "type": "str",
        "choices": [
          "",
          "QUIET",
          "FATAL",
          "ERROR",
          "INFO",
          "VERBOSE",
          "DEBUG",
          "DEBUG2",
          "DEBUG3"
        ]
      },
      "passwordauth": {
        "type": "bool"
      },
      "rootlogin": {
        "type": "bool"
      },
      "kerberosauth": {
        "type": "bool"
      },
      "weak_ciphers": {
        "type": "list"
      },
      "tcpport": {
        "type": "int"
      },
      "options": {
        "type": "str"
      },
      "tcpfwd": {
        "type": "bool"
      }
    }
  },
  "pool_dataset_create_0": {
    "type": "dict",
    "options": {
      "acltype": {
        "type": "str",
        "choices": [
          "NOACL",
          "NFS4ACL",
          "POSIXACL"
        ]
      },
      "sync": {
        "type": "str",
        "choices": [
          "STANDARD",
          "ALWAYS",
          "DISABLED"
        ]
      },
      "quota_critical": {
        "type": "int"
      },
      "refquota_warning": {
        "type": "int"
      },
      "casesensitivity": {
        "type": "str",
        "choices": [
          "SENSITIVE",
          "INSENSITIVE",
          "MIXED"
        ]
      },
      "special_small_block_size": {
        "type": "int"
      },
      "xattr": {
        "type": "str",
        "choices": [
          "ON",
          "SA"
        ]
      },
      "force_size": {
        "type": "bool"
      },
      "share_type": {
        "type": "str",
        "choices": [
          "GENERIC",
          "SMB"
        ]
      },
      "encryption": {
        "type": "bool"
      },
      "aclmode": {
        "type": "str",
        "choices": [
          "PASSTHROUGH",
          "RESTRICTED"
        ]
      },
      "copies": {
        "type": "int"
      },
      "comments": {
        "type": "str"
      },
      "managedby": {
        "type": "str"
      },
      "readonly": {
        "type": "str",
        "choices": [
          "ON",
          "OFF"
        ]
      },
      "quota_warning": {
        "type": "int"
      },
      "type": {
        "type": "str",
        "choices": [
          "FILESYSTEM",
          "VOLUME"
        ]
      },
      "deduplication": {
        "type": "str",
        "choices": [
          "ON",
          "VERIFY",
          "OFF"
        ]
      },
      "exec": {
        "type": "str",
        "choices": [
          "ON",
          "OFF"
        ]
      },
      "refquota": {
        "type": "int"
      },
      "inherit_encryption": {
        "type": "bool"
      },
      "quota": {
        "type": "int"
      },
      "refquota_critical": {
        "type": "int"
      },
      "volsize": {
        "type": "int"
      },
      "reservation": {
        "type": "int"
      },
      "atime": {
        "type": "str",
        "choices": [
          "ON",
          "OFF"
        ]
      },
      "recordsize": {
        "type": "str",
        "choices": [
          "512",
          "1K",
          "2K",
          "4K",
          "8K",
          "16K",
          "32K",
          "64K",
          "128K",
          "256K",
          "512K",
          "1024K"
        ]
      },
      "compression": {
        "type": "str",
        "choices": [
          "OFF",
          "LZ4",
          "GZIP",
          "GZIP-1",
          "GZIP-9",
          "ZSTD",
          "ZSTD-FAST",
          "ZLE",
          "LZJB",
          "ZSTD-1",
          "ZSTD-2",
          "ZSTD-3",
          "ZSTD-4",
          "ZSTD-5",
          "ZSTD-6",
          "ZSTD-7",
          "ZSTD-8",
          "ZSTD-9",
          "ZSTD-10",
          "ZSTD-11",
          "ZSTD-12",
          "ZSTD-13",
          "ZSTD-14",
          "ZSTD-15",
          "ZSTD-16",
          "ZSTD-17",
          "ZSTD-18",
          "ZSTD-19",
          "ZSTD-FAST-1",
          "ZSTD-FAST-2",
          "ZSTD-FAST-3",
          "ZSTD-FAST-4",
          "ZSTD-FAST-5",
          "ZSTD-FAST-6",
          "ZSTD-FAST-7",
          "ZSTD-FAST-8",
          "ZSTD-FAST-9",
          "ZSTD-FAST-10",
          "ZSTD-FAST-20",
          "ZSTD-FAST-30",
          "ZSTD-FAST-40",
          "ZSTD-FAST-50",
          "ZSTD-FAST-60",
          "ZSTD-FAST-70",
          "ZSTD-FAST-80",
          "ZSTD-FAST-90",
          "ZSTD-FAST-100",
          "ZSTD-FAST-500",
          "ZSTD-FAST-1000"
        ]
      },
      "volblocksize": {
        "type": "str",
        "choices": [
          "512",
          "1K",
          "2K",
          "4K",
          "8K",
          "16K",
          "32K",
          "64K",
          "128K"
        ]
      },
      "name": {
        "type": "str"
      },
      "encryption_options": {
        "type": "dict",
        "suboptions": {
          "generate_key": {
            "type": "bool"
          },
          "algorithm": {
            "type": "str",
            "choices": [
              "AES-128-CCM",
              "AES-192-CCM",
              "AES-256-CCM",
              "AES-128-GCM",
              "AES-192-GCM",
              "AES-256-GCM"
            ]
          },
          "passphrase": {
            "type": "str"
          },
          "key": {
            "type": "str"
          },
          "pbkdf2iters": {
            "type": "int"
          }
        }
      },
      "checksum": {
        "type": "str",
        "choices": [
          "ON",
          "OFF",
          "FLETCHER2",
          "FLETCHER4",
          "SHA256",
          "SHA512",
          "SKEIN"
        ]
      },
      "refreservation": {
        "type": "int"
      },
      "sparse": {
        "type": "bool"
      },
      "snapdir": {
        "type": "str",
        "choices": [
          "VISIBLE",
          "HIDDEN"
        ]
      }
    }
  }
}
