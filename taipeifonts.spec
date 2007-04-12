Summary:	taipei chinese big5 fonts 
Name:		taipeifonts
Version:	1.2
Release:	20mdk
License:	Public Domain
Group:		System/Fonts/X11 bitmap
Source0:	%{name}-%{version}.tar.bz2
Source1:	taipeifonts.alias
Prereq:		/bin/grep, XFree86, /bin/cat 
Requires:	/bin/grep, XFree86, /bin/cat
#Packager:	platin@ch.ntu.edu.tw
Buildroot:	%{_tmppath}/taipei-root
BuildArch:	noarch        
Provides:	zh-pcf-fonts, taipei16, taipeik20, taipeik24, taipeim20, taipeim24
## Conflicts:	twmoe_ming-xfonts 

%description
These are the Traditional Chinese fonts for XFree86 found on GNU's ftp mirror.

You will need to install these if you wish to see and use the Traditional
Chinese fonts under XFree86.

%prep
%setup -q

%build
bdftopcf taipei24.bdf | gzip -c > taipei24.pcf.gz
bdftopcf taipei20.bdf | gzip -c > taipei20.pcf.gz
bdftopcf taipei16.bdf | gzip -c > taipei16.pcf.gz

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/X11R6/%{_lib}/X11/fonts/misc

install -m 644 taipei24.pcf.gz $RPM_BUILD_ROOT%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/
install -m 644 taipei20.pcf.gz $RPM_BUILD_ROOT%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/
install -m 644 taipei16.pcf.gz $RPM_BUILD_ROOT%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/
install -m 644 vga12x24.pcf.gz $RPM_BUILD_ROOT%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/

%clean
rm -rf $RPM_BUILD_ROOT

%postun
if [ "$1" = "0" ];then
    if [ -f %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias ] ; then
        cat %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias | \
			grep -v "\!ByRPM" > %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias.tmp
        mv -f %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias.tmp \
			%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias
        %{_prefix}/X11R6/bin/mkfontdir %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/
		[ -z "$DISPLAY" ] || xset fp rehash
    fi
fi

%triggerin -- taipeifonts, XFree86
if [ -f %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias ] ; then
    cat %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias | \
		grep -v "\!ByRPM" > %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias.tmp
    mv -f %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias.tmp \
		%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias
    cat %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/taipeifonts.alias \
		>> %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/fonts.alias 
    %{_prefix}/X11R6/bin/mkfontdir %{_prefix}/X11R6/%{_lib}/X11/fonts/misc/
	[ -z "$DISPLAY" ] || xset fp rehash
fi

%files 
%defattr(0644,root,root,0755)
%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/taipei16.pcf.gz
%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/taipei20.pcf.gz
%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/taipei24.pcf.gz            
%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/vga12x24.pcf.gz
%{_prefix}/X11R6/%{_lib}/X11/fonts/misc/taipeifonts.alias

