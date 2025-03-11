#
# Conditional build:
%bcond_without	tests	# unit tests

%define 	module	pyscard
Summary:	A framework for building smart card aware applications in Python 3
Summary(pl.UTF-8):	Szkielet do tworzenia w Pythonie 3 aplikacji wykorzystujących karty procesorowe
Name:		python3-%{module}
Version:	2.0.7
Release:	3
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	https://downloads.sourceforge.net/pyscard/pyscard-%{version}.tar.gz
# Source0-md5:	9b58a6327e41dd8c7c72fa0211e7067f
URL:		https://sourceforge.net/projects/pyscard/
BuildRequires:	pcsc-lite-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	swig-python >= 2
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
Requires:	python3-modules >= 1:3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pyscard smartcard library is a framework for building smart card
aware applications in Python. The smartcard module is built on top of
the PCSC API Python wrapper module.

%description -l pl.UTF-8
Biblioteka pyscard smartcard to szkielet do tworzenia w Pythonie
aplikacji wykorzystujących karty procesorowe. Moduł smartcard jest
zbudowany w oparciu o moduł Pythona obudowujący API PCSC.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -a smartcard/Examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
find $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version} -name '*.py' \
	| xargs sed -i '1s|^#!.*env python3|#!%{__python3}|'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS ChangeLog README.md TODO
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
%{py3_sitedir}/smartcard/wx/resources
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
