Name: sailfishos-patch-documents-swipe-to-remove
BuildArch: noarch
Summary: Swipe right to remove a file in the Documents list view of sailfish-office
Version: 0.1.0
Release: 1
Group: System/Patches
License: TODO
Source0: %{name}-%{version}.tar.xz
Requires: patchmanager
Requires: sailfish-office >= 1.1.33

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
