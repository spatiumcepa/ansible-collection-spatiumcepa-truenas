# Spatium Cepa TrueNAS Ansible Collection

This repo contains the `spatiumcepa.truenas` Ansible Collection for TrueNAS system management.

## Requirements

- Ansible 2.10+
- jmespath

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

Test collection is installed and usable by listing plugins and modules:

```sh
$ ansible-doc -t connection -l | grep spatium
spatiumcepa.truenas.api             TODO BBQ ...
$ ansible-doc -t module -l | grep spatium
```

## Roles

Roles provided by the spatiumcepa.truenas collection:

- configure - Manage TrueNAS instances via the [TrueNAS API 2.0](https://www.truenas.com/docs/core/api/)
- update - Update TrueNAS instances via the [TrueNAS API 2.0](https://www.truenas.com/docs/core/api/)

## Development

Changes and improvements should be done in a python virtual environment based on the repository Pipfile.

```sh
cd ~/src/ansible-collection-spatiumcepa-truenas
pipenv install --dev --python python3.8
pipenv shell
```

Then you can build and install the collection locally to run test plays

```sh
# specify example config and vault-id for vaulted cluster_secret variable
export ANSIBLE_CONFIG=examples/ansible.cfg

# test collection by installing in local directory
ansible-galaxy collection build --force
rm -rf collections/ansible_collections/spatiumcepa/truenas
ansible-galaxy collection install spatiumcepa-truenas-0.0.1.tar.gz -p ./collections

# make sure the api connection plugin is available
ansible-doc -t connection -l | grep spatium
```

Connection plugin doc list sample output

```sh
(ansible-collection-spatiumcepa-truenas-2rxB0Ia1) nkiraly@galp5-lwx:~/src/ansible-collection-spatiumcepa-truenas$ ansible-doc -t connection -l | grep spatium
spatiumcepa.truenas.api             TODO BBQ ...
```

## Testing in coordination with playbook development

To streamline development testing, symlink this collection into your playbook virtual environment collections directory, such as:

```sh
cd ~/.local/share/virtualenvs/truenas-ansible-playbook-ayo7nGjX/collections/ansible_collections/spatiumcepa/
ln -s ~/src/ansible-collection-spatiumcepa-truenas truenas
```

## Testing with ansible-test

To ansible-test the collection locally, it needs to be in an opinionated directory structure
```sh
mkdir -p /tmp/ansible_collections/spatiumcepa
rm -rf /tmp/ansible_collections/spatiumcepa/truenas
cp -a ~/src/ansible-collection-spatiumcepa-truenas /tmp/ansible_collections/spatiumcepa/truenas
cd /tmp/ansible_collections/spatiumcepa/truenas

ansible-test sanity
```
