# Spatium Cepa TrueNAS Ansible Collection

This repo contains the `spatiumcepa.truenas` Ansible Collection for TrueNAS system management.

## Installation

Specify the collection in your ansible requirements.yml a la

```yaml
roles: []

collections:
  - name: git@github.com:spatium-cepa/ansible-collection-spatiumcepa-truenas.git
    version: 0.0.1
    type: git
```

then install the collection by referencing the requirements.yml

```sh
$ ansible-galaxy collection install -r requirements.yml
```
