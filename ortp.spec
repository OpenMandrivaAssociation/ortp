%define major 15
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define _disable_rebuild_configure 1

Summary:	Real-time Transport Protocol Stack
Name:		ortp
Version:	5.1.61
Release:	1
License:	LGPLv2+
Group:		Communications
Url:		https://linphone.org/
Source0:	https://gitlab.linphone.org/BC/public/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
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

#---------------------------------------------------------------------------

%package -n	%{libname}
Summary:	Real-time Transport Protocol Stack
Group:		System/Libraries

%description -n	%{libname}
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

%files -n %{libname}
%{_libdir}/libortp.so.%{major}*

#---------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Headers, libraries and docs for the oRTP library
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains header files and development libraries needed to
develop programs using the oRTP library.

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_libdir}/cmake/ortp

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake \
	-DENABLE_STATIC:BOOL=NO \
	-DENABLE_STRICT:BOOL=NO \
	-DENABLE_DOC:BOOL=NO \
	-G Ninja
%ninja_build

%install
%ninja_install -C build
rm -rf %{buildroot}%{_docdir}

