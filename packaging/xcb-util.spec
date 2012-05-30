Name:       xcb-util
Summary:    utility libraries for X C Binding
Version:    0.3.6
Release:    0
Group:      System/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.gz
Source1001: packaging/xcb-util.manifest 

BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-shm)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xproto)
BuildRequires: gperf


%description
Description: %{summary}



%package -n libxcb-atom
Summary:    utility libraries for X C Binding -- atom
Group:      System/Libraries
%description -n libxcb-atom
This package contains the library files needed to run software using
libxcb-atom, providing standard core X atom constants and atom caching.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n libxcb-atom-devel
Summary:    utility libraries for X C Binding -- atom
Group:      Development/Libraries
Requires:   libxcb-atom = %{version}-%{release}
Requires:   pkgconfig(xcb)
%description -n libxcb-atom-devel
This package contains the header and library files needed to build software
using libxcb-atom, providing standard core X atom constants and atom caching.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.


%package -n libxcb-aux
Summary:    utility libraries for X C Binding -- aux
Group:      System/Libraries
%description -n libxcb-aux
This package contains the library files needed to run software using
libxcb-aux, providing convenient access to connection setup and some
core requests.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n libxcb-aux-devel
Summary:    utility libraries for X C Binding -- aux
Group:      Development/Libraries
Requires:   libxcb-aux = %{version}-%{release}
Requires:   pkgconfig(xcb)
%description -n libxcb-aux-devel
This package contains the header and library files needed to build software
using libxcb-aux, providing convenient access to connection setup and some
core requests.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.


%package -n libxcb-event
Summary:    utility libraries for X C Binding -- event
Group:      System/Libraries
%description -n libxcb-event
This package contains the library files needed to run software using
libxcb-event, providing X callback event handling.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n libxcb-event-devel
Summary:    utility libraries for X C Binding -- event
Group:      Development/Libraries
Requires:   libxcb-event = %{version}-%{release}
Requires:   pkgconfig(xcb)
%description -n libxcb-event-devel
This package contains the header and library files needed to build software
using libxcb-event, providing X callback event handling.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.


%package -n libxcb-image
Summary:    utility libraries for X C Binding -- image
Group:      System/Libraries
%description -n libxcb-image
This package contains the library files needed to run software using
libxcb-image, providing port of Xlib's XImage and XShmImage functions.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n libxcb-image-devel
Summary:    utility libraries for X C Binding -- image
Group:      Development/Libraries
Requires:   libxcb-image = %{version}-%{release}
Requires:   pkgconfig(xcb)
%description -n libxcb-image-devel
This package contains the header and library files needed to build software
using libxcb-image, providing port of Xlib's XImage and XShmImage functions.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.


%package -n libxcb-keysyms
Summary:    utility libraries for X C Binding -- keysyms
Group:      System/Libraries
%description -n libxcb-keysyms
This package contains the library files needed to run software using
libxcb-keysyms, providing standard X key constants and conversion to/from
keycodes.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n libxcb-keysyms-devel
Summary:    utility libraries for X C Binding -- ekysyms
Group:      Development/Libraries
Requires:   libxcb-keysyms = %{version}-%{release}
Requires:   pkgconfig(xcb)
%description -n libxcb-keysyms-devel
This package contains the header and library files needed to build software
using libxcb-keysyms, providing standard X key constants and conversion to/from
keycodes.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.


%package -n libxcb-property
Summary:    utility libraries for X C Binding -- property
Group:      System/Libraries
%description -n libxcb-property
This package contains the library files needed to run software using
libxcb-property, providing callback X property-change handling.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n libxcb-property-devel
Summary:    utility libraries for X C Binding -- property
Group:      Development/Libraries
Requires:   libxcb-property = %{version}-%{release}
Requires:   libxcb-event-devel = %{version}-%{release}
Requires:   pkgconfig(xcb)
%description -n libxcb-property-devel
This package contains the header and library files needed to build software
using libxcb-property, providing callback X property-change handling.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.


%package -n libxcb-render-util
Summary:    utility libraries for X C Binding -- render-util
Group:      System/Libraries
%description -n libxcb-render-util
This package contains the library files needed to run software using
libxcb-render-util, providing convenience functions for the Render extension.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n libxcb-render-util-devel
Summary:    utility libraries for X C Binding -- render-util
Group:      Development/Libraries
Requires:   libxcb-render-util = %{version}-%{release}
Requires:   pkgconfig(xcb)
Requires:   pkgconfig(xcb-render)
%description -n libxcb-render-util-devel
This package contains the header and library files needed to build software
using libxcb-render-util, providing convenience functions for the Render
extension.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.


%package -n libxcb-reply
Summary:    utility libraries for X C Binding -- reply
Group:      System/Libraries
%description -n libxcb-reply
This package contains the library files needed to run software using
libxcb-reply.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n libxcb-reply-devel
Summary:    utility libraries for X C Binding -- reply
Group:      Development/Libraries
Requires:   libxcb-reply = %{version}-%{release}
Requires:   pkgconfig(xcb)
%description -n libxcb-reply-devel
This package contains the header and library files needed to build software
using libxcb-reply.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.


%package -n libxcb-icccm
Summary:    utility libraries for X C Binding -- icccm
Group:      System/Libraries
%description -n libxcb-icccm
This package contains the library files needed to run software using
libxcb-icccm, providing client and window-manager helpers for ICCCM.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n libxcb-icccm-devel
Summary:    utility libraries for X C Binding -- icccm 
Group:      Development/Libraries
Requires:   libxcb-icccm = %{version}-%{release}
Requires:   libxcb-atom-devel = %{version}-%{release}
Requires:   libxcb-property-devel = %{version}-%{release}
Requires:   pkgconfig(xcb)
%description -n libxcb-icccm-devel
This package contains the header and library files needed to build software
using libxcb-icccm, providing client and window-manager helpers for ICCCM.
.
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.


%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%reconfigure --disable-static

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install






%files -n libxcb-atom
%manifest xcb-util.manifest
/usr/lib/libxcb-atom.so.*

%files -n libxcb-atom-devel
%manifest xcb-util.manifest
/usr/include/xcb/xcb_atom.h
/usr/lib/libxcb-atom.so
/usr/lib/pkgconfig/xcb-atom.pc


%files -n libxcb-aux
%manifest xcb-util.manifest
/usr/lib/libxcb-aux.so.*

%files -n libxcb-aux-devel
%manifest xcb-util.manifest
/usr/include/xcb/xcb_aux.h
/usr/lib/libxcb-aux.so
/usr/lib/pkgconfig/xcb-aux.pc


%files -n libxcb-event
%manifest xcb-util.manifest
/usr/lib/libxcb-event.so.*

%files -n libxcb-event-devel
%manifest xcb-util.manifest
/usr/include/xcb/xcb_event.h
/usr/lib/libxcb-event.so
/usr/lib/pkgconfig/xcb-event.pc


%files -n libxcb-icccm
%manifest xcb-util.manifest
/usr/lib/libxcb-icccm.so.*

%files -n libxcb-icccm-devel
%manifest xcb-util.manifest
/usr/include/xcb/xcb_icccm.h
/usr/lib/libxcb-icccm.so
/usr/lib/pkgconfig/xcb-icccm.pc

%files -n libxcb-image
%manifest xcb-util.manifest
/usr/lib/libxcb-image.so.*

%files -n libxcb-image-devel
%manifest xcb-util.manifest
/usr/include/xcb/xcb_image.h
/usr/lib/libxcb-image.so
/usr/lib/pkgconfig/xcb-image.pc

%files -n libxcb-keysyms
%manifest xcb-util.manifest
/usr/lib/libxcb-keysyms.so.*

%files -n libxcb-keysyms-devel
%manifest xcb-util.manifest
/usr/include/xcb/xcb_keysyms.h
/usr/lib/libxcb-keysyms.so
/usr/lib/pkgconfig/xcb-keysyms.pc

%files -n libxcb-property
%manifest xcb-util.manifest
/usr/lib/libxcb-property.so.*

%files -n libxcb-property-devel
%manifest xcb-util.manifest
/usr/include/xcb/xcb_property.h
/usr/lib/libxcb-property.so
/usr/lib/pkgconfig/xcb-property.pc

%files -n libxcb-render-util
%manifest xcb-util.manifest
/usr/lib/libxcb-render-util.so.*

%files -n libxcb-render-util-devel
%manifest xcb-util.manifest
/usr/include/xcb/xcb_renderutil.h
/usr/lib/libxcb-render-util.so
/usr/lib/pkgconfig/xcb-renderutil.pc

%files -n libxcb-reply
%manifest xcb-util.manifest
/usr/lib/libxcb-reply.so.*

%files -n libxcb-reply-devel
%manifest xcb-util.manifest
/usr/include/xcb/xcb_reply.h
/usr/lib/libxcb-reply.so
/usr/lib/pkgconfig/xcb-reply.pc
%exclude /usr/include/xcb/xcb_bitops.h
%exclude /usr/include/xcb/xcb_pixel.h

