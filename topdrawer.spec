Summary:	A program for drawing physics graphs
Name:		topdrawer
Version:	5.12.14c
Release:	1
License:	Free
Group:		X11/Applications/Science
Source0:	ftp://iris.riken.go.jp/pub/topdrawer/topdrawer-all.tar.gz
BuildRequires:	X11-devel
BuildRequires:	gcc-g77
#Requires:	ugs >= 2.10d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Topdrawer is a keyword-driven interface designed to produce physics
graphs with minimal specifications.  It uses UGS (Unified Graphics
System) also developed at SLAC.

%prep
%setup -n topdrawer -q
sed -i -e 's@UGS = .*@UGS = -lugs@;s@FLAGS  = -O2@FLAGS  = -O0@' \
	Imakefile.def
sed -i -e \
	"s@topdrawer.gih@/usr/doc/topdrawer-%%{PACKAGE_VERSION}/doc/topdrawer4.0.gih@" \
	src/help_.c
rm -f doc/doc2gih doc/doc2tex

%build
xmkmf
%{__make} Makefiles
%{__make} clean
%{__make}

#%{__make} FC=g77 FFLAGS='-O2 -fno-automatic -finit-local-zero'

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install td $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* HINTS doc examples contrib
%attr(755,root,root) %{_bindir}/*
