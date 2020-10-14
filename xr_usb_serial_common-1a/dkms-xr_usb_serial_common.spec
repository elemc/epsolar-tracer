%define module_name xr_usb_serial_common
%define _srcdir %{_prefix}/src

Name:		dkms-%{module_name}
Version:  	1a
Release:	1%{?dist}
Summary:	Kernel module for Exar USB RS-485 converter

Group:		System Environment/Kernel
License:	GPLv2
URL:		https://github.com/elemc/epsolar-tracer/tree/master/xr_usb_serial_common-1a
Source0:	%{module_name}-%{version}.tar.xz
Source1:	dkms.conf
Source2:	%{module_name}-blacklist.conf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	dkms kernel-devel gcc
BuildArch:	noarch

%description
Kernel module source for backlight support some of samsung laptops

%prep
%setup -q -n %{module_name}-%{version}

#build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_srcdir}
mkdir -p $RPM_BUILD_ROOT%{_srcdir}/%{module_name}-%{version}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/
cp -r %{_builddir}/%{module_name}-%{version}/* $RPM_BUILD_ROOT%{_srcdir}/%{module_name}-%{version}/
install -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_srcdir}/%{module_name}-%{version}/dkms.conf
install -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/%{module_name}-dkms-blacklist.conf


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_srcdir}/%{module_name}-%{version}/*
%{_sysconfdir}/modprobe.d/*
%doc README.txt

%post
/usr/sbin/dkms add -m %{module_name} -v %{version}

%preun
/usr/sbin/dkms uninstall -m %{module_name} -v %{version}
/usr/sbin/dkms remove -m %{module_name} -v %{version} --all

%changelog
* Wed Oct 14 2020 Alexei Panov <alexei@panov.email> - 1a-1
- Initial build