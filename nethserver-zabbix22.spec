Summary: nethserver-zabbix22 sets up the monitoring system
%define name nethserver-zabbix22
Name: %{name}
%define version 0.1.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: nethserver-mysql
Requires: zabbix22-server-mysql
Requires: zabbix22-web-mysql
Requires: zabbix22-agent
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
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist

%post
%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
