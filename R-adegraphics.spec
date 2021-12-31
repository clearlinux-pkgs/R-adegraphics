#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-adegraphics
Version  : 1.0.16
Release  : 36
URL      : https://cran.r-project.org/src/contrib/adegraphics_1.0-16.tar.gz
Source0  : https://cran.r-project.org/src/contrib/adegraphics_1.0-16.tar.gz
Summary  : An S4 Lattice-Based Package for the Representation of
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RColorBrewer
Requires: R-ade4
Requires: R-latticeExtra
Requires: R-sp
BuildRequires : R-Guerry
BuildRequires : R-RColorBrewer
BuildRequires : R-ade4
BuildRequires : R-latticeExtra
BuildRequires : R-sp
BuildRequires : R-spdep
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n adegraphics
cd %{_builddir}/adegraphics

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640884642

%install
export SOURCE_DATE_EPOCH=1640884642
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegraphics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegraphics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegraphics
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc adegraphics || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/adegraphics/CITATION
/usr/lib64/R/library/adegraphics/DESCRIPTION
/usr/lib64/R/library/adegraphics/INDEX
/usr/lib64/R/library/adegraphics/Meta/Rd.rds
/usr/lib64/R/library/adegraphics/Meta/features.rds
/usr/lib64/R/library/adegraphics/Meta/hsearch.rds
/usr/lib64/R/library/adegraphics/Meta/links.rds
/usr/lib64/R/library/adegraphics/Meta/nsInfo.rds
/usr/lib64/R/library/adegraphics/Meta/package.rds
/usr/lib64/R/library/adegraphics/Meta/vignette.rds
/usr/lib64/R/library/adegraphics/NAMESPACE
/usr/lib64/R/library/adegraphics/R/adegraphics
/usr/lib64/R/library/adegraphics/R/adegraphics.rdb
/usr/lib64/R/library/adegraphics/R/adegraphics.rdx
/usr/lib64/R/library/adegraphics/doc/adegraphics.R
/usr/lib64/R/library/adegraphics/doc/adegraphics.Rmd
/usr/lib64/R/library/adegraphics/doc/adegraphics.html
/usr/lib64/R/library/adegraphics/doc/index.html
/usr/lib64/R/library/adegraphics/help/AnIndex
/usr/lib64/R/library/adegraphics/help/adegraphics.rdb
/usr/lib64/R/library/adegraphics/help/adegraphics.rdx
/usr/lib64/R/library/adegraphics/help/aliases.rds
/usr/lib64/R/library/adegraphics/help/paths.rds
/usr/lib64/R/library/adegraphics/html/00Index.html
/usr/lib64/R/library/adegraphics/html/R.css
/usr/lib64/R/library/adegraphics/tests/add.R
/usr/lib64/R/library/adegraphics/tests/ade4-functions.R
/usr/lib64/R/library/adegraphics/tests/adegraphics.R
/usr/lib64/R/library/adegraphics/tests/nbgraph.R
/usr/lib64/R/library/adegraphics/tests/panelSpatial.R
/usr/lib64/R/library/adegraphics/tests/parameter.R
/usr/lib64/R/library/adegraphics/tests/s.arrow.R
/usr/lib64/R/library/adegraphics/tests/s.class.R
/usr/lib64/R/library/adegraphics/tests/s.corcircle.R
/usr/lib64/R/library/adegraphics/tests/s.density.R
/usr/lib64/R/library/adegraphics/tests/s.distri.R
/usr/lib64/R/library/adegraphics/tests/s.image.R
/usr/lib64/R/library/adegraphics/tests/s.label.R
/usr/lib64/R/library/adegraphics/tests/s.logo.R
/usr/lib64/R/library/adegraphics/tests/s.match.R
/usr/lib64/R/library/adegraphics/tests/s.traject.R
/usr/lib64/R/library/adegraphics/tests/s.value.R
/usr/lib64/R/library/adegraphics/tests/s1d.barchart.R
/usr/lib64/R/library/adegraphics/tests/s1d.boxplot.R
/usr/lib64/R/library/adegraphics/tests/s1d.class.R
/usr/lib64/R/library/adegraphics/tests/s1d.density.R
/usr/lib64/R/library/adegraphics/tests/s1d.distri.R
/usr/lib64/R/library/adegraphics/tests/s1d.gauss.R
/usr/lib64/R/library/adegraphics/tests/s1d.hist.R
/usr/lib64/R/library/adegraphics/tests/s1d.label.R
/usr/lib64/R/library/adegraphics/tests/s1d.match.R
/usr/lib64/R/library/adegraphics/tests/table.image.R
/usr/lib64/R/library/adegraphics/tests/table.value.R
/usr/lib64/R/library/adegraphics/tests/triangle.R
