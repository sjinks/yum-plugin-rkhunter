# dnf-plugin-rkhunter and yum-plugin-rkhunter

These plugins are designed to automate the update of rkhunter's file property database after RPM transactions if 'rkhunter --check' returns 0. The idea is borrowed from Debian's rkhunter package, where `dpkg` can be instructed to run `rkhunter --propupd` after each install/upgrade/removal operation automatically, so the user doesn't have to type `rkhunter --propupd` manually.

## Installation
### Manual Installation

#### dnf-plugin-rkhunter.py
Copy `dnf-plugin-rkhunter.py` to `/usr/lib/python3.6/site-packages/dnf-plugins/`:

```bash
sudo cp dnf-plugin-rkhunter.py /usr/lib/python3.6/site-packages/dnf-plugins/
```

Activate plugins:
```ini
# /etc/dnf/dnf.conf
plugins=1
```

#### yum-plugin-rkhunter.py
Copy `yum-plugin-rkhunter.py` to `/etc/yum/pluginconf.d/`:

```bash
sudo cp yum-plugin-rkhunter.py /etc/yum/pluginconf.d/
```

Activate plugins:
```ini
# /etc/yum.conf
plugins=1
```

## Notes
* Just like in Debian, if 'hashes' and 'attributes' tests are disabled, the property database is **not** updated automatically:
```bash
if ! grep -qsE '^DISABLE_TESTS=.*(hashes.*attributes|attributes.*hashes|properties)' /etc/rkhunter.conf /etc/rkhunter.conf.local || \
     grep -qsE '^ENABLE_TESTS=.*(hashes|attributes|properties)' /etc/rkhunter.conf /etc/rkhunter.conf.local; then
         rkhunter --propupd --nolog
fi
```

* Both plugins have been extended with an automatic `rkhunter --check` that is launched in the 'pre_transaction' phase for DNF and in the 'init' phase for Yum. It can be temporarily excluded by running DNF/Yum with the `--disableplugin=dnf-plugin-rkhunter` or `--disableplugin=yum-plugin-rkhunter` flag, respectively.
* Both plugins check for changes with `rkhunter --check`; if the check is passed, they update the property database with `rkhunter --propupd` after each RPM transaction.

**Both plugins come with two SECURITY WARNINGS** (copied from README.Debian):
* When using automatic database update after each package install/upgrade, an attacker could replace a file after it is installed and before `rkhunter --propupd` is run. On highly protected machines, it is recommended to disable automatic database updates.
* It is the users' responsibility to ensure that the files on the system are genuine and from a reliable source. Rkhunter can only report if a file has changed, but not on what has caused the change. Hence, if a file has changed and the `--propupd` command option is used, then rkhunter will assume that the file is genuine.
