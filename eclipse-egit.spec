
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		eclipse-egit
Version:	3.2.0
Release:	1.0
License:	GPLv3+
Source0:	eclipse-egit-3.2.0-1.0-omv2014.0.noarch.rpm
Source1:	eclipse-egit-mylyn-3.2.0-1.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/eclipse-egit
BuildArch:	noarch
Summary:	eclipse-egit bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-jgit >= 3.2.0
Requires:	eclipse-platform >= 1:3.5.0
Requires:	osgi(com.jcraft.jsch)
Requires:	osgi(org.eclipse.compare)
Requires:	osgi(org.eclipse.core.expressions)
Requires:	osgi(org.eclipse.core.filesystem)
Requires:	osgi(org.eclipse.core.net)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.core.variables)
Requires:	osgi(org.eclipse.equinox.security)
Requires:	osgi(org.eclipse.help)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.jsch.core)
Requires:	osgi(org.eclipse.jsch.ui)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.team.ui)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.cheatsheets)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.navigator)
Requires:	osgi(org.eclipse.ui.workbench.texteditor)
Provides:	eclipse-egit = 3.2.0-1.0:2014.0
Provides:	osgi(org.eclipse.egit) = 3.2.0
Provides:	osgi(org.eclipse.egit.core) = 3.2.0
Provides:	osgi(org.eclipse.egit.doc) = 3.2.0
Provides:	osgi(org.eclipse.egit.ui) = 3.2.0

%description
eclipse-egit bootstrap version.

%files
/usr/share/doc/eclipse-egit
/usr/share/doc/eclipse-egit/LICENSE
/usr/share/doc/eclipse-egit/README.md
/usr/share/eclipse/dropins/egit
/usr/share/eclipse/dropins/egit/eclipse
/usr/share/eclipse/dropins/egit/eclipse/features
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/META-INF
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/META-INF/maven
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/META-INF/maven/org.eclipse.egit.feature
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/META-INF/maven/org.eclipse.egit.feature/org.eclipse.egit
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/META-INF/maven/org.eclipse.egit.feature/org.eclipse.egit/pom.properties
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/META-INF/maven/org.eclipse.egit.feature/org.eclipse.egit/pom.xml
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/epl-v10.html
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/feature.properties
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/feature.xml
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit_3.2.0.201312181205-r/license.html
/usr/share/eclipse/dropins/egit/eclipse/plugins
/usr/share/eclipse/dropins/egit/eclipse/plugins/org.eclipse.egit.core_3.2.0.201312181205-r.jar
/usr/share/eclipse/dropins/egit/eclipse/plugins/org.eclipse.egit.doc_3.2.0.201312181205-r.jar
/usr/share/eclipse/dropins/egit/eclipse/plugins/org.eclipse.egit.ui_3.2.0.201312181205-r.jar
/usr/share/eclipse/dropins/egit/eclipse/plugins/org.eclipse.egit_3.2.0.201312181205-r.jar

#------------------------------------------------------------------------
%package	-n eclipse-egit-mylyn
Version:	3.2.0
Release:	1.0
Summary:	eclipse-egit-mylyn bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-egit = 3.2.0-1.0
Requires:	eclipse-mylyn-context-team
Requires:	eclipse-mylyn-docs-wikitext
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.jface)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.mylyn.context.core)
Requires:	osgi(org.eclipse.mylyn.monitor.core)
Requires:	osgi(org.eclipse.mylyn.resources.ui)
Requires:	osgi(org.eclipse.mylyn.tasks.core)
Requires:	osgi(org.eclipse.mylyn.tasks.ui)
Requires:	osgi(org.eclipse.mylyn.team.ui)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.navigator.resources)
Requires:	osgi(org.eclipse.ui.workbench)
Requires:	osgi(org.eclipse.ui.workbench.texteditor)
Provides:	eclipse-egit-mylyn = 3.2.0-1.0:2014.0
Provides:	osgi(org.eclipse.egit.mylyn.ui) = 3.2.0

%description	-n eclipse-egit-mylyn
eclipse-egit-mylyn bootstrap version.

%files		-n eclipse-egit-mylyn
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/META-INF
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/META-INF/maven
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/META-INF/maven/org.eclipse.egit.feature
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/META-INF/maven/org.eclipse.egit.feature/org.eclipse.egit.mylyn
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/META-INF/maven/org.eclipse.egit.feature/org.eclipse.egit.mylyn/pom.properties
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/META-INF/maven/org.eclipse.egit.feature/org.eclipse.egit.mylyn/pom.xml
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/epl-v10.html
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/feature.properties
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/feature.xml
/usr/share/eclipse/dropins/egit/eclipse/features/org.eclipse.egit.mylyn_3.2.0.201312181205-r/license.html
/usr/share/eclipse/dropins/egit/eclipse/plugins/org.eclipse.egit.mylyn.ui_3.2.0.201312181205-r.jar

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
