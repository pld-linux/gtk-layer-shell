#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	Library to create components for Wayland using the Layer Shell
Summary(pl.UTF-8):	Biblioteka do tworzenia komponentów Waylanda przy użyciu protokołu Layer Shell
Name:		gtk-layer-shell
Version:	0.6.0
Release:	1
License:	LGPL v3+, MIT
Group:		Libraries
#Source0Download: https://github.com/wmww/gtk-layer-shell/releases
Source0:	https://github.com/wmww/gtk-layer-shell/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	33959717f3bbfdf05d68995105359431
URL:		https://github.com/wmww/gtk-layer-shell
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gtk+3-devel >= 3.22.0
%{?with_apidocs:BuildRequires:	gtk-doc}
BuildRequires:	meson >= 0.45.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpm-build >= 4.6
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
Shell features including popups and popovers (GTK popups Just Work
(TM)).

%description -l pl.UTF-8
Biblioteka do tworzenia aplikacji GTK, wykorzystujących protokół Layer
Shell. Jest to protokół Wayland dla komponentów powłok graficznych,
takich jak panele, powiadomienia i tapety. Można go używać do
zakotwiczania okien w roku lub przy brzegu wyjścia, albo rozciągania
ich na całe wyjście. Biblioteka ma sens tylko dla zarządców składania
Wayland obsługujących protokół Layer Shell, nie będzie działać na X11.
Obsługuje wszystkie możliwości protokołu Layer Shell, w tym
wyskakujące okna.

%package devel
Summary:	Header files for gtk-layer-shell library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gtk-layer-shell
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel >= 3.22.0
Requires:	wayland-devel >= 1.10.0

%description devel
Header files for gtk-layer-shell library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtk-layer-shell.

%package static
Summary:	Static gtk-layer-shell library
Summary(pl.UTF-8):	Biblioteka statyczna gtk-layer-shell
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtk-layer-shell library.

%description static -l pl.UTF-8
Biblioteka statyczna gtk-layer-shell.

%package apidocs
Summary:	API documentation for gtk-layer-shell library
Summary(pl.UTF-8):	Dokumentacja API biblioteki gtk-layer-shell
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for gtk-layer-shell library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gtk-layer-shell.

%prep
%setup -q

%build
%meson build \
	%{?with_apidocs:-Ddocs=true}

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
%doc CHANGELOG.md LICENSE_MIT.txt README.md compatibility.md
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

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtk-layer-shell
%endif
