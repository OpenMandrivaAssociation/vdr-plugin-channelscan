%define plugin	channelscan

Summary:	VDR plugin: Plugin for satellite scan
Name:		vdr-plugin-%plugin
Version:	0.1.0
Release:	20
Group:		Video
License:	GPL
URL:		http://kikko77.altervista.org/
Source:		vdr-%plugin-%version.tar.bz2
Patch1:		channelscan-extra-qualification.patch
Patch2:		90_channelscan-0.1.0-1.5.10.dpatch
Patch3:		channelscan-0.1.0-i18n-1.6.patch
Patch4:		channelscan-format-string.patch
Patch5:		channelscan-includes.patch
# warning: cannot pass objects of non-POD type ‘class cString’ through ‘...’; call will abort at runtime
Patch6:		channelscan-non-pod-type.patch
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
%patch4 -p1
%patch5 -p1
%patch6 -p1

%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_datadir}/%{plugin}
install -m644 transponders/* %{buildroot}%{_vdr_plugin_datadir}/%{plugin}

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
ln -s %{_vdr_plugin_datadir}/%{plugin} %{buildroot}%{_vdr_plugin_cfgdir}/transponders

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY TODO
%{_vdr_plugin_cfgdir}/transponders
%{_vdr_plugin_datadir}/%{plugin}




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-17mdv2010.0
+ Revision: 402742
- fix a bug that would cause an "Illegal instruction" error
  (non-pod-type.patch)

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-15mdv2009.1
+ Revision: 359699
- fix includes (includes.patch)
- fix format strings (format-string.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-14mdv2009.0
+ Revision: 197909
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-13mdv2009.0
+ Revision: 197640
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of vdr 1.5.10 (P2 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-12mdv2008.1
+ Revision: 145047
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-11mdv2008.1
+ Revision: 103073
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-10mdv2008.0
+ Revision: 49979
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-9mdv2008.0
+ Revision: 42066
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-8mdv2008.0
+ Revision: 22725
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-7mdv2007.0
+ Revision: 90901
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-6mdv2007.1
+ Revision: 73972
- rebuild for new vdr
- Import vdr-plugin-channelscan

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-2mdv2007.0
- rebuild for new vdr

* Wed Jun 21 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-1mdv2007.0
- initial Mandriva release

