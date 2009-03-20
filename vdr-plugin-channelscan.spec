
%define plugin	channelscan
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	15

Summary:	VDR plugin: Plugin for satellite scan
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://kikko77.altervista.org/
Source:		vdr-%plugin-%version.tar.bz2
Patch1:		channelscan-extra-qualification.patch
Patch2:		90_channelscan-0.1.0-1.5.10.dpatch
Patch3:		channelscan-0.1.0-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin reads some information about the satellite transponders
from a .ini file and then scan this sat to get a channel list.

%prep
%setup -q -n %plugin-%version
%patch1 -p0 -b .extra
%patch2 -p1
%patch3 -p1

%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_datadir}/%{plugin}
install -m644 transponders/* %{buildroot}%{_vdr_plugin_datadir}/%{plugin}

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
ln -s %{_vdr_plugin_datadir}/%{plugin} %{buildroot}%{_vdr_plugin_cfgdir}/transponders

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY TODO
%{_vdr_plugin_cfgdir}/transponders
%{_vdr_plugin_datadir}/%{plugin}


