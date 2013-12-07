%define name	taipeifonts
%define version	1.2

Summary:	Taipei Chinese big5 fonts 
Name:		%{name}
Version:	%{version}
Release:	31
License:	Public Domain
Group:		System/Fonts/X11 bitmap
Source0:	%{name}-%{version}.tar.bz2
#Packager:	platin@ch.ntu.edu.tw
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch   
BuildRequires:	bdftopcf
Requires(post,postun):	mkfontscale
Requires(post,postun):	mkfontdir     
Provides:	zh-pcf-fonts, taipei16, taipeik20, taipeik24, taipeim20, taipeim24

%description
These are the Traditional Chinese fonts for X found on GNU's FTP mirror.

%prep
%setup -q

%build
bdftopcf taipei24.bdf | gzip -c > taipei24.pcf.gz
bdftopcf taipei20.bdf | gzip -c > taipei20.pcf.gz
bdftopcf taipei16.bdf | gzip -c > taipei16.pcf.gz

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/misc

install -m 644 taipei24.pcf.gz $RPM_BUILD_ROOT%{_datadir}/fonts/misc/
install -m 644 taipei20.pcf.gz $RPM_BUILD_ROOT%{_datadir}/fonts/misc/
install -m 644 taipei16.pcf.gz $RPM_BUILD_ROOT%{_datadir}/fonts/misc/
install -m 644 vga12x24.pcf.gz $RPM_BUILD_ROOT%{_datadir}/fonts/misc/

%post
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%postun
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(0644,root,root,0755)
%{_datadir}/fonts/misc/*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2-28mdv2011.0
+ Revision: 670662
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-27mdv2011.0
+ Revision: 607968
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-26mdv2010.1
+ Revision: 524159
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2-25mdv2010.0
+ Revision: 427278
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.2-24mdv2009.1
+ Revision: 351500
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2-23mdv2009.0
+ Revision: 225609
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2-22mdv2008.1
+ Revision: 179612
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 14 2007 Adam Williamson <awilliamson@mandriva.org> 1.2-21mdv2008.0
+ Revision: 39269
- do mkfontdir and mkfontscale in post and postun instead of shipping files; clean spec; rebuild for new era


* Sat Jul 12 2003 Per 喕vind Karlsen <peroyvind@sintrax.net> 1.2-20mdk
- macroize
- s/Copyright/License/
- cosmetics
- quiet setup
- fix use-of-RPM_SOURCE_DIR

* Sat Apr 14 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2-19mdk
- Work around a problem with not installing / updating in X (Abel Cheung).

* Sun Mar 25 2001 Andrew Lee <andrew@linux.org.tw> 1.2-18mdk
- change -default-fixed to -default-ming (avoid possible confuse)
- add -default-ming alias for gb2312
- use %%triggerin
- Geoffrey Lee <snailtalk@mandrakesoft.com>
  - Better description, more professional. :)

* Tue Mar 06 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2-17mdk
- Do nothing but rebuild.

* Mon Aug 14 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2-16mdk
- adapted Group: to mdk conventions
- rewrote the scripts to avoid possible vulnerabilities

* Tue Feb 01 2000 Cheng Yuan-Cheng <platin@cle.linux.org.tw>
- use %%post instead of %%triggerin XFree86
- prereq/requires fixed
- taipeifonts.alias fixed,, use default-ming

* Thu Mar 18 1999 Cheng Yuan-Cheng <platin@cle.linux.org.tw>
- fonts.alias bug fix
- scripts fixed

* Mon Dec 14 1998 Cheng Yuan-Cheng <platin@cle.linux.org.tw>
- uninstall script bug fix

* Thu Nov 05 1998 Cheng Yuan-Cheng <platin@cle.linux.org.tw>
- rebuild on redhat-5.2

* Fri Oct 02 1998 Cheng Yuan-Cheng <platin@ms.ccafps.khc.edu.tw>
- alias to fit the new ttfed X-Server

* Wed Sep 02 1998 Cheng Yuan-Cheng <platin@ms.ccafps.khc.edu.tw>
- Group --> Extensions/Chinese

* Mon Jul 20 1998 Cheng Yuan-Cheng <platin@ms.ccafps.khc.edu.tw>
- move the font dir to misc
- remove 8x16.pcf.gz

* Thu Jun 18 1998 Cheng Yuan-Cheng <platin@ms.ccafps.khc.edu.tw>
- Change the group tag to Extensions/chinese

* Thu Jun 11 1998 Cheng Yuan-Chung <platin@ms.ccafps.khc.edu.tw>
- Revised the font file. Now those file was created from the bdf fonts 
  included in GNU's `intlfonts' package.
- Conflict: tag added

* Tue Apr 14 1998 Cheng Yuan-Chung <platin@ms.ccafps.khc.edu.tw>
- Revised the fonts.alias file to fit the useage of lyx-I18N
- 把楷體字拿掉了，but 為了 CXwin 使用，仍用 alias 做出 taipeik20、taipeik24。

* Fri Jan 09 1998 Cheng Yuan-Chung <platin@ms.ccafps.khc.edu.tw> 
- add fonts 8x16.pcf.gz && vga12x24.pcf.gz

* Thu Jan 01 1998 Cheng Yuan-Chung <platin@ms.ccafps.khc.edu.tw>
- 這些 taipei 字形是從我的字形目錄裡面選出來的，我也不知道
- 他們的出處‧‧‧希望沒有版權問題才好。
- will automatically change the FontPath lines in XF86Config
- - must have perl

