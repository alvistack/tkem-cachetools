# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-cachetools
Epoch: 100
Version: 5.3.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Extensible memoizing collections and decorators
License: MIT
URL: https://github.com/tkem/cachetools/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library @lru_cache
function decorator.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-cachetools
Summary: Extensible memoizing collections and decorators
Requires: python3
Provides: python3-cachetools = %{epoch}:%{version}-%{release}
Provides: python3dist(cachetools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cachetools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cachetools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cachetools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cachetools) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-cachetools
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library @lru_cache
function decorator.

%files -n python%{python3_version_nodots}-cachetools
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-cachetools
Summary: Extensible memoizing collections and decorators
Requires: python3
Provides: python3-cachetools = %{epoch}:%{version}-%{release}
Provides: python3dist(cachetools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cachetools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cachetools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cachetools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cachetools) = %{epoch}:%{version}-%{release}

%description -n python3-cachetools
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library @lru_cache
function decorator.

%files -n python3-cachetools
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
