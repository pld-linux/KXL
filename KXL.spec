%define name KXL
%define version  1.1.3
%define release  1

Summary:	KXL -- a visual & sound library
Summary(pl):	KBX -- biblioteka X11 - dzwiÍk i wideo
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www2.mwnet.or.jp/~fc3srx7/download/%{name}-%{version}.tar.gz
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
URL:		http://www2.mwnet.or.jp/~fc3srx7/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Kacchan X Windows System Liblary (KXL) is a visual & sound library.

%description -l pl
Kacchan X Windows System Liblary (KXL) to biblioteka dzwiÍku i video.

%prep
rm -rf $RPM_BUILD_ROOT

%post
echo Trwa rejestrowanie bibliotek w systemie...
/sbin/ldconfig

%setup -q

%build
./configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog KXL.html README
%{_prefix}/share/aclocal/KXL.m4
%{_includedir}/*
%{_libdir}/*
