#define git 0
%undefine _debugsource_packages

Name: lxqt-wayland-session
Version: 0.3.0
%if 0%{?git:1}
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: https://github.com/lxqt/lxqt-wayland-session/releases/download/%{version}/lxqt-wayland-session-%{version}.tar.xz
%endif
Summary: Session manager for the LXQt desktop
URL: https://lxqt-project.org/
License: GPL
Group: Graphical desktop/KDE
BuildSystem: cmake
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(qt6xdg) >= 3.9.1
BuildRequires: cmake(qtxdg-tools) >= 4.0.0
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: cmake(LayerShellQt)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libproc2)
BuildRequires: xdg-user-dirs
Requires: xdg-utils
Requires: qtxdg-tools
Requires: xdg-user-dirs
# dbus-launch is used by startlxqt
Requires: dbus-x11
# lxqt-session uses dbus-update-activiation-environment
Requires: dbus-tools
# workaround for missing icons in desktop files on lxqt desktop
Requires: sed
Requires: plasma6-breeze
Requires: kf6-breeze-icons

%description
Wayland session manager for the LXQt desktop.

%prep
%if 0%{?git:1}
%autosetup -p1 -n %{name}-%{git}
%else
%autosetup -p1
%endif

%files
%{_bindir}/lxqt-qdbus
%{_bindir}/startlxqtwayland
%{_datadir}/lxqt/graphics/*
%{_datadir}/lxqt/wallpapers/*
%{_datadir}/lxqt/wayland
%{_datadir}/themes/Vent
%{_datadir}/themes/Vent-dark
%{_datadir}/wayland-sessions/lxqt-wayland.desktop
%{_mandir}/man1/lxqt-wayland-session.1*
%{_mandir}/man1/startlxqtwayland.1*
