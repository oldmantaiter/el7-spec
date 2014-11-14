Name:          jtoaster
Version:       1.0.5
Release:       1%{?dist}
Summary:       Java utility class for swing applications
Group:         Development/Libraries
License:       ASL 2.0
URL:           http://jtoaster.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/jtoaster/%{name}/1.0/%{name}-%{version}.jar
Source1:       %{name}-template.pom
BuildRequires: java-devel
BuildRequires: jpackage-utils

Requires:      java
Requires:      jpackage-utils
BuildArch:     noarch

%description
Java Toaster is a java utility class for your swing applications
that show an animate box coming from the bottom of your screen
with a notification message and/or an associated image (like MSN
online/offline notifications).

%package javadoc
Group:         Documentation
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c
find . -name "*.class" -delete

cp -p %{SOURCE1} %{name}.pom
sed -i "s|@version@|%{version}|" %{name}.pom

mkdir -p src/com/nitido/utils/toaster docs
mv ./\ com/nitido/utils/toaster/Toaster.java src/com/nitido/utils/toaster/

%build

%javac -encoding UTF-8 $(find src -type f -name "*.java")
(
  cd src
  %jar cvf ../%{name}.jar $(find . -name "*.class")
)
%javadoc -d docs -encoding UTF-8 $(find src -type f -name "*.java")

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{name}.pom %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc README apache2.0_license.txt com

%files javadoc
%{_javadocdir}/%{name}
%doc apache2.0_license.txt

%changelog
* Sat Apr 27 2013 gil cattaneo <puntogil@libero.it> 1.0.5-1
- initial rpm
