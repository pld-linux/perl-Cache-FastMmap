#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Cache
%define		pnam	FastMmap
Summary:	Cache::FastMmap - Uses an mmap'ed file to act as a shared memory interprocess cache
Summary(pl.UTF-8):	Cache::FastMmap - użycie mmapowanego pliku jako współdzielonej pamięci podręcznej
Name:		perl-Cache-FastMmap
Version:	1.40
Release:	15
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e0929ba556c629a43f5d65a2b6cb9a2f
URL:		http://search.cpan.org/dist/Cache-FastMmap/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uses an mmap'ed file to act as a shared memory interprocess cache.

%description -l pl.UTF-8
Ten moduł pozwala na używanie mmapowanego pliku jako pamięci
podręcznej współdzielonej między procesami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Cache/*.pm
%dir %{perl_vendorarch}/auto/Cache/FastMmap
%attr(755,root,root) %{perl_vendorarch}/auto/Cache/FastMmap/FastMmap.so
%{_mandir}/man3/*
