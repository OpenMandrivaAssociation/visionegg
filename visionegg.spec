%define name visionegg
%define version 1.0
%define release %mkrel 5

Summary:   Python package for producing stimuli for vision research experiments
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source0:   %{name}-%{version}.tar.bz2
Patch0:	   visionegg-mandriva.patch
License:   LGPL
Group:     Sciences/Other
Url:       http://www.visionegg.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:  python >= 2.1
Requires:  python-numeric >= 21.0
Requires:  python-numarray 
Requires:  python-imaging >= 1.1.2
Requires:  python-opengl
Requires:  pygame
BuildRequires: python-devel >= 2.1
BuildRequires: libx11-devel, GL-devel, python-numeric-devel >= 21.0

%description 
The Vision Egg uses Python and OpenGL to provide a powerful, flexible,
and free way to produce stimuli for vision research experiments. In
addition to methods for automatic generation of traditional visual
stimuli such as sinusoidal gratings and random dot patterns, it defines a
number of functions for moving numeric data, images, movies, text, and
3D objects to and from your computer's video card and making use of 
features like perspective distortion. 

%package demos

Summary:  Demo programs for VisionEgg
Group:	  Sciences/Other
Requires: %{name}

%description demos
This package contains sample programs demonstrating the use of VisionEgg.

%prep
%setup -q
%patch -p0

%build
CFLAGS="-L/usr/X11R6/%_lib" %__python setup.py build 

%install
%__rm -rf %{buildroot}
%__python setup.py install --skip-build --root=%{buildroot} --record=INSTALLED_FILES
%__cp -rp ./demo %{buildroot}%py_libdir/VisionEgg/demo

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.txt README-DEMOS.txt CHANGELOG.txt LICENSE.txt README-BINARY-DEMOS.txt doc/

%files -n %{name}-demos
%defattr(-,root,root)
%py_libdir/VisionEgg/demo


