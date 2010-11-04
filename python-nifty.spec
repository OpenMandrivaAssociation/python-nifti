%define module	nifti
%define name	python-%{module}
%define version	0.20100607.1
%define release	%mkrel 2

Summary:	Pythonic access to NIfTI and ANALYZE files 
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://sourceforge.net/projects/niftilib/files/pynifti/0.20100607.1/pynifti_0.20100607.1.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://niftilib.sourceforge.net/pynifti
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	swig
BuildRequires:	nifti-devel
BuildRequires:	python-numpy-devel
Requires:	python-numpy
%py_requires -d

%description
The PyNIfTI module is a Python interface to the NIfTI I/O libraries.
Using PyNIfTI, one can easily read and write NIfTI and ANALYZE images from
within Python. The NiftiImage class provides pythonic access to the full
header information and for a maximum of interoperability the image data
is made available via NumPy arrays.

%prep
%setup -q -n py%{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
