Summary:	KXL -- a visual & sound library
Summary(pl):	KXL -- biblioteka X11 - d╪wiЙk i grafika
Name:		KXL
Version:	1.1.4
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/Библиотеки
Group(uk):	X11/Б╕бл╕отеки
Source0:	http://www2.mwnet.or.jp/~fc3srx7/download/%{name}-%{version}.tar.gz
URL:		http://www2.mwnet.or.jp/~fc3srx7/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Kacchan X Windows System Library (KXL) is a visual & sound library.

%description -l pl
Kacchan X Windows System Library (KXL) to biblioteka d╪wiЙku i grafiki.

%package devel
Summary:	Development resources for KXL
Summary(pl):	Pliki nagЁСwkowe i doumentacja do KXL
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Development resources for KXL.

%description -l pl devel
Pliki nagЁСwkowe i dokumentacja do KXL.

%package static
Summary:	Static KXL library
Summary(pl):	Statyczna biblioteka KXL
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static KXL library.

%description -l pl static
Statyczna biblioteka KXL.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

gzip -9nf ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -s %{_libdir}/lib%{name}-%{version}.so %{_libdir}/lib%{name}.so
/sbin/ldconfig

%postun 
rm %{_libdir}/lib%{name}.so
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib%{name}-%{version}.so
%attr(755,root,root) %{_libdir}/lib%{name}.la

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_aclocaldir}/KXL.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.a
