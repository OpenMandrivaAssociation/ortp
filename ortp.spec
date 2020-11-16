%define major 15
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define _disable_rebuild_configure 1

Summary:	Real-time Transport Protocol Stack
Name:		ortp
Version:	4.4.8
Release:	1
License:	LGPLv2+
Group:		Communications
Url:		https://gitlab.linphone.org/BC/public/ortp
Source0:	https://gitlab.linphone.org/BC/public/ortp/-/archive/%{version}/ortp-%{version}.tar.bz2
Patch0:		ortp-4.4.6-cmake-fix-pkgconfig-pc-file.patch
BuildRequires:	cmake
BuildRequires:	ninja
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
%autosetup -p1
%cmake \
	-DENABLE_STATIC:BOOL=NO \
	-DENABLE_STRICT:BOOL=NO \
	-DENABLE_DOC:BOOL=NO \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
rm -rf %{buildroot}%{_docdir}

%files -n %{libname}
%{_libdir}/libortp.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_libdir}/cmake/ortp
