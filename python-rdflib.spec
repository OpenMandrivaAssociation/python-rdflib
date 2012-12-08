%define oname rdflib
%define version 3.1.0
%define release %mkrel 2

Summary:	Python library for working with RDF
Name:		python-%{oname}
Version:	%{version}
Release:	%{release}
Source0:	%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools
Url:		http://rdflib.net/

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
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
%__rm -rf %{buildroot}%{py_platsitedir}/test

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc CHANGELOG LICENSE README examples/


%changelog
* Wed Nov 02 2011 Götz Waschk <waschk@mandriva.org> 3.1.0-2mdv2012.0
+ Revision: 711831
- rebuild

* Wed Aug 10 2011 Lev Givon <lev@mandriva.org> 3.1.0-1
+ Revision: 693853
- Update to 3.1.0.

* Mon Nov 01 2010 Götz Waschk <waschk@mandriva.org> 2.4.2-3mdv2011.0
+ Revision: 591518
- rebuild for python 2.7

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Thu Oct 07 2010 Götz Waschk <waschk@mandriva.org> 2.4.2-1mdv2011.0
+ Revision: 583931
- update to new version 2.4.2

* Fri Aug 06 2010 Götz Waschk <waschk@mandriva.org> 2.4.0-1mdv2011.0
+ Revision: 566625
- downgrade to 2.4.0
- update file list
- no more noarch

* Fri Aug 06 2010 Götz Waschk <waschk@mandriva.org> 3.0.0-1mdv2011.0
+ Revision: 566599
- import python-rdflib


