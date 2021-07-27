from __future__ import (absolute_import, division, print_function)
from ansible_collections.spatiumcepa.truenas.plugins.module_utils.common import HTTPResponse
from ansible.plugins.loader import connection_loader
from ansible.plugins.connection import ConnectionBase, ensure_connect
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import Request, ConnectionError
from ansible.errors import AnsibleConnectionFailure
import json
from base64 import b64encode
__metaclass__ = type

DOCUMENTATION = """
author: Nicholas Kiraly <kiraly.nicholas@gmail.com>
connection: truenas_api
short_description: TrueNAS API connection for truenas_api_* modules
description:
  - Connectivity for modules that talk to the TrueNAS REST API version 2.0
version_added: 2.10

options:
  address:
    description:
      - TrueNAS HTTP(S) connection address, e.g. https://truenas1.mydomain
    required: true
    vars:
      - name: ansible_truenas_api_address
    type: str
  username:
    description:
      - username to present for API authentication
    vars:
      - name: ansible_truenas_api_username
    type: str
  password:
    description:
      - password to present for API authentication
    vars:
      - name: ansible_truenas_api_password
    type: str
    aliases:
    - password  # Needed for --ask-pass to come through on delegation
  token:
    description:
      - API token to present for API authentication
    vars:
      - name: ansible_truenas_api_token
    type: str
  validate_certs:
    description:
      - Should SSL certificates be validated
    vars:
      - name: ansible_truenas_validate_certs
    type: bool
    default: True
  persistent_connect_timeout:
    type: int
    description:
    - Configures, in seconds, the amount of time to wait when trying to initially
      establish a persistent connection.  If this value expires before the connection
      to the remote device is completed, the connection will fail.
    default: 30
    ini:
    - section: persistent_connection
      key: connect_timeout
    env:
    - name: ANSIBLE_PERSISTENT_CONNECT_TIMEOUT
    vars:
    - name: ansible_connect_timeout
  persistent_command_timeout:
    type: int
    description:
    - Configures, in seconds, the amount of time to wait for a command to return from
      the remote device.  If this timer is exceeded before the command returns, the
      connection plugin will raise an exception and close.
    default: 30
    ini:
    - section: persistent_connection
      key: command_timeout
    env:
    - name: ANSIBLE_PERSISTENT_COMMAND_TIMEOUT
    vars:
    - name: ansible_command_timeout
  persistent_log_messages:
    type: boolean
    description:
    - This flag will enable logging the command executed and response received from
      target device in the ansible log file. For this option to work 'log_path' ansible
      configuration option is required to be set to a file path with write access.
    - Be sure to fully understand the security implications of enabling this option
      as it could create a security vulnerability by logging sensitive information
      in log file.
    default: false
    ini:
    - section: persistent_connection
      key: log_messages
    env:
    - name: ANSIBLE_PERSISTENT_LOG_MESSAGES
    vars:
    - name: ansible_persistent_log_messages
"""


API_URL_BASE_PATH = "/api/v2.0"


class Connection(ConnectionBase):
    force_persistence = True
    transport = "pms"

    def __init__(self, play_context, *args, **kwargs):
        super(Connection, self).__init__(play_context, *args, **kwargs)
        self._messages = []
        self._sub_plugin = {}
        self._conn_closed = False

        # we are a local connection that performs HTTP requests
        self._local = connection_loader.get("local", play_context, "/dev/null")
        self._local.set_options()

        self._headers = {
            'Accept': 'application/json',
        }

    def _connect(self):
        if self._connected:
            return

        self._address = self.get_option("address").rstrip("/")
        self._base_url = self._address + API_URL_BASE_PATH
        self._username = self.get_option("username")
        self._password = self.get_option("password")
        self._token = self.get_option("token")
        self._validate_certs = self.get_option("validate_certs")
        self._client = Request(
            validate_certs=self._validate_certs
        )

        if self._token:
            self._headers["Authorization"] = "Bearer {}".format(self._token)
        elif self._username:
            self._headers["Authorization"] = "Basic {}".format(
                b64encode(
                    bytes("%s:%s" % (self._username, self._password), "utf-8")
                ).decode("ascii")
            )

        self._local._connect()
        self._connected = True

    def exec_command(self, *args, **kwargs):
        return self._local.exec_command(*args, **kwargs)

    def put_file(self, in_path, out_path):
        return self._local.put_file(in_path, out_path)

    def fetch_file(self, in_path, out_path):
        return self._local.fetch_file(in_path, out_path)

    def close(self):
        self._conn_closed = True
        if not self._connected:
            return
        self._local.close()
        self._connected = False

    def queue_message(self, level, message):
        self._messages.append((level, message))

    def pop_messages(self):
        messages, self._messages = self._messages, []
        return messages

    def _log_messages(self, data):
        pass

    @ensure_connect
    def send_request(self, http_method, url_path, body_params=None, path_params=None, query_params=None):
        headers = self._headers.copy()
        body_data = None
        if body_params:
            body_data = json.dumps(body_params)
            headers["Content-Type"] = "application/json"

        url = self._base_url + url_path
        try:
            response = self._client.open(http_method, url, data=body_data, headers=headers)
            response_status = response.getcode()
            response_headers = dict(response.headers)
            response_body = response.read().decode("utf-8")
            response_data = json.loads(response_body) if response_body else {}
        except HTTPError as e:
            response_status = e.code
            response_headers = {}
            response_data = dict(msg=str(e.reason))
        except (ConnectionError, URLError) as e:
            raise AnsibleConnectionFailure(
                "Could not connect to {0}: {1}".format(url, e.reason)
            )

        response = {
            HTTPResponse.STATUS_CODE: response_status,
            HTTPResponse.HEADERS: response_headers,
            HTTPResponse.BODY: response_data,
        }
        return response
