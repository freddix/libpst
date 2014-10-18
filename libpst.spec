Summary:	Outlook .pst file converter library
Name:		libpst
Version:	0.6.63
Release:	1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Libraries
Source0:	http://www.five-ten-sg.com/libpst/packages/%{name}-%{version}.tar.gz
# Source0-md5:	cf047faf8c671a0a074a65767e7d2bd7
BuildRequires:	libgsf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shared pst library.

%package devel
Summary:	Header files for pst library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for pst library.

%package utils
Summary:	Outlook .pst file converting utilities
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description utils
Outlook .pst file converting utilities.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
        --disable-dii		\
        --disable-python	\
        --disable-static	\
        --enable-libpst-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libpst.so.4
%attr(755,root,root) %{_libdir}/libpst.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpst.so
%{_includedir}/libpst-4
%{_pkgconfigdir}/*.pc
%{_mandir}/man5/*.5*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lspst
%attr(755,root,root) %{_bindir}/nick2ldif
%attr(755,root,root) %{_bindir}/pst2ldif
%attr(755,root,root) %{_bindir}/readpst
%{_mandir}/man1/*.1*

