Summary: nethserver-zabbix22 sets up the monitoring system
%define name nethserver-zabbix22
Name: %{name}
%define version 0.1.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source0: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name}
Requires: nethserver-mysql
Requires: zabbix22-server-mysql
Requires: zabbix22-web-mysql
Requires: zabbix22-agent
BuildRequires: perl
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
NethServer Zabbix22 configuration

%changelog
* Sun Dec 03 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-1
- Initial NS7 release

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
