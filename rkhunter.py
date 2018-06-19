import re
import os
import os.path
import yum
from yum.plugins import TYPE_CORE

requires_api_version = '2.1'
plugin_type = (TYPE_CORE,)

active = False

def init_hook(conduit):
    global active
    active = False
    try:
        content = open('/etc/rkhunter.conf').read()
        if not re.match('^DISABLE_TESTS=.*(hashes.*attributes|attributes.*hashes|properties)', content) or re.match('^ENABLE_TESTS=.*(hashes|attributes|properties)', content):
            active = True
    except:
        pass

def posttrans_hook(conduit):
    global active
    exe = '/usr/bin/rkhunter'
    if active and os.path.isfile(exe):
        conduit.info(2, 'Updating rkhunter property database')
        command = '%s --propupd --pkgmgr RPM --nolog' % exe
        os.system(command)
