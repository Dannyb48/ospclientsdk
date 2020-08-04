import pytest
import mock
import os
from string import Template
from ospclientsdk.helpers import *


class TestCommandDecorator(object):

    def exec_local_cmd(*args, **kwargs):
        if args[2] and isinstance(args[2], SshContext):
            return dict(rc=0, stdout=args[2].hostname)
        return dict(rc=0, stdout=dict(id=123456), stderr="err")

    @staticmethod
    @mock.patch.object(Command, 'exec_local_cmd', exec_local_cmd)
    def test_command_call_func():
        def mock_run(func, cmd, option):
            print("%s %s %s" % (func.__name__, cmd, option))

        cmd = Command(func=mock_run)
        cmd(mock_run, 'server_show', dict(name='test'))

    @staticmethod
    @mock.patch.object(Command, 'exec_local_cmd', exec_local_cmd)
    def test_command_call_func_with_raw():
        def mock_raw_run(func, option):
            print("%s %s" % (func.__name__, option))

        cmd = Command(func=mock_raw_run)
        cmd(mock_raw_run, 'server_show')

    @staticmethod
    @mock.patch.object(Command, 'exec_local_cmd', exec_local_cmd)
    def test_command_call_mixin_func():
        def mock_mixin_run(func, option):
            print("%s %s" % (func.__name__, option))

        cmd = Command(func=mock_mixin_run)
        cmd(mock_mixin_run, 'server_show')

    @staticmethod
    @mock.patch.object(Command, 'exec_local_cmd', exec_local_cmd)
    def test_command_call_normalize_options():
        final_options="""
        --list-1 k-1=v1,k-2=v2 --list-1 k-3=v3,k-4=v4 --list-2 k-5=v5 --list-3 net1 --list-3 net2 --is-true --max 2 --p-dir /tmp --p-file /tmp/key test tgt
        """
        options = dict(
                    res='test',
                    tgt_res='tgt',
                    list_1=[
                        dict(k_1='v1',
                             k_2='v2'
                             ),
                        dict(k_3='v3',
                             k_4='v4'
                             )
                    ],
                    list_2=[
                        dict(k_5='v5')
                    ],
                    list_3=['net1', 'net2'],
                    is_true=True,
                    max=2,
                    p_dir='/tmp',
                    p_file='/tmp/key')

        def mock_run(func, option):
            print("%s %s" % (func, option))

        cmd = Command(func=mock_run)
        noption = getattr(cmd, '_normalize_options')(options)
        assert noption.find(final_options)

    @staticmethod
    @mock.patch.object(Command, 'exec_local_cmd', exec_local_cmd)
    def test_cxt_command_call_func():
        def mock_run(func, cmd, option):
            print("%s %s %s" % (func.__name__, cmd, option))

        with remote_shell(hostname='127.0.0.1'):
            cmd = Command(func=mock_run)
            r = cmd(mock_run, 'command_list', dict())
            assert r['stdout'] == '127.0.0.1'


class TestContext(object):

    @staticmethod
    def test_remote_shell_context():

        with remote_shell(hostname='127.0.0.1'):
            cxt = cur_context()
            assert  cxt.hostname == '127.0.0.1'
