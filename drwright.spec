Summary:	A program that reminds you to take wrist breaks
Summary(pl):	Program przypominaj±cy, ¿eby daæ odpocz±æ nadgarstkom
Name:		drwright
Version:	0.17
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.17/%{name}-%{version}.tar.bz2
# Source0-md5:	e23acadea9bfede4b22611b058b80648
Patch0:		%{name}-schemas.patch
URL:		http://www.imendio.com/projects/drwright/
BuildRequires:	GConf2-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	gtk+2-devel >= 2.0.4
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	pango-devel >= 1.0.99
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

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install

%{__make} CFLAGS="%{rpmcflags} -fno-strict-aliasing"

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/drwright.schemas
%{_desktopdir}/*.desktop
%{_datadir}/drwright
