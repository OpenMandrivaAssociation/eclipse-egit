%{?_javapackages_macros:%_javapackages_macros}
%global install_loc      %{_datadir}/eclipse/dropins/egit
%global version_suffix 201312181205-r

%{?scl:%scl_package eclipse-egit}
%{!?scl:%global pkg_name %{name}}

Summary:          Eclipse Git Integration
Name:             %{?scl_prefix}eclipse-egit
Version:          3.2.0
Release:          1.1%{?dist}
License:          EPL
URL:              http://www.eclipse.org/egit

Source0:          http://git.eclipse.org/c/egit/egit.git/snapshot/egit-%{version}.%{version_suffix}.tar.bz2

BuildRequires:    java-devel >= 1.6.0
BuildRequires:    %{?scl_prefix}eclipse-jgit >= 3.2.0
BuildRequires:    %{?scl_prefix}jgit >= 1.3.0
BuildRequires:    tycho
BuildRequires:    %{?scl_prefix}eclipse-mylyn-context-team
BuildRequires:    %{?scl_prefix}eclipse-mylyn-docs-wikitext
Requires:         %{?scl_prefix}eclipse-platform >= 1:3.5.0
Requires:         %{?scl_prefix}eclipse-jgit >= 3.2.0
%{?scl:Requires: %scl_runtime}

BuildArch:        noarch

%description
The eclipse-egit package contains Eclipse plugins for
interacting with Git repositories.


%package mylyn
Summary:     Git integration for mylyn.
Requires:    %{?scl_prefix}eclipse-mylyn-context-team
Requires:    %{?scl_prefix}eclipse-egit = %{version}-%{release}
Requires:    %{?scl_prefix}eclipse-mylyn-docs-wikitext


%description mylyn
Git integration for mylyn.

%prep
%setup -n egit-%{version}.%{version_suffix} -q
%pom_xpath_remove "pom:repositories"
%pom_xpath_remove "pom:dependencies"
%pom_xpath_remove "pom:profiles"
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin/pom:configuration/pom:target"
%pom_xpath_remove "*[local-name() ='plugin' and (child::*[text()='tycho-packaging-plugin'])]"
%pom_xpath_remove "pom:dependencies" org.eclipse.egit.doc/pom.xml
%pom_disable_module org.eclipse.egit.target
%pom_disable_module org.eclipse.egit.core.test
%pom_disable_module org.eclipse.egit.ui.test
%pom_disable_module org.eclipse.egit.mylyn.ui.test

#TODO: revisit jgit packaging and maybe package source?
sed -i -e "15,29d" org.eclipse.egit.repository/category.xml
sed -i -e "9,11d" org.eclipse.egit.repository/category.xml

%build
mvn-rpmbuild verify -Dmaven.test.skip=true

%install
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/eclipse
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/eclipse/features
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/eclipse/plugins

unzip -q -d $RPM_BUILD_ROOT%{install_loc}/eclipse org.eclipse.egit.repository/target/org.eclipse.egit.repository-%{version}.*-r.zip
pushd $RPM_BUILD_ROOT%{install_loc}/eclipse/features
  for f in * ; do
    f_name=${f/.jar//}
    mkdir -p $f_name
    unzip -d $f_name $f
    rm $f 
  done
popd
rm $RPM_BUILD_ROOT%{install_loc}/eclipse/*.jar

%files
%dir %{install_loc}
%dir %{install_loc}/eclipse
%dir %{install_loc}/eclipse/plugins
%dir %{install_loc}/eclipse/features
%{install_loc}/eclipse/features/org.eclipse.egit_*
%{install_loc}/eclipse/plugins/
%exclude %{install_loc}/eclipse/plugins/org.eclipse.egit.mylyn.ui_*.jar
%doc LICENSE README.md

%files mylyn
%{install_loc}/eclipse/features/org.eclipse.egit.mylyn_*
%{install_loc}/eclipse/plugins/org.eclipse.egit.mylyn.ui_*.jar

%changelog
* Sun Dec 29 2013 Alexander Kurtakov <akurtako@redhat.com> 3.2.0-1
- Update to 3.2.0.

* Mon Oct 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.1.0-3
- Fix feature installation.

* Wed Oct 16 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.1.0-2
- Package Egit integration for mylyn.
- Changed building process to reflect upstream one.

* Thu Oct 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.1.0-1
- Update to Kepler SR1.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 5 2013 Neil Brian Guzman <nguzman@redhat.com> 3.0.0-3
- Bump release

* Tue Jun 25 2013 Neil Brian Guzman <nguzman@redhat.com> 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jun 25 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.0.0-1
- Update to 3.0.0.

* Thu Feb 21 2013 Sami Wagiaalla <swagiaal@redhat.com> 2.3.1-1
- SCL-ized.

* Thu Feb 21 2013 Sami Wagiaalla <swagiaal@redhat.com> 2.3.1-1
- Update to 2.3.1.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.2.0-1
- Update to latest upstream.

* Mon Oct 1 2012 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-1
- Update to 2.1.0 release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 2 2012 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-1
- Update to 2.0.0 upstream release.

* Fri Apr 27 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.3.0-3
- Use eclipse-pdebuild over pdebuild in lib.

* Thu Apr 26 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.3.0-2
- Fix 1.3.0 which was previously using wrong sources.
- Fix JGit BR/R since EGit depends on the same version of JGit.

* Fri Feb 17 2012 Andrew Robinson <arobinso@redhat.com> 1.3.0-1
- Update to 1.3.0 upstream release.

* Thu Jan 5 2012 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-1
- Update to upstream 1.2.0.

* Fri Nov 18 2011 Alexander Kurtakov <akurtako@redhat.com> 1.1.0-2
- Add patch to fix New git repo wizard.

* Mon Jun 27 2011 Andrew Robinson <arobinso@redhat.com> 1.1.0-1
- Update to upstream release 1.1.0.

* Tue Jun 14 2011 Chris Aniszczyk <zx@redhat.com> 1.0.0-2
- Update to final upstream release v1.0.0.201106090707-r.

* Tue Jun 07 2011 Chris Aniszczyk <zx@redhat.com> 1.0.0-1
- Update to upstream release 1.0.0.

* Tue May 03 2011 Chris Aniszczyk <zx@redhat.com> 0.12.1-1
- Update to upstream release 0.12.1.

* Tue Feb 22 2011 Chris Aniszczyk <zx@redhat.com> 0.11.3-2
- Update to fix issue with GitCloneWizard file.

* Tue Feb 22 2011 Chris Aniszczyk <zx@redhat.com> 0.11.3-1
- Update to upstream release 0.11.3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Chris Aniszczyk <zx@redhat.com> 0.10.1-1
- Update to upstream release 0.10.1.

* Thu Oct 7 2010 Chris Aniszczyk <zx@redhat.com> 0.9.3-1
- Update to upstream release 0.9.3.

* Wed Sep 15 2010 Severin Gehwolf <sgehwolf@redhat.com> 0.9.1-1
- Update to upstream release 0.9.1.
- Remove git-core dependency.

* Thu Aug 26 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.9.0-0.1.20100825git
- Make release tag more readable (separate "0.1" and pre-release tag by ".").

* Wed Aug 25 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.9.0-0.120100825git
- Pre-release of EGit 0.9.0

* Thu Jun 24 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.8.4-1
- Rebase to 0.8.4 release.

* Tue Apr 13 2010 Jeff Johnston <jjohnstn@redhat.com> 0.7.1-2
- Bump up release.

* Tue Apr 13 2010 Jeff Johnston <jjohnstn@redhat.com> 0.7.1-1
- Rebase to 0.7.1.

* Fri Mar 19 2010 Alexander Kurtakov <akurtako@redhat.com> 0.7.0-1
- Update to 0.7.0.
- License is only EPL now.

* Tue Feb 9 2010 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-0.1.git20100208
- New git snapshot.

* Tue Nov 10 2009 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-0.1.git20091029
- Update to 0.6 git.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Alexander Kurtakov <akurtako@redhat.com> 0.5.0-1
- Update to 0.5.0.

* Mon Mar 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.0-3.20090323
- Update to latest snapshot.

* Mon Mar 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.0-3.20090217
- Rebuild to not ship p2 context.xml.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2.20090217
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.0-1.20090217
- New snapshot.

* Wed Dec 10 2008 Alexander Kurtakov <akurtako@redhat.com> 0.4.0-1
- Update to 0.4.0.

* Wed Oct 22 2008 Alexander Kurtakov <akurtako@redhat.com> 0.3.1.20081022-3
- New git version.

* Wed Jul 30 2008 Andrew Overholt <overholt@redhat.com> 0.3.1-2
- Move files and update build for Eclipse SDK 3.4
- Use pdebuild

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.1-1
- fix license tag

* Tue Apr 08 2008 Jesse Keating <jkeating@redhat.com> - 0.3.1-0
- New upstream release 0.3.1, makes committing / diffing actually work

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.0-3
- Autorebuild for GCC 4.3

* Thu Oct 04 2007 Ben Konrath <bkonrath@redhat.com> 0.3.0-2.fc8
- Require git-core instead of git.
- Resolves: #319321

* Mon Sep 24 2007 Ben Konrath <bkonrath@redhat.com> 0.3.0-1.fc8
- 0.3.0

* Wed Sep 19 2007 Ben Konrath <bkonrath@redhat.com> 0.2.99-0.git20070919.fc8
- 0.2.99 git20070919

* Mon Sep 17 2007 Ben Konrath <bkonrath@redhat.com> 0.2.2-2.git20070911.fc8
- Update add feature and plugin patch.

* Mon Sep 17 2007 Ben Konrath <bkonrath@redhat.com> 0.2.2-1.git20070911.fc8
- Require eclipse-platform >= 3.2.1 

* Fri Sep 14 2007 Ben Konrath <bkonrath@redhat.com> 0.2.2-0.git20070911.fc8
- Update to git20070911.
- Update feature and accosicated branding plugin.

* Wed Aug 29 2007 Ben Konrath <bkonrath@redhat.com> 0.2.2-0.git20070826.fc8
- Initial version
