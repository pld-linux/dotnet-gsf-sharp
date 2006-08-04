#
%include	/usr/lib/rpm/macros.mono
%define		snap 20051130
#
Summary:	Gsf# - libgsf .NET Binding
Summary(pl):	Gsf# - wi±zanie .NET dla libgsf
Name:		dotnet-gsf-sharp
Version:	0.7
Release:	0.%{snap}.8
Epoch:		0
License:	LGPL
Group:		Libraries
Source0:	gsf-sharp-%{version}-%{snap}.tar.bz2
# Source0-md5:	afb75dd835afea2f014d91ae73344fd7
Patch0:		%{name}-pkgconfig.patch
Patch1:		%{name}-version_check.patch
Patch2:		%{name}-sharp20.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.8.2
BuildRequires:	libgsf-gnome-devel >= 1.13
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.13.8
BuildRequires:	monodoc >= 1.1.13
BuildRequires:	pkgconfig
Requires:	mono >= 1.1.13.8
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x
ExcludeArch:	i386
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
Requires:	dotnet-gtk-sharp2-devel >= 2.8.2

%description devel
Gsf# development files.

%description devel -l pl
Pliki programistyczne Gsf#.

%package static
Summary:	Gsf# static library
Summary(pl):	Biblioteka statyczna Gsf#
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Gsf# static library.

%description static -l pl
Biblioteka statyczna Gsf#.

%prep
%setup -q -n gsf-sharp-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so
%{_prefix}/lib/mono/gac/gsf-sharp

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_prefix}/lib/mono/gtk-sharp-2.0/gsf-sharp.dll
%{_datadir}/gapi-2.0/gsf-api.xml
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
