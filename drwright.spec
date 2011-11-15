Summary:	A program that reminds you to take wrist breaks
Summary(pl.UTF-8):	Program przypominający, żeby dać odpocząć nadgarstkom
Name:		drwright
Version:	3.2.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/drwright/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	082bef2e925b7be677a35e32970b64ef
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-settings-daemon-devel >= 3.0.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	gnome-control-center >= 3.0.0
Requires:	gnome-settings-daemon >= 3.0.0
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DrWright is a program that forces you to take wrist breaks to rest
your hands.

%description -l pl.UTF-8
DrWright to program zmuszający do rozluźnienia nadgarstków, aby dać
odpocząć dłoniom.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/control-center-1/panels/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/*.la

# already exists as zu
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/tmp

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/control-center-1/panels/libdrwrightccp.so
%dir %{_libdir}/drwright
%attr(755,root,root) %{_libdir}/drwright/gnome-typing-monitor
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libtyping-break.so
%{_libdir}/gnome-settings-daemon-3.0/typing-break.gnome-settings-plugin
%{_desktopdir}/gnome-typing-break-panel.desktop
%{_datadir}/drwright
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.typing-break.gschema.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
