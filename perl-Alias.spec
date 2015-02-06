%define	upstream_name Alias
%define	upstream_version 2.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	CPAN %{upstream_name} module for aliasing services
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Alias/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Alias-2.32-perl-5.14-fix.patch

BuildRequires:	perl-devel

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
%patch0 -p1 -b .perl514~

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*/Alias.pm
%{perl_vendorlib}/*/auto/Alias/*
%{_mandir}/*/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.320.0-4
+ Revision: 773482
- clean out
- fix build with perl 5.14 (P0)
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.320.0-3
+ Revision: 680449
- mass rebuild

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.320.0-2mdv2011.0
+ Revision: 555418
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.320.0-1mdv2010.0
+ Revision: 402092
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.32-6mdv2009.0
+ Revision: 255266
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 2.32-4mdv2008.1
+ Revision: 151812
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 2.32-3mdv2008.0
+ Revision: 25442
- rebuild


* Thu Apr 27 2006 Nicolas L�cureuil <neoclust@mandriva.org> 2.32-2mdk
- Fix BuildRequires Using perl Policies
	- Source URL
- use mkrel

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 2.32-1mdk
- initial Mandriva package

