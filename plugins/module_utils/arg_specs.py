from __future__ import absolute_import, division, print_function
__metaclass__ = type

# module argument specs derived from TrueNAS API v2.0 OpenAPI Spec 3.0 definition

API_ARG_SPECS = {
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
    }
}
