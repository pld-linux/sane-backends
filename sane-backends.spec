# conditional build
# _without_dist_kernel		without kernel from distribution

%define		_plustek_ver	0_42_5

Summary:	SANE - Easy local and networked scanner access
Summary(es):	SANE - acceso a scanners en red y locales
Summary(pl):	SANE - Prosta obs�uga skaner�w lokalnych i sieciowych
Summary(pt_BR):	SANE - acesso a scanners locais e em rede
Name:		sane-backends
Version:	1.0.8
%define	rel	4
Release:	%{rel}
License:	relaxed LGPL (libraries), and public domain (docs)
Group:		Libraries
Source0:	ftp://ftp.mostang.com/pub/sane/sane-%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.rc-inetd
Source2:	http://home.t-online.de/home/g-jaeger/current/plustek-sane-%{_plustek_ver}.tar.gz
Patch0:		%{name}-no_libs.patch
Patch1:		%{name}-mustek-path.patch
Patch2:		%{name}-spatc.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-acinclude.patch
Patch5:		%{name}-plustek-Makefile.patch
URL:		http://www.mostang.com/sane/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	gphoto2-lib-devel >= 2.0.1
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
%ifarch %{ix86}
BuildRequires:	libieee1284-devel
%endif
%ifnarch sparc sparc64 sparcv9
BuildRequires:	libusb-devel
%endif
%{!?_without_dist_kernel:BuildRequires: kernel-headers}
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
PreReq:		rc-inetd
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post,postun):	/sbin/ldconfig
Requires(preun):	/usr/sbin/userdel
Requires(preun):	/usr/sbin/groupdel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	sane

%description
SANE (Scanner Access Now Easy) is a sane and simple interface to both
local and networked scanners and other image acquisition devices like
digital still and video cameras. SANE currently includes modules for
accessing:

Scanners: Abaton, Agfa, Apple, Artec, Avision, Bell+Howell, Canon,
Epson, Fujitsu, HP, LEO, Microtek, Mustek, NEC, Nikon, Panasonic, PIE,
Plustek, Ricoh, Sceptre, Sharp, Siemens, Tamarack, Teco, UMAX

Digital cameras: Kodak, Polaroid, Connectix QuickCam

and other SANE devices via network.

%description -l es
SANE - acceso a scanners en red y locales.

%description -l pl
SANE (Scanner Access Now Easy) jest rozs�dnym i prostym insterfejsem
do skaner�w, zar�wno lokalnych jak i sieciowych, oraz innych urz�dze�
do pozyskiwania obraz�w, jak cyfrowe aparaty i kamery. SANE aktualnie
zawiera modu�y do obs�ugi:

Skanery: Abaton, Agfa, Apple, Artec, Avision, Bell+Howell, Canon,
Epson, Fujitsu, HP, LEO, Microtek, Mustek, NEC, Nikon, Panasonic, PIE,
Plustek, Ricoh, Sceptre, Sharp, Siemens, Tamarack, Teco, UMAX

Aparaty cyfrowe: Kodak, Polaroid, Connectix QuickCam

oraz inne urz�dzenia dost�pne przez sie�.

%description -l pt_BR
O SANE (Scanner Access Now Easy) � uma interface simples para scanners
e outros dispositivos de captura de imagens como c�meras fotogr�ficas
digitais e de v�deo conectados diretamente ou atrav�s da rede.

%package devel
Summary:	Development part of SANE
Summary(es):	Archivos necesarios para el desarrollo de programas que usen SANE
Summary(pl):	Cz�� SANE przeznaczona dla programist�w
Summary(pt_BR):	Arquivos necess�rios ao desenvolvimento de programas que usem o SANE
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	sane-backends-sane-devel
Obsoletes:	sane-backends-sane-static

%description devel
Development part of SANE.

%description devel -l es
Archivos necesarios para el desarrollo de programas que usen SANE.

%description devel -l pl
Cz�� SANE dla programist�w.

%description devel -l pt_BR
Arquivos necess�rios ao desenvolvimento de programas que usem o SANE.

%package static
Summary:	Static SANE libraries
Summary(pl):	Statyczne biblioteki SANE
Summary(pt_BR):	Ferramentas de desenvolvimento para o SANE (bibliotecas est�ticas)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	sane-backends-sane-static

%description static
Static SANE libraries.

%description static -l pl
Biblioteki statyczne SANE.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento de m�dulos do SANE.

%package -n sane-mustek600IIN
Summary:	Mustek 600 II N scanner tool
Summary(pl):	Narz�dzie do skanera Mustek 600 II N
Group:		Applications/System
Requires:	%{name} = %{version}

%description -n sane-mustek600IIN
Tool which turns Mustek 600 II N scanner off. Sometimes scanner hangs
and can't be turned off by (x)scanimage in normal way.

Note: this program needs root privileges or access to /dev/port.

%description -n sane-mustek600IIN -l pl
Narz�dzie wymuszaj�ce wy��czenie skanera Mustek 600 II N. Czasem
skaner zawiesza si� i nie jest mo�liwe wy��czenie go zwyk�ym sposobem
przez program (x)scanimage.

Ten program wymaga uprawnie� roota albo dost�pu do /dev/port.

%package canon_pp
Summary:	SANE backend for Canon parallel port flatbed scanners
Summary(pl):	Sterownik SANE do skaner�w Canona pod��czanych do portu r�wnoleg�ego
Group:		Applications/System
Requires:	%{name} = %{version}

%description canon_pp
SANE backend for Canon parallel port flatbed scanners.

%description canon_pp -l pl
Sterownik SANE do p�askich skaner�w Canona pod��czanych do portu
r�wnoleg�ego.

%package gphoto2
Summary:	SANE backend for gphoto2 supported cameras
Summary(pl):	Sterownik SANE do aparat�w obs�ugiwanych przez gphoto2
Group:		Applications/System
Requires:	%{name} = %{version}

%description gphoto2
SANE backend for gphoto2 supported cameras.

%description gphoto2 -l pl
Sterownik SANE do aparat�w obs�ugiwanych przez gphoto2.

%package sm3600
Summary:	SANE backend for Microtek scanners with M011 USB chip
Summary(pl):	Sterownik SANE dla skaner�w Microteka z uk�adem USB M011
Group:		Applications/System
Requires:	%{name} = %{version}

%description sm3600
SANE backend for Microtek scanners with M011 USB chip.

%description sm3600 -l pl
Sterownik SANE dla skaner�w Microteka z uk�adem USB M011.

%package plustek
Summary:	Plustek scanner driver
Summary(pl):	Sterownik do skaner�w Plustek
Group:		Applications/System
Requires:	%{name} = %{version}

%description plustek
This package contains driver for Plustek scanners.

%description plustek -l pl
Pakiet zawiera sterownik dla skaner�w Plustek.

%package -n kernel-char-plustek
Summary:	Plustek scanner kernel module
Summary(pl):	Modu� j�dra dla skaner�w Plustek
Release:	%{rel}@%{_kernel_ver_str}
Group:		Applications/System
%{!?_without_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
Requires:	%{name} = %{version}
Requires:	%{name}-plustek = %{version}

%description -n kernel-char-plustek
This package contains kernel module which drives Plustek scanners.

%description -n kernel-char-plustek -l pl
Pakiet zawiera modu� steruj�cy skanerami Plustek.

%package -n kernel-smp-char-plustek
Summary:	Plustek scanner kernel module (SMP)
Summary(pl):	Modu� j�dra dla skaner�w Plustek (SMP)
Release:	%{rel}@%{_kernel_ver_str}
Group:		Applications/System
%{!?_without_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod
Requires:	%{name} = %{version}
Requires:	%{name}-plustek = %{version}

%description -n kernel-smp-char-plustek
This package contains kernel module which drives Plustek scanners.

%description -n kernel-smp-char-plustek -l pl
Pakiet zawiera modu� steruj�cy skanerami Plustek.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mkdir tmp-plustek_driver
cd tmp-plustek_driver
tar xfz %{SOURCE2}
# NOTE: we need original dll.conf!
rm -f backend/dll.conf
cp -Rf * ..
cd ..

%patch5 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%configure \
	--enable-static \
	--enable-pnm-backend \
	--enable-translations \
	--with-gphoto2

%{__make}

%ifarch %{ix86}
cd tools
%{__cc} -DHAVE_SYS_IO_H %{rpmcflags} \
	-I../include -o mustek600iin-off mustek600iin-off.c
cd ..
%endif

%ifnarch sparc sparc64 sparcv9
cd backend/plustek_driver
%{__make} all BUILD_SMP=1 OPT_FLAGS="%{rpmcflags}"
mv -f pt_drv.o{,.smp}
%{__make} clean
%{__make} all OPT_FLAGS="%{rpmcflags}" CC=%{kgcc}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%ifnarch sparc sparc64 sparcv9
install  backend/plustek_driver/pt_drv.o.smp	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/pt_drv.o
install  backend/plustek_driver/pt_drv.o	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc
%endif

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/saned

%ifarch %{ix86}
install tools/mustek600iin-off $RPM_BUILD_ROOT%{_bindir}
%endif

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid saned`" ]; then
        if [ "`getgid saned`" != "90" ]; then
                echo "Error: group saned doesn't have gid=90. Correct this before installing sane." 1>&2
                exit 1
        fi
else
        /usr/sbin/groupadd -g 90 -r -f saned
fi
if [ -n "`id -u saned 2>/dev/null`" ]; then
        if [ "`id -u saned`" != "90" ]; then
                echo "Error: user saned doesn't have uid=90. Correct this before installing sane." 1>&2
                exit 1
        fi
else
        /usr/sbin/useradd -u 90 -r -d /no/home -s /bin/false -c "SANE remote scanning daemon" -g saned saned 1>&2
fi

%post
/sbin/ldconfig
if [ -f /var/lock/subsys/rc-inetd ]; then
        /etc/rc.d/init.d/rc-inetd reload
else
        echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	/usr/sbin/userdel saned 2>/dev/null
	/usr/sbin/groupdel saned 2>/dev/null
fi

%postun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/rc-inetd ]; then
		/etc/rc.d/init.d/rc-inetd reload
	fi
fi
/sbin/ldconfig

%post -n kernel-char-plustek
/sbin/depmod -a

%post -n kernel-smp-char-plustek
/sbin/depmod -a

%postun -n kernel-char-plustek
/sbin/depmod -a

%postun -n kernel-smp-char-plustek
/sbin/depmod -a

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE LEVEL2 NEWS PROBLEMS PROJECTS TODO ChangeLog
%doc doc/canon doc/matsushita doc/mustek doc/mustek_usb doc/sceptre
%doc doc/teco doc/umax
%dir %{_sysconfdir}/sane.d
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/[^cg]*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/c[^a]*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/canon.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/canon630u.conf
%config %{_sysconfdir}/sysconfig/rc-inetd/saned
%dir %{_libdir}/sane
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/sane/libsane-[^cgs]*.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-c[^a]*.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon630u.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-s[^m]*.so.*
%attr(755,root,root) %{_bindir}/scanimage
%attr(755,root,root) %{_bindir}/sane-find-scanner
%attr(755,root,root) %{_sbindir}/saned
%{_mandir}/man1/*
%{_mandir}/man5/sane-[^cgps]*
%{_mandir}/man5/sane-c[^a]*
%{_mandir}/man5/sane-canon.5*
%{_mandir}/man5/sane-canon630u.5*
%{_mandir}/man5/sane-p[^l]*
%{_mandir}/man5/sane-s[^m]*
%{_mandir}/man7/*

%files devel
%defattr(644,root,root,755)
%doc doc/sane.ps
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

%ifnarch ppc
%files canon_pp
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/canon_pp.conf
%attr(755,root,root) %{_libdir}/sane/libsane-canon_pp.so.*
%{_mandir}/man5/sane-canon_pp.5*
%endif

#%files gphoto2
#%defattr(644,root,root,755)
#%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/gphoto2.conf
#%attr(755,root,root) %{_libdir}/sane/libsane-gphoto2.so.*
#%{_mandir}/man5/sane-gphoto2.5*

%files sm3600
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sane/libsane-sm3600.so.*
%{_mandir}/man5/sane-sm3600.5*

%ifarch %{ix86}
%files -n sane-mustek600IIN
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mustek600iin-off
%endif

%files plustek
%defattr(644,root,root,755)
%doc backend/plustek_driver/README backend/plustek_driver/TODO
%doc backend/plustek_driver/FAQ backend/plustek_driver/ChangeLog
%{_mandir}/man5/sane-plustek.5*

%ifnarch sparc sparc64 sparcv9
%files -n kernel-char-plustek
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*

%files -n kernel-smp-char-plustek
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/*
%endif
