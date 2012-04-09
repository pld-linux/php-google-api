# TODO
# - make it possible to use user config (via local_config.php path)

%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	Google APIs Client Library for PHP
Name:		php-google-api
Version:	0.5.0
Release:	0.1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	https://google-api-php-client.googlecode.com/files/google-api-php-client-%{version}.tar.gz
# Source0-md5:	8e26c7e3789ffcc00387b1fe1a38e48c
URL:		https://code.google.com/p/google-api-php-client/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-curl
Requires:	php-date
Requires:	php-hash
Requires:	php-json
Requires:	php-openssl
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/google-api
%define		_noautopear	pear
%define		_noautoreq	%{?_noautophpreq} %{?_noautopear}

%description
The Google API Client Library enables you to work with Google APIs
such as Analytics, Adsense, Google+, Calendar, Moderator, Tasks, or
Latitude on your server.

%prep
%setup -qc
mv google-api-php-client/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a src/* $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE README
%{_appdir}
%{_examplesdir}/%{name}-%{version}
