from dnfpluginscore import logger

import os
import dnf
import re

class RkhunterPlugin(dnf.Plugin):

    name = 'dnf-plugin-rkhunter'
    active = False

    def _out(self, msg):
        logger.debug('dnf-plugin-rkhunter: %s', msg)

    #def resolved(self):
    def pre_transaction(self):
        global active
        active = False
        exe= '/usr/bin/rkhunter'
        try:
            content = open('/etc/rkhunter.conf').read()
            if not re.match('^DISABLE_TESTS=.*(hashes.*attributes|attributes.*hashes|properties)', content) or re.match('^ENABLE_TESTS=.*(hashes|attributes|properties)', content):
                active = True
        except:
            raise dnf.exceptions.Error('dnf-plugin-rkhunter: hashes, attributes and properties must be disabled.')
        if active and os.path.isfile(exe):
            self._out('dnf-plugin-rkhunter: running rkhunter --check ...')
            if os.system('%s --check --report-warnings-only' % exe) != 0:
                raise dnf.exceptions.Error('dnf-plugin-rkhunter: rkhunter POSITIVE')
            else:
                self._out('dnf-plugin-rkhunter: rkhunter OK')

    def transaction(self):
        global active
        exe = '/usr/bin/rkhunter'
        if active and os.path.isfile(exe):
            self._out('dnf-plugin-rkhunter: running rkhunter --propupd ...')
            command = '%s --propupd --pkgmgr RPM --nolog ' % exe
            os.system(command)
