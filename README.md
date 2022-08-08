# yum-plugin-rkhunter

Yum plugin to automatically update rkhunter's file property database after RPM transactions if 'rkhunter --check" returns 0.

The idea is borrowed from Debian's rkhunter package: in Debian, it is possible to instruct `dpkg`
to run `rkhunter --propupd` after each install/upgrade/removal operation automatically so that
the user does not have to type `rkhunter --propupd` manually.

#### The plugin can be temporarily excluded by running yum with the '--disableplugin=yum-plugin-rkhunter' flag.

This feature comes with two SECURITY WARNINGS (copied from README.Debian):

     When using automatic database update after each package install/upgrade,
     an attacker could replace a file after it is installed, and before --propupd
     is run. On a highly protected machine, it is recommended to disable the.
     automatic database update.
 
     It is the users' responsibility to ensure that the files on the system are genuine and from
     a reliable source. rkhunter can only report if a file has changed, but not on what has
     caused the change. Hence, if a file has changed, and  the  --propupd  command
     option is used, then rkhunter will assume that the file is genuine.

## Build RPM

```bash
rpmbuild --undefine=_disable_source_fetch -ba yum-plugin-rkhunter.spec
```

## Manual Installation

Run

```bash
cp rkhunter.py /usr/lib/yum-plugins/rkhunter.py
cp rkhunter.conf /etc/yum/pluginconf.d/rkhunter.conf
```

as root (or use `sudo`).

## Notes

Just like in Debian, if 'hashes' and 'attributes' tests are disabled, property database is **not** updated automatically:

```bash
if ! grep -qsE '^DISABLE_TESTS=.*(hashes.*attributes|attributes.*hashes|properties)' /etc/rkhunter.conf /etc/rkhunter.conf.local || \
     grep -qsE '^ENABLE_TESTS=.*(hashes|attributes|properties)' /etc/rkhunter.conf /etc/rkhunter.conf.local; then
         rkhunter --propupd --nolog
fi
```
