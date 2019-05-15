session-recording
=========

This role configures a system for terminal session recording.

Requirements
------------

This role has no required pre-requisites currently.

Role Variables
--------------

Configure session recording with SSSD, the preferred way of managing recorded users or groups:

- `use_sssd` (default: `True`)

Configure SSSD recording scope - `all` / `some` / `none`:

- `scope_sssd` (default: `none`)

Comma-separated list of users to be recorded ( e.g. recordeduser, testuser1 ):

- `users_sssd` (default: `""`)

Comma-separated list of groups to be recorded ( e.g. recordedgroup, wheel, ):

- `groups_sssd` (default: `""`)

Install`the cockpit-session-recording`package(RHEL8 only, currently):

- `install_session_player` (default: `False`)

Log writer type(output destination) of tlog-rec-session. Possible values are: `rsyslog` , `journal`:

- `session_recording_output` (default: `journal`)

ElasticSearch hostname, used when session recording is configured to send to ElasticSearch through rsyslog:

- `elastic_host` (default: `localhost`)

Restart the Cockpit service:

- `restart_cockpit` (default: `False`)

Enable Cockpit to start at system boot (this will not start Cockpit right away, only after reboot)

- `enable_cockpit` (default: `False`)



Dependencies
------------

This role has no dependencies currently.

Example Playbook
----------------
~~~
---
- name: SR
  become: yes
  hosts: all
  roles:
    - role: session-recording
      vars:
          scope_sssd: "some"
          users_sssd: "recordeduser"
          install_session_player: True
          restart_cockpit: True
          enable_cockpit: True
~~~
Testing
-------
In-tree tests are provided that use molecule to test the role against docker containers.
These tests are designed to be used by CI, but they can also be run locally to test it
out while developing.  This is best done by installing molecule in a virtualenv:

  `$ virtualenv .venv`

  `$ source .venv/bin/activate`

  `$ pip install molecule docker`

It is required to run the tests as a user who is authorized to run the 'docker' command
without using sudo.  This is typically accomplished by adding your user to the 'docker'
group on your system.

Additionally, there is a challenge around python-libselinux on platforms that use SELinux.
If you are using a virtualenv, you need to make sure that the selinux python module is
available in the virtualenv.  Even if it is installed on your ansible controller host
and the target host, some of the tasks that are delegated to the locahost will use the
virtualenv.  The selinux module can't be installed via pip.  A workaround for this is
to copy the entire `selinux` directory from your system site-packages location into
the virtualenv site-packages.  You also need to copy the `_selinux.so` file from
site-locations as well.

Once your virtualenv is properly set up, the tests can be run with these commands:

  `$ molecule test`

By default, the test target will be the latest `centos` image from Docker Hub.  You
can test against a different image/tag like so:

  `$ MOLECULE_DISTRO="fedora:28" molecule test`

License
-------

GPL v3.0

Author Information
------------------

- Nathan Kinder @nkinder

- Kirill Glebov @sabbaka
