
%define		_plustek_ver	0_42_5

%define		_kernel_ver %(grep UTS_RELEASE %{_kernelsrcdir}/include/linux/version.h 2>/dev/null | cut -d'"' -f2)
%define		_kernel_ver_str	%(echo %{_kernel_ver} | sed s/-/_/g)

Summary:	SANE - Easy local and networked scanner access
Summary(es):	SANE - acceso a scanners en red y locales
Summary(pl):	SANE - Prosta obs�uga skaner�w lokalnych i sieciowych
Summary(pt_BR):	SANE - acesso a scanners locais e em rede
Name:		sane-backends
Version:	1.0.7
Release:	2
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
URL:		http://www.mostang.com/sane/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel
Prereq:		/sbin/ldconfig
Prereq:		grep
Prereq:		sh-utils
Prereq:		shadow
Prereq:		rc-inetd
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

%description -l pt_BR
O SANE (Scanner Access Now Easy) � uma interface simples para scanners
e outros dispositivos de captura de imagens como c�meras fotogr�ficas
digitais e de v�deo conectados diretamente ou atrav�s da rede.

%description -l pl
SANE (Scanner Access Now Easy) jest rozs�dnym i prostym insterfejsem
do skaner�w, zar�wno lokalnych jak i sieciowych, oraz innych urz�dze�
do pozyskiwania obraz�w, jak cyfrowe aparaty i kamery. SANE aktualnie
zawiera modu�y do obs�ugi:

Skanery: Abaton, Agfa, Apple, Artec, Avision, Bell+Howell, Canon,
Epson, Fujitsu, HP, Microtek, Mustek, NEC, Nikon, PIE, Plustek, Ricoh,
Sharp, Siemens, Tamarack, UMAX

Aparaty cyfrowe: Kodak, Polaroid, Connectix QuickCam

oraz inne urz�dzenia dost�pne przez sie�.

%description -l es
SANE - acceso a scanners en red y locales.

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
Narz�dzie wymuszaj�ce wy��czyczenie skanera Mustek 600 II N. Czasem
skaner zawiesza si� i nie jest mo�liwe wy��czenie go zwyk�ym sposobem
przez program (x)scanimage.

Ten program wymaga uprawnie� roota albo dost�pu do /dev/port.

%package plustek
Summary:	Plustek scanner driver
Summary(pl):	Sterownik do skaner�w Plustek
Group:		Applications/System
Requires:	%{name} = %{version}
PreReq:		/sbin/depmod

%description plustek
This package contains kernel module which drives Plustek scanners.

%description plustek -l pl
Pakiet zawiera modu� steruj�cy skanerami Plustek.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

(
	mkdir tmp-plustek_driver
	cd tmp-plustek_driver
	tar xfz %{SOURCE2}
	# NOTE: we need original dll.conf!
	rm backend/dll.conf
	cp -Rf * ..
)

%build
libtoolize --copy --force
aclocal
autoconf
%configure
%{__make}

(cd tools
%{__cc} -DHAVE_SYS_IO_H %{rpmcflags} \
	-I../include -o mustek600iin-off mustek600iin-off.c
)

%{__make} all -C backend/plustek_driver

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install  backend/plustek_driver/pt_drv.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/saned
install tools/mustek600iin-off $RPM_BUILD_ROOT%{_bindir}

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
        %{_sbindir}/userdel saned 2>/dev/null
        %{_sbindir}/groupdel saned 2>/dev/null
fi

%postun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/rc-inetd ]; then
	        /etc/rc.d/init.d/rc-inetd reload
	fi
fi
/sbin/ldconfig

%post plustek
/sbin/depmod -a

%postun plustek
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
%{_mandir}/man5/*

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

%files -n sane-mustek600IIN
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mustek600iin-off
%doc backend/plustek_driver/README backend/plustek_driver/TODO
%doc backend/plustek_driver/FAQ backend/plustek_driver/ChangeLog

%files plustek
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*
