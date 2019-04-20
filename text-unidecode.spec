#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : text-unidecode
Version  : 1.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/f0/a2/40adaae7cbdd007fb12777e550b5ce344b56189921b9f70f37084c021ca4/text-unidecode-1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/f0/a2/40adaae7cbdd007fb12777e550b5ce344b56189921b9f70f37084c021ca4/text-unidecode-1.2.tar.gz
Summary  : The most basic Text::Unidecode port
Group    : Development/Tools
License  : Artistic-1.0
Requires: text-unidecode-python3
Requires: text-unidecode-license
Requires: text-unidecode-python
BuildRequires : buildreq-distutils3

%description
==============

%package license
Summary: license components for the text-unidecode package.
Group: Default

%description license
license components for the text-unidecode package.


%package python
Summary: python components for the text-unidecode package.
Group: Default
Requires: text-unidecode-python3

%description python
python components for the text-unidecode package.


%package python3
Summary: python3 components for the text-unidecode package.
Group: Default
Requires: python3-core

%description python3
python3 components for the text-unidecode package.


%prep
%setup -q -n text-unidecode-1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533043901
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/text-unidecode
cp LICENSE %{buildroot}/usr/share/doc/text-unidecode/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/text-unidecode/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
