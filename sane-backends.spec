Summary:	SANE --- Easy local and networked scanner access
Summary(pl):	SANE --- Prosta obs³uga skanerów lokalnych i sieciowych
Name:		sane-backends
Version:	1.0.4
Release:	1
License:	relaxed LGPL (libraries), and public domain (docs)
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.mostang.com/pub/sane/%{name}-%{version}.tar.gz
Source1:	%{name}.rc-inetd
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-no_libs.patch
Patch2:		%{name}-includes.patch
Patch3:		%{name}-mustek-gamma.patch
Patch4:		%{name}-mustek-path.patch
URL:		http://www.mostang.com/sane/
BuildRequires:	autoconf
BuildRequires:	libjpeg-devel
Prereq:		/sbin/ldconfig
Prereq:		sh-utils
Prereq:		shadow
Prereq:		grep
Requires:	rc-inetd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	sane

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
SANE (Scanner Access Now Easy) jest rozs±dnym i prostym insterfejsem
do skanerów, zarówno lokalnych jak i sieciowych, oraz innych urz±dzeñ
do pozyskiwania obrazów, jak cyfrowe aparaty i kamery. SANE aktualnie
zawiera modu³y do obs³ugi:

Skanery: Agfa SnapScan, Apple, Artec, Canon, CoolScan, Epson, HP,
         Microtek, Mustek, Nikon, Siemens, Tamarack, UMAX

Inne:    Connectix, QuickCams

oraz inne urz±dzenia dostêpne przez sieæ.

%package -n sane-devel
Summary:	Development part of SANE 
Summary(pl):	Czê¶æ SANE przeznaczona dla programistów
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description -n sane-devel
Development part of SANE.

%description -l pl -n sane-devel
Czê¶æ SANE dla programistów.

%package -n sane-static
Summary:	Static SANE libraries
Summary(pl):	statyczne biblioteki SANE
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	sane-devel = %{version}

%description -n sane-static
Static SANE libraries.

%description -l pl -n sane-static
Biblioteki statyczne SANE.

%package -n sane-mustek600IIN
Summary:	Mustek 600 II N scanner tool
Summary(pl):	Narzêdzie do skanera Mustek 600 II N
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Requires:	%{name}

%description -n sane-mustek600IIN
Tool which turns Mustek 600 II N scanner off. Sometimes scanner hangs
and can't be turned off by (x)scanimage in normal way.

Note: this program needs root privileges or access to /dev/port.

%description -n sane-mustek600IIN -l pl
Narzêdzie wymuszaj±ce wy³±czyczenie skanera Mustek 600 II N. Czasem
skaner zawiesza siê i nie jest mo¿liwe wy³±czenie go zwyk³ym sposobem
przez program (x)scanimage.

Ten program wymaga uprawnieñ roota albo dostêpu do /dev/port.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoconf
%configure
%{__make}

(cd tools
%{__cc} -DHAVE_SYS_IO_H %{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} \
	-I../include -o mustek600iin-off mustek600iin-off.c
)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/saned
install tools/mustek600iin-off $RPM_BUILD_ROOT%{_bindir}

gzip -9nf AUTHORS LICENSE LEVEL2 NEWS PROBLEMS PROJECTS TODO ChangeLog

%pre
if [ "$1" = 1 ]; then
	getgid saned >/dev/null 2>&1 || %{_sbindir}/groupadd -g 90 -f saned
	id -u saned >/dev/null 2>&1 || %{_sbindir}/useradd -g saned -M -u 90 \
		-c "SANE remote scanning daemon" saned
	grep -q '^sane' /etc/services || echo -e \
		'sane\t\t6566/tcp\t\t\t#network scanner daemon' >>/etc/services
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

%files -n sane-devel
%defattr(644,root,root,755)
%{_includedir}/sane
%attr(755,root,root) %{_bindir}/sane-config
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/sane/lib*.la
%attr(755,root,root) %{_libdir}/sane/lib*.so

%files -n sane-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/sane/lib*.a

%files -n sane-mustek600IIN
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mustek600iin-off
