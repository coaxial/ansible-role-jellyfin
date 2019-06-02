import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pkg_install(host):
    p = host.package("jellyfin")

    assert p.is_installed


def test_jellyfin_started(host):
    s = host.service('jellyfin')

    assert s.is_running
    assert s.is_enabled
