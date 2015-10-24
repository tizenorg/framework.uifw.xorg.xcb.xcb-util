Name:    xcb-util
Summary: utility libraries for X C Binding
Version: 0.3.9.1
Release: 1
Group:   System/Libraries
License: MIT
URL:     http://xcb.freedesktop.org/
Source: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(xorg-macros)
BuildRequires: libxcb-devel >= 1.4, m4
BuildRequires: pkgconfig(xproto)
BuildRequires: gperf
Provides:	xcb-renderutil

%description
Description: %{summary}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package 	devel
Summary:	Development and header files for xcb-util
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}, pkgconfig

%description	devel
Development files for xcb-util.

%prep
%setup -q

%build

./autogen.sh
%reconfigure --disable-static

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%remove_docs

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_libdir}/libxcb-util.so.1*
/usr/share/license/%{name}

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h


