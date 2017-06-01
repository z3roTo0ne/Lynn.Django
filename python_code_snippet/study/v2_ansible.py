#!/usr/bin/env python
# coding:utf-8

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from v2_callbacks import DansibleCallbackModule
from ansible.utils.vars import load_extra_vars
from ansible.utils.display import Display
from ansible.plugins.callback import default
import os

os.environ.get('ANSIBLE_DEBUG', True)

Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'remote_user',
                      'private_key_file', 'ssh_common_args', 'ssh_extra_args',
                      'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user',
                      'verbosity', 'check', 'extra_vars'])
# 这些options都在task_queue_manager的set_options()中

# initialize needed objects
variable_manager = VariableManager()
loader = DataLoader()
options = Options(connection='ssh', module_path='', forks=100, remote_user='root',
                  private_key_file=None, ssh_common_args=None, ssh_extra_args=None,
                  sftp_extra_args=None, scp_extra_args=None, become=False, become_method='su', become_user='root',
                  verbosity=None, check=False,
                  extra_vars={'host': 'all'}
                  )

# connection ssh local
passwords = dict(conn_pass='123456', become_pass='123456')


# create inventory and pass to var manager
inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=["192.168.5.133", "192.168.5.135"])
variable_manager.set_inventory(inventory)
variable_manager.extra_vars = options.extra_vars
# variable_manager.extra_vars = load_extra_vars(loader=loader, options=options)

# create play with tasks
# play_source_test = dict(
#         name="Ansible Play",
#         hosts='localhost',
#         gather_facts='no',
#         tasks=[dict(action=dict(module='debug', args=dict(msg='hello world'))) ]
#     )

play_source = loader.load_from_file('test.yml')
play_source = dict(play_source.pop())
play_source['name'] = options.extra_vars.get('host')
play_source['port'] = 22
# play_source['strategy'] = 'serial'
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
print play.get_ds()

tqm = None

display = Display(5)
cb = default.CallbackModule(display)
try:
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords,
        stdout_callback=cb,
        # stdout_callback为一个CallbackBase类的实例或者是一个插件的名称，如“default”
    )
    # result = tqm.run(play)

finally:
    if tqm is not None:
        tqm.cleanup()
