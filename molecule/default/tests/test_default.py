import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nfs_package(host):
    pkg = host.package('nfs-utils')

    assert pkg.is_installed


def test_nfs_service(host):
    vrt = host.ansible("setup")["ansible_facts"]["ansible_virtualization_type"]

    if vrt != 'docker':
        if host.system_info.distribution == "CentOS" or \
           host.system_info.distribution == "RedHat":
            srv = host.service('nfs')

            assert srv.is_running
            assert srv.is_enabled

        if host.system_info.distribution == "Fedora":
            srv = host.service('nfs-server')

            assert srv.is_running
            assert srv.is_enabled


def test_nfs_directory(host):
    dir = host.file('/testshare')

    if host.system_info.distribution == "CentOS" or \
       host.system_info.distribution == "RedHat":

        assert dir.is_directory
        assert dir.user == 'nfsnobody'
        assert dir.group == 'nfsnobody'

    if host.system_info.distribution == "Fedora":

        assert dir.is_directory
        assert dir.user == 'nobody'
        assert dir.group == 'nobody'


def test_nfs_exports(host):
    file = host.file('/etc/exports')

    assert file.is_file
    assert file.user == 'root'
    assert file.group == 'root'


def test_nfs_exports_d(host):
    file = host.file('/etc/exports.d/testshare.exports')

    assert file.is_file
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.contains('/testshare')
