#
# Conditional build:
%bcond_without	gphoto	# no gphoto backend (which requires libgphoto2)
%bcond_without	lpt	# no parallel port backends (which require libieee1284)
%bcond_without	usb	# without USB scanners support (which requires libusb)
%bcond_without	rts88xx # rts88xx scanner support (hp4400/4470)
#
%ifarch sparc sparc64 sparcv9
%undefine	with_usb
%endif
# XXX: really only x86*?
%ifnarch %{ix86} %{x8664}
%undefine	with_lpt
%endif
Summary:	SANE - easy local and networked scanner access
Summary(es):	SANE - acceso a scanners en red y locales
Summary(ko):	½ºÄ³³Ê¸¦ ´Ù·ç´Â ¼ÒÇÁÆ®¿þ¾î
Summary(pl):	SANE - prosta obs³uga skanerów lokalnych i sieciowych
Summary(pt_BR):	SANE - acesso a scanners locais e em rede
Name:		sane-backends
Version:	1.0.16
Release:	3
License:	relaxed LGPL (libraries), and Public Domain (docs)
Group:		Libraries
Source0:	ftp://ftp.sane-project.org/pub/sane/%{name}-%{version}/sane-backends-%{version}.tar.gz
# Source0-md5:	bec9b9262246316b4ebfe2bc7451aa28
Source1:	%{name}.rc-inetd
Source2:	%{name}.m4
# http://hp44x0backend.sourceforge.net/
Source3:	http://dl.sourceforge.net/hp44x0backend/sane_hp_rts88xx-0.17n.tar.gz
# Source3-md5:	01cae741a347fc73eeaf32aeb731d9af
#Source3:	http://home.foni.net/~johanneshub/sane_hp_rts88xx-0.17k.tar.gz
Patch1:		%{name}-mustek-path.patch
Patch2:		%{name}-spatc.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-pmake.patch
Patch5:		%{name}-locale-names.patch
Patch6:		%{name}-hp_rts88xx-fixes.patch
Patch7:		%{name}-pl.po-update.patch
URL:		http://www.sane-project.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?with_gphoto:BuildRequires:	libgphoto2-devel >= 2.0.1}
%{?with_lpt:BuildRequires:	libieee1284-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
%{?with_usb:BuildRequires:	libusb-devel}
BuildRequires:	pkgconfig
BuildRequires:	resmgr-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	tetex-latex-psnfss
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name}-devel = %{version}-%{release}
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
Requires:	rc-inetd
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post,postun):	/sbin/ldconfig
Requires(preun):	/usr/sbin/groupdel
Requires(preun):	/usr/sbin/userdel
Requires:	%{name} = %{version}-%{release}
Provides:	group(saned)
Provides:	user(saned)

%description saned
saned is the SANE (Scanner Access Now Easy) daemon that allows remote
clients to access image acquisition devices available on the local
host.

%description saned -l pl
saned to demon SANE pozwalaj±cy zdalnym klientom na dostêp do urz±dzeñ
odczytuj±cych obraz pod³±czonych lokalnie.

%package -n sane-mustek600IIN
Summary:	Mustek 600 II N scanner tool
Summary(pl):	Narzêdzie do skanera Mustek 600 II N
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n sane-mustek600IIN
Tool which turns Mustek 600 II N scanner off. Sometimes scanner hangs
and can't be turned off by (x)scanimage in normal way.

Note: this program needs root privileges or access to /dev/port.

%description -n sane-mustek600IIN -l pl
Narzêdzie wymuszaj±ce wy³±czenie skanera Mustek 600 II N. Czasem
skaner zawiesza siê i nie jest mo¿liwe wy³±czenie go zwyk³ym sposobem
przez program (x)scanimage.

Ten program wymaga uprawnieñ roota albo dostêpu do /dev/port.

%package gphoto2
Summary:	SANE backend for gphoto2 supported cameras
Summary(pl):	Sterownik SANE do aparatów obs³ugiwanych przez gphoto2
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description gphoto2
SANE backend for gphoto2 supported cameras.

%description gphoto2 -l pl
Sterownik SANE do aparatów obs³ugiwanych przez gphoto2.

%package pp
Summary:	SANE backends for parallel port scanners
Summary(pl):	Starowniki SANE dla skanerów pod³±czanych do portu równoleg³ego
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Obsoletes:	sane-backends-canon_pp
Obsoletes:	sane-backends-hpsj5s
# in case sb used parport scanner
Obsoletes:	sane-backends-plustek
Obsoletes:	kernel-char-plustek
Obsoletes:	kernel-smp-char-plustek

%description pp
SANE backends for parallel port scanners. It includes the following
drivers:
- canon_pp (Canon CanoScan FBxxxP, CanoScan NxxxP)
- hpsj5s (HP ScanJet 5S)
- mustek_pp (Mustek CIS and CCD scanners)
- plustek_pp (Plustek)

%description pp -l pl
Starowniki SANE dla skanerów pod³±czanych do portu równoleg³ego:
- canon_pp (Canon CanoScan FBxxxP, CanoScan NxxxP)
- hpsj5s (HP ScanJet 5S)
- mustek_pp (skanery Mustek CIS i CCD)
- plustek_pp (Plustek)

%prep
%setup -q -a3
# kill libtool.m4 copy
grep -B 100000 'libtool.m4 - Configure libtool for the host system' acinclude.m4 > acinclude.m4.tmp
mv -f acinclude.m4.tmp acinclude.m4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%if %{with rts88xx}
%patch6 -p1
cd sane_hp_rts88xx/sane_hp_rts88xx
sh -x patch-sane.sh `pwd`/../..
cd ../..
%endif
%patch7 -p1
mv -f po/sane-backends.{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-static \
	--enable-pnm-backend \
	--enable-translations \
	%{?with_gphoto:--with-gphoto2}

%{__make}

%ifarch %{ix86}
cd tools
%{__cc} -DHAVE_SYS_IO_H %{rpmcflags} \
	-I../include -o mustek600iin-off mustek600iin-off.c
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/sysconfig/rc-inetd,%{_aclocaldir},/var/lock/sane}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/saned
install %{SOURCE2} $RPM_BUILD_ROOT%{_aclocaldir}

%ifarch %{ix86}
install tools/mustek600iin-off $RPM_BUILD_ROOT%{_bindir}
%endif

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

# only shared modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/sane/libsane-*.{so,la,a}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%pre saned
%groupadd -g 90 saned
%useradd -u 90 -d /usr/share/empty -s /bin/false -c "SANE remote scanning daemon" -g saned saned

%post saned
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun saned
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/rc-inetd ]; then
		/etc/rc.d/init.d/rc-inetd reload
	fi
	%userremove saned
	%groupremove saned
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS PROBLEMS PROJECTS README README.linux
%doc doc/canon doc/gt68xx doc/leo doc/matsushita doc/mustek doc/mustek_usb
%doc doc/plustek doc/sceptre doc/teco doc/umax
%dir %{_sysconfdir}/sane.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/[!cghmp]*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/c[!a]*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/canon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/canon630u.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/genesys.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/gt68xx.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp5400.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/m[!u]*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/mustek.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/mustek_usb.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/p[!l]*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/plustek.conf
%{?with_rts88xx:%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/hp_rt* }
%dir %{_libdir}/sane
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/sane/libsane-[!cghmp]*.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-c[!a]*.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-canon630u.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-genesys.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-gt68xx.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-hp5400.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-m[!u]*.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-mustek.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-mustek_usb.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-p[!l]*.so.*
%attr(755,root,root) %{_libdir}/sane/libsane-plustek.so.*
%{?with_rts88xx:%attr(755,root,root) %{_libdir}/sane/libsane-hp_rts88xx.so.* }
%attr(755,root,root) %{_bindir}/sane-find-scanner
%attr(755,root,root) %{_bindir}/scanimage
%attr(755,root,root) %{_bindir}/gamma4scanimage
%dir %attr(775,root,usb) /var/lock/sane
%{_mandir}/man1/sane-find-scanner.1*
%{_mandir}/man1/scanimage.1*
%{_mandir}/man1/gamma4scanimage.1*
%{_mandir}/man1/sane-config.1*
%{_mandir}/man5/sane-[!cghmp]*
%{_mandir}/man5/sane-c[!a]*
%{_mandir}/man5/sane-canon.5*
%{_mandir}/man5/sane-canon630u.5*
%{_mandir}/man5/sane-genesys.5*
%{_mandir}/man5/sane-gt68xx.5*
%{_mandir}/man5/sane-hp.5*
%{_mandir}/man5/sane-hp5400.5*
%{_mandir}/man5/sane-m[!u]*
%{_mandir}/man5/sane-mustek.5*
%{_mandir}/man5/sane-mustek_usb.5*
%{_mandir}/man5/sane-p[!l]*
%{_mandir}/man5/sane-plustek.5*
%{?with_rts88xx:%{_mandir}/man5/sane-hp_rts88xx* }
%{_mandir}/man7/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sane-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/sane
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files saned
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/saned
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sane.d/saned.conf
%attr(755,root,root) %{_sbindir}/saned
%{_mandir}/man8/saned.8*

%ifarch %{ix86}
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
