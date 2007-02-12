Summary:	KXL - a visual & sound library
Summary(pl.UTF-8):   KXL - biblioteka X11 - dźwięk i grafika
Name:		KXL
Version:	1.1.7
Release:	3
License:	GPL
Group:		X11/Libraries
Source0:	http://kxl.hn.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	321bfad9dee29840656225b54bb6feb0
Patch0:		%{name}-am18.patch
URL:		http://kxl.hn.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kacchan X Window System Library (KXL) is a visual & sound library.

%description -l pl.UTF-8
Kacchan X Window System Library (KXL) to biblioteka dźwięku i
grafiki.

%package devel
Summary:	Development resources for KXL
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja do KXL
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	XFree86-devel

%description devel
Development resources for KXL.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do KXL.

%package static
Summary:	Static KXL library
Summary(pl.UTF-8):   Statyczna biblioteka KXL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static KXL library.

%description static -l pl.UTF-8
Statyczna biblioteka KXL.

%prep
%setup -q
%patch0 -p1

%build
# libKXL uses libX11, so should be linked with it:
echo 'libKXL_la_LIBADD = -L/usr/X11R6/%{_lib} -lX11' >> src/Makefile.am
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
