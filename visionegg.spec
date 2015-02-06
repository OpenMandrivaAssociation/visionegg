Summary:	Python library for producing stimuli for vision research experiments
Name:		visionegg
Version:	1.2.1
Release:	5
Source0:	%{name}-%{version}.tar.gz
License:	LGPL
Group:		Sciences/Other
Url:		http://www.visionegg.org/
Obsoletes:	visionegg-demos
Requires:	python-numpy >= 1.0
Requires:	python-imaging >= 1.1.2
Requires:	python-opengl >= 2.0
Requires:	pygame >= 1.5.3
BuildRequires:	python-setuptools, pkgconfig(x11), GL-devel, python-numpy-devel >= 1.0
BuildRequires:	python-devel
BuildRequires:  pkgconfig(lapack)

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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --skip-build --root=%{buildroot} --record=FILELIST
sed -i 's/.*egg-info$//' FILELIST

%files -f FILELIST
%defattr(-,root,root)
%doc *.txt doc/ demo/


%changelog
* Sun Oct 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2.1-2mdv2011.0
+ Revision: 590946
- rebuild for python-2.7
- drop the obsolete %%py_requires macro and use python-devel instead

* Tue Mar 09 2010 Lev Givon <lev@mandriva.org> 1.2.1-1mdv2010.1
+ Revision: 517186
- Update to 1.2.1.

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.1.1-3mdv2010.0
+ Revision: 445695
- rebuild

* Sat Jan 10 2009 Funda Wang <fwang@mandriva.org> 1.1.1-2mdv2009.1
+ Revision: 327906
- rebuild

* Fri Nov 07 2008 Lev Givon <lev@mandriva.org> 1.1.1-1mdv2009.1
+ Revision: 300409
- Update to 1.1.1.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0-7mdv2009.0
+ Revision: 255561
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0-5mdv2008.1
+ Revision: 140929
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Jan 23 2007 Lev Givon <lev@mandriva.org> 1.0-5mdv2007.0
+ Revision: 112489
- Add build dependencies.
- Wrong dependency.
- Fix Python build dependencies.
- Accomodate different Python versions.
- Patch to make installation more FHS compliant.
- Fix dependencies, include demos in separate subpackage,
  install system directory in FHS-compliant location.
- Import visionegg

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Rebuild against new python

* Mon May 01 2006 Emmanuel Blindauer <blindauer@mandriva.org> 1.0-3mdk
- fix ExclusiveArch

* Mon Jan 23 2006 Lev Givon <lev@mandriva.org> 1.0-2mdk
- Build correctly on x86_64.

* Thu Jan 19 2006 Lev Givon <lev@mandriva.org> 1.0-1mdk
- Initial Mandriva package.

