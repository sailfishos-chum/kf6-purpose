%global kf_version 6.28.0

Name:    kf6-purpose
Summary: Framework for providing abstractions to get the developer's purposes fulfilled
Version: 6.28.0
Release: 1%{?dist}

License: GPLv2 or GPLv3
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: %{name}-%{version}.tar.bz2

BuildRequires: kf6-extra-cmake-modules >= %{kf_version}
BuildRequires: kf6-rpm-macros

#Core Qml Gui Widgets Network Test

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
# optional
BuildRequires: cmake(Qt6DBus)

BuildRequires: kf6-kconfig-devel >= %{kf_version}
BuildRequires: kf6-kcoreaddons-devel >= %{kf_version}
BuildRequires: kf6-ki18n-devel >= %{kf_version}
BuildRequires: kf6-kio-devel >= %{kf_version}
BuildRequires: kf6-kirigami-devel >= %{kf_version}
BuildRequires: kf6-knotifications-devel >= %{kf_version}

%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
#Requires:       cmake(KF6CoreAddons)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/purpose.*
%{_kf6_libdir}/libKF6Purpose.so.*
%{_kf6_libdir}/libKF6PurposeWidgets.so.*
%{_kf6_plugindir}/purpose/
%dir %{_kf6_plugindir}/kfileitemaction/
%{_kf6_plugindir}/kfileitemaction/sharefileitemaction.so
%{_kf6_qmldir}/org/kde/purpose/
%{_kf6_datadir}/kf6/purpose/
%{_kf6_libexecdir}/purposeprocess
%{_datadir}/icons/hicolor/*/apps/*-purpose6.*

%files devel
%{_kf6_libdir}/libKF6Purpose.so
%{_kf6_libdir}/libKF6PurposeWidgets.so
%{_kf6_includedir}/Purpose/
%{_kf6_includedir}/PurposeWidgets/
%{_kf6_libdir}/cmake/KF6Purpose/
