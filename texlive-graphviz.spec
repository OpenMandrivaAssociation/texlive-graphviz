%global tl_name graphviz
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.94
Release:	%{tl_revision}.1
Summary:	Write graphviz (dot+neato) inline in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/graphviz
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphviz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphviz.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphviz.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows inline use of graphviz code, in a LaTeX document.

