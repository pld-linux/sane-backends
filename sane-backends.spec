# conditional build
# _without_dist_kernel		without kernel from distribution
# TODO: 
# - write kernel-plustek.spec (with kernel{,-smp}-char-plustek packages)
# - separate usb drivers (which depend on libusb)?
#	usb-only: artec_eplus48u,canon630u,gt68xx,mustek_usb,umax1220u
#	usb/scsi: coolscan2,hp,snapscan,umax
#	usb/scsi/pp: epson
#   what about sane-find-scanner tool? (linked with libusb)
#
Summary:	SANE - easy local and networked scanner access
Summary(es):	SANE - acceso a scanners en red y locales
Summary(ko):	½ºÄ³³Ê¸¦ ´Ù·ç´Â ¼ÒÇÁÆ®¿þ¾î
Summary(pl):	SANE - prosta obs³uga skanerów lokalnych i sieciowych
Summary(pt_BR):	SANE - acesso a scanners locais e em rede
Name:		sane-backends
Version:	1.0.10
Release:	2
License:	relaxed LGPL (libraries), and Public Domain (docs)
Group:		Libraries
# Source0:	ftp://ftp.mostang.com/pub/sane/%{name}-%{version}/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.mostang.com/pub/sane/old-versions/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f54e7819e98fa15ffc70bac39eb49123
Source1:	%{name}.rc-inetd
Patch0:		%{name}-no_libs.patch
Patch1:		%{name}-mustek-path.patch
Patch2:		%{name}-spatc.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-acinclude.patch
Patch5:		%{name}-plustek-Makefile.patch
Patch6:		%{name}-alpha.patch
Patch7:		%{name}-ac.patch
URL:		http://www.mostang.com/sane/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gphoto2-devel >= 2.0.1
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
BuildRequires:	gettext-devel
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
SANE (Scanner Access Now Easy) jest rozs±dnym i prostym insterfejsem
do skanerów, zarówno lokalnych jak i sieciowych, oraz innych urz±dzeñ
do pozyskiwania obrazów, jak cyfrowe aparaty i kamery. SANE aktualnie
zawiera modu³y do obs³ugi:

Skanery: Abaton, Agfa, Apple, Artec, Avision, Bell+Howell, Canon,
Epson, Fujitsu, HP, LEO, Microtek, Mustek, NEC, Nikon, Panasonic, PIE,
Plustek, Ricoh, Sceptre, Sharp, Siemens, Tamarack, Teco, UMAX

Aparaty cyfrowe: Kodak, Polaroid, Connectix QuickCam

oraz inne urz±dzenia dostêpne przez sieæ.

%description -l pt_BR
O SANE (Scanner Access Now Easy) é uma interface simples para scanners
e outros dispositivos de captura de imagens como câmeras fotográficas
digitais e de vídeo conectados diretamente ou através da rede.

%package devel
Summary:	Development part of SANE
Summary(es):	Archivos necesarios para el desarrollo de programas que usen SANE
Summary(pl):	Czê¶æ SANE przeznaczona dla programistów
Summary(pt_BR):	Arquivos necessários ao desenvolvimento de programas que usem o SANE
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	sane-backends-sane-devel
Obsoletes:	sane-backends-sane-static

%description devel
Development part of SANE.

%description devel -l es
Archivos necesarios para el desarrollo de programas que usen SANE.

%description devel -l pl
Czê¶æ SANE dla programistów.

%description devel -l pt_BR
Arquivos necessários ao desenvolvimento de programas que usem o SANE.

%package static
Summary:	Static SANE libraries
Summary(pl):	Statyczne biblioteki SANE
Summary(pt_BR):	Ferramentas de desenvolvimento para o SANE (bibliotecas estáticas)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	sane-backends-sane-static

%description static
Static SANE libraries.

%description static -l pl
Biblioteki statyczne SANE.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento de módulos do SANE.

%package saned
Summary:	SANE network daemon
Summary(pl):	Demon sieciowy SANE
Group:		Networking/Daemons
PreReq:         rc-inetd
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post,postun):	/sbin/ldconfig
Requires(preun):	/usr/sbin/userdel
Requires(preun):	/usr/sbin/groupdel
Requires:	%{name} = %{version}

%description saned
saned is the SANE (Scanner Access Now Easy) daemon that allows remote
clients to access image acquisition devices available on the local
host.
      
%description saned -l pl
saned to demon SANE pozwalaj±cy zdalnym klientom na dostêp do
urz±dzeñ odczytuj±cych obraz pod³±czonych lokalnie.

%package -n sane-mustek600IIN
Summary:	Mustek 600 II N scanner tool
Summary(pl):	Narzêdzie do skanera Mustek 600 II N
Group:		Applications/System
Requires:	%{name} = %{version}

%description -n sane-mustek600IIN
Tool which turns Mustek 600 II N scanner off. Sometimes scanner hangs
and can't be turned off by (x)scanimage in normal way.

Note: this program needs root privileges or access to /dev/port.

%description -n sane-mustek600IIN -l pl
Narzêdzie wymuszaj±ce wy³±czenie skanera Mustek 600 II N. Czasem
skaner zawiesza siê i nie jest mo¿liwe wy³±czenie go zwyk³ym sposobem
przez program (x)scanimage.

Ten program wymaga uprawnieñ roota albo dostêpu do /dev/port.

%package canon_pp
Summary:	SANE backend for Canon parallel port flatbed scanners
Summary(pl):	Sterownik SANE do skanerów Canona pod³±czanych do portu równoleg³ego
Group:		Applications/System
Requires:	%{name} = %{version}

%description canon_pp
SANE backend for Canon parallel port flatbed scanners.

%description canon_pp -l pl
Sterownik SANE do p³askich skanerów Canona pod³±czanych do portu
równoleg³ego.

%package gphoto2
Summary:	SANE backend for gphoto2 supported cameras
Summary(pl):	Sterownik SANE do aparatów obs³ugiwanych przez gphoto2
Group:		Applications/System
Requires:	%{name} = %{version}

%description gphoto2
SANE backend for gphoto2 supported cameras.

%description gphoto2 -l pl
Sterownik SANE do aparatów obs³ugiwanych przez gphoto2.

%package hpsj5s
Summary:	SANE backend for HP ScanJet 5s parallel port scanners
Summary(pl):	Sterownik SANE do skanerów HP ScanJest 5s pod³±czanych do portu równoleg³ego
Group:		Applications/System
Requires:	%{name} = %{version}

%description hpsj5s
SANE backend for HP ScanJet 5s parallel port scanners.

%description hpsj5s -l pl
Sterownik SANE do skanerów HP ScanJest 5s pod³±czanych do portu
równoleg³ego.

%package plustek
Summary:	Plustek scanner driver
Summary(pl):	Sterownik do skanerów Plustek
Group:		Applications/System
Requires:	%{name} = %{version}

%description plustek
This package contains driver for Plustek scanners.

%description plustek -l pl
Pakiet zawiera sterownik dla skanerów Plustek.

%package sm3600
Summary:	SANE backend for Microtek scanners with M011 USB chip
Summary(pl):	Sterownik SANE dla skanerów Microteka z uk³adem USB M011
Group:		Applications/System
Requires:	%{name} = %{version}

%description sm3600
SANE backend for Microtek scanners with M011 USB chip.

%description sm3600 -l pl
Sterownik SANE dla skanerów Microteka z uk³adem USB M011.

%package -n kernel-char-plustek
Summary:	Plustek scanner kernel module
Summary(pl):	Modu³ j±dra dla skanerów Plustek
Release:	%{rel}@%{_kernel_ver_str}
Group:		Applications/System
%{!?_without_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
Requires:	%{name} = %{version}
Requires:	%{name}-plustek = %{version}

%description -n kernel-char-plustek
This package contains kernel module which drives Plustek scanners.

%description -n kernel-char-plustek -l pl
Pakiet zawiera modu³ steruj±cy skanerami Plustek.

%package -n kernel-smp-char-plustek
Summary:	Plustek scanner kernel module (SMP)
Summary(pl):	Modu³ j±dra dla skanerów Plustek (SMP)
Release:	%{rel}@%{_kernel_ver_str}
Group:		Applications/System
%{!?_without_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod
Requires:	%{name} = %{version}
Requires:	%{name}-plustek = %{version}

%description -n kernel-smp-char-plustek
This package contains kernel module which drives Plustek scanners.

%description -n kernel-smp-char-plustek -l pl
Pakiet zawiera modu³ steruj±cy skanerami Plustek.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 -b .wiget
#%%patch5 -p1
#%%patch6 -p1
%patch7 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/saned

%ifarch %{ix86}
install tools/mustek600iin-off $RPM_BUILD_ROOT%{_bindir}
%endif

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%pre saned
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

%post saned
if [ -f /var/lock/subsys/rc-inetd ]; then
        /etc/rc.d/init.d/rc-inetd reload
else
        echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%preun saned
if [ "$1" = "0" ]; then
	/usr/sbin/userdel saned 2>/dev/null
	/usr/sbin/groupdel saned 2>/dev/null
fi

%postun saned
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/rc-inetd ]; then
		/etc/rc.d/init.d/rc-inetd reload
	fi
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS PROBLEMS PROJECTS TODO ChangeLog
%doc doc/canon doc/matsushita doc/mustek doc/mustek_usb doc/sceptre
%doc doc/teco doc/umax
%dir %{_sysconfdir}/sane.d
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/[!cghps]*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/c[!a]*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/canon.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/canon630u.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/gt68xx.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/hp.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/p[!l]*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/s[!a]*
%dir %{_libdir}/sane
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/sane/libsane-[!cghps]*.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-c[!a]*.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon630u.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-gt68xx.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-p[!l]*.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-s[!m]*.so.*
%attr(755,root,root) %{_bindir}/sane-find-scanner
%attr(755,root,root) %{_bindir}/scanimage
%attr(755,root,root) %{_bindir}/gamma4scanimage
%{_mandir}/man1/sane-find-scanner.1*
%{_mandir}/man1/scanimage.1*
%{_mandir}/man1/gamma4scanimage.1*
%{_mandir}/man1/sane-config.1*
%{_mandir}/man5/sane-[!cghps]*
%{_mandir}/man5/sane-c[!a]*
%{_mandir}/man5/sane-canon.5*
%{_mandir}/man5/sane-canon630u.5*
%{_mandir}/man5/sane-gt68xx.5*
%{_mandir}/man5/sane-hp.5*
%{_mandir}/man5/sane-p[!l]*
%{_mandir}/man5/sane-s[!m]*
%{_mandir}/man7/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/sane
%attr(755,root,root) %{_bindir}/sane-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files saned
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/saned
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/saned.conf
%attr(755,root,root) %{_sbindir}/saned
%{_mandir}/man1/saned.1*

%ifarch %{ix86}
%files -n sane-mustek600IIN
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mustek600iin-off
%endif

%ifarch %{ix86}
%files canon_pp
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/canon_pp.conf
%attr(755,root,root) %{_libdir}/sane/libsane-canon_pp.so.*
%{_mandir}/man5/sane-canon_pp.5*
%endif

%files gphoto2
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/gphoto2.conf
%attr(755,root,root) %{_libdir}/sane/libsane-gphoto2.so.*
%{_mandir}/man5/sane-gphoto2.5*

%ifarch %{ix86}
%files hpsj5s
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/hpsj5s.conf
%attr(755,root,root) %{_libdir}/sane/libsane-hpsj5s.so.*
%{_mandir}/man5/sane-hpsj5s.5*
%endif

%files plustek
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sane.d/plustek.conf
%attr(755,root,root) %{_libdir}/sane/libsane-plustek.so.*
%{_mandir}/man5/sane-plustek.5*

%files sm3600
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sane/libsane-sm3600.so.*
%{_mandir}/man5/sane-sm3600.5*
