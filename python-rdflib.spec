%define oname rdflib

Summary:	Python library for working with RDF
Name:		python-%{oname}
Version:	7.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/42/ff/00084798ba8d21f9e79044c4b8e56d0fca4bb7dd428ae693bcbfdbaa4a06/rdflib-%{version}.tar.gz
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://rdflib.net/
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(pyparsing)
BuildRequires:	python%{pyver}dist(wheel)

%description
RDFLib is a Python library for working with RDF, a simple yet
powerful language for representing information.

%files
%license LICENSE
%doc README.md examples
%{_bindir}/csv2rdf
%{_bindir}/rdf2dot
%{_bindir}/rdfgraphisomorphism
%{_bindir}/rdfpipe
%{_bindir}/rdfs2dot
%{_bindir}/sparqlquery
%{python_sitelib}/rdflib
%{python_sitelib}/rdflib-%{version}.dist-info

