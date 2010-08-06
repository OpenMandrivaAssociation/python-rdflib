%define oname rdflib
#gw please don't upgrade to 3.0 as it is not API compatible
%define version 2.4.0
%define rel 1

Summary: Python library for working with RDF
Name: python-%{oname}
Version: %{version}
Release: %mkrel %rel
Source0: %{oname}-%{version}.tar.gz
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-setuptools
Url: http://rdflib.net/

%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information.

The library contains parsers and serializers for RDF/XML, N3,
NTriples, Turtle, TriX and RDFa . The library presents a Graph
interface which can be backed by any one of a number of Store
implementations, including, Memory, MySQL, Redland, SQLite, Sleepycat
and SQLObject.  If you have recently reported a bug marked as fixed,
or have a craving for the very latest, you may want the development
version instead: http://rdflib.googlecode.com/svn/trunk#egg=rdflib-dev

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT
rm -rf %buildroot%py_platsitedir/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/rdfpipe
%py_platsitedir/%oname
%py_platsitedir/rdflib_tools
%py_platsitedir/*.egg-info
