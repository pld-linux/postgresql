%define beta 0

%{?beta:%define __os_install_post /usr/lib/rpm/brp-compress}
%{!?perl:%define perl 1}
%{!?tcl:%define tcl 1}
%{!?tkpkg:%define tkpkg 0}
%{!?odbc:%define odbc 1}
%{!?jdbc:%define jdbc 1}
%{!?test:%define test 0}
%{!?python:%define python 1}
%{!?pltcl:%define pltcl 1}
%{?forceplperl:%define plperl %{expand:forceplperl}}
%{!?forceplperl:%define forceplperl 0}
%{!?plperl:%define plperl 0}
%{!?ssl:%define ssl 1}
%{!?kerberos:%define kerberos 0}
%{!?nls:%define nls 1}
%{!?pam:%define pam 1}
%{!?sgmldocs:%define sgmldocs 0}


# Utility feature defines.
%{!?enable_mb:%define enable_mb 1}
%{!?pgaccess:%define pgaccess 0}

# Python major version.
%{expand:%%define pyver %(python -c 'import sys;print(sys.version[0:3])')%{nil}}
%{expand:%%define pynextver %(python -c 'import sys;print(float(sys.version[0:3])+0.1)')%{nil}}

Summary:	PostgreSQL client programs and libraries.
Name:		postgresql
Version:	7.2.3
Release:	0.1
License:	BSD
Group:		Applications/Databases
Source0:	ftp://ftp.postgresql.org/pub/source/v%{version}/%{name}-%{version}.tar.gz
Source3:	%{name}.init
Source4:	file-lists.tar.gz
Source6:	README.rpm-dist
Source7:	migration-scripts.tar.gz
Source8:	http://jdbc.postgresql.org/download/devpgjdbc1.jar
Source9:	http://jdbc.postgresql.org/download/devpgjdbc2.jar
Source10:	http://jdbc.postgresql.org/download/pgjdbc1.jar
Source11:	http://jdbc.postgresql.org/download/pgjdbc2.jar
Source15:	%{name}-bashprofile
Patch1:		%{name}-rpm.patch
Patch3:		%{name}-7.2rc2-betterquote.patch
Patch4:		%{name}-7.2-tighten.patch
Patch5:		%{name}-7.2.1-mktime.patch
Patch6:		%{name}-aurox.patch
Patch7:		%{name}-DESTDIR.patch
Buildrequires:	perl glibc-devel bison flex
Prereq:		/sbin/ldconfig initscripts
BuildPrereq:	perl
BuildPrereq:	readline-devel >= 4.0
BuildPrereq:	zlib-devel >= 1.0.4
BuildPrereq:	patch >= 2.5.4
Url:		http://www.postgresql.org/
Requires:	postgresql-libs = %{version}
%if %ssl
BuildPrereq:	openssl-devel
%endif
%if %kerberos
BuildPrereq:	krb5-devel
%endif
%if %nls
BuildPrereq:	gettext >= 0.10.36
%endif
Obsoletes:	postgresql-clients
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
# Obsolete the packages we are not building...
%if ! %{plperl}
Obsoletes:	postgresql-plperl
%endif
%if %{tcl}
Buildrequires:	tcl
%endif
%if ! %{tcl}
Obsoletes:	postgresql-tcl
%endif
%if ! %{tkpkg}
Obsoletes:	postgresql-tk
%endif
%if ! %{odbc}
Obsoletes:	postgresql-odbc
%endif
%if ! %{perl}
Obsoletes:	postgresql-perl
%endif
%if %{python}
BuildRequires:	python-devel
%endif
%if ! %{python}
Obsoletes:	postgresql-python
%endif
%if ! %{jdbc}
Obsoletes:	postgresql-jdbc
%endif
%if ! %{test}
Obsoletes:	postgresql-test
%endif
%if ! %{sgmldocs}
Obsoletes:	postgresql-docs
%endif
%if %{pam}
BuildRequires:	pam-devel
%endif

%description
PostgreSQL is an advanced Object-Relational database management system
(DBMS) that supports almost all SQL constructs (including
transactions, subselects and user-defined types and functions). The
postgresql package includes the client programs and libraries that
you'll need to access a PostgreSQL DBMS server. These PostgreSQL
client programs are programs that directly manipulate the internal
structure of PostgreSQL databases on a PostgreSQL server. These client
programs can be located on the same machine with the PostgreSQL
server, or may be on a remote machine which accesses a PostgreSQL
server over a network connection. This package contains the docs in
HTML for the whole package, as well as command-line utilities for
managing PostgreSQL databases on a PostgreSQL server.

If you want to manipulate a PostgreSQL database on a remote PostgreSQL
server, you need this package. You also need to install this package
if you're installing the postgresql-server package.

%package libs
Summary:	The shared libraries required for any PostgreSQL clients.
Group:		Applications/Databases
Provides:	libpq.so.2 libpq.so.2.0 libpq.so

%description libs
The postgresql-libs package provides the essential shared libraries
for any PostgreSQL client program or interface. You will need to
install this package to use any other PostgreSQL package or any
clients that need to connect to a PostgreSQL server.

%package server
Summary:	The programs needed to create and run a PostgreSQL server.
Group:		Applications/Databases
Prereq:		/usr/sbin/useradd /sbin/chkconfig
Requires:	postgresql = %{version} libpq.so
Requires:	postgresql-libs = %{version}

#------------
%if %sgmldocs
%package docs
Summary:	Extra documentation for PostgreSQL
Group:		Applications/Databases
%description docs
The postgresql-docs package includes the SGML source for the
documentation as well as the documentation in other formats, and some
extra documentation. Install this package if you want to help with the
PostgreSQL documentation project, or if you want to generate printed
documentation.
%endif

%package contrib
Summary:	Contributed source and binaries distributed with PostgreSQL
Group:		Applications/Databases
Requires:	libpq.so postgresql = %{version}
%description contrib
The postgresql-contrib package includes the contrib tree distributed
with the PostgreSQL tarball. Selected contrib modules are prebuilt.

%description server
The postgresql-server package includes the programs needed to create
and run a PostgreSQL server, which will in turn allow you to create
and maintain PostgreSQL databases. PostgreSQL is an advanced
Object-Relational database management system (DBMS) that supports
almost all SQL constructs (including transactions, subselects and
user-defined types and functions). You should install
postgresql-server if you want to create and maintain your own
PostgreSQL databases and/or your own PostgreSQL server. You also need
to install the postgresql package.

%package devel
Summary:	PostgreSQL development header files and libraries.
Group:		Development/Libraries
Requires:	postgresql-libs = %{version}

%description devel
The postgresql-devel package contains the header files and libraries
needed to compile C or C++ applications which will directly interact
with a PostgreSQL database management server and the ecpg Embedded C
Postgres preprocessor. You need to install this package if you want to
develop applications which will interact with a PostgreSQL server. If
you're installing postgresql-server, you need to install this package.

#------------
%if %plperl
%package plperl
Summary:	The PL/Perl procedural language for PostgreSQL.
Group:		Applications/Databases
Requires:	perl, postgresql = %{version}

%description plperl
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-plperl package contains the the PL/Perl
procedural language for the backend.
%endif

#------------
%if %tcl
%package tcl
Summary:	A Tcl client library, and the PL/Tcl procedural language for PostgreSQL.
Group:		Applications/Databases
Requires:	tcl >= 8.0

%description tcl
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-tcl package contains the libpgtcl client
library, the pg-enhanced pgtclsh, and the PL/Tcl procedural language
for the backend.
%endif

#------------
%if %tkpkg
%package tk
Summary:	Tk shell and tk-based GUI for PostgreSQL.
Group:		Applications/Databases
Requires:	tcl >= 8.0, tk >= 8.0

%description tk
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-tk package contains the pgaccess program.
Pgaccess is a graphical front end, written in Tcl/Tk, for the psql and
related PostgreSQL client programs.
%endif

#------------
%if %odbc
%package odbc
Summary:	The ODBC driver needed for accessing a PostgreSQL DB using ODBC.
Group:		Applications/Databases

%description odbc
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-odbc package includes the ODBC (Open DataBase
Connectivity) driver and sample configuration files needed for
applications to access a PostgreSQL database using ODBC.
%endif

#------------
%if %perl
%package perl
Summary:	Development module needed for Perl code to access a PostgreSQL DB.
Group:		Applications/Databases
Requires:	perl >= 5.004-4

%description perl
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-perl package includes a module for developers
to use when writing Perl code for accessing a PostgreSQL database.
%endif

#------------
%if %python
%package python
Summary:	Development module for Python code to access a PostgreSQL DB.
Group:		Applications/Databases
Requires:	python
Conflicts:	python < %pyver, python >= %pynextver


%description python
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-python package includes a module for developers
to use when writing Python code for accessing a PostgreSQL database.
%endif

#----------
%if %jdbc
%package jdbc
Summary:	Files needed for Java programs to access a PostgreSQL database.
Group:		Applications/Databases

%description jdbc
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-jdbc package includes the .jar file needed for
Java programs to access a PostgreSQL database.
%endif

#------------
%if %test
%package test
Summary:	The test suite distributed with PostgreSQL.
Group:		Applications/Databases
Requires:	postgresql = %{version}

%description test
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-test package includes the sources and pre-built
binaries of various tests for the PostgreSQL database management
system, including regression tests and benchmarks.
%endif

%prep
%setup -q

%patch1 -p1
#patch2 -p1
#patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7	-p1

#binary
rm contrib/spi/preprocessor/step1.e

%build

# Get file lists....
tar xzf %{SOURCE4}

#Commented out for testing on other platforms for now.
# If libtool installed, copy some files....
#if [ -d /usr/share/libtool ]
#then
#	cp /usr/share/libtool/config.* .
#fi

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS

# Strip out -ffast-math from CFLAGS....

CFLAGS=`echo $CFLAGS|xargs -n 1|grep -v ffast-math|xargs -n 100`

./configure --enable-locale --with-CXX --prefix=%{_prefix} --disable-rpath\
%if %beta
	--enable-debug \
	--enable-cassert \
%endif
%if %perl
	--with-perl \
%endif
%if %enable_mb
	--enable-multibyte \
%endif
%if %tcl
	--with-tcl \
%endif
%if %tkpkg
%else
	--without-tk \
%endif
%if %odbc
	--with-odbc \
%endif
	--enable-syslog\
%if %python
	--with-python \
%endif
%if %ssl
	--with-openssl \
%endif
%if %pam
	--with-pam \
%endif
%if %kerberos
	--with-krb5=/usr/kerberos \
%endif
%if %nls
	--enable-nls \
%endif
	--sysconfdir=/etc/pgsql \
	--mandir=%{_mandir} \
	--docdir=%{_docdir} \
	--includedir=%{_includedir} \
	--datadir=/usr/share/pgsql


make all


%if %test
	pushd src/test
	make all
	popd
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%if %perl
	make DESTDIR=$RPM_BUILD_ROOT -C src/interfaces/perl5 -f Makefile install

	# Get rid of the packing list generated by the perl Makefile, and build my own...
	find $RPM_BUILD_ROOT%{_libdir}/perl5 -name .packlist -exec rm -f {} \;
	find $RPM_BUILD_ROOT%{_libdir}/perl5 -type f -print | \
		sed -e "s|$RPM_BUILD_ROOT/|/|g"  | \
		sed -e "s|.*/man/.*|&\*|" > perlfiles.list
	find $RPM_BUILD_ROOT%{_libdir}/perl5 -type d -name Pg -print | \
		sed -e "s|$RPM_BUILD_ROOT/|%dir /|g" >> perlfiles.list

	# check and fixup Pg manpage location....
	if [ ! -e $RPM_BUILD_ROOT%{_mandir}/man3/Pg.* ]
	then
		install -d $RPM_BUILD_ROOT%{_mandir}/man3
		cp src/interfaces/perl5/blib/man3/Pg.3pm $RPM_BUILD_ROOT%{_mandir}/man3
	fi

	pushd src/interfaces
	install -d $RPM_BUILD_ROOT%{_datadir}/pgsql/perl5
	cp -a perl5/test.pl $RPM_BUILD_ROOT%{_datadir}/pgsql/perl5
	popd
	# remove perllocal.pod and Pg.bs from the file list - only occurs with 5.6

	perl -pi -e "s/^.*perllocal.pod$//" perlfiles.list
	perl -pi -e "s/^.*Pg.bs$//" perlfiles.list
	install -d $RPM_BUILD_ROOT%{_libdir}/perl5/site_perl/%{_arch}-linux/auto/Pg

%endif


# install dev headers.

make DESTDIR=$RPM_BUILD_ROOT install-all-headers

# copy over Makefile.global to the include dir....
install -m755 src/Makefile.global $RPM_BUILD_ROOT/usr/include/pgsql

%if %pgaccess
	# pgaccess installation
	pushd src/bin
	install -m 755 pgaccess/pgaccess $RPM_BUILD_ROOT/usr/bin
	mkdir -p $RPM_BUILD_ROOT/usr/share/pgsql/pgaccess
	install -m 644 pgaccess/main.tcl $RPM_BUILD_ROOT/usr/share/pgsql/pgaccess
	tar cf - pgaccess/lib pgaccess/images | tar xf - -C $RPM_BUILD_ROOT/usr/share/pgsql
	cp -a pgaccess/doc/html   ../../doc/pgaccess
	cp    pgaccess/demo/*.sql ../../doc/pgaccess
	popd
%endif

%if %jdbc
	# Java/JDBC
	# The user will have to set a CLASSPATH to find it here, but not sure where else to put it...

	# JDBC jars
	install -m 755 %{SOURCE8} $RPM_BUILD_ROOT/usr/share/pgsql
	install -m 755 %{SOURCE9} $RPM_BUILD_ROOT/usr/share/pgsql
	install -m 755 %{SOURCE10} $RPM_BUILD_ROOT/usr/share/pgsql
	install -m 755 %{SOURCE11} $RPM_BUILD_ROOT/usr/share/pgsql

%endif

# The initscripts....
# Redhat-style....
if [ -d /etc/rc.d/init.d ]
then
	install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
	install -m 755 %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/postgresql
	mv redhat-style-files.lst files.lst
fi

# SuSE-style....
# NOTE: SuSE stuff not yet fully implemented -- this is likely to not work yet.
# Putting SuSE-style stuff here
if [ -d /sbin/init.d ]
then
	# install the SuSE stuff...
	mv suse-style-files.lst files.lst
fi


# PGDATA needs removal of group and world permissions due to pg_pwd hole.
install -d -m 700 $RPM_BUILD_ROOT/var/lib/pgsql/data

# backups of data go here...
install -d -m 700 $RPM_BUILD_ROOT/var/lib/pgsql/backups

# postgres' .bash_profile
install -m 644 %{SOURCE15} $RPM_BUILD_ROOT/var/lib/pgsql/.bash_profile

%if %test
	# tests. There are many files included here that are unnecessary, but include
	# them anyway for completeness.
	mkdir -p $RPM_BUILD_ROOT/usr/lib/pgsql/test
	cp -a src/test/regress $RPM_BUILD_ROOT/usr/lib/pgsql/test
	install -m 0755 contrib/spi/refint.so $RPM_BUILD_ROOT/usr/lib/pgsql/test/regress
	install -m 0755 contrib/spi/autoinc.so $RPM_BUILD_ROOT/usr/lib/pgsql/test/regress
	pushd  $RPM_BUILD_ROOT/usr/lib/pgsql/test/regress/
	strip *.so
	popd
%endif

# Upgrade scripts.
pushd $RPM_BUILD_ROOT
tar xzf %{SOURCE7}
popd

# logrotate script removed until future release
#logrotate script source (which needs WORK)
#mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
#cp %{SOURCE8} $RPM_BUILD_ROOT/etc/logrotate.d/postgres
#chmod 0644 $RPM_BUILD_ROOT/etc/logrotate.d/postgres

# Fix some more documentation
# gzip doc/internals.ps
cp %{SOURCE6} README.rpm-dist
mv $RPM_BUILD_ROOT%{_docdir}/postgresql/html doc

# Build contrib stuff....
pushd contrib
make clean
make all
popd
# move the contrib tree to the right place after building....
cp -r contrib $RPM_BUILD_ROOT/usr/lib/pgsql
# We'll do more prep work in a later release.....

#more massaging

pushd $RPM_BUILD_ROOT/usr/lib/pgsql/contrib

# Get rid of useless makefiles
rm -f Makefile */Makefile

# array
pushd array
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/array|" *
popd

#  btree_gist
pushd btree_gist
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/btree_gist|" *.sql
popd

# chkpass
pushd chkpass
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/chkpass|" *.sql
popd

# cube
pushd cube
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/cube|" cube.sql
popd

# dblink
pushd dblink
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/dblink|" dblink.sql
popd

# earthdistance
pushd earthdistance
perl -pi -e "s|/usr/share/pgsql/contrib|/usr/lib/pgsql/contrib/earthdistance|" *.sql
popd

# fulltext
pushd fulltextindex
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/fulltextindex|" *.sql
popd

# fuzzystrmatch
pushd fuzzystrmatch
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/fuzzystrmatch|" *.sql
popd

# intarray
pushd intarray
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/intarray|" *.sql
popd

# isbn_issn
pushd isbn_issn
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/isbn_issn|" *.sql
popd

# lo
pushd lo
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/lo|" *.sql
popd

# miscutil
pushd miscutil
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/miscutil|" *.sql
popd

# noupdate
pushd noupdate
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/noupdate|" *.sql
popd

# pgcrypto
pushd pgcrypto
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/pgcrypto|" *.sql
perl -pi -e "s|/usr/lib/pgsql/contrib/pgcrypto/pgcrypto|/usr/lib/pgsql/contrib/pgcrypto/libpgcrypto|" *.sql
rm -f *.in *.o
popd

# pgstattuple
pushd pgstattuple
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/pgstattuple|" *.sql
popd

# rserv
pushd rserv
perl -pi -e "s|/usr/share/|/usr/lib/|" *
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib|" *
perl -pi -e "s|/usr/bin|/usr/lib/pgsql/contrib/rserv|" *
popd

# rtree_gist
pushd pgstattuple
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib|" *.sql
popd

# seg
pushd seg
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib|" *.sql
popd

# spi
pushd spi
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/spi|" *.sql
popd

# Don"t need these
rm -fr startscripts

# string
pushd string
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/string|" *.sql
popd

# tsearch
pushd tsearch
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/tsearch|" *.sql
popd

# userlock
pushd userlock
perl -pi -e "s|\\\$libdir|/usr/lib/pgsql/contrib/userlock|" *.sql
popd

popd

#more broken symlinks
rm -f $RPM_BUILD_ROOT/usr/lib/pgsql/contrib/pg_resetxlog/pg_crc.c $RPM_BUILD_ROOT/usr/lib/pgsql/contrib/pg_controldata/pg_crc.c
cp src/backend/utils/hash/pg_crc.c $RPM_BUILD_ROOT/usr/lib/pgsql/contrib/pg_resetxlog/pg_crc.c
ln $RPM_BUILD_ROOT/usr/lib/pgsql/contrib/pg_resetxlog/pg_crc.c $RPM_BUILD_ROOT/usr/lib/pgsql/contrib/pg_controldata/pg_crc.c

# Symlink libpq.so.2.0 to libpq.so.2 for backwards compatibility, until
# -soname patches are the norm.
pushd $RPM_BUILD_ROOT/usr/lib
ln -s libpq.so.2 libpq.so.2.0
popd

# arch backups should go in /usr/lib, not /usr/share
pushd $RPM_BUILD_ROOT
mkdir -p usr/lib/pgsql/backup
mv usr/share/pgsql/backup/pg_dumpall_new usr/lib/pgsql/backup/pg_dumpall_new
popd


%find_lang libpq
%find_lang pg_dump
%find_lang postgres
%find_lang psql

cat psql.lang pg_dump.lang > main.lst
cat postgres.lang files.lst > server.lst

%pre
# Need to make backups of some executables if an upgrade
# They will be needed to do a dump of the old version's database.
# All output redirected to /dev/null.

if [ $1 -gt 1 ]
then
   mkdir -p /usr/lib/pgsql/backup > /dev/null
   pushd /usr/bin > /dev/null
   cp -fp postmaster postgres pg_dump pg_dumpall psql /usr/lib/pgsql/backup > /dev/null 2>&1  || :
   popd > /dev/null
   pushd /usr/lib > /dev/null
   cp -fp libpq.* /usr/lib/pgsql/backup > /dev/null 2>&1 || :
   popd > /dev/null
fi

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%pre server
groupadd -g 26 -o -r postgres >/dev/null 2>&1 || :
useradd -M -n -g postgres -o -r -d /var/lib/pgsql -s /bin/bash \
	-c "PostgreSQL Server" -u 26 postgres >/dev/null 2>&1 || :
touch /var/log/pgsql
chown postgres.postgres /var/log/pgsql
chmod 0700 /var/log/pgsql


%post server
chkconfig --add postgresql
/sbin/ldconfig

%preun server
if [ $1 = 0 ] ; then
	chkconfig --del postgresql
fi

%postun server
/sbin/ldconfig
if [ $1 -ge 1 ]; then
  /sbin/service postgresql condrestart >/dev/null 2>&1
fi
if [ $1 = 0 ] ; then
	userdel postgres >/dev/null 2>&1 || :
	groupdel postgres >/dev/null 2>&1 || :
fi

%if %odbc
%post -p /sbin/ldconfig  odbc
%postun -p /sbin/ldconfig  odbc
%endif

%if %tcl
%post -p /sbin/ldconfig   tcl
%postun -p /sbin/ldconfig   tcl
%endif

%if %plperl
%post -p /sbin/ldconfig   plperl
%postun -p /sbin/ldconfig   plperl
%endif

%if %test
%post test
chown -R postgres.postgres /usr/share/pgsql/test >/dev/null 2>&1 || :
%endif

%clean
rm -rf $RPM_BUILD_ROOT
rm -f perlfiles.list

# Ok, we are dynamically generating some filelists.  These are by default
# under the BUILD/postgresql-x.y.z tree.

# Note that macros such as config are available in those lists.
# The lists differentiate between RedHat, SuSE, and others.

%files -f main.lst
%defattr(644,root,root,755)
%doc doc/FAQ doc/KNOWN_BUGS doc/MISSING_FEATURES doc/README*
%doc COPYRIGHT README HISTORY doc/bug.template
%doc README.rpm-dist
%doc doc/html
%attr(755,root,root) %{_bindir}/createdb
%attr(755,root,root) %{_bindir}/createlang
%attr(755,root,root) %{_bindir}/createuser
%attr(755,root,root) %{_bindir}/dropdb
%attr(755,root,root) %{_bindir}/droplang
%attr(755,root,root) %{_bindir}/dropuser
%attr(755,root,root) %{_bindir}/pg_dump
%attr(755,root,root) %{_bindir}/pg_dumpall
%attr(755,root,root) %{_bindir}/pg_encoding
%attr(755,root,root) %{_bindir}/pg_id
%attr(755,root,root) %{_bindir}/pg_restore
%attr(755,root,root) %{_bindir}/psql
%attr(755,root,root) %{_bindir}/vacuumdb
%{_mandir}/man1/createdb.1*
%{_mandir}/man1/createlang.1*
%{_mandir}/man1/createuser.1*
%{_mandir}/man1/dropdb.1*
%{_mandir}/man1/droplang.1*
%{_mandir}/man1/dropuser.1*
%{_mandir}/man1/pg_dump.1*
%{_mandir}/man1/pg_dumpall.1*
%{_mandir}/man1/psql.1*
%{_mandir}/man1/vacuumdb.1*
%{_mandir}/man1/pg_restore.1*
%{_mandir}/man7/*

%if %sgmldocs
%files docs
%defattr(644,root,root,755)
%doc doc/src/*
%endif

%files contrib
%defattr(644,root,root,755)
%dir %{_libdir}/pgsql/contrib/
%{_libdir}/pgsql/contrib/*

%files libs -f libpq.lang
%defattr(644,root,root,755)
%{_libdir}/libpq.so.*
%{_libdir}/libecpg.so.*
%{_libdir}/libpq++.so.*
%{_libdir}/libpgeasy.so.*

%files server -f server.lst
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/initdb
%attr(755,root,root) %{_bindir}/initlocation
%attr(755,root,root) %{_bindir}/ipcclean
%attr(755,root,root) %{_bindir}/pg_ctl
%attr(755,root,root) %{_bindir}/pg_passwd
%attr(755,root,root) %{_bindir}/postgres
%attr(755,root,root) %{_bindir}/postmaster
%{_mandir}/man1/initdb.1*
%{_mandir}/man1/initlocation.1*
%{_mandir}/man1/ipcclean.1*
%{_mandir}/man1/pg_ctl.1*
%{_mandir}/man1/pg_passwd.1*
%{_mandir}/man1/postgres.1*
%{_mandir}/man1/postmaster.1*
%{_datadir}/pgsql/postgres.bki
%{_datadir}/pgsql/postgres.description
%{_datadir}/pgsql/*.sample
%{_libdir}/pgsql/plpgsql.so
%dir %{_libdir}/pgsql
%dir %{_datadir}/pgsql
%attr(700,postgres,postgres) %dir %{_libdir}/pgsql/backup
%{_libdir}/pgsql/backup/pg_dumpall_new
%attr(700,postgres,postgres) %dir /var/lib/pgsql
%attr(700,postgres,postgres) %dir /var/lib/pgsql/data
%attr(700,postgres,postgres) %dir /var/lib/pgsql/backups
%attr(644,postgres,postgres) %config(noreplace) /var/lib/pgsql/.bash_profile

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_bindir}/ecpg
%attr(755,root,root) %{_bindir}/pg_config
%{_libdir}/libpq.so
%{_libdir}/libecpg.so
%{_libdir}/libpq++.so
%{_libdir}/libpgeasy.so
%{_libdir}/libpq.a
%{_libdir}/libecpg.a
%{_libdir}/libpq++.a
%{_libdir}/libpgeasy.a
%if %tcl
%{_libdir}/libpgtcl.a
%endif
%{_mandir}/man1/ecpg.1*
%{_mandir}/man1/pg_config.1*

%if %tcl
%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpgtcl.so.*
%{_libdir}/libpgtcl.so
%attr(755,root,root) %{_bindir}/pgtclsh
%attr(755,root,root) %{_bindir}/pltcl_delmod
%attr(755,root,root) %{_bindir}/pltcl_listmod
%attr(755,root,root) %{_bindir}/pltcl_loadmod
%{_mandir}/man1/pgtclsh.1*
%{_libdir}/pgsql/pltcl.so
%{_datadir}/pgsql/unknown.pltcl
%endif

%if %tkpkg
%files tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pgtksh
%{_mandir}/man1/pgtksh.1*
%endif

%if %pgaccess
%doc doc/pgaccess/*
/usr/share/pgsql/pgaccess
/usr/bin/pgaccess
%{_mandir}/man1/pgaccess.1*
%endif

%if %odbc
%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpsqlodbc.so*
%{_datadir}/pgsql/odbc.sql
%endif

%if %perl
%files -f perlfiles.list perl
%defattr(644,root,root,755)
%dir %{_libdir}/perl5/site_perl/%{_arch}-linux/auto
%{_datadir}/pgsql/perl5
%{_mandir}/man3/Pg.*
%{_libdir}/pgsql/plperl.so
%endif

%if %plperl
%files plperl
%defattr(644,root,root,755)
%{_libdir}/pgsql/plperl.so
%endif

%if %python
%files python
%defattr(644,root,root,755)
%doc src/interfaces/python/README src/interfaces/python/tutorial
%{_libdir}/python%{pyver}/site-packages/_pgmodule.so
%{_libdir}/python%{pyver}/site-packages/*.py
%{_libdir}/pgsql/plpython.so
%endif

%if %jdbc
%files jdbc
%defattr(644,root,root,755)
%{_datadir}/pgsql/*jar
%endif

%if %test
%files test
%defattr(644,root,root,755)
%attr(-,postgres,postgres) %{_libdir}/pgsql/test/*
%attr(-,postgres,postgres) %dir %{_libdir}/pgsql/test
%endif
