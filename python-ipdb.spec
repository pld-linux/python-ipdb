%define 	module	ipdb
Summary:	IPython-enabled pdb
Name:		python-%{module}
%define		ver 0.1dev
%define		svn_rev	1716
Version:	%{ver}
Release:	0.r%{svn_rev}.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/i/ipdb/ipdb-%{ver}-r%{svn_rev}.tar.gz
# Source0-md5:	21354e9d4c7fd87908d543418de0d131
URL:		http://pypi.python.org/pypi/ipdb/
BuildRequires:	python
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows to use: 'from ipdb import set_trace; set_trace()'

You then get all the nice stuff from IPython (tab completion, nice tracebacks)
right in pdb.

%prep
%setup -q -n %{module}-%{ver}-r%{svn_rev}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
