Summary:	KXL - a visual & sound library
Summary(pl):	KXL - biblioteka X11 - d¼wiêk i grafika
Name:		KXL
Version:	1.1.5
Release:	1
License:	GPL
Group:		X11/Libraries
Group(cs):	X11/Knihovny
Group(da):	X11/Biblioteker
Group(de):	X11/Bibliotheken
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(is):	X11/Aðgerðasöfn
Group(it):	X11/Librerie
Group(ja):	X11/¥é¥¤¥Ö¥é¥ê
Group(no):	X11/Biblioteker
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(pt):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(sl):	X11/Knji¾nice
Group(sv):	X11/Bibliotek
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Source0:	http://www2.mwnet.or.jp/~fc3srx7/download/%{name}-%{version}.tar.gz
URL:		http://www2.mwnet.or.jp/~fc3srx7/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Kacchan X Windows System Library (KXL) is a visual & sound library.

%description -l pl
Kacchan X Windows System Library (KXL) to biblioteka d¼wiêku i
grafiki.

%package devel
Summary:	Development resources for KXL
Summary(pl):	Pliki nag³ówkowe i doumentacja do KXL
Group:		X11/Development/Libraries
Group(cs):	X11/Vývojové prostøedky/Knihovny
Group(da):	X11/Udvikling/Biblioteker
Group(de):	X11/Entwicklung/Bibliotheken
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(is):	X11/Þróunartól/Aðgerðasöfn
Group(it):	X11/Sviluppo/Librerie
Group(ja):	X11/³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	X11/Applikasjoner/Biblioteker
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(pt):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	X11/Razvoj/Knji¾nice
Group(sv):	X11/Utveckling/Bibliotek
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
Development resources for KXL.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do KXL.

%package static
Summary:	Static KXL library
Summary(pl):	Statyczna biblioteka KXL
Group:		X11/Development/Libraries
Group(cs):	X11/Vývojové prostøedky/Knihovny
Group(da):	X11/Udvikling/Biblioteker
Group(de):	X11/Entwicklung/Bibliotheken
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(is):	X11/Þróunartól/Aðgerðasöfn
Group(it):	X11/Sviluppo/Librerie
Group(ja):	X11/³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	X11/Applikasjoner/Biblioteker
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(pt):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	X11/Razvoj/Knji¾nice
Group(sv):	X11/Utveckling/Bibliotek
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static KXL library.

%description static -l pl
Statyczna biblioteka KXL.

%prep
%setup -q

%build
# libKXL uses libX11, so should be linked with it:
echo 'libKXL_la_LIBADD = -L/usr/X11R6/lib -lX11' >> src/Makefile.am
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib%{name}-%{version}.so
%attr(755,root,root) %{_libdir}/lib%{name}.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so
%{_includedir}/*
%{_aclocaldir}/KXL.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.a
