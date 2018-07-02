#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-adegraphics
Version  : 1.0.10
Release  : 3
URL      : https://cran.r-project.org/src/contrib/adegraphics_1.0-10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/adegraphics_1.0-10.tar.gz
Summary  : An S4 Lattice-Based Package for the Representation of
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Guerry
Requires: R-RColorBrewer
Requires: R-ade4
Requires: R-sp
BuildRequires : R-Guerry
BuildRequires : R-RColorBrewer
BuildRequires : R-ade4
BuildRequires : R-sp
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n adegraphics

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530496181

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530496181
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegraphics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegraphics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegraphics
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library adegraphics|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
