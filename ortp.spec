%define major 13
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define _disable_rebuild_configure 1

Summary:	Real-time Transport Protocol Stack
Name:		ortp
Version:	1.0.2
Release:	1
License:	LGPLv2+
Group:		Communications
Url:		http://linphone.org/ortp/
Source0:	https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
# (wally) fix pkconfig pc file when cmake is used
Patch0:		ortp-1.0.2-cmake-fix-pkgconfig-pc-file.patch
# (wally) alow overriding cmake config file location from cmd line
Patch1:		ortp-1.0.2-cmake-config-location.patch
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	pkgconfig(openssl)
BuildRequires:	bctoolbox-static-devel

%description
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

%package -n	%{libname}
Summary:	Real-time Transport Protocol Stack
Group:		System/Libraries

%description -n	%{libname}
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

%package -n	%{devname}
Summary:	Headers, libraries and docs for the oRTP library
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains header files and development libraries needed to
develop programs using the oRTP library.

%prep
%setup -qn %{name}-%{version}-0
%apply_patches

%build
export CC=gcc
export CXX=g++
%cmake \
  -DENABLE_STATIC=NO \
  -DENABLE_STRICT:BOOL=NO \
  -DENABLE_DOC:BOOL=NO \
  -DCONFIG_PACKAGE_LOCATION:PATH=%{_libdir}/cmake/oRTP

%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libortp.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog NEWS README.md
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_libdir}/cmake/oRTP/
%{_docdir}/%{name}-%{version}

