Summary:	Advanced Linux Sound Architecture (ALSA) - Library
Name:		alsa-lib
Version:	1.0.28
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.bz2
# Source0-md5:	c9e21b88a2b3e6e12ea7ba0f3b271fc3
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

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/alsa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D utils/alsa.m4 $RPM_BUILD_ROOT%{_aclocaldir}/alsa.m4

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{,alsa-lib/smixer/}*.la

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

%dir %{_datadir}/alsa
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_datadir}/alsa/cards
%dir %{_datadir}/alsa/pcm

%{_datadir}/alsa/*.conf
%{_datadir}/alsa/pcm/*.conf
%{_datadir}/alsa/*.alisp
%{_datadir}/alsa/cards

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libasound.so
%{_aclocaldir}/alsa.m4
%{_includedir}/sys/*.h
%{_includedir}/alsa
%{_pkgconfigdir}/*.pc

