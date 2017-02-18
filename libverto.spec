#
# Conditional build:
%bcond_without	libev		# libev interface
%bcond_without	libevent	# libevent interface
%bcond_without	tevent		# tevent interface
%bcond_without	static_libs	# static libraries
#
Summary:	Main loop abstraction library
Summary(pl.UTF-8):	Biblioteka abstrakcji głównej pętli
Name:		libverto
Version:	0.2.6
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://fedorahosted.org/releases/l/i/libverto/%{name}-%{version}.tar.gz
# Source0-md5:	d4e81c21403031089d71eaab07708b89
URL:		https://fedorahosted.org/libverto/
#BuildRequires:	autoconf >= 2.59
#BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 2.0
%{?with_libev:BuildRequires:	libev-devel}
%{?with_libevent:BuildRequires:	libevent-devel >= 2.0}
#BuildRequires:	libtool
BuildRequires:	pkgconfig
%{?with_tevent:BuildRequires:	tevent-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libverto provides a way for libraries to expose asynchronous
interfaces without having to choose a particular event loop,
offloading this decision to the end application which consumes the
library.

%description -l pl.UTF-8
libverto udostępnia środki pozwalające bibliotekom udostępniać
interfejsy asynchroniczne bez konieczności wyboru konkretnej pętli
zdarzeń, pozostawiając tę decyzję aplikacji końcowej wykorzystującej
bibliotekę.

%package devel
Summary:	Header files for verto library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki verto
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for verto library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki verto.

%package static
Summary:	Static verto library
Summary(pl.UTF-8):	Statyczna biblioteka verto
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static verto library.

%description static -l pl.UTF-8
Statyczna biblioteka verto.

%package glib
Summary:	libverto module providing integration with GLib
Summary(pl.UTF-8):	Moduł libverto zapewniający integrację z biblioteką GLib
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description glib
libverto module providing integration with GLib.

%description glib -l pl.UTF-8
Moduł libverto zapewniający integrację z biblioteką GLib.

%package glib-devel
Summary:	Header file for libverto-glib library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libverto-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}
Requires:	glib2-devel >= 2.0

%description glib-devel
Header file for libverto-glib library.

%description glib-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libverto-glib.

%package glib-static
Summary:	Static libverto-glib library
Summary(pl.UTF-8):	Statyczna biblioteka libverto-glib
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
Static libverto-glib library.

%description glib-static -l pl.UTF-8
Statyczna biblioteka libverto-glib.

%package libev
Summary:	libverto module providing integration with libev
Summary(pl.UTF-8):	Moduł libverto zapewniający integrację z biblioteką libev
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description libev
libverto module providing integration with libev.

%description libev -l pl.UTF-8
Moduł libverto zapewniający integrację z biblioteką libev.

%package libev-devel
Summary:	Header file for libverto-libev library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libverto-libev
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-libev = %{version}-%{release}
Requires:	libev-devel

%description libev-devel
Header file for libverto-libev library.

%description libev-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libverto-libev.

%package libev-static
Summary:	Static libverto-libev library
Summary(pl.UTF-8):	Statyczna biblioteka libverto-libev
Group:		Development/Libraries
Requires:	%{name}-libev-devel = %{version}-%{release}

%description libev-static
Static libverto-libev library.

%description libev-static -l pl.UTF-8
Statyczna biblioteka libverto-libev.

%package libevent
Summary:	libverto module providing integration with libevent
Summary(pl.UTF-8):	Moduł libverto zapewniający integrację z biblioteką libevent
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description libevent
libverto module providing integration with libevent.

%description libevent -l pl.UTF-8
Moduł libverto zapewniający integrację z biblioteką libevent.

%package libevent-devel
Summary:	Header file for libverto-libevent library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libverto-libevent
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-libevent = %{version}-%{release}
Requires:	libevent-devel >= 2.0

%description libevent-devel
Header file for libverto-libevent library.

%description libevent-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libverto-libevent.

%package libevent-static
Summary:	Static libverto-libevent library
Summary(pl.UTF-8):	Statyczna biblioteka libverto-libevent
Group:		Development/Libraries
Requires:	%{name}-libevent-devel = %{version}-%{release}

%description libevent-static
Static libverto-libevent library.

%description libevent-static -l pl.UTF-8
Statyczna biblioteka libverto-libevent.

%package tevent
Summary:	libverto module providing integration with tevent
Summary(pl.UTF-8):	Moduł libverto zapewniający integrację z biblioteką tevent
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tevent
libverto module providing integration with tevent.

%description tevent -l pl.UTF-8
Moduł libverto zapewniający integrację z biblioteką tevent.

%package tevent-devel
Summary:	Header file for libverto-tevent library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libverto-tevent
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-tevent = %{version}-%{release}
Requires:	tevent-devel

%description tevent-devel
Header file for libverto-tevent library.

%description tevent-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libverto-tevent.

%package tevent-static
Summary:	Static libverto-tevent library
Summary(pl.UTF-8):	Statyczna biblioteka libverto-tevent
Group:		Development/Libraries
Requires:	%{name}-tevent-devel = %{version}-%{release}

%description tevent-static
Static libverto-tevent library.

%description tevent-static -l pl.UTF-8
Statyczna biblioteka libverto-tevent.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	%{!?with_libev:--without-libev} \
	%{!?with_libevent:--without-libevent} \
	%{!?with_tevent:--without-tevent}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libverto*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	libev -p /sbin/ldconfig
%postun	libev -p /sbin/ldconfig

%post	libevent -p /sbin/ldconfig
%postun	libevent -p /sbin/ldconfig

%post	tevent -p /sbin/ldconfig
%postun	tevent -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libverto.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libverto.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libverto.so
%{_includedir}/verto.h
%{_includedir}/verto-module.h
%{_pkgconfigdir}/libverto.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libverto.a
%endif

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libverto-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libverto-glib.so.1

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libverto-glib.so
%{_includedir}/verto-glib.h
%{_pkgconfigdir}/libverto-glib.pc

%if %{with static_libs}
%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libverto-glib.a
%endif

%if %{with libev}
%files libev
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libverto-libev.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libverto-libev.so.1

%files libev-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libverto-libev.so
%{_includedir}/verto-libev.h
%{_pkgconfigdir}/libverto-libev.pc

%if %{with static_libs}
%files libev-static
%defattr(644,root,root,755)
%{_libdir}/libverto-libev.a
%endif
%endif

%if %{with libevent}
%files libevent
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libverto-libevent.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libverto-libevent.so.1

%files libevent-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libverto-libevent.so
%{_includedir}/verto-libevent.h
%{_pkgconfigdir}/libverto-libevent.pc

%if %{with static_libs}
%files libevent-static
%defattr(644,root,root,755)
%{_libdir}/libverto-libevent.a
%endif
%endif

%if %{with tevent}
%files tevent
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libverto-tevent.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libverto-tevent.so.1

%files tevent-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libverto-tevent.so
%{_includedir}/verto-tevent.h
%{_pkgconfigdir}/libverto-tevent.pc

%if %{with static_libs}
%files tevent-static
%defattr(644,root,root,755)
%{_libdir}/libverto-tevent.a
%endif
%endif
