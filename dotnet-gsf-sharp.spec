%define		snap 20050113
Summary:	Gsf# - libgsf .NET Binding
Summary(pl):	Gsf# - wi±zanie .NET dla libgsf
Name:		dotnet-gsf-sharp
Version:	0.2
Release:	2
Epoch:		0
License:	LGPL
Group:		Libraries
Source0:	gsf-sharp-%{version}-%{snap}.tar.gz
# Source0-md5:	5d7f10536541a18cfeb7b4444d57af86
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp-devel >= 0.98
BuildRequires:	gtksourceview-devel
BuildRequires:	libgsf-gnome-devel
BuildRequires:	mono-csharp >= 0.96
BuildRequires:	pkgconfig
Requires:	dotnet-gtk-sharp >= 0.98
Requires:	gtksourceview
ExcludeArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gsf# - libgsf .NET Binding.

%description -l pl
Gsf# - wi±zanie .NET dla libgsf.

%package devel
Summary:	Gsf# development files
Summary(pl):	Pliki programistyczne Gsf#
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Gsf# development files.

%description devel -l pl
Pliki programistyczne Gsf#.

%prep
%setup -q -n gsf-sharp-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/mono/gac/gsf-sharp

%files devel
%defattr(644,root,root,755)
%{_libdir}/mono/gtk-sharp/gsf-sharp.dll
%{_datadir}/gapi/gsf-api.xml
%{_pkgconfigdir}/*
