# Makefile.am for GPGMEPP.
# Copyright (C) 2016 Bundesamt für Sicherheit in der Informationstechnik
# Software engineering by Intevation GmbH
#
# This file is part of GPGMEPP.
#
# GPGME-CL is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# GPGME-CL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA
lib_LTLIBRARIES = libqgpgme.la
EXTRA_DIST = QGpgmeConfig.cmake.in.in QGpgmeConfigVersion.cmake.in \
             qgpgme_debug.h qgpgme_version.h.in \
             QGpgmeConfig-w32.cmake.in.in

qgpgme_sources = \
    dataprovider.cpp \
    debug.cpp \
    job.cpp multideletejob.cpp qgpgmeadduseridjob.cpp \
    qgpgmeaddexistingsubkeyjob.cpp \
    qgpgmebackend.cpp qgpgmechangeexpiryjob.cpp qgpgmechangeownertrustjob.cpp \
    qgpgmechangepasswdjob.cpp qgpgmedecryptjob.cpp \
    qgpgmedecryptverifyjob.cpp qgpgmedeletejob.cpp qgpgmedownloadjob.cpp \
    qgpgmeencryptjob.cpp qgpgmeexportjob.cpp qgpgmeimportfromkeyserverjob.cpp \
    qgpgmeimportjob.cpp qgpgmekeygenerationjob.cpp qgpgmekeylistjob.cpp \
    qgpgmelistallkeysjob.cpp qgpgmenewcryptoconfig.cpp \
    qgpgmereceivekeysjob.cpp \
    qgpgmerefreshsmimekeysjob.cpp \
    qgpgmerevokekeyjob.cpp \
    qgpgmesetprimaryuseridjob.cpp \
    qgpgmesignencryptjob.cpp \
    qgpgmesignjob.cpp qgpgmesignkeyjob.cpp qgpgmeverifydetachedjob.cpp \
    qgpgmeverifyopaquejob.cpp qgpgmewkdlookupjob.cpp threadedjobmixin.cpp \
    qgpgmekeyformailboxjob.cpp qgpgme_debug.cpp \
    qgpgmetofupolicyjob.cpp qgpgmequickjob.cpp \
    defaultkeygenerationjob.cpp qgpgmewkspublishjob.cpp \
    qgpgmegpgcardjob.cpp changeexpiryjob.cpp encryptjob.cpp importjob.cpp \
    signencryptjob.cpp \
    dn.cpp cryptoconfig.cpp wkdlookupresult.cpp \
    util.cpp

# If you add one here make sure that you also add one in camelcase
qgpgme_headers= \
    abstractimportjob.h \
    addexistingsubkeyjob.h \
    adduseridjob.h \
    changeexpiryjob.h \
    changeownertrustjob.h \
    changepasswdjob.h \
    dataprovider.h \
    debug.h \
    decryptjob.h \
    decryptverifyjob.h \
    downloadjob.h \
    encryptjob.h \
    exportjob.h \
    hierarchicalkeylistjob.h \
    job.h \
    keyformailboxjob.h \
    multideletejob.h \
    protocol.h \
    qgpgme_export.h \
    qgpgmenewcryptoconfig.h \
    quickjob.h \
    receivekeysjob.h \
    revokekeyjob.h \
    setprimaryuseridjob.h \
    specialjob.h \
    signjob.h \
    signkeyjob.h \
    signencryptjob.h \
    verifyopaquejob.h \
    refreshkeysjob.h \
    cryptoconfig.h \
    deletejob.h \
    importfromkeyserverjob.h \
    importjob.h \
    keygenerationjob.h \
    keylistjob.h \
    listallkeysjob.h \
    verifydetachedjob.h \
    defaultkeygenerationjob.h \
    tofupolicyjob.h \
    wkdlookupjob.h \
    wkdlookupresult.h \
    wkspublishjob.h \
    gpgcardjob.h \
    dn.h

camelcase_headers= \
    AddExistingSubkeyJob \
    AddUserIDJob \
    AbstractImportJob \
    ChangeExpiryJob \
    ChangeOwnerTrustJob \
    ChangePasswdJob \
    DataProvider \
    Debug \
    DecryptJob \
    DecryptVerifyJob \
    DN \
    DownloadJob \
    EncryptJob \
    ExportJob \
    HierarchicalKeyKistJob \
    Job \
    MultiDeleteJob \
    Protocol \
    QGpgMENewCryptoConfig \
    QuickJob \
    ReceiveKeysJob \
    RevokeKeyJob \
    SetPrimaryUserIDJob \
    SpecialJob \
    SignJob \
    SignKeyJob \
    SignEncryptJob \
    VerifyOpaqueJob \
    RefreshKeysJob \
    CryptoConfig \
    DeleteJob \
    ImportFromKeyserverJob \
    ImportJob \
    KeyGenerationJob \
    KeyListJob \
    ListAllKeysJob \
    VerifyDetachedJob \
    KeyForMailboxJob \
    DefaultKeyGenerationJob \
    WKDLookupJob \
    WKDLookupResult \
    WKSPublishJob \
    TofuPolicyJob \
    GpgCardJob

private_qgpgme_headers = \
    qgpgme_export.h \
    protocol_p.h \
    job_p.h \
    qgpgmeaddexistingsubkeyjob.h \
    qgpgmeadduseridjob.h \
    qgpgmebackend.h \
    qgpgmechangeexpiryjob.h \
    qgpgmechangeownertrustjob.h \
    qgpgmechangepasswdjob.h \
    qgpgmedecryptjob.h \
    qgpgmedecryptverifyjob.h \
    qgpgmedeletejob.h \
    qgpgmedownloadjob.h \
    qgpgmeencryptjob.h \
    qgpgmeexportjob.h \
    qgpgmeimportfromkeyserverjob.h \
    qgpgmeimportjob.h \
    qgpgmekeygenerationjob.h \
    qgpgmekeylistjob.h \
    qgpgmelistallkeysjob.h \
    qgpgmereceivekeysjob.h \
    qgpgmerefreshsmimekeysjob.h \
    qgpgmerevokekeyjob.h \
    qgpgmesetprimaryuseridjob.h \
    qgpgmesignencryptjob.h \
    qgpgmesignjob.h \
    qgpgmesignkeyjob.h \
    qgpgmeverifydetachedjob.h \
    qgpgmeverifyopaquejob.h \
    qgpgmewkdlookupjob.h \
    qgpgmekeyformailboxjob.h \
    qgpgmewkspublishjob.h \
    qgpgmetofupolicyjob.h \
    qgpgmegpgcardjob.h \
    qgpgmequickjob.h \
    threadedjobmixin.h \
    util.h

qgpgme_moc_sources = \
    abstractimportjob.moc \
    addexistingsubkeyjob.moc \
    adduseridjob.moc \
    changeexpiryjob.moc \
    changeownertrustjob.moc \
    changepasswdjob.moc \
    decryptjob.moc \
    decryptverifyjob.moc \
    deletejob.moc \
    downloadjob.moc \
    encryptjob.moc \
    exportjob.moc \
    hierarchicalkeylistjob.moc \
    importfromkeyserverjob.moc \
    importjob.moc \
    job.moc \
    keygenerationjob.moc \
    keylistjob.moc \
    listallkeysjob.moc \
    multideletejob.moc \
    qgpgmeaddexistingsubkeyjob.moc \
    qgpgmeadduseridjob.moc \
    qgpgmechangeexpiryjob.moc \
    qgpgmechangeownertrustjob.moc \
    qgpgmechangepasswdjob.moc \
    qgpgmedecryptjob.moc \
    qgpgmedecryptverifyjob.moc \
    qgpgmedeletejob.moc \
    qgpgmedownloadjob.moc \
    qgpgmeencryptjob.moc \
    qgpgmeexportjob.moc \
    qgpgmeimportfromkeyserverjob.moc \
    qgpgmeimportjob.moc \
    qgpgmekeygenerationjob.moc \
    qgpgmekeylistjob.moc \
    qgpgmelistallkeysjob.moc \
    qgpgmereceivekeysjob.moc \
    qgpgmerefreshsmimekeysjob.moc \
    qgpgmerevokekeyjob.moc \
    qgpgmesetprimaryuseridjob.moc \
    qgpgmesignencryptjob.moc \
    qgpgmesignjob.moc \
    qgpgmesignkeyjob.moc \
    qgpgmeverifydetachedjob.moc \
    qgpgmeverifyopaquejob.moc \
    qgpgmewkdlookupjob.moc \
    qgpgmewkspublishjob.moc \
    tofupolicyjob.moc \
    qgpgmetofupolicyjob.moc \
    receivekeysjob.moc \
    refreshkeysjob.moc \
    revokekeyjob.moc \
    setprimaryuseridjob.moc \
    signencryptjob.moc \
    signjob.moc \
    signkeyjob.moc \
    specialjob.moc \
    verifydetachedjob.moc \
    verifyopaquejob.moc \
    wkdlookupjob.moc \
    keyformailboxjob.moc \
    wkspublishjob.moc \
    qgpgmekeyformailboxjob.moc \
    defaultkeygenerationjob.moc \
    quickjob.moc \
    qgpgmequickjob.moc \
    gpgcardjob.moc \
    qgpgmegpgcardjob.moc

qgpgmeincludedir = $(includedir)/qgpgme
qgpgmeinclude_HEADERS = $(qgpgme_headers)
camelcaseincludedir = $(includedir)/QGpgME
camelcaseinclude_HEADERS = $(camelcase_headers)
nodist_qgpgmeinclude_HEADERS = qgpgme_version.h

libqgpgme_la_SOURCES = $(qgpgme_sources) $(qgpgme_headers) $(private_qgpgme_headers)

AM_CPPFLAGS = -I$(top_srcdir)/lang/cpp/src -I$(top_builddir)/src \
              @GPGME_QT_CFLAGS@ @GPG_ERROR_CFLAGS@ @LIBASSUAN_CFLAGS@ \
              -DBUILDING_QGPGME -Wsuggest-override \
              -Wzero-as-null-pointer-constant

libqgpgme_la_LIBADD = ../../cpp/src/libgpgmepp.la ../../../src/libgpgme.la \
                       @LIBASSUAN_LIBS@ @GPG_ERROR_LIBS@ @GPGME_QT_LIBS@
libqgpgme_la_LDFLAGS = -no-undefined -version-info \
    @LIBQGPGME_LT_CURRENT@:@LIBQGPGME_LT_REVISION@:@LIBQGPGME_LT_AGE@

if HAVE_MACOS_SYSTEM
libsuffix=.dylib
else
libsuffix=.so
endif

if HAVE_W32_SYSTEM
QGpgmeConfig.cmake: QGpgmeConfig-w32.cmake.in
	sed -e 's|[@]resolved_bindir@|$(bindir)|g' < "$<" | \
	sed -e 's|[@]resolved_libdir@|$(libdir)|g' | \
	sed -e 's|[@]resolved_includedir@|$(includedir)|g' > $@
else
QGpgmeConfig.cmake: QGpgmeConfig.cmake.in
	sed -e 's|[@]resolved_libdir@|$(libdir)|g' < "$<" | \
	sed -e 's|[@]libsuffix@|$(libsuffix)|g' | \
	sed -e 's|[@]resolved_includedir@|$(includedir)|g' > $@
endif

$(camelcase_headers): Makefile.am
	echo -n "#include \"qgpgme/" > "$@"
	echo -n "$@" | tr '[:upper:]' '[:lower:]' >> "$@"
	echo ".h\"" >> "$@"

install-cmake-files: QGpgmeConfig.cmake QGpgmeConfigVersion.cmake
	-$(INSTALL) -d $(DESTDIR)$(libdir)/cmake/QGpgme
	$(INSTALL) -m 644 QGpgmeConfig.cmake \
        $(DESTDIR)$(libdir)/cmake/QGpgme/QGpgmeConfig.cmake
	$(INSTALL) -m 644 QGpgmeConfigVersion.cmake \
        $(DESTDIR)$(libdir)/cmake/QGpgme/QGpgmeConfigVersion.cmake

uninstall-cmake-files:
	-rm $(DESTDIR)$(libdir)/cmake/QGpgme/QGpgmeConfigVersion.cmake
	-rm $(DESTDIR)$(libdir)/cmake/QGpgme/QGpgmeConfig.cmake
	-rmdir $(DESTDIR)$(libdir)/cmake/QGpgme/

install-data-local: install-cmake-files

uninstall-local: uninstall-cmake-files

BUILT_SOURCES = $(qgpgme_moc_sources) $(camelcase_headers)

CLEANFILES = $(qgpgme_moc_sources) $(camelcase_headers) QGpgmeConfig.cmake \
             qgpgme_version.h QGpgmeConfig.cmake.in \
             QGpgmeConfigVersion.cmake

nodist_libqgpgme_la_SOURCES = $(qgpgme_moc_sources)

.h.moc:
	$(MOC) `test -f '$<' || echo '$(srcdir)/'`$< -o $@
