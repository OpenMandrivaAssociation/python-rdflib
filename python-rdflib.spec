%define oname rdflib

Summary:	Python library for working with RDF
Name:		python-%{oname}
Version:	3.1.0
Release:	4
License:	BSD
Group:		Development/Python
Url:		http://rdflib.net/
Source0:	%{oname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools

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
%setup -qn %{oname}-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
%__rm -rf %{buildroot}%{py_platsitedir}/test

%files -f FILE_LIST
%doc CHANGELOG LICENSE README examples/

