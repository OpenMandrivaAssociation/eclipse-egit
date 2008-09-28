%define gcj_support     0

Summary:          Eclipse Git plug-in
Name:             eclipse-egit
Version:          0.3.1
Release:          %mkrel 0.2.1
License:          EPL GPLv2 LGPLv2
URL:              http://repo.or.cz/w/egit.git
Group:            Development/Java

# retrieved from http://repo.or.cz/w/egit.git?a=snapshot;h=31185033bceae1c77b0f6a4182dea3fc56f882ba;sf=tgz
Source0:          egit-3cd4f3f9119b79750bbfc542119451a668c462e3.tar.gz
Requires:         eclipse-platform >= 1:3.2.1
Requires:         git-core
%if %{gcj_support}
BuildRequires:    java-1.5.0-gcj-devel
%else
BuildRequires:    java-devel >= 1.6.0
%endif

BuildRequires:    eclipse-pde
BuildRequires:    java-rpmbuild >= 0:1.5
BuildRequires:    zip
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
%{_libdir}/eclipse/buildscripts/pdebuild \
   -a "-DjavacSource=1.5 -DjavacTarget=1.5"

%install
rm -rf $RPM_BUILD_ROOT
installDir=$RPM_BUILD_ROOT/%{_datadir}/eclipse/dropins/egit
install -d -m755 $installDir

# egit main feature
unzip -q -d $installDir/ \
            build/rpmBuild/org.spearce.egit.zip
%{gcj_compile}

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
%{_datadir}/eclipse/dropins/egit
%gcj_files
