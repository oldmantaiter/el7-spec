Summary:        Google C++ Mocking Framework
Name:           gmock
Version:        1.6.0
Release:        2%{?dist}
License:        BSD
Group:          System Environment/Libraries
URL:            http://code.google.com/p/googlemock/
Source0:        gmock-1.6.0.zip
Patch0:         install.patch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
BuildRequires:  gtest-devel >= 1.6.0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  python
Requires:       gtest >= 1.6.0

%description
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s
specifics in mind, Google C++ Mocking Framework (or Google Mock for
short) is a library for writing and using C++ mock classes.

Google Mock:

 o lets you create mock classes trivially using simple macros,
 o supports a rich set of matchers and actions,
 o handles unordered, partially ordered, or completely ordered
   expectations,
 o is extensible by users, and
 o works on Linux, Mac OS X, Windows, Windows Mobile, minGW, and
   Symbian.

%package        devel
Summary:        Development files for %{name}
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%setup -q
%patch0 -p1

%build
# needed for mahe check to work without failures
autoreconf -fvi     
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install INSTALL="%{__install} -p" DESTDIR=%{buildroot}

%check
make check

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc CHANGES CONTRIBUTORS COPYING README

%files devel
%defattr(-, root, root, -)
%{_bindir}/gmock-config
%{_includedir}/../src/%{name}/
%{_includedir}/%{name}/
%{_datadir}/pkgconfig/*
%{_datadir}/%{name}/generator/

%changelog
* Tue Aug 6 2013 Timothy St. Clair <tstclair@redhat.com> - 1.6.0-2
- Change package to noarch

* Mon Jul 29 2013 Timothy St. Clair <tstclair@redhat.com> - 1.6.0-1
- Update to 1.6.0 release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 12 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.5.0-1
- 1.5.0
- req gtest 1.5.0
- fix description
- fix group
- fix files section
- remove name macro
- rpmlint error free
- don't build with bundled gtest
- make check works
- add some buildreqs

* Sun Oct 4 2009 Tejas Dinkar <tejas@gja.in> - 1.4.0-1
- Initial gmock 1.4.0
