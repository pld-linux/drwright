Summary:	A program that reminds you to take wrist breaks
Name:		drwright
Version:	0.14
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://drwright.codefactory.se/download/%{name}-%{version}.tar.gz
URL:		http://drwright.codefactory.se/
BuildRequires:	pango-devel >= 1.0.99
BuildRequires:	gtk+2-devel >= 2.0.4
BuildRequires:	GConf2-devel >= 1.2.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	Xft-devel
BuildRequires:	fontconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DrWright is a program that forces you to take wrist breaks to rest
your hands.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)

%doc AUTHORS COPYING ChangeLog NEWS README

%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/drwright.schemas
%{_datadir}/applications/*.desktop
%{_datadir}/drwright
