#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-generics
Version  : 0.1.0
Release  : 23
URL      : https://cran.r-project.org/src/contrib/generics_0.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/generics_0.1.0.tar.gz
Summary  : Common S3 Generics not Provided by Base R Methods Related to
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
and conflicts, generics provides a number of commonly used S3
    generics.

%prep
%setup -q -c -n generics
cd %{_builddir}/generics

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604340277

%install
export SOURCE_DATE_EPOCH=1604340277
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library generics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library generics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library generics
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc generics || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/generics/DESCRIPTION
/usr/lib64/R/library/generics/INDEX
/usr/lib64/R/library/generics/LICENSE
/usr/lib64/R/library/generics/Meta/Rd.rds
/usr/lib64/R/library/generics/Meta/features.rds
/usr/lib64/R/library/generics/Meta/hsearch.rds
/usr/lib64/R/library/generics/Meta/links.rds
/usr/lib64/R/library/generics/Meta/nsInfo.rds
/usr/lib64/R/library/generics/Meta/package.rds
/usr/lib64/R/library/generics/NAMESPACE
/usr/lib64/R/library/generics/NEWS.md
/usr/lib64/R/library/generics/R/generics
/usr/lib64/R/library/generics/R/generics.rdb
/usr/lib64/R/library/generics/R/generics.rdx
/usr/lib64/R/library/generics/help/AnIndex
/usr/lib64/R/library/generics/help/aliases.rds
/usr/lib64/R/library/generics/help/generics.rdb
/usr/lib64/R/library/generics/help/generics.rdx
/usr/lib64/R/library/generics/help/paths.rds
/usr/lib64/R/library/generics/html/00Index.html
/usr/lib64/R/library/generics/html/R.css
/usr/lib64/R/library/generics/tests/testthat.R
/usr/lib64/R/library/generics/tests/testthat/helper-expect_known_cat.R
/usr/lib64/R/library/generics/tests/testthat/helper-skip_if_below_r_version.R
/usr/lib64/R/library/generics/tests/testthat/test-generics-extension.R
/usr/lib64/R/library/generics/tests/testthat/test-multiple-packages.R
/usr/lib64/R/library/generics/tests/testthat/test-s4.R
/usr/lib64/R/library/generics/tests/testthat/test-same-rd.R
/usr/lib64/R/library/generics/tests/testthat/test-single-package.R
/usr/lib64/R/library/generics/tests/testthat/test-special-cases.R
/usr/lib64/R/library/generics/tests/testthat/testGenericsExtension/DESCRIPTION
/usr/lib64/R/library/generics/tests/testthat/testGenericsExtension/NAMESPACE
/usr/lib64/R/library/generics/tests/testthat/testGenericsExtension/R/a.r
/usr/lib64/R/library/generics/tests/testthat/testGenericsExtension/man/reexports.Rd
/usr/lib64/R/library/generics/tests/testthat/testGenericsExtension/man/tidy-special.Rd
/usr/lib64/R/library/generics/tests/testthat/testGenericsExtension/test-1.txt
/usr/lib64/R/library/generics/tests/testthat/testMultiMethod/DESCRIPTION
/usr/lib64/R/library/generics/tests/testthat/testMultiMethod/NAMESPACE
/usr/lib64/R/library/generics/tests/testthat/testMultiMethod/R/a.r
/usr/lib64/R/library/generics/tests/testthat/testMultiMethod/man/multi-method-2.Rd
/usr/lib64/R/library/generics/tests/testthat/testMultiMethod/man/multi-method-3.Rd
/usr/lib64/R/library/generics/tests/testthat/testMultiMethod/man/multi-method.Rd
/usr/lib64/R/library/generics/tests/testthat/testMultiMethod/test-1.txt
/usr/lib64/R/library/generics/tests/testthat/testMultiPackage/DESCRIPTION
/usr/lib64/R/library/generics/tests/testthat/testMultiPackage/NAMESPACE
/usr/lib64/R/library/generics/tests/testthat/testMultiPackage/R/a.r
/usr/lib64/R/library/generics/tests/testthat/testMultiPackage/man/multi-method-4.Rd
/usr/lib64/R/library/generics/tests/testthat/testMultiPackage/test-1.txt
/usr/lib64/R/library/generics/tests/testthat/testS4Docs/DESCRIPTION
/usr/lib64/R/library/generics/tests/testthat/testS4Docs/NAMESPACE
/usr/lib64/R/library/generics/tests/testthat/testS4Docs/R/a.r
/usr/lib64/R/library/generics/tests/testthat/testS4Docs/man/multi_method.Rd
/usr/lib64/R/library/generics/tests/testthat/testS4Docs/test-1.txt
/usr/lib64/R/library/generics/tests/testthat/testS4Docs/test-2.txt
/usr/lib64/R/library/generics/tests/testthat/testSameRd/DESCRIPTION
/usr/lib64/R/library/generics/tests/testthat/testSameRd/NAMESPACE
/usr/lib64/R/library/generics/tests/testthat/testSameRd/R/a.r
/usr/lib64/R/library/generics/tests/testthat/testSameRd/man/same_rd_name-2.Rd
/usr/lib64/R/library/generics/tests/testthat/testSameRd/man/same_rd_name.Rd
/usr/lib64/R/library/generics/tests/testthat/testSameRd/test-1.txt
/usr/lib64/R/library/generics/tests/testthat/testSingleMethod/DESCRIPTION
/usr/lib64/R/library/generics/tests/testthat/testSingleMethod/NAMESPACE
/usr/lib64/R/library/generics/tests/testthat/testSingleMethod/R/a.r
/usr/lib64/R/library/generics/tests/testthat/testSingleMethod/man/single-method-2.Rd
/usr/lib64/R/library/generics/tests/testthat/testSingleMethod/man/single-method.Rd
/usr/lib64/R/library/generics/tests/testthat/testSingleMethod/test-1.txt
