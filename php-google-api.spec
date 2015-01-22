%define		php_min_version 5.2.2
%include	/usr/lib/rpm/macros.php
Summary:	Google APIs Client Library for PHP
Name:		php-google-api
Version:	1.1.2
Release:	0.5
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	https://github.com/google/google-api-php-client/archive/%{version}/google-api-php-client-%{version}.tar.gz
# Source0-md5:	44f2252aa279364236823fb3fc129d53
Patch0:		php52.patch
Patch1:		gapi.patch
Patch2:		autoload.patch
URL:		https://developers.google.com/api-client-library/php/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
Requires:	php(core) >= %{php_min_version}
Requires:	php(curl)
Requires:	php(date)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(openssl)
Requires:	php(pcre)
Suggests:	php-seclib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/google-api
%define		_noautopear	pear
%define		_noautoreq	%{?_noautophpreq} %{?_noautopear}

%description
Google APIs Client Library for PHP provides access to many Google
APIs. It is designed for PHP client-application developers and offers
simple, flexible, powerful API access.

%prep
%setup -qn google-api-php-client-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# use single autoload so could use different autoloader than provided by this project
# you intend to use this, you need to call it before accessing other classes
# this is also addressed upstream: https://github.com/google/google-api-php-client/issues/400
mv autoload.php src/Google
grep -r 'require_once.*autoload.php' src -l | xargs %{__sed} -i -e '/require_once.*autoload.php/d'

# fixup paths in examples
grep -r 'require_once.*autoload.php' examples -l | xargs %{__sed} -i -e "
	s,realpath(dirname(__FILE__) . '/../autoload.php'),'Google/autoload.php',
"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CONTRIBUTING.md
%{php_data_dir}/Google
%{_examplesdir}/%{name}-%{version}
