Summary:	Advanced Linux Sound Architecture (ALSA) - Library
Name:		alsa-lib
Version:	1.0.27.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.bz2
# Source0-md5:	17102aaab10e9d4b19f6b02937bab015
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-driver-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced Linux Sound Architecture (ALSA) - Library

%package devel
Summary:	Advanced Linux Sound Architecture (ALSA) - header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-driver-devel

%description devel
Advanced Linux Sound Architecture (ALSA) - header files.

%prep
%setup -q

%{__sed} -i "s|AM_CONFIG_HEADER|AC_CONFIG_HEADERS|" configure.in

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-configdir=%{_sysconfdir}/alsa
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/alsa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D utils/alsa.m4 $RPM_BUILD_ROOT%{_aclocaldir}/alsa.m4

rm -f $RPM_BUILD_ROOT%{_libdir}/alsa-lib/smixer/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libasound.so.?
%attr(755,root,root) %{_libdir}/libasound.so.*.*.*

%dir %{_libdir}/alsa-lib
%dir %{_libdir}/alsa-lib/smixer
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-ac97.so
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-hda.so
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-sbase.so

%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa/cards
%dir %{_sysconfdir}/alsa/pcm
%dir %{_datadir}/alsa

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/alsa/*.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/alsa/pcm/*.conf
%{_sysconfdir}/alsa/*.alisp
%{_sysconfdir}/alsa/cards

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libasound.so
%{_aclocaldir}/alsa.m4
%{_includedir}/sys/*.h
%{_includedir}/alsa
%{_pkgconfigdir}/*.pc

