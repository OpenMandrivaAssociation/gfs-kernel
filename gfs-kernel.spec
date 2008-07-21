%define name gfs-kernel
%define version 2.6.9
%define pre cvs
%define release  %mkrel 3
%define rkernel %(/bin/bash ~/rpm/SOURCES/get_version.sh)

Summary: gfs-kernel The Global File System kernel modules
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}-%pre.tar.bz2
Source1: get_version.sh
Patch1: gfs-Makefile.patch.bz2
Patch0: configure_kernel.patch
License: GPL
Group: System
#Url: 
Buildrequires: dlm-kernel, iddev, gulm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
requires: kernel-source

%description
GFS - The Global File System is a symmetric, shared-disk, cluster file
system.

%package -n %name-%{rkernel}
Summary: gfs-kernel The Global File System kernel modules
requires: kernel
Group: System/Kernel and Hardware

%description -n %name-%{rkernel}
gfs-kernel The Global File System kernel modules

%prep
%setup -q -n %{name}-%{version}-%pre
%patch -p0
%patch1 -p0

%build
./configure --incdir=%{_includedir} \
	--kernel_src=/usr/src/linux \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--sbindir=%{_sbindir} \
	--module_dir=/lib/modules/%{rkernel}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%post -n %name-%{rkernel}
depmod -a -F /boot/System.map-%{rkernel} %{rkernel}

%postun -n %name-%{rkernel}
depmod -a -F /boot/System.map-%{rkernel} %{rkernel}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_includedir}/linux
%doc

%files -n %name-%{rkernel}
/lib/modules/*


