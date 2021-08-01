from __future__ import absolute_import, division, print_function
__metaclass__ = type

# module argument specs derived from TrueNAS API v2.0 OpenAPI Spec 3.0 definition


def strip_null_module_params(params):
    return {k: v for k, v in params.items() if v is not None}


API_ARG_SPECS = {
    "interface_create": {
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
    "smb_update": {
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
    "ntp_create": {
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
    "mail_update": {
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
    "ssh_update": {
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
    "group_create": {
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
    "global_configuration_update": {
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
    "system_advanced_update": {
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
    "nfs_update": {
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
    "general_settings": {
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
    "user_create": {
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
    "alert_service_create": {
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
    }
}
