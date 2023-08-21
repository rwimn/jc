Name: python3-module-jc
Version: 1.23.4
Release: alt1

Summary: 
License: MIT
Group: Development/Python
Url: https://pypi.org/project/

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3

%description
%summary
smbus2 is drop-in replacement of lm-sensors smbus package

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*

%changelog
* Mon Aug 21 2023 Anatoliy Sinelnikov <noizydwarf@gmail.com> 1.23.4-alt1
- build to ALT

