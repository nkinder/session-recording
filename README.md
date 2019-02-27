session-recording
=========

This role configures a system for terminal session recording.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

You could specify usage of SSSD which is prefered way of managing recorded users or groups:

- `use_sssd` (default: `True`)

The next variable provides info for SSSD recording scope - `all` / `some` / `none`:

- `scope_sssd` (default: `none`)

List of users separated by coma which will be recorded ( e.g. root,user1,q ):

- `users_sssd` (default: `""`)

List of users separated by coma which will be recorded ( e.g. users,wheel ):

- `groups_sssd` (default: `""`)

You can choose to install `cockpit-session-recording` package or not:

- `install_session_player` (default: `False`)

Next variable specifies output of `tlog-rec-session`. Possible values are: `rsyslog` , `journal`:

- `session_recording_output` (default: `journal`)

You can choose to send recorded session to ElasticSearch through rsyslog, therefore next variable provides value hostname of ElasticSearch:

- `elastic_host` (default: `localhost`)

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

---
- name: SR
  become: yes
  hosts: all
  roles:
    - role: session-recording
      vars:
          scope_sssd: "some"
          users_sssd: "q"
          install_session_player: True
          restart_cockpit: True
          enable_cockpit: True

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

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
