%define		_snap 20060316
Summary:	A Java mail/news client
Summary(pl):	Napisany w Javie klient poczty/newsów
Name:		grendel
Version:	cvs
Release:	0.%{_snap}.1
License:	LGPL
Group:		Libraries
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	77d59a5174837c2b4339529b174e8793
#Source1:	http://wired.st-and.ac.uk/~hash9/grendel/%{name}-jar-pack-20051224.zip
Source1:	http://mirrors.trfenv.com/rlk/%{name}-jar-pack.zip
# NoSource1-md5:	9e6d2e6b2727151cbd07b79e9d8fbb70
# not sure about licenses, so NoSource for now
NoSource:	1
URL:		http://wiki.mozilla.org/Grendel
BuildRequires:	ant >= 1.6
BuildRequires:	java-activation
BuildRequires:	javamail
BuildRequires:	jdk >= 1.5.0
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	java >= 1.5.0
# JavaBeans Activation Framework (JAF) (http://java.sun.com/beans/glasgow/jaf.html)
# JavaMail (http://java.sun.com/products/javamail/)
# Netscape Directory SDK for Java (http://www.mozilla.org/directory/)
# ORO Matcher (http://www.savarese.org/oro/)
# MozCreator XUL Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grendel is the mail-news portion of the Xena project written in Java.
Its goal is to be a true cross-platform application with a feature set
that satisfies the poweruser.

%description -l pl
Grendel to czê¶æ pocztowo-newsowa projektu Xena napisana w Javie. Jej
celem jest bycie naprawdê przeno¶n± aplikacj± o mo¿liwo¶ciach
satysfakcjonuj±cych do¶wiadczonego u¿ytkownika.

%prep
%setup -qc
rm -f mozilla/grendel/extlib/rhino.jar
%{__unzip} -qd mozilla/grendel/extlib %{SOURCE1}

%build
cd mozilla/grendel

required_jars="mail activation jaxp_parser_impl"
export CLASSPATH=$(%{_bindir}/build-classpath $required_jars)

%ant build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
cd mozilla/grendel

# should make jar from dist/ with manifest but 'ant jar' doesn't exist.
%ant makeZip

install %{name}.zip $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
exec %{_bindir}/java -jar %{name}.jar
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/*.jar
