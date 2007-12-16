%define gcj_support     1

Summary:          Eclipse Git plug-in
Name:             eclipse-egit
Version:          0.3.0
Release:          %mkrel 0.2.2
License:          EPL GPLv2 LGPLv2
URL:              http://repo.or.cz/w/egit.git
Group:            Development/Java

# retrieved from http://repo.or.cz/w/egit.git?a=snapshot;h=31185033bceae1c77b0f6a4182dea3fc56f882ba;sf=tgz
Source0:          egit-31185033bceae1c77b0f6a4182dea3fc56f882ba.tar.gz

Requires:         eclipse-platform >= 1:3.2.1
Requires:         git-core
%if %{gcj_support}
BuildRequires:    java-1.5.0-gcj-devel
%else
BuildRequires:    java-devel >= 1.6.0
%endif

BuildRequires:    eclipse-pde
BuildRequires:    java-rpmbuild >= 0:1.5

%if %{gcj_support}
%else
BuildArch:        noarch
%endif
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The eclipse-egit package contains Eclipse plugins for
interacting with Git repositories.

%prep
%setup -q -c 

%build
# Copy the SDK for build
/bin/sh -x %{_datadir}/eclipse/buildscripts/copy-platform SDK %{_datadir}/eclipse
SDK=$(cd SDK > /dev/null && pwd)

# Eclipse may try to write to the home directory.
mkdir home
homedir=$(cd home > /dev/null && pwd)

# build the main egit feature
%{java} -cp $SDK/startup.jar                              \
     -Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration  \
     org.eclipse.core.launcher.Main                    \
     -application org.eclipse.ant.core.antRunner       \
     -Dtype=feature                                    \
     -Did=org.spearce.egit                             \
     -DbaseLocation=$SDK                               \
     -DjavacSource=1.5  -DjavacTarget=1.5              \
     -DsourceDirectory=$(pwd)                          \
     -DbuildDirectory=$(pwd)/build                     \
     -Dbuilder=%{_datadir}/eclipse/plugins/org.eclipse.pde.build/templates/package-build \
     -f %{_datadir}/eclipse/plugins/org.eclipse.pde.build/scripts/build.xml \
     -vmargs -Duser.home=$homedir

%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT/%{_datadir}/eclipse

# egit main feature
unzip -q -d $RPM_BUILD_ROOT%{_datadir}/eclipse/.. \
            build/rpmBuild/org.spearce.egit.zip

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean 
rm -rf $RPM_BUILD_ROOT

%if %{gcj_support}
%post
%{update_gcjdb}

%postun
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%{_datadir}/eclipse/features/org.spearce.egit*
%{_datadir}/eclipse/plugins/org.spearce.egit*
%{_datadir}/eclipse/plugins/org.spearce.egit.core*
%{_datadir}/eclipse/plugins/org.spearce.egit.ui*
%{_datadir}/eclipse/plugins/org.spearce.jgit*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*
%endif

