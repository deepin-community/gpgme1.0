# This is a template.  The dist target uses it to create the real file.
Summary: GPGME - GnuPG Made Easy
Name: gpgme
Version: 1.18.0
Release: 1
URL: https://gnupg.org/gpgme.html
Source: https://www.gnupg.org/ftp/gcrypt/gpgme/%{name}-%{version}.tar.gz
Group: Development/Libraries
Copyright: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildRequires: make
Prereq: /sbin/ldconfig /sbin/install-info
Requires: gnupg

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG easier
for applications. It provides a High-Level Crypto API for encryption,
decryption, signing, signature verification and key management.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
./configure --prefix=/usr
make

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr infodir=$RPM_BUILD_ROOT%{_infodir}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -fr $RPM_BUILD_ROOT
make distclean

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/gpgme.info.gz %{_infodir}/dir
/sbin/install-info %{_infodir}/gpgme-python-howto.info.gz %{_infodir}/dir

%preun
if [ "$1" = 0 ]; then
 /sbin/install-info --delete %{_infodir}/gpgme.info.gz %{_infodir}/dir
 /sbin/install-info --delete %{_infodir}/gpgme-python-howto.info.gz %{_infodir}/dir
fi

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING COPYING.LESSER AUTHORS README INSTALL NEWS ChangeLog TODO THANKS
%attr(0755,root,root) %{_bindir}/gpgme-config
%attr(0755,root,root) %{_libdir}/*gpgme.so*
%attr(0755,root,root) %{_libdir}/*gpgme.la
%attr(0644,root,root) %{_libdir}/*gpgme.a
%{_includedir}/gpgme.h
%{_datadir}/aclocal/gpgme.m4
%{_infodir}/gpgme.info*
%{_infodir}/gpgme-python-howto.info*

%changelog
* Sat Aug 30 2003 Robert Schiele <rschiele@uni-mannheim.de>
- %{_infodir}/dir is not packaged, remove to prevent checking failure
* Mon Jul 01 2002 Wojciech Polak <polak@lodz.pdi.net>
- initial specfile release for GPGME.

# EOF
