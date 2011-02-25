#
# Conditional build:
%bcond_without	gphoto	# no gphoto backend (which requires libgphoto2)
%bcond_without	lpt	# no parallel port backends (which require libieee1284)
#
Summary:	SANE - easy local and networked scanner access
Summary(es.UTF-8):	SANE - acceso a scanners en red y locales
Summary(ko.UTF-8):	스캐너를 다루는 소프트웨어
Summary(pl.UTF-8):	SANE - prosta obsługa skanerów lokalnych i sieciowych
Summary(pt_BR.UTF-8):	SANE - acesso a scanners locais e em rede
Name:		sane-backends
Version:	1.0.22
Release:	1
License:	relaxed GPL v2+ (libraries), Public Domain (docs)
Group:		Libraries
Source0:	ftp://ftp.sane-project.org/pub/sane/%{name}-%{version}/sane-backends-%{version}.tar.gz
# Source0-md5:	fadf56a60f4776bfb24491f66b617cf5
Source1:	%{name}.rc-inetd
Source2:	%{name}.m4
Patch0:		%{name}-lockpath_group.patch
Patch1:		%{name}-mustek-path.patch
Patch2:		%{name}-spatc.patch
Patch4:		%{name}-link.patch
URL:		http://www.sane-project.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?with_gphoto:BuildRequires:	libgphoto2-devel >= 2.0.1}
%{?with_lpt:BuildRequires:	libieee1284-devel >= 0.1.5}
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
%if "%{pld_release}" == "ac"
BuildRequires:	libusb-devel < 1.0
%else
BuildRequires:	libusb-compat-devel >= 0.1.0
%endif
BuildRequires:	libv4l-devel
BuildRequires:	pkgconfig
BuildRequires:	resmgr-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	tetex-latex-psnfss
%if "%{pld_release}" != "ti" && "%{pld_release}" != "ac"
BuildRequires:	texlive-latex-effects
%endif
Requires:	setup >= 2.4.10-1
Obsoletes:	sane
Obsoletes:	sane-backends-sm3600
Conflicts:	sane-backends-plustek
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es.UTF-8
SANE - acceso a scanners en red y locales.

%description -l pl.UTF-8
SANE (Scanner Access Now Easy) jest rozsądnym i prostym insterfejsem
do skanerów, zarówno lokalnych jak i sieciowych, oraz innych urządzeń
do pozyskiwania obrazów, jak cyfrowe aparaty i kamery. SANE aktualnie
zawiera moduły do obsługi:

Skanery: Abaton, Agfa, Apple, Artec, Avision, Bell+Howell, Canon,
Epson, Fujitsu, HP, LEO, Microtek, Mustek, NEC, Nikon, Panasonic, PIE,
Plustek, Ricoh, Sceptre, Sharp, Siemens, Tamarack, Teco, UMAX

Aparaty cyfrowe: Kodak, Polaroid, Connectix QuickCam

oraz inne urządzenia dostępne przez sieć.

%description -l pt_BR.UTF-8
O SANE (Scanner Access Now Easy) é uma interface simples para scanners
e outros dispositivos de captura de imagens como câmeras fotográficas
digitais e de vídeo conectados diretamente ou através da rede.

%package devel
Summary:	Development part of SANE
Summary(es.UTF-8):	Archivos necesarios para el desarrollo de programas que usen SANE
Summary(pl.UTF-8):	Część SANE przeznaczona dla programistów
Summary(pt_BR.UTF-8):	Arquivos necessários ao desenvolvimento de programas que usem o SANE
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libieee1284-devel
Requires:	libusb-compat-devel >= 0.1.0
Requires:	resmgr-devel
Obsoletes:	sane-backends-sane-devel
Obsoletes:	sane-backends-sane-static

%description devel
Development part of SANE.

%description devel -l es.UTF-8
Archivos necesarios para el desarrollo de programas que usen SANE.

%description devel -l pl.UTF-8
Część SANE dla programistów.

%description devel -l pt_BR.UTF-8
Arquivos necessários ao desenvolvimento de programas que usem o SANE.

%package static
Summary:	Static SANE libraries
Summary(pl.UTF-8):	Statyczne biblioteki SANE
Summary(pt_BR.UTF-8):	Ferramentas de desenvolvimento para o SANE (bibliotecas estáticas)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	sane-backends-sane-static

%description static
Static SANE libraries.

%description static -l pl.UTF-8
Biblioteki statyczne SANE.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de módulos do SANE.

%package saned
Summary:	SANE network daemon
Summary(pl.UTF-8):	Demon sieciowy SANE
Group:		Networking/Daemons
Requires(post,postun):	/sbin/ldconfig
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(preun):	/usr/sbin/groupdel
Requires(preun):	/usr/sbin/userdel
Requires:	%{name} = %{version}-%{release}
Requires:	rc-inetd
Provides:	group(saned)
Provides:	user(saned)

%description saned
saned is the SANE (Scanner Access Now Easy) daemon that allows remote
clients to access image acquisition devices available on the local
host.

%description saned -l pl.UTF-8
saned to demon SANE pozwalający zdalnym klientom na dostęp do urządzeń
odczytujących obraz podłączonych lokalnie.

%package -n sane-mustek600IIN
Summary:	Mustek 600 II N scanner tool
Summary(pl.UTF-8):	Narzędzie do skanera Mustek 600 II N
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n sane-mustek600IIN
Tool which turns Mustek 600 II N scanner off. Sometimes scanner hangs
and can't be turned off by (x)scanimage in normal way.

Note: this program needs root privileges or access to /dev/port.

%description -n sane-mustek600IIN -l pl.UTF-8
Narzędzie wymuszające wyłączenie skanera Mustek 600 II N. Czasem
skaner zawiesza się i nie jest możliwe wyłączenie go zwykłym sposobem
przez program (x)scanimage.

Ten program wymaga uprawnień roota albo dostępu do /dev/port.

%package gphoto2
Summary:	SANE backend for gphoto2 supported cameras
Summary(pl.UTF-8):	Sterownik SANE do aparatów obsługiwanych przez gphoto2
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description gphoto2
SANE backend for gphoto2 supported cameras.

%description gphoto2 -l pl.UTF-8
Sterownik SANE do aparatów obsługiwanych przez gphoto2.

%package pp
Summary:	SANE backends for parallel port scanners
Summary(pl.UTF-8):	Starowniki SANE dla skanerów podłączanych do portu równoległego
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Obsoletes:	sane-backends-canon_pp
Obsoletes:	sane-backends-hpsj5s
# in case sb used parport scanner
Obsoletes:	kernel-char-plustek
Obsoletes:	kernel-smp-char-plustek
Obsoletes:	sane-backends-plustek

%description pp
SANE backends for parallel port scanners. It includes the following
drivers:
- canon_pp (Canon CanoScan FBxxxP, CanoScan NxxxP)
- hpsj5s (HP ScanJet 5S)
- mustek_pp (Mustek CIS and CCD scanners)
- plustek_pp (Plustek)

%description pp -l pl.UTF-8
Starowniki SANE dla skanerów podłączanych do portu równoległego:
- canon_pp (Canon CanoScan FBxxxP, CanoScan NxxxP)
- hpsj5s (HP ScanJet 5S)
- mustek_pp (skanery Mustek CIS i CCD)
- plustek_pp (Plustek)

%package v4l
Summary:	SANE backend for Video4Linux supported devices
Summary(pl.UTF-8):	Sterownik SANE do urządzeń obsługiwanych przez system Video4Linux
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description v4l
SANE backend for Video4Linux supported devicecameras.

%description v4l -l pl.UTF-8
Sterownik SANE do urządzeń obsługiwanych przez system Video4Linux.

%prep
%setup -q
# kill libtool.m4 inclusion
grep -v '^m4_include' acinclude.m4 > acinclude.m4.tmp
mv -f acinclude.m4.tmp acinclude.m4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-pthread \
	--enable-static \
	--enable-pnm-backend \
	--enable-translations \
	%{?with_gphoto:--with-gphoto2}

# --enable-avahi? (BR: avahi-devel >= 0.6.24, R: for net backend)
# --enable-libusb_1_0 to use libusb 1.0 (but libgphoto2 still uses old libusb, so stick to this for now)

%{__make}

%ifarch %{ix86} %{x8664}
cd tools
%{__cc} %{rpmcppflags} -DHAVE_SYS_IO_H %{rpmcflags} %{rpmldflags} \
	-I../include -o mustek600iin-off mustek600iin-off.c
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/sysconfig/rc-inetd,%{_aclocaldir},/var/lock/sane}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/saned
install %{SOURCE2} $RPM_BUILD_ROOT%{_aclocaldir}

%ifarch %{ix86} %{x8664}
install tools/mustek600iin-off $RPM_BUILD_ROOT%{_bindir}
%endif

%{__rm} -rf $RPM_BUILD_ROOT%{_prefix}/doc

# only shared modules - shut up check-files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/sane/libsane-*.{so,la,a}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%pre saned
%groupadd -g 90 saned
%useradd -u 90 -d /usr/share/empty -s /bin/false -c "SANE remote scanning daemon" -g saned saned

%post saned
%service -q rc-inetd reload

%postun saned
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
	%userremove saned
	%groupremove saned
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* LICENSE NEWS PROBLEMS PROJECTS README README.linux
%doc doc/canon doc/gt68xx doc/leo doc/matsushita doc/mustek doc/mustek_usb
%doc doc/mustek_usb2 doc/niash doc/plustek doc/sceptre doc/teco doc/u12 doc/umax
%attr(755,root,root) %{_bindir}/sane-find-scanner
%attr(755,root,root) %{_bindir}/scanimage
%attr(755,root,root) %{_bindir}/gamma4scanimage
%dir %{_sysconfdir}/sane.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/abaton.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/agfafocus.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/apple.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/artec.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/artec_eplus48u.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/avision.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/bh.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/canon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/canon630u.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/canon_dr.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/cardscan.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/coolscan.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/coolscan2.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/coolscan3.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dc210.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dc240.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dc25.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dell1600n_net.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dll.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/dmc.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/epjitsu.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/epson.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/epson2.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/fujitsu.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/genesys.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/gt68xx.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp3900.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp4200.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp5400.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hs2p.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/ibm.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/kodak.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/leo.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/lexmark.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/ma1509.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/matsushita.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/microtek.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/microtek2.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/mustek.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/mustek_usb.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/nec.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/net.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/p5.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/pie.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/pixma.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/plustek.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/qcam.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/ricoh.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/rts8891.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/s9036.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/sceptre.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/sharp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/sm3840.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/snapscan.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/sp15c.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/st400.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/stv680.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/tamarack.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/teco1.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/teco2.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/teco3.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/test.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/u12.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/umax.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/umax1220u.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/umax_pp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/xerox_mfp.conf
%attr(755,root,root) %{_libdir}/libsane.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsane.so.1
%dir %{_libdir}/sane
%attr(755,root,root) %{_libdir}/sane/libsane-abaton.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-agfafocus.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-apple.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-artec.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-artec_eplus48u.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-as6e.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-avision.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-bh.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon630u.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon_dr.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-cardscan.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-coolscan.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-coolscan2.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-coolscan3.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dc210.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dc240.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dc25.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dell1600n_net.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dll.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-dmc.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-epjitsu.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-epson.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-epson2.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-fujitsu.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-genesys.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-gt68xx.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp3500.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp3900.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp4200.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp5400.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp5590.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hpljm1005.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hs2p.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-ibm.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-kodak.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-kvs1025.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-leo.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-lexmark.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-ma1509.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-matsushita.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-microtek.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-microtek2.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-mustek.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-mustek_usb.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-mustek_usb2.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-nec.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-net.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-niash.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-p5.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-pie.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-pixma.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-plustek.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-pnm.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-qcam.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-ricoh.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-rts8891.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-s9036.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-sceptre.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-sharp.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-sm3600.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-sm3840.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-snapscan.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-sp15c.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-st400.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-stv680.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-tamarack.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-teco1.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-teco2.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-teco3.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-test.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-u12.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-umax.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-umax1220u.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-umax_pp.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-xerox_mfp.so.*
%dir %attr(775,root,usb) /var/lock/sane
%{_mandir}/man1/sane-find-scanner.1*
%{_mandir}/man1/scanimage.1*
%{_mandir}/man1/gamma4scanimage.1*
%{_mandir}/man1/sane-config.1*
%{_mandir}/man5/sane-abaton.5*
%{_mandir}/man5/sane-agfafocus.5*
%{_mandir}/man5/sane-apple.5*
%{_mandir}/man5/sane-artec.5*
%{_mandir}/man5/sane-artec_eplus48u.5*
%{_mandir}/man5/sane-as6e.5*
%{_mandir}/man5/sane-avision.5*
%{_mandir}/man5/sane-bh.5*
%{_mandir}/man5/sane-canon.5*
%{_mandir}/man5/sane-canon630u.5*
%{_mandir}/man5/sane-canon_dr.5*
%{_mandir}/man5/sane-cardscan.5*
%{_mandir}/man5/sane-coolscan.5*
%{_mandir}/man5/sane-coolscan2.5*
%{_mandir}/man5/sane-coolscan3.5*
%{_mandir}/man5/sane-dc210.5*
%{_mandir}/man5/sane-dc240.5*
%{_mandir}/man5/sane-dc25.5*
%{_mandir}/man5/sane-dll.5*
%{_mandir}/man5/sane-dmc.5*
%{_mandir}/man5/sane-epjitsu.5*
%{_mandir}/man5/sane-epson.5*
%{_mandir}/man5/sane-epson2.5*
%{_mandir}/man5/sane-fujitsu.5*
%{_mandir}/man5/sane-genesys.5*
%{_mandir}/man5/sane-gt68xx.5*
%{_mandir}/man5/sane-hp.5*
%{_mandir}/man5/sane-hp3500.5*
%{_mandir}/man5/sane-hp3900.5*
%{_mandir}/man5/sane-hp4200.5*
%{_mandir}/man5/sane-hp5400.5*
%{_mandir}/man5/sane-hp5590.5*
%{_mandir}/man5/sane-hpljm1005.5*
%{_mandir}/man5/sane-hs2p.5*
%{_mandir}/man5/sane-ibm.5*
%{_mandir}/man5/sane-kodak.5*
%{_mandir}/man5/sane-kvs1025.5*
%{_mandir}/man5/sane-leo.5*
%{_mandir}/man5/sane-lexmark.5*
%{_mandir}/man5/sane-ma1509.5*
%{_mandir}/man5/sane-matsushita.5*
%{_mandir}/man5/sane-microtek.5*
%{_mandir}/man5/sane-microtek2.5*
%{_mandir}/man5/sane-mustek.5*
%{_mandir}/man5/sane-mustek_usb.5*
%{_mandir}/man5/sane-mustek_usb2.5*
%{_mandir}/man5/sane-nec.5*
%{_mandir}/man5/sane-net.5*
%{_mandir}/man5/sane-niash.5*
%{_mandir}/man5/sane-p5.5*
%{_mandir}/man5/sane-pie.5*
%{_mandir}/man5/sane-pixma.5*
%{_mandir}/man5/sane-plustek.5*
%{_mandir}/man5/sane-pnm.5*
%{_mandir}/man5/sane-qcam.5*
%{_mandir}/man5/sane-ricoh.5*
%{_mandir}/man5/sane-rts8891.5*
%{_mandir}/man5/sane-s9036.5*
%{_mandir}/man5/sane-sceptre.5*
%{_mandir}/man5/sane-scsi.5*
%{_mandir}/man5/sane-sharp.5*
%{_mandir}/man5/sane-sm3600.5*
%{_mandir}/man5/sane-sm3840.5*
%{_mandir}/man5/sane-snapscan.5*
%{_mandir}/man5/sane-sp15c.5*
%{_mandir}/man5/sane-st400.5*
%{_mandir}/man5/sane-stv680.5*
%{_mandir}/man5/sane-tamarack.5*
%{_mandir}/man5/sane-teco1.5*
%{_mandir}/man5/sane-teco2.5*
%{_mandir}/man5/sane-teco3.5*
%{_mandir}/man5/sane-test.5*
%{_mandir}/man5/sane-u12.5*
%{_mandir}/man5/sane-umax.5*
%{_mandir}/man5/sane-umax1220u.5*
%{_mandir}/man5/sane-umax_pp.5*
%{_mandir}/man5/sane-usb.5*
%{_mandir}/man5/sane-xerox_mfp.5*
%{_mandir}/man7/sane.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sane-config
%attr(755,root,root) %{_libdir}/libsane.so
%{_libdir}/libsane.la
%{_includedir}/sane
%{_aclocaldir}/sane-backends.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libsane.a

%files saned
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/saned
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/saned.conf
%attr(755,root,root) %{_sbindir}/saned
%{_mandir}/man8/saned.8*

%ifarch %{ix86} %{x8664}
%files -n sane-mustek600IIN
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mustek600iin-off
%endif

%if %{with gphoto}
%files gphoto2
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/gphoto2.conf
%attr(755,root,root) %{_libdir}/sane/libsane-gphoto2.so.*
%{_mandir}/man5/sane-gphoto2.5*
%endif

%if %{with lpt}
%files pp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/canon_pp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hpsj5s.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/mustek_pp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/plustek_pp.conf
%attr(755,root,root) %{_libdir}/sane/libsane-canon_pp.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hpsj5s.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-mustek_pp.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-plustek_pp.so.*
%{_mandir}/man5/sane-canon_pp.5*
%{_mandir}/man5/sane-hpsj5s.5*
%{_mandir}/man5/sane-mustek_pp.5*
%{_mandir}/man5/sane-plustek_pp.5*
%endif

%files v4l
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/v4l.conf
%attr(755,root,root) %{_libdir}/sane/libsane-v4l.so.*
%{_mandir}/man5/sane-v4l.5*
