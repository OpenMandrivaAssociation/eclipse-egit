%global eclipse_base     %{_libdir}/eclipse
%global install_loc      %{_datadir}/eclipse/dropins/egit

Summary:          Eclipse Git plug-in
Name:             eclipse-egit
Version:          0.11.3
Release:          4
License:          EPL
URL:              http://www.eclipse.org/egit/
Group:            Development/Java

# retrieved from http://egit.eclipse.org/w/?p=egit.git;a=snapshot;h=v0.11.3;sf=tbz2
Source0:          egit-v0.11.3.tar.bz2

BuildRequires:    java-devel >= 1.6.0
BuildRequires:    eclipse-pde
BuildRequires:    eclipse-jgit >= 0.11.3
BuildRequires:    jpackage-utils >= 0:1.5
Requires:         eclipse-platform >= 1:3.5.0
Requires:         eclipse-jgit >= 0.11.3

BuildArch:        noarch
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The eclipse-egit package contains Eclipse plugins for
interacting with Git repositories.

%prep
%setup -n eclipse-egit -q -c
NR=$((`wc -l egit/org.eclipse.egit.ui/src/org/eclipse/egit/ui/internal/clone/GitCloneWizard.java | \
            cut -d' ' -f1` - 1))
       tail -n$NR egit/org.eclipse.egit.ui/src/org/eclipse/egit/ui/internal/clone/GitCloneWizard.java > part2.java
echo "/*******************************************************************************" > part1.java
cat part1.java part2.java > egit/org.eclipse.egit.ui/src/org/eclipse/egit/ui/internal/clone/GitCloneWizard.java

%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.egit -d "jgit"

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}

# egit main feature
unzip -q -d $RPM_BUILD_ROOT%{install_loc}/ build/rpmBuild/org.eclipse.egit.zip

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{install_loc}
%doc egit/LICENSE
%doc egit/README

