Summary: NethServer zabbix22 configuration
Name: nethserver-zabbix22
Version: 0.1.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: check-mk-agent
Requires: nethserver-base
Requires: nethserver-mysql
Requires: zabbix22-server-mysql
Requires: zabbix22-web-mysql
Requires: zabbix22-agent

BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
NethServer omd configuration

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Sun Dec 03 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-1
- Initial NS7 release
