#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	LWP
%define		pnam	MediaTypes
Summary:	LWP::MediaTypes - guess media type for a file or a URL
Summary(pl.UTF-8):	LWP::MediaTypes - zgadywanie typu zawartości dla pliku lub URL-a
Name:		perl-LWP-MediaTypes
Version:	6.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/LWP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	84b799a90c0d2ce52897a7cb4c0478d0
URL:		https://metacpan.org/dist/LWP-MediaTypes
%if %{with tests}
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Conflicts:	perl-libwww < 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions for handling media (also known as MIME)
types and encodings. The mapping from file extensions to media types
is defined by the media.types file. If the ~/.media.types file exists
it is used instead. For backwards compatibility the module will also
look for ~/.mime.types.

%description -l pl.UTF-8
Ten moduł udostępnia funkcje do obsługi typów zawartości (znanych też
jako typy MIME) plików oraz ich kodowań. Odwzorowanie rozszerzeń
plików na typy zawartości jest definiowane w pliku media.types; jeśli
istnieje plik ~/.media.types, jest on używany zamiast domyślnego
pliku. Dla kompatybilności wstecznej moduł sprawdza także plik
~/.mime.types.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/LWP
%{perl_vendorlib}/LWP/MediaTypes.pm
%{perl_vendorlib}/LWP/media.types
%{_mandir}/man3/LWP::MediaTypes.3pm*
