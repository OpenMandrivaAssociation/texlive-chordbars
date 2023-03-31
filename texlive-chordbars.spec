Name:		texlive-chordbars
Version:	49569
Release:	2
Summary:	Print chord grids for pop/jazz tunes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chordbars
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chordbars.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chordbars.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This Tikz-based music-related package is targeted at pop/jazz
guitar/bass/piano musicians. They usually need only the chords
and the song structure. This package produces rectangular song
patterns with "one square per bar", with the chord shown inside
the square. It also handles the song structure by showing the
bar count and the repetitions of the patterns.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/chordbars
%doc %{_texmfdistdir}/doc/latex/chordbars

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
