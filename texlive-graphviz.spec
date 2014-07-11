# revision 31517
# category Package
# catalog-ctan /macros/latex/contrib/graphviz
# catalog-date 2013-08-26 01:14:13 +0200
# catalog-license lppl1.3
# catalog-version 0.94
Name:		texlive-graphviz
Version:	0.94
Release:	8
Summary:	Write graphviz (dot+neato) inline in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/graphviz
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphviz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphviz.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphviz.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows inline use of graphviz code, in a LaTeX
document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/graphviz/graphviz.sty
%doc %{_texmfdistdir}/doc/latex/graphviz/LICENSE
%doc %{_texmfdistdir}/doc/latex/graphviz/Makefile
%doc %{_texmfdistdir}/doc/latex/graphviz/README
%doc %{_texmfdistdir}/doc/latex/graphviz/README.md
%doc %{_texmfdistdir}/doc/latex/graphviz/graphviz.pdf
%doc %{_texmfdistdir}/doc/latex/graphviz/test/Makefile
%doc %{_texmfdistdir}/doc/latex/graphviz/test/body.tex
%doc %{_texmfdistdir}/doc/latex/graphviz/test/pdf-singlefile-tmpdir.tex
%doc %{_texmfdistdir}/doc/latex/graphviz/test/pdf-singlefile.tex
%doc %{_texmfdistdir}/doc/latex/graphviz/test/pdf-tmpdir.tex
%doc %{_texmfdistdir}/doc/latex/graphviz/test/pdf.tex
%doc %{_texmfdistdir}/doc/latex/graphviz/test/ps.tex
#- source
%doc %{_texmfdistdir}/source/latex/graphviz/graphviz.dtx
%doc %{_texmfdistdir}/source/latex/graphviz/graphviz.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
