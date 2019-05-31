<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_nfs.svg)](https://github.com/while-true-do/ansible-role-srv_nfs/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_nfs.svg)](https://github.com/while-true-do/ansible-role-srv_nfs/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_nfs.svg)](https://github.com/while-true-do/ansible-role-srv_nfs/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_nfs.svg)](https://github.com/while-true-do/ansible-role-srv_nfs/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_nfs.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_nfs)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_nfs%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_nfs)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_nfs%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_nfs)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_nfs%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_nfs)

# Ansible Role: srv_nfs

An Ansible Role to install and configure nfs.

## Motivation

NFS is one of the standard tools and used in many environments.

## Description

This role installs and configures nfs and nfs exports.

- install nfs packages
- start nfs services
- take care of firewalld
- create export directories
- configure exports

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible Template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
-   [Ansible Firewalld Module](https://docs.ansible.com/ansible/latest/modules/firewalld_module.html)
-   [Ansible package_facts Module](https://docs.ansible.com/ansible/latest/modules/package_facts_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_nfs)
```
ansible-galaxy install while_true_do.srv_nfs
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_nfs)
```
git clone https://github.com/while-true-do/ansible-role-srv_nfs.git while_true_do.srv_nfs
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_nfs

## Role Management
# Role can be client|server
wtd_srv_nfs_role: "server"

## Package Management
wtd_srv_nfs_package: "nfs-utils"
# State can be present|latest|absent
wtd_srv_nfs_package_state: "present"

### Everything below only applies to role=server.

## Configuration Management
wtd_srv_nfs_conf_exports: []
# - name: "testshare"           # will create /etc/exports.d/testshare.exports
#   path: "/testshare"          # will be created, if not existing
#   owner: "nobody"             # default: nobody
#   group: "nobody"             # default: nobody
#   mode: "0750"                # default: 0750
#   hosts:
#     - host: "192.168.0.1"
#       option: "rw,sync"       # default: sync
#     - host: "192.168.10.0/24"

## Service Management
wtd_srv_nfs_service: "nfs-server"
# State can be started|stopped
wtd_srv_nfs_service_state: "started"
wtd_srv_nfs_service_enabled: true

## Firewalld Management
wtd_srv_nfs_fw_mgmt: true
wtd_srv_nfs_fw_service: "nfs"
# State can be enabled|disabled
wtd_srv_nfs_fw_state: "enabled"
# Zone can be according to defined zones on your machine.
wtd_srv_nfs_fw_zone: "public"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_nfs
```

#### Advanced

```
- hosts: all
  roles:
  - role: while_true_do.srv_nfs
    wtd_srv_nfs_conf_exports:
      - name: "nfs"
        path: "/var/lib/nfs/"
        hosts:
          - host: "192.168.0.1"
          - host: "192.168.0.2"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_nfs/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_nfs/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
