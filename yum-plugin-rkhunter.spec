Name:      yum-plugin-rkhunter
Version:   0.1
Release:   1%{?dist}
Summary:   Automatically update rkhunter's file property database after RPM transactions
Source:    https://github.com/sjinks/yum-plugin-rkhunter/archive/0.1.tar.gz
Group:     Unspecified
License:   MIT
BuildArch: noarch
Requires:  rkhunter yum

%description
Update rkhunter's file property database automatically after each RPM transaction.

NOTE: rkhunter's 'hashes' and 'attributes' tests must be enabled.

%prep
%setup

%build

%install
%{__install} -m 0644 -p -D rkhunter.py "%{buildroot}%{_prefix}/lib/yum-plugins/rkhunter.py"
%{__install} -m 0644 -p -D rkhunter.conf "%{buildroot}%{_sysconfdir}/yum/pluginconf.d/rkhunter.conf"

%files
%defattr(-, root, root, -)
#%doc GPL INSTALL TODO README
%dir %{_prefix}/lib/yum-plugins
%dir %{_sysconfdir}/yum/pluginconf.d
%{_prefix}/lib/yum-plugins/rkhunter.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/rkhunter.conf

%changelog
* Tue Jun 12 2018 Volodymyr Kolesnykov <volodymyr@wildwolf.name> - 0.1-1
- Initial release
