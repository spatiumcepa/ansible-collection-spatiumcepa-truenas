from __future__ import absolute_import, division, print_function
__metaclass__ = type

# module argument specs derived from TrueNAS API v2.0 OpenAPI Spec 3.0 definition


def strip_null_module_params(params):
    return {k: v for k, v in params.items() if v is not None}


API_ARG_SPECS = {
    "activedirectory_update": {
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
    "alert_service_create": {
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
    "idmap_domain_create": {
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
    "nfs_update": {
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
    "smb_update": {
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
    "ssh_update": {
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
    "ntp_create": {
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
