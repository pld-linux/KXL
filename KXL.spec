Summary:	KXL - a visual & sound library
Summary(pl):	KXL - biblioteka X11 - d¼wiêk i grafika
Name:		KXL
Version:	1.1.7
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://kxl.hn.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	321bfad9dee29840656225b54bb6feb0
URL:		http://kxl.hn.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kacchan X Window System Library (KXL) is a visual & sound library.

%description -l pl
Kacchan X Window System Library (KXL) to biblioteka d¼wiêku i
grafiki.

%package devel
Summary:	Development resources for KXL
Summary(pl):	Pliki nag³ówkowe i dokumentacja do KXL
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development resources for KXL.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do KXL.

%package static
Summary:	Static KXL library
Summary(pl):	Statyczna biblioteka KXL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static KXL library.

%description static -l pl
Statyczna biblioteka KXL.

%prep
%setup -q

%build
# libKXL uses libX11, so should be linked with it:
echo 'libKXL_la_LIBADD = -L/usr/X11R6/%{_lib} -lX11' >> src/Makefile.am
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib%{name}-%{version}.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.la
%{_includedir}/*
%{_aclocaldir}/KXL.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.a
