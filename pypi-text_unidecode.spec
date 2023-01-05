#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-text_unidecode
Version  : 1.3
Release  : 34
URL      : https://files.pythonhosted.org/packages/ab/e2/e9a00f0ccb71718418230718b3d900e71a5d16e701a3dae079a21e9cd8f8/text-unidecode-1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/ab/e2/e9a00f0ccb71718418230718b3d900e71a5d16e701a3dae079a21e9cd8f8/text-unidecode-1.3.tar.gz
Summary  : The most basic Text::Unidecode port
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: pypi-text_unidecode-license = %{version}-%{release}
Requires: pypi-text_unidecode-python = %{version}-%{release}
Requires: pypi-text_unidecode-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
==============

%package license
Summary: license components for the pypi-text_unidecode package.
Group: Default

%description license
license components for the pypi-text_unidecode package.


%package python
Summary: python components for the pypi-text_unidecode package.
Group: Default
Requires: pypi-text_unidecode-python3 = %{version}-%{release}

%description python
python components for the pypi-text_unidecode package.


%package python3
Summary: python3 components for the pypi-text_unidecode package.
Group: Default
Requires: python3-core
Provides: pypi(text_unidecode)

%description python3
python3 components for the pypi-text_unidecode package.


%prep
%setup -q -n text-unidecode-1.3
cd %{_builddir}/text-unidecode-1.3
pushd ..
cp -a text-unidecode-1.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656368803
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-text_unidecode
cp %{_builddir}/text-unidecode-1.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-text_unidecode/41daa613919d46f8422f7784166d5881b008121e
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
/usr/share/package-licenses/pypi-text_unidecode/41daa613919d46f8422f7784166d5881b008121e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
