Name: python3-module-jc
Version: 1.23.4
Release: alt1

Summary: jc accepts piped input from STDIN and outputs a JSON representation of the previous command's output to STDOUT.
License: MIT
Group: Development/Python
Url: https://pypi.org/project/

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3

%description
%summary
jc accepts piped input from STDIN and outputs a JSON representation of the previous command's output to STDOUT.

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

