Summary:	Serbo-Croatian and Slovenian language pair for Apertium
Summary(pl.UTF-8):	Para języków serbsko-chorwacki i słoweński dla Apertium
%define	lpair	hbs-slv
Name:		apertium-dict-%{lpair}
Version:	0.5.0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	b382273d0a84b2b572fd39dcfae0940d
Patch0:		%{name}-cg-fix.patch
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	apertium-lex-tools
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox >= 3.2.0
BuildRequires:	pkgconfig
BuildRequires:	vislcg3
Requires:	apertium >= 3.2.0
Requires:	apertium-lex-tools
Requires:	lttoolbox >= 3.2.0
Requires:	vislcg3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between Serbo-Croatian and Slovenian, morphological analysis or
part-of-speech tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między serbsko-chorwackim a słoweńskim, a także analizy morfologicznej
lub oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apertium/modes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed here (see modes subdir) and contain wrong (builddir) paths
%{__rm} $RPM_BUILD_ROOT%{_datadir}/apertium/apertium-%{lpair}/*.mode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/hbs-slv.mode
%{_datadir}/apertium/modes/slv-hbs_BS.mode
%{_datadir}/apertium/modes/slv-hbs_HR.mode
%{_datadir}/apertium/modes/slv-hbs_SR.mode
