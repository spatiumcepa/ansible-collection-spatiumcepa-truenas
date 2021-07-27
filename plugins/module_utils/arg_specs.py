# module argument specs derived from TrueNAS API v2.0 OpenAPI Spec 3.0 definition

# TODO: define specs as dict for resource module implementations to refer to by key name ?
# TODO: generate specs from OAS ?

mail_update_arg_spec = {
    'type': 'dict',
    'options': {
        'fromemail': dict(type='str', required=True),
        'fromname': dict(type='str'),
        'outgoingserver': dict(type='str'),
        'port': dict(type='int', required=True),
        'security': dict(type='str', default='PLAIN', choices=['PLAIN','SSL','TLS']),
        'smtp': dict(type='bool', aliases=['smtp_auth']),
        'user': dict(type='str'),
        'pass': dict(type='str'),
        'oauth': dict(
            type='dict',
            options=dict(
                client_id=dict(type='str'),
                client_secret=dict(type='str'),
                refresh_token=dict(type='str'),
            )
        )
    }
}
