%define fontname	stix
%define fontdir	 	%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Scientific and Technical Information Exchange fonts
Name:		fonts-otf-%{fontname}
Version:	1.0.0
Release:	4
Source0:	STIXv%{version}.zip
License:	OFLv1.1
Group:		System/Fonts/True type
Url:		https://www.stixfonts.org/
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
%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 Fonts/*.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}/%{fontdir}
mkfontdir %{buildroot}/%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%files
%doc License/*.pdf *.pdf
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*
