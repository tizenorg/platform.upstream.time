Name:           time
Version:        1.7
Release:        1
License:        GPL-2.0+
Summary:        A GNU utility for monitoring a program's use of system resources
Url:            http://www.gnu.org/software/time/
Group:          Applications/System
Source:         ftp://prep.ai.mit.edu/pub/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1001: 	time.manifest
%description
The GNU time utility runs another program, collects information about
the resources used by that program while it is running, and displays
the results.

%prep
%setup -q
cp %{SOURCE1001} .

%build
echo "ac_cv_func_wait3=\${ac_cv_func_wait3='yes'}" >> config.cache
%configure
make %{?_smp_mflags}

%install
%make_install

%docs_package

%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/time
