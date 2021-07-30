from __future__ import absolute_import, division, print_function
__metaclass__ = type

# module argument specs derived from TrueNAS API v2.0 OpenAPI Spec 3.0 definition


def strip_null_module_params(params):
    return {k: v for k, v in params.items() if v is not None}


API_ARG_SPECS = {
    "group_create": {
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
    "interface_create": {
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
    "mail_update": {
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
    "global_configuration_update": {
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
    "system_advanced_update": {
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
    "general_settings": {
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
    "user_create": {
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
    }
}
