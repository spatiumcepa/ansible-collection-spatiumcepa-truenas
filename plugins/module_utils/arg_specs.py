from __future__ import absolute_import, division, print_function
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import TruenasModelError
__metaclass__ = type

# truenas_api_* module argument specs map
# derived from TrueNAS API v2.0 OpenAPI Spec 3.0 definition
# generated using tools/generate_api_arg_specs.py
API_ARG_SPECS = {
  "activedirectory_update_0": {
    "type": "dict",
    "options": {
      "domainname": {
        "type": "str"
      },
      "bindname": {
        "type": "str"
      },
      "bindpw": {
        "type": "str"
      },
      "verbose_logging": {
        "type": "bool"
      },
      "use_default_domain": {
        "type": "bool"
      },
      "allow_trusted_doms": {
        "type": "bool"
      },
      "allow_dns_updates": {
        "type": "bool"
      },
      "disable_freenas_cache": {
        "type": "bool"
      },
      "restrict_pam": {
        "type": "bool"
      },
      "site": {
        "type": "str"
      },
      "kerberos_realm": {
        "type": "int"
      },
      "kerberos_principal": {
        "type": "str"
      },
      "timeout": {
        "type": "int"
      },
      "dns_timeout": {
        "type": "int"
      },
      "nss_info": {
        "type": "str",
        "choices": [
          "SFU",
          "SFU20",
          "RFC2307"
        ]
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
      "netbiosalias": {
        "type": "list"
      },
      "enable": {
        "type": "bool"
      }
    }
  },
  "alertservice_create_0": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "type": {
        "type": "str"
      },
      "attributes": {
        "type": "dict",
        "suboptions": {}
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
      },
      "enabled": {
        "type": "bool"
      }
    }
  },
  "alertservice_update_1": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "type": {
        "type": "str"
      },
      "attributes": {
        "type": "dict",
        "suboptions": {}
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
      },
      "enabled": {
        "type": "bool"
      }
    }
  },
  "cronjob_create_0": {
    "type": "dict",
    "options": {
      "enabled": {
        "type": "bool"
      },
      "stderr": {
        "type": "bool"
      },
      "stdout": {
        "type": "bool"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "minute": {
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
          }
        }
      },
      "command": {
        "type": "str"
      },
      "description": {
        "type": "str"
      },
      "user": {
        "type": "str"
      }
    }
  },
  "cronjob_update_1": {
    "type": "dict",
    "options": {
      "enabled": {
        "type": "bool"
      },
      "stderr": {
        "type": "bool"
      },
      "stdout": {
        "type": "bool"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "minute": {
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
          }
        }
      },
      "command": {
        "type": "str"
      },
      "description": {
        "type": "str"
      },
      "user": {
        "type": "str"
      }
    }
  },
  "group_create_0": {
    "type": "dict",
    "options": {
      "gid": {
        "type": "int"
      },
      "name": {
        "type": "str"
      },
      "smb": {
        "type": "bool"
      },
      "sudo": {
        "type": "bool"
      },
      "sudo_nopasswd": {
        "type": "bool"
      },
      "sudo_commands": {
        "type": "list"
      },
      "allow_duplicate_gid": {
        "type": "bool"
      },
      "users": {
        "type": "list"
      }
    }
  },
  "group_update_1": {
    "type": "dict",
    "options": {
      "gid": {
        "type": "int"
      },
      "name": {
        "type": "str"
      },
      "smb": {
        "type": "bool"
      },
      "sudo": {
        "type": "bool"
      },
      "sudo_nopasswd": {
        "type": "bool"
      },
      "sudo_commands": {
        "type": "list"
      },
      "allow_duplicate_gid": {
        "type": "bool"
      },
      "users": {
        "type": "list"
      }
    }
  },
  "idmap_create_0": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "dns_domain_name": {
        "type": "str"
      },
      "range_low": {
        "type": "int"
      },
      "range_high": {
        "type": "int"
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
      "certificate": {
        "type": "int"
      },
      "options": {
        "type": "dict",
        "suboptions": {
          "schema_mode": {
            "type": "str",
            "choices": [
              "RFC2307",
              "SFU",
              "SFU20"
            ]
          },
          "unix_primary_group": {
            "type": "bool"
          },
          "unix_nss_info": {
            "type": "bool"
          },
          "rangesize": {
            "type": "int"
          },
          "readonly": {
            "type": "bool"
          },
          "ignore_builtin": {
            "type": "bool"
          },
          "ldap_base_dn": {
            "type": "str"
          },
          "ldap_user_dn": {
            "type": "str"
          },
          "ldap_user_dn_password": {
            "type": "str"
          },
          "ldap_url": {
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
          "linked_service": {
            "type": "str",
            "choices": [
              "LOCAL_ACCOUNT",
              "LDAP",
              "NIS"
            ]
          },
          "ldap_server": {
            "type": "str"
          },
          "ldap_realm": {
            "type": "bool"
          },
          "bind_path_user": {
            "type": "str"
          },
          "bind_path_group": {
            "type": "str"
          },
          "user_cn": {
            "type": "bool"
          },
          "cn_realm": {
            "type": "str"
          },
          "ldap_domain": {
            "type": "str"
          },
          "sssd_compat": {
            "type": "bool"
          }
        }
      }
    }
  },
  "idmap_update_1": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "dns_domain_name": {
        "type": "str"
      },
      "range_low": {
        "type": "int"
      },
      "range_high": {
        "type": "int"
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
      "certificate": {
        "type": "int"
      },
      "options": {
        "type": "dict",
        "suboptions": {
          "schema_mode": {
            "type": "str",
            "choices": [
              "RFC2307",
              "SFU",
              "SFU20"
            ]
          },
          "unix_primary_group": {
            "type": "bool"
          },
          "unix_nss_info": {
            "type": "bool"
          },
          "rangesize": {
            "type": "int"
          },
          "readonly": {
            "type": "bool"
          },
          "ignore_builtin": {
            "type": "bool"
          },
          "ldap_base_dn": {
            "type": "str"
          },
          "ldap_user_dn": {
            "type": "str"
          },
          "ldap_user_dn_password": {
            "type": "str"
          },
          "ldap_url": {
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
          "linked_service": {
            "type": "str",
            "choices": [
              "LOCAL_ACCOUNT",
              "LDAP",
              "NIS"
            ]
          },
          "ldap_server": {
            "type": "str"
          },
          "ldap_realm": {
            "type": "bool"
          },
          "bind_path_user": {
            "type": "str"
          },
          "bind_path_group": {
            "type": "str"
          },
          "user_cn": {
            "type": "bool"
          },
          "cn_realm": {
            "type": "str"
          },
          "ldap_domain": {
            "type": "str"
          },
          "sssd_compat": {
            "type": "bool"
          }
        }
      }
    }
  },
  "interface_create_0": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "description": {
        "type": "str"
      },
      "type": {
        "type": "str",
        "choices": [
          "BRIDGE",
          "LINK_AGGREGATION",
          "VLAN"
        ]
      },
      "disable_offload_capabilities": {
        "type": "bool"
      },
      "ipv4_dhcp": {
        "type": "bool"
      },
      "ipv6_auto": {
        "type": "bool"
      },
      "aliases": {
        "type": "list"
      },
      "failover_critical": {
        "type": "bool"
      },
      "failover_group": {
        "type": "int"
      },
      "failover_vhid": {
        "type": "int"
      },
      "failover_aliases": {
        "type": "list"
      },
      "failover_virtual_aliases": {
        "type": "list"
      },
      "bridge_members": {
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
      "lag_ports": {
        "type": "list"
      },
      "vlan_parent_interface": {
        "type": "str"
      },
      "vlan_tag": {
        "type": "int"
      },
      "vlan_pcp": {
        "type": "int"
      },
      "mtu": {
        "type": "int"
      },
      "options": {
        "type": "str"
      }
    }
  },
  "interface_update_1": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "description": {
        "type": "str"
      },
      "disable_offload_capabilities": {
        "type": "bool"
      },
      "ipv4_dhcp": {
        "type": "bool"
      },
      "ipv6_auto": {
        "type": "bool"
      },
      "aliases": {
        "type": "list"
      },
      "failover_critical": {
        "type": "bool"
      },
      "failover_group": {
        "type": "int"
      },
      "failover_vhid": {
        "type": "int"
      },
      "failover_aliases": {
        "type": "list"
      },
      "failover_virtual_aliases": {
        "type": "list"
      },
      "bridge_members": {
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
      "lag_ports": {
        "type": "list"
      },
      "vlan_parent_interface": {
        "type": "str"
      },
      "vlan_tag": {
        "type": "int"
      },
      "vlan_pcp": {
        "type": "int"
      },
      "mtu": {
        "type": "int"
      },
      "options": {
        "type": "str"
      }
    }
  },
  "mail_update_0": {
    "type": "dict",
    "options": {
      "fromemail": {
        "type": "str"
      },
      "fromname": {
        "type": "str"
      },
      "outgoingserver": {
        "type": "str"
      },
      "port": {
        "type": "int"
      },
      "security": {
        "type": "str",
        "choices": [
          "PLAIN",
          "SSL",
          "TLS"
        ]
      },
      "smtp": {
        "type": "bool"
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
          "client_id": {
            "type": "str"
          },
          "client_secret": {
            "type": "str"
          },
          "refresh_token": {
            "type": "str"
          }
        }
      }
    }
  },
  "network_configuration_update_0": {
    "type": "dict",
    "options": {
      "hostname": {
        "type": "str"
      },
      "hostname_b": {
        "type": "str"
      },
      "hostname_virtual": {
        "type": "str"
      },
      "domain": {
        "type": "str"
      },
      "domains": {
        "type": "list"
      },
      "service_announcement": {
        "type": "dict",
        "suboptions": {
          "netbios": {
            "type": "bool"
          },
          "mdns": {
            "type": "bool"
          },
          "wsd": {
            "type": "bool"
          }
        }
      },
      "ipv4gateway": {
        "type": "str"
      },
      "ipv6gateway": {
        "type": "str"
      },
      "nameserver1": {
        "type": "str"
      },
      "nameserver2": {
        "type": "str"
      },
      "nameserver3": {
        "type": "str"
      },
      "httpproxy": {
        "type": "str"
      },
      "netwait_enabled": {
        "type": "bool"
      },
      "netwait_ip": {
        "type": "list"
      },
      "hosts": {
        "type": "str"
      }
    }
  },
  "nfs_update_0": {
    "type": "dict",
    "options": {
      "servers": {
        "type": "int"
      },
      "udp": {
        "type": "bool"
      },
      "allow_nonroot": {
        "type": "bool"
      },
      "v4": {
        "type": "bool"
      },
      "v4_v3owner": {
        "type": "bool"
      },
      "v4_krb": {
        "type": "bool"
      },
      "v4_domain": {
        "type": "str"
      },
      "bindip": {
        "type": "list"
      },
      "mountd_port": {
        "type": "int"
      },
      "rpcstatd_port": {
        "type": "int"
      },
      "rpclockd_port": {
        "type": "int"
      },
      "userd_manage_gids": {
        "type": "bool"
      },
      "mountd_log": {
        "type": "bool"
      },
      "statd_lockd_log": {
        "type": "bool"
      }
    }
  },
  "pool_dataset_create_0": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "type": {
        "type": "str",
        "choices": [
          "FILESYSTEM",
          "VOLUME"
        ]
      },
      "volsize": {
        "type": "int"
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
      "sparse": {
        "type": "bool"
      },
      "force_size": {
        "type": "bool"
      },
      "comments": {
        "type": "str"
      },
      "sync": {
        "type": "str",
        "choices": [
          "STANDARD",
          "ALWAYS",
          "DISABLED"
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
      "atime": {
        "type": "str",
        "choices": [
          "ON",
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
      "managedby": {
        "type": "str"
      },
      "quota": {
        "type": "int"
      },
      "quota_warning": {
        "type": "int"
      },
      "quota_critical": {
        "type": "int"
      },
      "refquota": {
        "type": "int"
      },
      "refquota_warning": {
        "type": "int"
      },
      "refquota_critical": {
        "type": "int"
      },
      "reservation": {
        "type": "int"
      },
      "refreservation": {
        "type": "int"
      },
      "special_small_block_size": {
        "type": "int"
      },
      "copies": {
        "type": "int"
      },
      "snapdir": {
        "type": "str",
        "choices": [
          "VISIBLE",
          "HIDDEN"
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
      "readonly": {
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
      "casesensitivity": {
        "type": "str",
        "choices": [
          "SENSITIVE",
          "INSENSITIVE",
          "MIXED"
        ]
      },
      "aclmode": {
        "type": "str",
        "choices": [
          "PASSTHROUGH",
          "RESTRICTED"
        ]
      },
      "acltype": {
        "type": "str",
        "choices": [
          "NOACL",
          "NFS4ACL",
          "POSIXACL"
        ]
      },
      "share_type": {
        "type": "str",
        "choices": [
          "GENERIC",
          "SMB"
        ]
      },
      "xattr": {
        "type": "str",
        "choices": [
          "ON",
          "SA"
        ]
      },
      "encryption_options": {
        "type": "dict",
        "suboptions": {
          "generate_key": {
            "type": "bool"
          },
          "pbkdf2iters": {
            "type": "int"
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
          }
        }
      },
      "encryption": {
        "type": "bool"
      },
      "inherit_encryption": {
        "type": "bool"
      }
    }
  },
  "pool_dataset_update_1": {
    "type": "dict",
    "options": {
      "volsize": {
        "type": "int"
      },
      "force_size": {
        "type": "bool"
      },
      "comments": {
        "type": "str"
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
      "atime": {
        "type": "str",
        "choices": [
          "ON",
          "OFF",
          "INHERIT"
        ]
      },
      "exec": {
        "type": "str",
        "choices": [
          "ON",
          "OFF",
          "INHERIT"
        ]
      },
      "managedby": {
        "type": "str"
      },
      "quota": {
        "type": "int"
      },
      "quota_warning": {
        "type": "str"
      },
      "quota_critical": {
        "type": "str"
      },
      "refquota": {
        "type": "int"
      },
      "refquota_warning": {
        "type": "str"
      },
      "refquota_critical": {
        "type": "str"
      },
      "reservation": {
        "type": "int"
      },
      "refreservation": {
        "type": "int"
      },
      "special_small_block_size": {
        "type": "int"
      },
      "copies": {
        "type": "int"
      },
      "snapdir": {
        "type": "str",
        "choices": [
          "VISIBLE",
          "HIDDEN",
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
      "readonly": {
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
      "aclmode": {
        "type": "str",
        "choices": [
          "PASSTHROUGH",
          "RESTRICTED"
        ]
      },
      "acltype": {
        "type": "str",
        "choices": [
          "NOACL",
          "NFS4ACL",
          "POSIXACL"
        ]
      },
      "xattr": {
        "type": "str",
        "choices": [
          "ON",
          "SA"
        ]
      }
    }
  },
  "pool_snapshottask_create_0": {
    "type": "dict",
    "options": {
      "dataset": {
        "type": "str"
      },
      "recursive": {
        "type": "bool"
      },
      "exclude": {
        "type": "list"
      },
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
      "naming_schema": {
        "type": "str"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "minute": {
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
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          }
        }
      },
      "allow_empty": {
        "type": "bool"
      },
      "enabled": {
        "type": "bool"
      }
    }
  },
  "pool_snapshottask_update_1": {
    "type": "dict",
    "options": {
      "dataset": {
        "type": "str"
      },
      "recursive": {
        "type": "bool"
      },
      "exclude": {
        "type": "list"
      },
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
      "naming_schema": {
        "type": "str"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "minute": {
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
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          }
        }
      },
      "allow_empty": {
        "type": "bool"
      },
      "enabled": {
        "type": "bool"
      }
    }
  },
  "replication_create_0": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "direction": {
        "type": "str",
        "choices": [
          "PUSH",
          "PULL"
        ]
      },
      "transport": {
        "type": "str",
        "choices": [
          "SSH",
          "SSH+NETCAT",
          "LOCAL"
        ]
      },
      "ssh_credentials": {
        "type": "int"
      },
      "netcat_active_side": {
        "type": "str",
        "choices": [
          "LOCAL",
          "REMOTE"
        ]
      },
      "netcat_active_side_listen_address": {
        "type": "str"
      },
      "netcat_active_side_port_min": {
        "type": "int"
      },
      "netcat_active_side_port_max": {
        "type": "int"
      },
      "netcat_passive_side_connect_address": {
        "type": "str"
      },
      "source_datasets": {
        "type": "list"
      },
      "target_dataset": {
        "type": "str"
      },
      "recursive": {
        "type": "bool"
      },
      "exclude": {
        "type": "list"
      },
      "properties": {
        "type": "bool"
      },
      "properties_exclude": {
        "type": "list"
      },
      "replicate": {
        "type": "bool"
      },
      "encryption": {
        "type": "bool"
      },
      "encryption_key": {
        "type": "str"
      },
      "encryption_key_format": {
        "type": "str",
        "choices": [
          "HEX",
          "PASSPHRASE"
        ]
      },
      "encryption_key_location": {
        "type": "str"
      },
      "periodic_snapshot_tasks": {
        "type": "list"
      },
      "naming_schema": {
        "type": "list"
      },
      "also_include_naming_schema": {
        "type": "list"
      },
      "auto": {
        "type": "bool"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "minute": {
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
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          }
        }
      },
      "restrict_schedule": {
        "type": "dict",
        "suboptions": {
          "minute": {
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
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          }
        }
      },
      "only_matching_schedule": {
        "type": "bool"
      },
      "allow_from_scratch": {
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
      "hold_pending_snapshots": {
        "type": "bool"
      },
      "retention_policy": {
        "type": "str",
        "choices": [
          "SOURCE",
          "CUSTOM",
          "NONE"
        ]
      },
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
      "compression": {
        "type": "str",
        "choices": [
          "LZ4",
          "PIGZ",
          "PLZIP"
        ]
      },
      "speed_limit": {
        "type": "int"
      },
      "large_block": {
        "type": "bool"
      },
      "embed": {
        "type": "bool"
      },
      "compressed": {
        "type": "bool"
      },
      "retries": {
        "type": "int"
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
      "enabled": {
        "type": "bool"
      }
    }
  },
  "replication_update_1": {
    "type": "dict",
    "options": {
      "name": {
        "type": "str"
      },
      "direction": {
        "type": "str",
        "choices": [
          "PUSH",
          "PULL"
        ]
      },
      "transport": {
        "type": "str",
        "choices": [
          "SSH",
          "SSH+NETCAT",
          "LOCAL"
        ]
      },
      "ssh_credentials": {
        "type": "int"
      },
      "netcat_active_side": {
        "type": "str",
        "choices": [
          "LOCAL",
          "REMOTE"
        ]
      },
      "netcat_active_side_listen_address": {
        "type": "str"
      },
      "netcat_active_side_port_min": {
        "type": "int"
      },
      "netcat_active_side_port_max": {
        "type": "int"
      },
      "netcat_passive_side_connect_address": {
        "type": "str"
      },
      "source_datasets": {
        "type": "list"
      },
      "target_dataset": {
        "type": "str"
      },
      "recursive": {
        "type": "bool"
      },
      "exclude": {
        "type": "list"
      },
      "properties": {
        "type": "bool"
      },
      "properties_exclude": {
        "type": "list"
      },
      "replicate": {
        "type": "bool"
      },
      "encryption": {
        "type": "bool"
      },
      "encryption_key": {
        "type": "str"
      },
      "encryption_key_format": {
        "type": "str",
        "choices": [
          "HEX",
          "PASSPHRASE"
        ]
      },
      "encryption_key_location": {
        "type": "str"
      },
      "periodic_snapshot_tasks": {
        "type": "list"
      },
      "naming_schema": {
        "type": "list"
      },
      "also_include_naming_schema": {
        "type": "list"
      },
      "auto": {
        "type": "bool"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "minute": {
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
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          }
        }
      },
      "restrict_schedule": {
        "type": "dict",
        "suboptions": {
          "minute": {
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
          "begin": {
            "type": "str"
          },
          "end": {
            "type": "str"
          }
        }
      },
      "only_matching_schedule": {
        "type": "bool"
      },
      "allow_from_scratch": {
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
      "hold_pending_snapshots": {
        "type": "bool"
      },
      "retention_policy": {
        "type": "str",
        "choices": [
          "SOURCE",
          "CUSTOM",
          "NONE"
        ]
      },
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
      "compression": {
        "type": "str",
        "choices": [
          "LZ4",
          "PIGZ",
          "PLZIP"
        ]
      },
      "speed_limit": {
        "type": "int"
      },
      "large_block": {
        "type": "bool"
      },
      "embed": {
        "type": "bool"
      },
      "compressed": {
        "type": "bool"
      },
      "retries": {
        "type": "int"
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
      "enabled": {
        "type": "bool"
      }
    }
  },
  "rsynctask_create_0": {
    "type": "dict",
    "options": {
      "path": {
        "type": "str"
      },
      "user": {
        "type": "str"
      },
      "remotehost": {
        "type": "str"
      },
      "remoteport": {
        "type": "int"
      },
      "mode": {
        "type": "str",
        "choices": [
          "MODULE",
          "SSH"
        ]
      },
      "remotemodule": {
        "type": "str"
      },
      "remotepath": {
        "type": "str"
      },
      "validate_rpath": {
        "type": "bool"
      },
      "direction": {
        "type": "str",
        "choices": [
          "PULL",
          "PUSH"
        ]
      },
      "desc": {
        "type": "str"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "minute": {
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
          }
        }
      },
      "recursive": {
        "type": "bool"
      },
      "times": {
        "type": "bool"
      },
      "compress": {
        "type": "bool"
      },
      "archive": {
        "type": "bool"
      },
      "delete": {
        "type": "bool"
      },
      "quiet": {
        "type": "bool"
      },
      "preserveperm": {
        "type": "bool"
      },
      "preserveattr": {
        "type": "bool"
      },
      "delayupdates": {
        "type": "bool"
      },
      "extra": {
        "type": "list"
      },
      "enabled": {
        "type": "bool"
      }
    }
  },
  "rsynctask_update_1": {
    "type": "dict",
    "options": {
      "path": {
        "type": "str"
      },
      "user": {
        "type": "str"
      },
      "remotehost": {
        "type": "str"
      },
      "remoteport": {
        "type": "int"
      },
      "mode": {
        "type": "str",
        "choices": [
          "MODULE",
          "SSH"
        ]
      },
      "remotemodule": {
        "type": "str"
      },
      "remotepath": {
        "type": "str"
      },
      "validate_rpath": {
        "type": "bool"
      },
      "direction": {
        "type": "str",
        "choices": [
          "PULL",
          "PUSH"
        ]
      },
      "desc": {
        "type": "str"
      },
      "schedule": {
        "type": "dict",
        "suboptions": {
          "minute": {
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
          }
        }
      },
      "recursive": {
        "type": "bool"
      },
      "times": {
        "type": "bool"
      },
      "compress": {
        "type": "bool"
      },
      "archive": {
        "type": "bool"
      },
      "delete": {
        "type": "bool"
      },
      "quiet": {
        "type": "bool"
      },
      "preserveperm": {
        "type": "bool"
      },
      "preserveattr": {
        "type": "bool"
      },
      "delayupdates": {
        "type": "bool"
      },
      "extra": {
        "type": "list"
      },
      "enabled": {
        "type": "bool"
      }
    }
  },
  "sharing_nfs_create_0": {
    "type": "dict",
    "options": {
      "paths": {
        "type": "list"
      },
      "comment": {
        "type": "str"
      },
      "networks": {
        "type": "list"
      },
      "hosts": {
        "type": "list"
      },
      "alldirs": {
        "type": "bool"
      },
      "ro": {
        "type": "bool"
      },
      "quiet": {
        "type": "bool"
      },
      "maproot_user": {
        "type": "str"
      },
      "maproot_group": {
        "type": "str"
      },
      "mapall_user": {
        "type": "str"
      },
      "mapall_group": {
        "type": "str"
      },
      "security": {
        "type": "list"
      },
      "enabled": {
        "type": "bool"
      }
    }
  },
  "sharing_nfs_update_1": {
    "type": "dict",
    "options": {
      "paths": {
        "type": "list"
      },
      "comment": {
        "type": "str"
      },
      "networks": {
        "type": "list"
      },
      "hosts": {
        "type": "list"
      },
      "alldirs": {
        "type": "bool"
      },
      "ro": {
        "type": "bool"
      },
      "quiet": {
        "type": "bool"
      },
      "maproot_user": {
        "type": "str"
      },
      "maproot_group": {
        "type": "str"
      },
      "mapall_user": {
        "type": "str"
      },
      "mapall_group": {
        "type": "str"
      },
      "security": {
        "type": "list"
      },
      "enabled": {
        "type": "bool"
      }
    }
  },
  "sharing_smb_create_0": {
    "type": "dict",
    "options": {
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
      "path_suffix": {
        "type": "str"
      },
      "home": {
        "type": "bool"
      },
      "name": {
        "type": "str"
      },
      "comment": {
        "type": "str"
      },
      "ro": {
        "type": "bool"
      },
      "browsable": {
        "type": "bool"
      },
      "timemachine": {
        "type": "bool"
      },
      "recyclebin": {
        "type": "bool"
      },
      "guestok": {
        "type": "bool"
      },
      "abe": {
        "type": "bool"
      },
      "hostsallow": {
        "type": "list"
      },
      "hostsdeny": {
        "type": "list"
      },
      "aapl_name_mangling": {
        "type": "bool"
      },
      "acl": {
        "type": "bool"
      },
      "durablehandle": {
        "type": "bool"
      },
      "shadowcopy": {
        "type": "bool"
      },
      "streams": {
        "type": "bool"
      },
      "fsrvp": {
        "type": "bool"
      },
      "auxsmbconf": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      }
    }
  },
  "sharing_smb_update_1": {
    "type": "dict",
    "options": {
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
      "path_suffix": {
        "type": "str"
      },
      "home": {
        "type": "bool"
      },
      "name": {
        "type": "str"
      },
      "comment": {
        "type": "str"
      },
      "ro": {
        "type": "bool"
      },
      "browsable": {
        "type": "bool"
      },
      "timemachine": {
        "type": "bool"
      },
      "recyclebin": {
        "type": "bool"
      },
      "guestok": {
        "type": "bool"
      },
      "abe": {
        "type": "bool"
      },
      "hostsallow": {
        "type": "list"
      },
      "hostsdeny": {
        "type": "list"
      },
      "aapl_name_mangling": {
        "type": "bool"
      },
      "acl": {
        "type": "bool"
      },
      "durablehandle": {
        "type": "bool"
      },
      "shadowcopy": {
        "type": "bool"
      },
      "streams": {
        "type": "bool"
      },
      "fsrvp": {
        "type": "bool"
      },
      "auxsmbconf": {
        "type": "str"
      },
      "enabled": {
        "type": "bool"
      }
    }
  },
  "smb_update_0": {
    "type": "dict",
    "options": {
      "netbiosname": {
        "type": "str"
      },
      "netbiosname_b": {
        "type": "str"
      },
      "netbiosalias": {
        "type": "list"
      },
      "workgroup": {
        "type": "str"
      },
      "description": {
        "type": "str"
      },
      "enable_smb1": {
        "type": "bool"
      },
      "unixcharset": {
        "type": "str"
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
      "syslog": {
        "type": "bool"
      },
      "aapl_extensions": {
        "type": "bool"
      },
      "localmaster": {
        "type": "bool"
      },
      "guest": {
        "type": "str"
      },
      "admin_group": {
        "type": "str"
      },
      "filemask": {
        "type": "str"
      },
      "dirmask": {
        "type": "str"
      },
      "ntlmv1_auth": {
        "type": "bool"
      },
      "bindip": {
        "type": "list"
      },
      "smb_options": {
        "type": "str"
      }
    }
  },
  "ssh_update_0": {
    "type": "dict",
    "options": {
      "bindiface": {
        "type": "list"
      },
      "tcpport": {
        "type": "int"
      },
      "rootlogin": {
        "type": "bool"
      },
      "passwordauth": {
        "type": "bool"
      },
      "kerberosauth": {
        "type": "bool"
      },
      "tcpfwd": {
        "type": "bool"
      },
      "compression": {
        "type": "bool"
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
      "weak_ciphers": {
        "type": "list"
      },
      "options": {
        "type": "str"
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
  "system_advanced_update_0": {
    "type": "dict",
    "options": {
      "advancedmode": {
        "type": "bool"
      },
      "autotune": {
        "type": "bool"
      },
      "boot_scrub": {
        "type": "int"
      },
      "consolemenu": {
        "type": "bool"
      },
      "consolemsg": {
        "type": "bool"
      },
      "debugkernel": {
        "type": "bool"
      },
      "fqdn_syslog": {
        "type": "bool"
      },
      "motd": {
        "type": "str"
      },
      "powerdaemon": {
        "type": "bool"
      },
      "serialconsole": {
        "type": "bool"
      },
      "serialport": {
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
      "swapondrive": {
        "type": "int"
      },
      "overprovision": {
        "type": "int"
      },
      "traceback": {
        "type": "bool"
      },
      "uploadcrash": {
        "type": "bool"
      },
      "anonstats": {
        "type": "bool"
      },
      "sed_user": {
        "type": "str",
        "choices": [
          "USER",
          "MASTER"
        ]
      },
      "sed_passwd": {
        "type": "str"
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
      "syslogserver": {
        "type": "str"
      },
      "syslog_transport": {
        "type": "str",
        "choices": [
          "UDP",
          "TCP",
          "TLS"
        ]
      },
      "syslog_tls_certificate": {
        "type": "int"
      }
    }
  },
  "system_general_update_0": {
    "type": "dict",
    "options": {
      "ui_certificate": {
        "type": "int"
      },
      "ui_httpsport": {
        "type": "int"
      },
      "ui_httpsredirect": {
        "type": "bool"
      },
      "ui_httpsprotocols": {
        "type": "list"
      },
      "ui_port": {
        "type": "int"
      },
      "ui_address": {
        "type": "list"
      },
      "ui_v6address": {
        "type": "list"
      },
      "kbdmap": {
        "type": "str"
      },
      "language": {
        "type": "str"
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
      "syslogserver": {
        "type": "str"
      },
      "timezone": {
        "type": "str"
      },
      "crash_reporting": {
        "type": "bool"
      },
      "usage_collection": {
        "type": "bool"
      }
    }
  },
  "system_ntpserver_create_0": {
    "type": "dict",
    "options": {
      "address": {
        "type": "str"
      },
      "burst": {
        "type": "bool"
      },
      "iburst": {
        "type": "bool"
      },
      "prefer": {
        "type": "bool"
      },
      "minpoll": {
        "type": "int"
      },
      "maxpoll": {
        "type": "int"
      },
      "force": {
        "type": "bool"
      }
    }
  },
  "system_ntpserver_update_1": {
    "type": "dict",
    "options": {
      "address": {
        "type": "str"
      },
      "burst": {
        "type": "bool"
      },
      "iburst": {
        "type": "bool"
      },
      "prefer": {
        "type": "bool"
      },
      "minpoll": {
        "type": "int"
      },
      "maxpoll": {
        "type": "int"
      },
      "force": {
        "type": "bool"
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
  "user_create_0": {
    "type": "dict",
    "options": {
      "uid": {
        "type": "int"
      },
      "username": {
        "type": "str"
      },
      "group": {
        "type": "int"
      },
      "group_create": {
        "type": "bool"
      },
      "home": {
        "type": "str"
      },
      "home_mode": {
        "type": "str"
      },
      "shell": {
        "type": "str"
      },
      "full_name": {
        "type": "str"
      },
      "email": {
        "type": "str"
      },
      "password": {
        "type": "str"
      },
      "password_disabled": {
        "type": "bool"
      },
      "locked": {
        "type": "bool"
      },
      "microsoft_account": {
        "type": "bool"
      },
      "smb": {
        "type": "bool"
      },
      "sudo": {
        "type": "bool"
      },
      "sudo_nopasswd": {
        "type": "bool"
      },
      "sudo_commands": {
        "type": "list"
      },
      "sshpubkey": {
        "type": "str"
      },
      "groups": {
        "type": "list"
      },
      "attributes": {
        "type": "dict",
        "suboptions": {}
      }
    }
  },
  "user_update_1": {
    "type": "dict",
    "options": {
      "uid": {
        "type": "int"
      },
      "username": {
        "type": "str"
      },
      "group": {
        "type": "int"
      },
      "home": {
        "type": "str"
      },
      "home_mode": {
        "type": "str"
      },
      "shell": {
        "type": "str"
      },
      "full_name": {
        "type": "str"
      },
      "email": {
        "type": "str"
      },
      "password": {
        "type": "str"
      },
      "password_disabled": {
        "type": "bool"
      },
      "locked": {
        "type": "bool"
      },
      "microsoft_account": {
        "type": "bool"
      },
      "smb": {
        "type": "bool"
      },
      "sudo": {
        "type": "bool"
      },
      "sudo_nopasswd": {
        "type": "bool"
      },
      "sudo_commands": {
        "type": "list"
      },
      "sshpubkey": {
        "type": "str"
      },
      "groups": {
        "type": "list"
      },
      "attributes": {
        "type": "dict",
        "suboptions": {}
      }
    }
  }
}
