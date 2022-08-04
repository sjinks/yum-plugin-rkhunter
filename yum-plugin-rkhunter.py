import re
import os
import os.path
import yum
from yum.plugins import TYPE_CORE
from subprocess import run

requires_api_version = '2.1'
plugin_type = (TYPE_CORE,)

active = False

def init_hook(conduit):
    global active
    active = False
    exe = '/usr/bin/rkhunter' 
    try:
        content = open('/etc/rkhunter.conf').read()
        if not re.match('^DISABLE_TESTS=.*(hashes.*attributes|attributes.*hashes|properties)', content) or re.match('^ENABLE_TESTS=.*(hashes|attributes|properties)', content):
            active = True
    except:
        pass
    if active and os.path.isfile(exe):
        p0 = run('rkhunter --quiet --check') # TODO: togliere --quiet && girare stdout di p0 in fstring -> conduit.info(2, f'{ rkhunterstdout }') -> diventa output di yum
        conduit.info(2, 'Running rkhunter scan...')
        if p0.returncode != 0:
            raise Exception(f'rkhunter exit code = { p.returncode }')
        else:
            conduit.info(2, f'rkhunter exit code = { p.returncode }')
            
def posttrans_hook(conduit):
    global active
    exe = '/usr/bin/rkhunter'
    if active and os.path.isfile(exe):
        conduit.info(2, 'running rkhunter --propupd')
        command = '%s --propupd --pkgmgr RPM --nolog --quiet' % exe
        os.system(command)
