%define		snap 20051130
Summary:	Gsf# - libgsf .NET Binding
Summary(pl.UTF-8):	Gsf# - wiązanie .NET dla libgsf
Name:		dotnet-gsf-sharp
Version:	0.8.1
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://primates.ximian.com/~joe/gsf-sharp-%{version}.tar.gz
# Source0-md5:	92bb68612bdcd8ca3c475b3fee097968
Patch0:		%{name}-pkgconfig.patch
Patch1:		%{name}-sharp20.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10.0
BuildRequires:	libgsf-devel >= 1.14.1
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.13.8
BuildRequires:	monodoc >= 1.1.13
BuildRequires:	pkgconfig
Requires:	mono >= 1.1.13.8
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gsf# - libgsf .NET Binding.

%description -l pl.UTF-8
Gsf# - wiązanie .NET dla libgsf.

%package devel
Summary:	Gsf# development files
Summary(pl.UTF-8):	Pliki programistyczne Gsf#
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 2.10.0

%description devel
Gsf# development files.

%description devel -l pl.UTF-8
Pliki programistyczne Gsf#.

%package static
Summary:	Gsf# static library
Summary(pl.UTF-8):	Biblioteka statyczna Gsf#
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Gsf# static library.

%description static -l pl.UTF-8
Biblioteka statyczna Gsf#.

%prep
%setup -q -n gsf-sharp-%{version}
%patch -P0 -p1
%patch -P1 -p1

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
