%define module	nifti

Summary:	Pythonic access to NIfTI and ANALYZE files 

Name:		python-%{module}
Version:	0.20100607.1
Release:	4
Source0:	http://sourceforge.net/projects/niftilib/files/pynifti/0.20100607.1/pynifti_0.20100607.1.tar.gz
Patch0:		pynifti-0.20100607.1_drop_noundef.patch
License:	BSD
Group:		Development/Python
Url:		http://niftilib.sourceforge.net/pynifti
BuildRequires:	swig
BuildRequires:	nifti-devel
BuildRequires:	python-numpy-devel
BuildRequires:	pkgconfig(lapack)
Requires:	python-numpy
BuildRequires:  python-devel

%description
The PyNIfTI module is a Python interface to the NIfTI I/O libraries.
Using PyNIfTI, one can easily read and write NIfTI and ANALYZE images from
within Python. The NiftiImage class provides pythonic access to the full
header information and for a maximum of interoperability the image data
is made available via NumPy arrays.

%prep
%setup -q -n py%{module}-%{version}
%patch0 -p1

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%files -f FILELIST


