Summary:	A program that reminds you to take wrist breaks
Summary(pl):	Program przypominaj±cy, ¿eby daæ odpocz±æ nadgarstkom
Name:		drwright
Version:	0.18
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/gnome/sources/drwright/0.18/%{name}-%{version}.tar.bz2
# Source0-md5:	5056d36520b0a506e5bf3211f08315b8
Patch0:		%{name}-locale-names.patch
URL:		http://www.imendio.com/projects/drwright/
BuildRequires:	GConf2-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.22
BuildRequires:	fontconfig-devel
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	intltool >= 0.29
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pango-devel >= 1:1.2.0
BuildRequires:	pkgconfig
BuildRequires:	xft-devel
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DrWright is a program that forces you to take wrist breaks to rest
your hands.

%description -l pl
DrWright to program zmuszaj±cy do rozlu¼nienia nadgarstków, aby daæ
odpocz±æ d³oniom.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

%{__make} \
	CFLAGS="%{rpmcflags} -fno-strict-aliasing"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/drwright.schemas
%{_desktopdir}/*.desktop
%{_datadir}/drwright
