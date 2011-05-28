%define upstream_name    Alias
%define upstream_version 2.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	CPAN %{upstream_name} module for aliasing services
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Alias/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This Perl module performs aliasing services. You may find this
module useful if you:
   * are tired of dereferencing hash-based object attributes
   * wish perl could make-do with fewer $, -> and {} things
   * are a little scared of using typeglobs
   * want the freedom to put what you want, when you want in
     the symbol table without having to deal with weird syntax
   * need to use scalar constants in your program since you don't
     trust yourself from changing $PI

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*/Alias.pm
%{perl_vendorlib}/*/auto/Alias/*
%{_mandir}/*/*
