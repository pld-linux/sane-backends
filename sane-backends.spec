Summary:	SANE --- Easy local and networked scanner access
Summary(pl):	SANE --- Prosta obs�uga skaner�w lokalnych i sieciowych
Name:		sane-backends
Version:	1.0.4
Release:	1
Group:		Libraries
Group(pl):	Biblioteki
License:	relaxed LGPL (libraries), and public domain (docs)
Source0:	ftp://ftp.mostang.com/pub/sane/%{name}-%{version}.tar.gz
Source1:	%{name}.rc-inetd
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-no_libs.patch
URL:		http://www.mostang.com/sane/
Prereq:		/sbin/ldconfig
Requires:	rc-inetd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SANE (Scanner Access Now Easy) is a sane and simple interface to both
local and networked scanners and other image acquisition devices like
digital still and video cameras. SANE currently includes modules for
accessing:

Scanners: Agfa SnapScan, Apple, Artec, Canon, CoolScan, Epson, HP,
          Microtek, Mustek, Nikon, Siemens, Tamarack, UMAX

Others:   Connectix, QuickCams

and other SANE devices via network.

%description -l pl
SANE (Scanner Access Now Easy) jest rozs�dnym i prostym insterfejsem
do skaner�w, zar�wno lokalnych jak i sieciowych, oraz innych urz�dze�
do pozyskiwania obraz�w, jak cyfrowe aparaty i kamery. SANE aktualnie
zawiera modu�y do obs�ugi:

Skanery: Agfa SnapScan, Apple, Artec, Canon, CoolScan, Epson, HP,
         Microtek, Mustek, Nikon, Siemens, Tamarack, UMAX

Inne:    Connectix, QuickCams

oraz inne urz�dzenia dost�pne przez sie�.

%package devel
Summary:	Development part of SANE 
Summary(pl):	Cz�� SANE przeznaczona dla programist�w
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development part of SANE.

%description devel -l pl
Cz�� SANE dla programist�w.

%package static
Summary:	Static SANE libraries
Summary(pl):	statyczne biblioteki SANE
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
Static SANE libraries.

%description static -l pl
Biblioteki statyczne SANE

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
LDFLAGS="-s" ; export LDFLAGS
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/saned

gzip -9nf AUTHORS LICENSE LEVEL2 NEWS PROBLEMS PROJECTS TODO ChangeLog

%pre
if [ "$1" = 1 ]; then
    getgid saned >/dev/null 2>&1 || %{_sbindir}/groupadd -g 90 -f saned
    id -u saned >/dev/null 2>&1 || %{_sbindir}/useradd -g saned -M -u 90 \
      -c "SANE remote scanning daemon" saned
fi

%post
/sbin/ldconfig
if [ -f /var/lock/subsys/rc-inetd ]; then
        /etc/rc.d/init.d/rc-inetd reload
else
        echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%preun
if [ "$1" = "0" ]; then
        %{_sbindir}/userdel saned 2>/dev/null
        %{_sbindir}/groupdel saned 2>/dev/null
fi

%postun
if [ -f /var/lock/subsys/rc-inetd ]; then
        /etc/rc.d/init.d/rc-inetd reload
fi
/sbin/ldconfig
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_sysconfdir}/sane.d
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/*
%config %{_sysconfdir}/sysconfig/rc-inetd/saned
%dir %{_libdir}/sane
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/sane/lib*.so.*
%attr(755,root,root) %{_bindir}/scanimage
%attr(755,root,root) %{_sbindir}/saned
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/sane
%attr(755,root,root) %{_bindir}/sane-config
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/sane/lib*.la
%attr(755,root,root) %{_libdir}/sane/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/sane/lib*.a
