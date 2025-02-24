Name: python-abiword
Version: 0.8.0
Release: %mkrel 2
Summary: Python bindings for libabiword
License: GPL+
Group: Development/Python
Url: https://abisource.com/

Source: http://www.abisource.com/downloads/pyabiword/%{version}/pyabiword-%{version}.tar.gz
Patch0: pyabiword-0.8.0-linkage.patch

Requires: abiword >= 2.8.0
Requires: python-gobject
Requires: pygtk2.0
%py_requires -d
BuildRequires: abiword-devel >= 2.8.0
BuildRequires: libglade2.0-devel
BuildRequires: python-gobject-devel  
BuildRequires: pygtk2.0-devel  
BuildRoot: %_tmppath/%name-%version-buildroot

%description
This package installs Python bindings for libabiword.

%prep
%setup -q -n pyabiword-%{version}
%patch0 -p0

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x am_cv_python_pyexecdir=%{python_sitelib}
%make

%install
rm -rf %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%{python_sitelib}/*
%{_datadir}/pygtk/2.0/defs/*.defs
%doc AUTHORS COPYING

