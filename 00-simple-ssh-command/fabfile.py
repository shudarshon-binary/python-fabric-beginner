from fabric.api import *
from fabric.contrib.files import *
from fabric.contrib.project import *
from fabric.task_utils import merge
import time, os

# these are test multipass hosts grouped by categories
# for local testing using env.user can be used
# for remote host management SSH config can be used with -H parameter. e.g. fab -H example.dev test
env.roledefs.update({
    'dev': [ '10.236.49.147' ],
    'staging': [ '10.236.49.51' ],
})

# create an 'all' role containing all hosts
env.roledefs.update({ 'all': merge([], ['dev', 'staging'], [], env.roledefs) })

# set custom properties here
env.always_use_pty = False
env.forward_agent = True
env.use_ssh_config = True
env.disable_known_hosts = True
env.user = "chaks"  

# python decorator only tying this function to <dev> role
@roles('dev')
def test_ping():
    """ Run 'ping' on all hosts, to test hostname resolution """
    for host in env.roledefs['dev']:
        run("ping -c 3 {0}".format(host))

# python decorator only tying this function to <dev> role
@roles('dev')
def test_ssh():
    """ Run 'hostname' on all hosts, to test ssh """
    run("hostname")
    run("free -mh")

def test():
    """ test ping and ssh connectivity """
    execute('test_ping')
    execute('test_ssh')
