import pytest
import os
from ospclientsdk.exceptions import OspShellError
from ospclientsdk import ClientShell


@pytest.fixture(scope='class')
def clouds_dict():
    return dict(clouds=dict(test=dict(auth=dict(auth_url='http://cloud.openstack.org'))))


@pytest.fixture(scope='class')
def flat_dict():
    return dict(auth_url='http://cloud.openstack.org',
                username='tester',
                password='changeMe123',
                project_name='test')


@pytest.fixture(scope='class')
def server_create_options():
    return dict(image='rhel-7.5-server-x86_64',
                flavor='m1.small',
                network=['provider_net', 'private_net'],
                max=2,
                key_name='test-key')


class TestShell(object):


    @staticmethod
    def test_shell_creds_dict(clouds_dict):
        shell = ClientShell(cloud_dict=clouds_dict, cloud='test')
        assert os.environ.get('OS_AUTH_URL', {})

    @staticmethod
    def test_shell_creds_wrong_cloud(clouds_dict):
        with pytest.raises(OspShellError):
            shell = ClientShell(cloud_dict=clouds_dict)

    @staticmethod
    def test_shell_creds_file():
        shell = ClientShell(cloud_file='assets/clouds.yaml')
        assert os.environ.get('OS_AUTH_URL', {})

    @staticmethod
    def test_shell_non_standard_creds_dict(flat_dict):
        shell = ClientShell(cloud_dict=flat_dict)
        assert os.environ.get('OS_AUTH_URL', {})

    @staticmethod
    def test_shell_invalid_cmd(clouds_dict):
        shell = ClientShell(cloud_dict=clouds_dict, cloud='test')
        assert not shell.is_valid_command('bingo_bango')

    @staticmethod
    def test_shell_valid_cmd(clouds_dict):
        shell = ClientShell(cloud_dict=clouds_dict, cloud='test')
        assert shell.is_valid_command('network_trunk_create')

    @staticmethod
    def test_shell_valid_cmd_no_underscores(clouds_dict):
        shell = ClientShell(cloud_dict=clouds_dict, cloud='test')
        assert shell.is_valid_command('network trunk create')

    @staticmethod
    def test_shell_sub_group_command_property(clouds_dict):
        shell = ClientShell(cloud_dict=clouds_dict, cloud='test')
        assert hasattr(shell, 'compute_commands') \
               and 'server_create' in getattr(shell, 'compute_commands')

    @staticmethod
    def test_shell_run_command(clouds_dict):
        shell = ClientShell(cloud_dict=clouds_dict, cloud='test')
        assert shell.run_command('command_list', {})

    @staticmethod
    def test_shell_run_raw_command(clouds_dict):
        shell = ClientShell(cloud_dict=clouds_dict, cloud='test')
        assert shell.run_raw_command('openstack module list -f json')





