# TODO
# - make it possible to use user config (via local_config.php path)

%define		php_min_version 5.2.2
%include	/usr/lib/rpm/macros.php
Summary:	Google APIs Client Library for PHP
Name:		php-google-api
Version:	0.6.7
Release:	1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	https://google-api-php-client.googlecode.com/files/google-api-php-client-%{version}.tar.gz
# Source0-md5:	4ea330e08f91963b7b78fab25314abee
Patch0:		php52.patch
Patch1:		gapi.patch
URL:		https://code.google.com/p/google-api-php-client/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-curl
Requires:	php-date
Requires:	php-hash
Requires:	php-json
Requires:	php-openssl
Requires:	php-pcre
Suggests:	php-seclib
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
%patch0 -p1
%patch1 -p8

grep -rl require_once examples | xargs %{__sed} -i -e '
	# fixup paths to source
	/require_once/ s,\.\./\.\./src/,google-api/,
	/require_once/ s,\.\./src/,google-api/,

	# lower php requirement to 5.2
	s,__DIR__,dirname(__FILE__),
'

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
