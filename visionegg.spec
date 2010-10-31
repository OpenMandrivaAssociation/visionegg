%define name	visionegg
%define version 1.2.1
%define release %mkrel 2

Summary:	Python library for producing stimuli for vision research experiments
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	LGPL
Group:		Sciences/Other
Url:		http://www.visionegg.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	visionegg-demos
Requires:	python-numpy >= 1.0
Requires:	python-imaging >= 1.1.2
Requires:	python-opengl >= 2.0
Requires:	pygame >= 1.5.3
BuildRequires:	python-setuptools, libx11-devel, GL-devel, python-numpy-devel >= 1.0
BuildRequires:	python-devel

%description 
The Vision Egg uses Python and OpenGL to provide a powerful, flexible,
and free way to produce stimuli for vision research experiments. In
addition to methods for automatic generation of traditional visual
stimuli such as sinusoidal gratings and random dot patterns, it defines a
number of functions for moving numeric data, images, movies, text, and
3D objects to and from your computer's video card and making use of 
features like perspective distortion. 

%prep
%setup -q

%build
CFLAGS="-L/usr/X11R6/%_lib" %__python setup.py build 

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --skip-build --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc *.txt doc/ demo/
