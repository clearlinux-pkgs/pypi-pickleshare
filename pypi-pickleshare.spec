#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pickleshare
Version  : 0.7.5
Release  : 54
URL      : https://files.pythonhosted.org/packages/d8/b6/df3c1c9b616e9c0edbc4fbab6ddd09df9535849c64ba51fcb6531c32d4d8/pickleshare-0.7.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/d8/b6/df3c1c9b616e9c0edbc4fbab6ddd09df9535849c64ba51fcb6531c32d4d8/pickleshare-0.7.5.tar.gz
Summary  : Tiny 'shelve'-like database with concurrency support
Group    : Development/Tools
License  : MIT
Requires: pypi-pickleshare-license = %{version}-%{release}
Requires: pypi-pickleshare-python = %{version}-%{release}
Requires: pypi-pickleshare-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Like shelve, a PickleShareDB object acts like a normal dictionary. Unlike shelve,
        many processes can access the database simultaneously. Changing a value in 
        database is immediately visible to other processes accessing the same database.
        
        Concurrency is possible because the values are stored in separate files. Hence
        the "database" is a directory where *all* files are governed by PickleShare.

%package license
Summary: license components for the pypi-pickleshare package.
Group: Default

%description license
license components for the pypi-pickleshare package.


%package python
Summary: python components for the pypi-pickleshare package.
Group: Default
Requires: pypi-pickleshare-python3 = %{version}-%{release}

%description python
python components for the pypi-pickleshare package.


%package python3
Summary: python3 components for the pypi-pickleshare package.
Group: Default
Requires: python3-core
Provides: pypi(pickleshare)

%description python3
python3 components for the pypi-pickleshare package.


%prep
%setup -q -n pickleshare-0.7.5
cd %{_builddir}/pickleshare-0.7.5
pushd ..
cp -a pickleshare-0.7.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656394109
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pickleshare
cp %{_builddir}/pickleshare-0.7.5/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pickleshare/a71cd80b42a13ff4c909a693893c2b65137c4e75
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pickleshare/a71cd80b42a13ff4c909a693893c2b65137c4e75

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
