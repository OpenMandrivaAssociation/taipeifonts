%define name	taipeifonts
%define version	1.2

Summary:	Taipei Chinese big5 fonts 
Name:		%{name}
Version:	%{version}
Release:	%mkrel 27
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
