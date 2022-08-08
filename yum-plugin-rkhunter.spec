Name:      yum-plugin-rkhunter
Version:   0.2
Release:   1%{?dist}
Summary:   Automatically update rkhunter's file property database after RPM transactions
Source:    https://github.com/meilichios/yum-plugin-rkhunter/archive/0.2.tar.gz
Group:     Unspecified
License:   MIT
BuildArch: noarch
Requires:  rkhunter yum 

%description
Update rkhunter's file property database automatically after each RPM transaction if 'rkhunter --check' returns 0.

NOTE: rkhunter's 'hashes' and 'attributes' tests must be enabled.

%prep
%setup

%build

%install
%{__install} -m 0644 -p -D yum-plugin-rkhunter.py "%{buildroot}%{_prefix}/lib/yum-plugins/yum-plugin-rkhunter.py"
%{__install} -m 0644 -p -D yum-plugin-rkhunter.conf "%{buildroot}%{_sysconfdir}/yum/pluginconf.d/yum-plugin-rkhunter.conf"

%files
%defattr(-, root, root, -)
#%doc GPL INSTALL TODO README
%dir %{_prefix}/lib/yum-plugins
%dir %{_sysconfdir}/yum/pluginconf.d
%{_prefix}/lib/yum-plugins/yum-plugin-rkhunter.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/yum-plugin-rkhunter.conf

%changelog
* Thu Aug 4 2022 Vittorio Distefano <vittorio.distefano@proton.me> - 0.2 
- Forked from sjinks/yum-plugin-rkhunter
- Changed file names
- rkhunter --check in pretrans phase
* Tue Jun 12 2018 Volodymyr Kolesnykov <volodymyr@wildwolf.name> - 0.1-1
- Initial release
