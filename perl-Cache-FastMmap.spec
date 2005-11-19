#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Cache
%define	pnam	FastMmap
Summary:	Cache::FastMmap - Uses an mmap'ed file to act as a shared memory interprocess cache
Summary(pl):	Cache::FastMmap - u¿ycie mmapowanego pliku jako wspó³dzielonej pamiêci podrêcznej
Name:		perl-Cache-FastMmap
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	513e715813ff55c534e7b0cebbffedad
URL:		http://search.cpan.org/dist/Cache-FastMmap/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uses an mmap'ed file to act as a shared memory interprocess cache.

%description -l pl
Ten modu³ pozwala na u¿ywanie mmapowanego pliku jako pamiêci
podrêcznej wspó³dzielonej miêdzy procesami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/Cache/FastMmap
%dir %{perl_vendorarch}/auto/Cache/FastMmap
%dir %{perl_vendorarch}/auto/Cache/FastMmap/CImpl
%{perl_vendorarch}/auto/Cache/FastMmap/CImpl/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Cache/FastMmap/CImpl/*.so
%{_mandir}/man3/*
