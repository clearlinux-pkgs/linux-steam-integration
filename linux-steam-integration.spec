#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x78E2387015C1205F (ikey@solus-project.com)
#
Name     : linux-steam-integration
Version  : 0.7.2
Release  : 14
URL      : https://github.com/solus-project/linux-steam-integration/releases/download/v0.7.2/linux-steam-integration-0.7.2.tar.xz
Source0  : https://github.com/solus-project/linux-steam-integration/releases/download/v0.7.2/linux-steam-integration-0.7.2.tar.xz
Source99 : https://github.com/solus-project/linux-steam-integration/releases/download/v0.7.2/linux-steam-integration-0.7.2.tar.xz.asc
Summary  : Common C library functions
Group    : Development/Tools
License  : LGPL-2.1
Requires: linux-steam-integration-bin = %{version}-%{release}
Requires: linux-steam-integration-data = %{version}-%{release}
Requires: linux-steam-integration-lib = %{version}-%{release}
Requires: linux-steam-integration-license = %{version}-%{release}
Requires: linux-steam-integration-locales = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32check)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(gtk+-3.0)
Patch1: 0001-Resync-po.patch
Patch2: 0002-intercept-Allow-disabling-build-time-the-udev-redire.patch
Patch3: 0003-Revert-intercept-Allow-disabling-build-time-the-udev.patch
Patch4: 0004-Add-new-snapd-pulseaudio-script-workaround.patch
Patch5: 0005-shim-When-in-snapd-mode-chdir-to-SNAP_USER_COMMON.patch
Patch6: 0006-redirect-Add-new-override-on-getpwuid.patch
Patch7: 0007-redirect-We-might-return-NULL-here.patch
Patch8: 0008-Fix-incorrect-snap-name-fixes-issue-50.patch
Patch9: 0009-shim-Remove-legacy-non-GLVND-path-support-for-snapd-.patch
Patch10: 0010-intercept-Support-new-sonames-in-Feral-s-Tomb-Raider.patch
Patch11: 0011-Add-StartupWMClass-to-lsi-steam.desktop.patch

%description
linux-steam-integration
-----------------------
Linux Steam* Integration is a helper system to make the Steam Client and Steam
games run better on Linux. In a nutshell, LSI automatically applies various workarounds
to get games working, and fixes long standing bugs in both games and the client.

%package bin
Summary: bin components for the linux-steam-integration package.
Group: Binaries
Requires: linux-steam-integration-data = %{version}-%{release}
Requires: linux-steam-integration-license = %{version}-%{release}

%description bin
bin components for the linux-steam-integration package.


%package data
Summary: data components for the linux-steam-integration package.
Group: Data

%description data
data components for the linux-steam-integration package.


%package lib
Summary: lib components for the linux-steam-integration package.
Group: Libraries
Requires: linux-steam-integration-data = %{version}-%{release}
Requires: linux-steam-integration-license = %{version}-%{release}

%description lib
lib components for the linux-steam-integration package.


%package lib32
Summary: lib32 components for the linux-steam-integration package.
Group: Default
Requires: linux-steam-integration-data = %{version}-%{release}
Requires: linux-steam-integration-license = %{version}-%{release}

%description lib32
lib32 components for the linux-steam-integration package.


%package license
Summary: license components for the linux-steam-integration package.
Group: Default

%description license
license components for the linux-steam-integration package.


%package locales
Summary: locales components for the linux-steam-integration package.
Group: Default

%description locales
locales components for the linux-steam-integration package.


%prep
%setup -q -n linux-steam-integration-0.7.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
pushd ..
cp -a linux-steam-integration-0.7.2 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545399215
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Dwith-steam-binary=/usr/bin/steam -Dwith-new-libcxx-abi=true -Dwith-frontend=true  builddir
ninja -v -C builddir
pushd ../build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="$ASFLAGS --32"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
meson --libdir=/usr/lib32 --prefix /usr --buildtype=plain -Dwith-steam-binary=/usr/bin/steam -Dwith-new-libcxx-abi=true -Dwith-frontend=true -Dwith-shim=none -Dwith-new-libcxx-abi=true -Dwith-frontend=false builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/linux-steam-integration
cp LICENSE %{buildroot}/usr/share/package-licenses/linux-steam-integration/LICENSE
cp src/libnica/LICENSE.LGPL2.1 %{buildroot}/usr/share/package-licenses/linux-steam-integration/src_libnica_LICENSE.LGPL2.1
pushd ../build32
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang linux-steam-integration

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lsi-exec
/usr/bin/lsi-settings
/usr/bin/steam

%files data
%defattr(-,root,root,-)
/usr/share/applications/lsi-settings.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblsi-intercept.so
/usr/lib64/liblsi-redirect.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/liblsi-intercept.so
/usr/lib32/liblsi-redirect.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/linux-steam-integration/LICENSE
/usr/share/package-licenses/linux-steam-integration/src_libnica_LICENSE.LGPL2.1

%files locales -f linux-steam-integration.lang
%defattr(-,root,root,-)

