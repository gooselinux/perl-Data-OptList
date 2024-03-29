Name:           perl-Data-OptList
Version:        0.104
Release:        4%{?dist}
Summary:        Parse and validate simple name/value option pairs
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-OptList/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Data-OptList-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Params::Util) >= 0.14
BuildRequires:  perl(Sub::Install) >= 0.92
# testing
BuildRequires:  perl(Test::Pod::Coverage), perl(Test::Pod)

#Requires:       perl(Params::Util) >= 0.14
#Requires:       perl(Sub::Install) >= 0.92
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Hashes are great for storing named data, but if you want more than one
entry for a name, you have to use a list of pairs. Even then, this is
really boring to write:

%prep
%setup -q -n Data-OptList-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.104-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.104-1
- update to 0.104

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.103-2
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.103-1
- rebuild for new perl
- bump to 0.103
- fix license tag

* Thu Sep 07 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.101-2
- bump

* Sat Sep 02 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.101-1
- Specfile autogenerated by cpanspec 1.69.1.
