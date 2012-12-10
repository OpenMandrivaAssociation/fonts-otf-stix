%define fontname	stix
%define name		fonts-otf-%{fontname}
%define version		1.0.0
%define release		%mkrel 2

%define fontdir	 	%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Scientific and Technical Information Exchange fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	STIXv%{version}.zip
License:	OFLv1.1
Group:		System/Fonts/True type
Url:		http://www.stixfonts.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	mkfontscale, mkfontdir

%description
The mission of the Scientific and Technical Information Exchange
(STIX) font creation project is the preparation of a comprehensive set
of fonts that serve the scientific and engineering community in the
process from manuscript creation through final publication, both in
electronic and print formats. Toward this purpose, the STIX fonts will
be made available, under royalty-free license, to anyone, including
publishers, software developers, scientists, students, and the general
public.

The STIX mission will be fully realized when:

* Fully hinted PostScript Type 1 and TrueType font sets have been created
* All characters/glyphs have been incorporated into Unicode
  representation or comparable representation and browsers include
  program logic to fully utilize the STIX font set in the electronic
  representation of scholarly scientific documents


%prep
%setup -q -n STIXv%{version}

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 Fonts/*.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}/%{fontdir}
mkfontdir %{buildroot}/%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc License/*.pdf *.pdf
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 675512
- br fontconfig for fc-query used in new rpm-setup-build

* Tue Dec 14 2010 Lev Givon <lev@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 621817
- import fonts-otf-stix


