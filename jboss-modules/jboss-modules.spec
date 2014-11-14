%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-modules
Version:          1.1.1
Release:          9%{?dist}
Summary:          A Modular Classloading System
Group:            Development/Libraries
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-modules

# git clone git://github.com/jbossas/jboss-modules.git
# cd jboss-modules/ && git archive --format=tar --prefix=jboss-modules-1.1.1.GA/ 1.1.1.GA | xz > jboss-modules-1.1.1.GA.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

# Fixes https://issues.jboss.org/browse/MODULES-128
Patch0:           MODULES-128.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-devel
BuildRequires:    maven-local
BuildRequires:    jboss-parent
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    junit4
%if 0%{?fedora}
BuildRequires:    apiviz
%endif

Requires:         jpackage-utils
Requires:         java

%description
Ths package contains A Modular Classloading System.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%patch0 -p1

# Conditionally remove dependency on apiviz
if [ %{?rhel} ]; then
    %pom_remove_plugin :maven-javadoc-plugin
fi

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# JAVADOC
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.1-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Sep  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-7
- Conditionally remove dependency on apiviz

* Mon Sep  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-6
- Remove unneeded BR: maven-injection-plugin

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.1.1-4
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Marek Goldmann <mgoldman@redhat.com> 1.1.1-3
- Patch to fix MODULES-128

* Thu Feb 23 2012 Marek Goldmann <mgoldman@redhat.com> 1.1.1-2
- Relocated jars to _javadir

* Sun Feb 19 2012 Marek Goldmann <mgoldman@redhat.com> 1.1.1-1
- Upstream release 1.1.1.GA

* Thu Jan 26 2012 Marek Goldmann <mgoldman@redhat.com> 1.1.0-0.3.CR8
- Upstream release 1.1.0.CR8

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.2.CR4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 02 2011 Marek Goldmann <mgoldman@redhat.com> 1.1.0-0.1.CR4
- Upstream release 1.1.0.CR4

* Tue Aug 02 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.2-1
- Initial packaging

