Summary:	Library to create components for Wayland using the Layer Shell
Name:		gtk-layer-shell
Version:	0.5.2
Release:	1
License:	LGPL v3+, MIT
Group:		Development/Libraries
Source0:	https://github.com/wmww/gtk-layer-shell/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ae70cd53ada2b1b4fb77aaba754fec35
URL:		https://github.com/wmww/gtk-layer-shell
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	meson >= 0.45.1
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	wayland-devel >= 1.10.0
BuildRequires:	wayland-protocols >= 1.16
Requires:	gtk+3 >= 3.22.0
Requires:	wayland >= 1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to write GTK applications that use Layer Shell. Layer Shell
is a Wayland protocol for desktop shell components, such as panels,
notifications and wallpapers. You can use it to anchor your windows to
a corner or edge of the output, or stretch them across the entire
output. This library only makes sense on Wayland compositors that
support Layer Shell, and will not work on X11. It supports all Layer
Shell features including popups and popovers (GTK popups Just Work™).
Please open issues for any bugs you come across.


%package devel
Summary:	Header files for gtk-layer-shell library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gtk-layer-shell library.

%package static
Summary:	Static gtk-layer-shell library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtk-layer-shell library.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libgtk-layer-shell.so.*.*.*
%ghost %{_libdir}/libgtk-layer-shell.so.0
%{_libdir}/girepository-1.0/GtkLayerShell-0.1.typelib

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgtk-layer-shell.so
%dir %{_includedir}/gtk-layer-shell
%{_includedir}/gtk-layer-shell/gtk-layer-shell.h
%{_pkgconfigdir}/gtk-layer-shell-0.pc
%{_datadir}/gir-1.0/GtkLayerShell-0.1.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtk-layer-shell.a
