jellyfin
=========
  [![Build Status](https://travis-ci.org/coaxial/ansible-role-jellyfin.svg?branch=master)](https://travis-ci.org/coaxial/ansible-role-jellyfin)

Install and configure [Jellyfin](https://jellyfin.media), a free software media system.

Role Variables
--------------

Name | Default | Possible values | Description
---|---|---|---
`jellyfin_repo_key_id` | `4918AABC486CA052358D778D49023CD01DE21A7B` | Any valid key id | Get the key id with `wget -O - https://repo.jellyfin.org/<your_os>/jellyfin_team.gpg.key | gpg --dry-run --import --import-options show-only -` (see the Debian and Ubuntu sections here: https://jellyfin.readthedocs.io/en/latest/administrator-docs/installing/)

Example Playbook
----------------

```yaml
- hosts: all
  vars:
  roles:
    - coaxial.jellyfin
```

License
-------

MIT

Author Information
------------------

Coaxial ([64b.it](https://64b.it))
