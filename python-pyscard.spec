#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pyscard
Summary:	A framework for building smart card aware applications in Python 2
Summary(pl.UTF-8):	Szkielet do tworzenia w Pythonie 2 aplikacji wykorzystujących karty procesorowe
Name:		python-%{module}
Version:	1.9.6
Release:	3
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	https://downloads.sourceforge.net/pyscard/pyscard-%{version}.tar.gz
# Source0-md5:	079343dbc469330e74dee8924bc8944e
URL:		https://sourceforge.net/projects/pyscard/
BuildRequires:	pcsc-lite-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	swig-python >= 2
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pyscard smartcard library is a framework for building smart card
aware applications in Python. The smartcard module is built on top of
the PCSC API Python wrapper module.

%description -l pl.UTF-8
Biblioteka pyscard smartcard to szkielet do tworzenia w Pythonie
aplikacji wykorzystujących karty procesorowe. Moduł smartcard jest
zbudowany w oparciu o moduł Pythona obudowujący API PCSC.

%package -n python3-%{module}
Summary:	A framework for building smart card aware applications in Python 3
Summary(pl.UTF-8):	Szkielet do tworzenia w Pythonie 3 aplikacji wykorzystujących karty procesorowe
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
The pyscard smartcard library is a framework for building smart card
aware applications in Python. The smartcard module is built on top of
the PCSC API Python wrapper module.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka pyscard smartcard to szkielet do tworzenia w Pythonie
aplikacji wykorzystujących karty procesorowe. Moduł smartcard jest
zbudowany w oparciu o moduł Pythona obudowujący API PCSC.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
cp -a smartcard/Examples/* $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
find $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version} -name '*.py' \
	| xargs sed -i '1s|^#!.*python\b|#!%{__python}|'
%endif
%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -a smartcard/Examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
find $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version} -name '*.py' \
	| xargs sed -i '1s|^#!.*python\b|#!%{__python3}|'
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ACKS ChangeLog README* TODO
%dir %{py_sitedir}/smartcard
%{py_sitedir}/smartcard/*.py[co]
%dir %{py_sitedir}/smartcard/scard
%attr(755,root,root) %{py_sitedir}/smartcard/scard/*.so
%{py_sitedir}/smartcard/scard/*.py[co]
%dir %{py_sitedir}/smartcard/pcsc
%{py_sitedir}/smartcard/pcsc/*.py[co]
%dir %{py_sitedir}/smartcard/pyro
%{py_sitedir}/smartcard/pyro/*.py[co]
%dir %{py_sitedir}/smartcard/reader
%{py_sitedir}/smartcard/reader/*.py[co]
%dir %{py_sitedir}/smartcard/sw
%{py_sitedir}/smartcard/sw/*.py[co]
%dir %{py_sitedir}/smartcard/util
%{py_sitedir}/smartcard/util/*.py[co]
%dir %{py_sitedir}/smartcard/wx
%{py_sitedir}/smartcard/wx/*.py[co]
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ACKS ChangeLog README* TODO
%dir %{py3_sitedir}/smartcard
%{py3_sitedir}/smartcard/*.py
%{py3_sitedir}/smartcard/__pycache__
%dir %{py3_sitedir}/smartcard/pcsc
%{py3_sitedir}/smartcard/pcsc/*.py
%{py3_sitedir}/smartcard/pcsc/__pycache__
%dir %{py3_sitedir}/smartcard/pyro
%{py3_sitedir}/smartcard/pyro/*.py
%{py3_sitedir}/smartcard/pyro/__pycache__
%dir %{py3_sitedir}/smartcard/reader
%{py3_sitedir}/smartcard/reader/*.py
%{py3_sitedir}/smartcard/reader/__pycache__
%dir %{py3_sitedir}/smartcard/scard
%attr(755,root,root) %{py3_sitedir}/smartcard/scard/_scard.*.so
%{py3_sitedir}/smartcard/scard/*.py
%{py3_sitedir}/smartcard/scard/__pycache__
%dir %{py3_sitedir}/smartcard/sw
%{py3_sitedir}/smartcard/sw/*.py
%{py3_sitedir}/smartcard/sw/__pycache__
%dir %{py3_sitedir}/smartcard/util
%{py3_sitedir}/smartcard/util/*.py
%{py3_sitedir}/smartcard/util/__pycache__
%dir %{py3_sitedir}/smartcard/wx
%{py3_sitedir}/smartcard/wx/*.py
%{py3_sitedir}/smartcard/wx/__pycache__
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif
