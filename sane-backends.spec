# conditional build
# _without_dist_kernel		without kernel from distribution

%define		_plustek_ver	0_42_5

Summary:	SANE - Easy local and networked scanner access
Summary(es):	SANE - acceso a scanners en red y locales
Summary(pl):	SANE - Prosta obs³uga skanerów lokalnych i sieciowych
Summary(pt_BR):	SANE - acesso a scanners locais e em rede
Name:		sane-backends
Version:	1.0.7
%define	rel	2.21
Release:	%{rel}
License:	relaxed LGPL (libraries), and public domain (docs)
Group:		Libraries
Source0:	ftp://ftp.mostang.com/pub/sane/sane-%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.rc-inetd
Source2:	http://home.t-online.de/home/g-jaeger/current/plustek-sane-%{_plustek_ver}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-no_libs.patch
Patch2:		%{name}-mustek-path.patch
Patch3:		%{name}-spatc.patch
Patch4:		%{name}-libusb-link.patch
Patch5:		%{name}-acinclude.patch
Patch6:		%{name}-plustek-Makefile.patch
URL:		http://www.mostang.com/sane/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel
%{!?_without_dist_kernel:BuildRequires: kernel-headers}
PreReq:		rc-inetd
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
Epson, Fujitsu, HP, Microtek, Mustek, NEC, Nikon, PIE, Plustek, Ricoh,
Sharp, Siemens, Tamarack, UMAX

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
Epson, Fujitsu, HP, Microtek, Mustek, NEC, Nikon, PIE, Plustek, Ricoh,
Sharp, Siemens, Tamarack, UMAX

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

%package plustek
Summary:	Plustek scanner driver
Summary(pl):	Sterownik do skanerów Plustek
Group:		Applications/System
Requires:	%{name} = %{version}

%description plustek
This package contains driver for Plustek scanners.

%description plustek -l pl
Pakiet zawiera sterownik dla skanerów Plustek.

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
%patch4 -p1
%patch5 -p1

mkdir tmp-plustek_driver
cd tmp-plustek_driver
tar xfz %{SOURCE2}
# NOTE: we need original dll.conf!
rm -f backend/dll.conf
cp -Rf * ..
cd ..

%patch6 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
%{__automake} ||
%{__autoconf}
%configure
%{__make}

%ifnarch ppc
cd tools
%{__cc} -DHAVE_SYS_IO_H %{rpmcflags} \
	-I../include -o mustek600iin-off mustek600iin-off.c
cd ..
%endif

cd backend/plustek_driver
%{__make} all BUILD_SMP=1 OPT_FLAGS="%{rpmcflags}"
mv -f pt_drv.o{,.smp}
%{__make} clean
%{__make} all OPT_FLAGS="%{rpmcflags}"
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install  backend/plustek_driver/pt_drv.o.smp	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/pt_drv.o
install  backend/plustek_driver/pt_drv.o	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/saned

%ifnarch ppc
install tools/mustek600iin-off $RPM_BUILD_ROOT%{_bindir}
%endif

gzip -9nf AUTHORS LICENSE LEVEL2 NEWS PROBLEMS PROJECTS TODO ChangeLog \
	backend/plustek_driver/README backend/plustek_driver/TODO \
	backend/plustek_driver/FAQ backend/plustek_driver/ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid saned`" ]; then
        if [ "`getgid saned`" != "90" ]; then
                echo "Warning: group saned haven't gid=90. Correct this before installing sane" 1>&2
                exit 1
        fi
else
        /usr/sbin/groupadd -g 90 -r -f saned
fi
if [ -n "`id -u saned 2>/dev/null`" ]; then
        if [ "`id -u saned`" != "90" ]; then
                echo "Warning: user saned haven't uid=90. Correct this before installing sane" 1>&2
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
%{_mandir}/man5/sane-[!p]*
%{_mandir}/man5/sane-p[!l]*

%files devel
%defattr(644,root,root,755)
%{_includedir}/sane
%attr(755,root,root) %{_bindir}/sane-config
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/sane/lib*.la
%attr(755,root,root) %{_libdir}/sane/lib*.so
%{_mandir}/man7/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/sane/lib*.a

%ifnarch ppc
%files -n sane-mustek600IIN
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mustek600iin-off
%endif

%files plustek
%defattr(644,root,root,755)
%doc backend/plustek_driver/*.gz
%{_mandir}/man5/sane-plustek*

%files -n kernel-char-plustek
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*

%files -n kernel-smp-char-plustek
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/*
