%include	/usr/lib/rpm/macros.perl
Summary:	PostgreSQL Data Base Management System
Summary(de):	PostgreSQL Datenbankverwaltungssystem
Summary(fr):	Sysème de gestion de base de données PostgreSQL
Summary(pl):	PostgreSQL system bazodanowy
Summary(tr):	Veri Tabaný Yönetim Sistemi
Name:		postgresql
Version:	7.0.3
Release:	1
License:	BSD
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Source0:	ftp://ftp.postgresql.org/pub/source/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	pgsql-Database-HOWTO-html.tar.gz
Source3:	%{name}.sysconfig
Patch0:		%{name}-opt.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-perl.patch
Patch3:		%{name}-python.patch
Patch4:		%{name}-no_libnsl.patch
Patch5:		%{name}-pgaccess-typo.patch
URL:		http://www.postgresql.org/
Prereq:		/sbin/chkconfig
Requires:	rc-scripts
BuildRequires:	autoconf
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	rpm-perlprov
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	%{name}-libs = %{version}
Obsoletes:	postgresql-server
Obsoletes:	postgresql-test

%define		pgsqldir	%{_libdir}/pgsql/sql
%define		pgmoduledir	%{_libdir}/pgsql/modules


%description
PostgreSQL Data Base Management System (formerly known as Postgres,
then as Postgres95).

PostgreSQL is an enhancement of the POSTGRES database management
system, a next-generation DBMS research prototype. While PostgreSQL
retains the powerful data model and rich data types of POSTGRES, it
replaces the PostQuel query language with an extended subset of SQL.
PostgreSQL is free and the complete source is available.

PostgreSQL development is being performed by a team of Internet
developers who all subscribe to the PostgreSQL development mailing
list. The current coordinator is Marc G. Fournier
(scrappy@postgreSQL.org). This team is now responsible for all current
and future development of PostgreSQL.

The authors of PostgreSQL 1.01 were Andrew Yu and Jolly Chen. Many
others have contributed to the porting, testing, debugging and
enhancement of the code. The original Postgres code, from which
PostgreSQL is derived, was the effort of many graduate students,
undergraduate students, and staff programmers working under the
direction of Professor Michael Stonebraker at the University of
California, Berkeley.

The original name of the software at Berkeley was Postgres. When SQL
functionality was added in 1995, its name was changed to Postgres95.
The name was changed at the end of 1996 to PostgreSQL.

PostgreSQL runs on Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD,
and most flavours of Unix.

%description -l de
PostgreSQL Datenbank-Managementsystem (früher als Postgres, dann als
Postgres95 bekannt).

PostgreSQL ist eine Verbesserung des POSTGRES-DB-Managementsystems,
ein DBMS-Forschungsprototyp der nächsten Generation. Während es das
leistungsfähige Datenmodell und die reichhaltigen Datentypen von
POSTGRES beibehält, ersetzt es die PostQuel-Abfragesprache durch ein
Subset von SQL. PostgreSQL ist gratis, der gesamte Quellcode ist
verfügbar.

Ein Team von Internet-Entwicklern befaßt sich mit PostgreSQL. Sie alle
sind auf der PostgreSQL-Entwickleradreßliste. Koordinator ist Marc G.
Fournier (scrappy@postgreSQL.org). Das Team ist verantwortlich für
alle aktuellen und künftigen Entwicklungen von PostgreSQL.

Die Autoren von PostgreSQL 1.01 waren Andrew Yu und Jolly Chen.
Zahlreiche andere haben zur Portierung, zum Testen, Debugging und zur
Verbesserung des Code beigetragen. Den Original-Postgres-Code, von dem
sich PostgreSQL ableitet, verdanken wir der Arbeit vieler Doktoranden,
Studenten und Programmierern unter der Leitung von Professor Michael
Stonebraker an der University of California, Berkeley.

Der ursprüngliche Name war Postgres. Als 1995 SQL-Funktionalität
hinzukam, wurde der Name in Postgres95 geändert. Ende 1996 schließlich
entschied man sich für PostgreSQL.

PostgreSQL läuft auf Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD
und den meisten Unix-Systemen.

%description -l fr
Système de gestion de bases de données PostgreSQL (D'abord nommé
Postgres, puis Postgres95).

PostgreSQL est une amélioration du système de gestion de bases de
données POSTGRES, un prototype de recherche de la génération suivant
DBMS. Tout en conservant le puissant modèle de donnée de et les types
de donée riches de Postgres, il remplace le langage de requêtes de
Postgres par un sous ensemble etendu de commandes SQL. PosrgreSQL est
libre, et ses sources sont disponibles.

Le développement de PostgreSQL est actuellement réalisé via internet
parune équipe de développeurs inscrits sur la mailing-list de
développement de PostgreSQL. Le coordinateur actuel est Marc G
Fournier (scrappy@postgreSQL.org). Cette équipe est responsable du
développemen actuel et à venir de PostgreSQL.

Les auteurs de PostgreSQL 1.01 étaient Andrew Yu et Jolly Chen.
Beaucoup d'autres ont contribué au portage, au test, au débogage et à
l'amélioration du code. Le code original de Postgres, duquel
PostgreSQL est dérivé, a été l'oeuvre d'étudiants de haut niveau, de
moins haut niveau, et de programmeurs travaillant sous la direction du
professeur Michael Stonebraker à l'université de Berkeley Californie.

Le nom original du logiciel était Postgres. Quand les fonctionnalitées
SQL furent ajoutées en 1995, son nom est devenu Postgres95. Il a été
rebaptisé PostgreSQL en 1996.

PostgreSQL tourne sur Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD,
et la plupart des Unix.

%description -l pl
PostgreSQL System Zarz±dzania Baz± Danych (dawniej znany jako
Postgres, nastêpnie jako Postgres95).

PostgreSQL mo¿e byæ uruchominy pod nastêpuj±cymi systemami: Solaris,
SunOS, HPUX, AIX, Linux, Irix, FreeBSD i innych systemach Unix.

%description -l tr
PostgreSQL, POSTGRES'den türemiþ bir veri tabaný yönetim sistemidir
(DBMS). Güçlü veri modeli ve zengin POSTGRES veri tiplerini
desteklerken SQL'in geniþletilmiþ bir altkümesi yerine PostQuel
sorgulama dilini koyar.

%package devel
Summary:	PostgreSQL development header files and libraries
Summary(de):	PostgreSQL-Entwicklungs-Header-Dateien und Libraries 
Summary(fr):	En-têtes et bibliothèques de développement PostgreSQL
Summary(pl):	PostgreSQL - pliki nag³ówkowe i biblioteki
Summary(tr):	PostgreSQL baþlýk dosyalarý ve kitaplýklar
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-libs = %{version}

%description devel
This package contains header files and libraries required to compile
applications that are talking directly to the PostgreSQL backend
server.

%description -l de devel
Dieses Paket enthält die Header-Dateien und Libraries, die zum
Kompilieren von Applikationen notwendig sind, die direkt mit dem
PostgreSQL-Backend-Server kommunizieren.

%description -l fr devel
Ce package contient les fichiers d'en-tête et les bibliothéques
nécessaires pour compiler des applications ayant des échanges directs
avec le serveur du backend PostgreSQL.

%description -l pl devel
Pakiet zawiera nag³ówki oraz biblioteki wymagane do kompilacji
aplikacji ³±cz±cych siê bezpo¶rednio z serwerem PostgreSQL.

%description -l tr devel
Bu paket, PostgreSQL sunucusuyla konuþacak yazýlýmlar geliþtirmek için
gereken baþlýk dosyalarýný ve kitaplýklarý içerir.

%package clients
Summary:	clients needed to access a PostgreSQL server
Summary(pl):	klienci wymagani do dostêpu do serwera PostgreSQL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name}-libs = %{version}

%description clients
This package includes only the clients and client libraries needed to
access an PostgreSQL server. The server is included in the main
package. If all you need is to connect to another PostgreSQL server,
the this is the only package you need to install.

In this package there are client libraries available for C and C++, as
well as several command-line utilities you can use to manage your
databases on a remote PostgreSQL server.

%description -l pl clients
Pakiet zawiera klientów oraz biblioteki niezbêdne dla dostêpu do
serwera PostgreSQL. Serwer znajduje siê w g³ównym pakiecie.

%package perl
Summary:	Perl interface to PostgreSQL database
Summary(pl):	Interface dla Perl'a umo¿liwiaj±cy dostêp do baz PostgreSQL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	perl >= 5.004
Requires:	%{name}-libs = %{version}

%description perl
This package includes only perl modules needed to access an PostgreSQL
server.

%description -l pl perl
Pakiet ten zawiera tylko modu³y Perl'a wymagane dla dostêpu do serwera
PostgreSQL.

%package python
Summary:	The python-based client programs needed for accessing a PostgreSQL server
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python >= 1.5
Requires:	%{name}-libs = %{version}

%description python
postgresql-python includes the python-based client programs and client
libraries that you'll need to access a PostgreSQL database management
system server.

%package doc
Summary:	Documentation for PostgreSQL
Summary(pl):	Dodatkowa dokumantacja dla PostgreSQL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych

%description doc
This package includes documentation and HOWTO for programmer, admin
etc., in HTML format.

%description -l pl doc
Pakiet ten zawiera dokumentacjê oraz HOWTO m.in. dla programistów,
administratorów w formacie HTML.

%package libs
Summary:	PostgreSQL libraries
Summary(pl):	Biblioteki dzielone programu PostgreSQL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki

%description libs
PostgreSQL libraries.

%description libs -l pl
Biblioteki dzielone programu PostgreSQL.

%package static
Summary:	PostgreSQL static libraries
Summary(pl):	Biblioteki statyczne programu PostgreSQL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
PostgreSQL static libraries.

%description -l pl static
Biblioteki statyczne programu PostgreSQL.

%package c++
Summary:	C++ interface to PostgreSQL
Summary(pl):	Interface C++ do PostgreSQL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name}-libs = %{version}

%description c++
This package includes library for C++ interface to PostgreSQL.

%description -l pl c++
Pakiet ten zawiera biblioteki dla interface'u C++ do PostgreSQL.

%package c++-devel
Summary:	C++ interface to PostgreSQL - development part
Summary(pl):	Interface C++ do PostgreSQL - cze¶æ programistyczna
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name}-c++ = %{version}
Requires:	%{name}-devel = %{version}

%description c++-devel
This package includes library and header files for C++ interface.

%description -l pl c++-devel
Pakiet ten zawiera biblioteki i pliki nag³ówkowe dla interface'u C++.

%package c++-static
Summary:	C++ interface to PostgreSQL - static libraries
Summary(pl):	Interface C++ do PostgreSQL - biblioteki statyczne
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name}-c++-devel = %{version}

%description c++-static
This package includes static library for interface C++.

%description -l pl c++-static
Pakiet ten zawiera biblioteki statyczne dla interface'u C++.

%package odbc
Summary:	ODBC interface to PostgreSQL
Summary(pl):	Interface ODBC do PostgreSQL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name}-libs = %{version}

%description odbc
This package includes library for interface ODBC.

%description -l pl odbc
Pakiet ten zawiera biblioteki dla interface'u ODBC.

%package odbc-devel
Summary:	ODBC interface to PostgreSQL - development part
Summary(pl):	Interface ODBC do PostgreSQL - cze¶æ programistyczna
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name}-odbc = %{version}
Requires:	%{name}-devel = %{version}

%description odbc-devel
This package includes library and header files for interface ODBC.

%description -l pl odbc-devel
Pakiet ten zawiera biblioteki i pliki nag³ówkowe dla interface'u ODBC.

%package odbc-static
Summary:	ODBC interface to PostgreSQL - static libraries
Summary(pl):	Interface ODBC do PostgreSQL - biblioteki statyczne
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name}-odbc-devel = %{version}

%description odbc-static
This package includes static library for interface ODBC.

%description -l pl odbc-static
Pakiet ten zawiera biblioteki statyczne dla interface'u ODBC.

%package -n pgaccess
Summary:	A free graphical database management tool for PostgreSQL.
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name}-tcl = %{version}

%description -n pgaccess
A free graphical database management tool for PostgreSQL.

%package tcl
Summary:	tcl interface for PostgreSQL
Summary(pl):	tcl interface dla PostgreSQL
Group:		Development/Languages/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(pl):	Programowanie/Jêzyki/Tcl
Requires:	%{name}-libs = %{version}

%description tcl
tcl interface for PostgreSQL.

%description tcl -l pl
tcl interface dla PostgreSQL.

%package tcl-devel
Summary:	Development part of tcl interface for PostgreSQL
Summary(pl):	Czê¶æ dla programistów interafece tcl dla PostgreSQL
Group:		Development/Languages/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(pl):	Programowanie/Jêzyki/Tcl
Requires:	%{name}-tcl = %{version}
Requires:	%{name}-devel = %{version}

%description tcl-devel
Development part of tcl interface for PostgreSQL.

%description tcl-devel -l pl
Czê¶æ dla programistów interafece tcl dla PostgreSQL.

%package tcl-static
Summary:	Static libraries of tcl interface for PostgreSQL
Summary(pl):	Biblioteki statyczne interafece tcl dla PostgreSQL
Group:		Development/Languages/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(pl):	Programowanie/Jêzyki/Tcl
Requires:	%{name}-tcl-devel = %{version}

%description tcl-static
Static libraries of tcl interface for PostgreSQL

%description tcl-devel -l pl
Biblioteki statyczne interafece tcl dla PostgreSQL

%package module-datetime
Summary:	Some useful datetime functions for PostgreSQL
Summary(pl):	Kilka u¿ytecznych funkcji operuj±cych na dacie i czasie dla PostgreSQL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name} = %{version}

%description module-datetime
Some useful datetime function for PostgreSQL such as:
- hhmm_in(opaque)
- hhmm_out(opaque)
- hhmm(time)
- time_difference(time,time)
- time_hours(time)
- time_minutes(time)
- time_seconds(time)
- as_minutes(time)
- as_seconds(time)
- date_day(date)
- date_month(date)
- date_year(date)
- currenttime()
- currentdate() To enable them you need to execute
  datetime_function.sql script. You can found it in /usr/share/pgsql/sql
  directory.

%description module-datetime -l pl
Kilka u¿ytecznych funkcji operuj±cych na dacie i czasie dla
PostgreSQL.
- hhmm_in(opaque)
- hhmm_out(opaque)
- hhmm(time)
- time_difference(time,time)
- time_hours(time)
- time_minutes(time)
- time_seconds(time)
- as_minutes(time)
- as_seconds(time)
- date_day(date)
- date_month(date)
- date_year(date)
- currenttime()
- currentdate() Po wykonaniu skryptu datetime_function.sql mo¿na
  u¿ywaæ tych funkcji z poziomu zapytañ SQL. Skrypt ten znajduje siê w
  katalogu /usr/share/pgsql/sql.

%package module-plpgsql
Summary:	PL/pgSQL - PostgreSQL procedural language
Summary(pl):	PL/pgSQL jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name} = %{version}

%description module-plpgsql
From PostgreSQL documentation.

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/pgSQL procedural language for your database you have to
run createlang command.

%description module-plpgsql -l pl
Z dokumentacji PostgreSQL.

Postgres ma wsparcie dla jêzyków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurê wyzwalacza lub funkcjê w jêzyku
proceduralnym, baza danych nie ma pojêcia jak interpretowaæ tego typu
funkcjê. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak j± wykonaæ. Interpreter jest odpowiedni±, specjaln±
funkcj±, która jest skompilowana w obiekt dzielony i ³adowany w razie
potrzeby.

Za pomoc± komendy createlang mo¿na dodaæ wsparcie dla jêzyka
proceduralnego PL/pgSQL dla swojej bazy danych.

%package module-pltcl
Summary:	PL/TCL - PostgreSQL procedural language
Summary(pl):	PL/TCL jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name} = %{version}

%description module-pltcl
From PostgreSQL documentation.

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/TCL procedural language for your database you have to run
createlang command.

%description module-pltcl -l pl
Z dokumentacji PostgreSQL.

Postgres ma wsparcie dla jêzyków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurê wyzwalacza lub funkcjê w jêzyku
proceduralnym, baza danych nie ma pojêcia jak interpretowaæ tego typu
funkcjê. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak j± wykonaæ. Interpreter jest odpowiedni±, specjaln±
funkcj±, która jest skompilowana w obiekt dzielony i ³adowany w razie
potrzeby.

Za pomoc± komendy createlang mo¿na dodaæ wsparcie dla jêzyka
proceduralnego PL/TCL dla swojej bazy danych.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# Erase all CVS dir
rm -fR `find contrib/ -type d -name CVS`

%build
PATH=$PATH:. ; export PATH
cd src


# NOTE: this doesn't work. 
#CONFIGURE_OPT=%{pgsql_with_locale?: "--enable-locale"}
#CONFIGURE_OPT="$CONFIGURE_FLAGS %{pgsql_with_unicode?: --with-mulitbyte=UNICODE}"

aclocal
autoconf
%configure \
%ifarch %{ix86}
	--with-template=linux_i386 \
%else
	--with-template=linux_%{_target_cpu} \
%endif
	--enable-hba \
	--with-odbc \
	--with-odbcinst=%{_sysconfdir} \
	--with-tcl \
	--with-tk \
	--with-python \
	--with-x \
	--with-perl $CONFIGURE_OPT

%{__make} OPT="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}" \
	  TEMPLATEDIR=%{_libdir}/pgsql

cd ..
%{__make} all PGDOCS=unpacked -C doc

# remake pgaccess
make -C src/bin/pgaccess clean pgaccess POSTGRESDIR=/usr/lib

# for datetime functions
make -C contrib/datetime LIBDIR=%{_libdir}/pgsql

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig} \
        $RPM_BUILD_ROOT/var/{lib/pgsql,log} \
	$RPM_BUILD_ROOT%{_libdir}/pgsql/{modules,sql}

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	TEMPLATEDIR=%{_libdir}/pgsql \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3

%{__make} -C doc install DESTDIR=$RPM_BUILD_ROOT
touch $RPM_BUILD_ROOT/var/log/pgsql

# pgaccess 
ln -sf . $RPM_BUILD_ROOT%{_libdir}/pgaccess/lib

# for datetime functions
%{__make} -C contrib/datetime install LIBDIR=$RPM_BUILD_ROOT%{_libdir}/pgsql

# Move PL/pgSQL procedural language to %{pgmoduledir}
( cd $RPM_BUILD_ROOT%{_libdir}
  mv -f plpgsql.so $RPM_BUILD_ROOT%{pgmoduledir}
)

# Move PL/TCL procedural language to %{pgmoduledir}
( cd $RPM_BUILD_ROOT%{_libdir}
  mv -f pltcl.so $RPM_BUILD_ROOT%{pgmoduledir}
)

# For Perl interface
( cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Pg
  mv -f .packlist .packlist.old
  sed -e "s|$RPM_BUILD_ROOT/|/|g" -e "s|./||" < .packlist.old > .packlist
  rm -f .packlist.old
)

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/postgresql
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/postgresql

install -d howto
( cd howto
  tar xzf $RPM_SOURCE_DIR/pgsql-Database-HOWTO-html.tar.gz
)

# Install all header files. They are required
# by executor/spi.h and commands/trigger.h

( cd src/include
  cp -rf * $RPM_BUILD_ROOT%{_includedir}/pgsql
)

%pre
getgid postgres >/dev/null 2>&1 || /usr/sbin/groupadd -g 88 -r -f postgres
id postgres >/dev/null 2>&1 || /usr/sbin/useradd -M -o -r -u 88 \
	-d /var/lib/pgsql -s /bin/sh -g postgres \
	-c "PostgreSQL Server" postgres

%post
/sbin/chkconfig --add postgresql

if [ -r /var/lock/subsys/postmaster ]; then
	/etc/rc.d/init.d/postgresql restart >&2
else
	echo "Run \"/etc/rc.d/init.d/postgresql start\" to start postgresql server."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/postmaster ]; then
		/etc/rc.d/init.d/postgresql stop
	fi
	/sbin/chkconfig --del postgresql
fi

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post   tcl -p /sbin/ldconfig
%postun tcl -p /sbin/ldconfig

%post   clients -p /sbin/ldconfig
%postun clients -p /sbin/ldconfig

%post   c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%post   odbc -p /sbin/ldconfig
%postun odbc -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT
rm -f /tmp/tmp_perl_info

%files
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/*

%attr(755,root,root) %{_bindir}/createdb
%attr(755,root,root) %{_bindir}/createuser
%attr(755,root,root) %{_bindir}/dropdb
%attr(755,root,root) %{_bindir}/dropuser
%attr(755,root,root) %{_bindir}/initdb
%attr(755,root,root) %{_bindir}/initlocation
%attr(755,root,root) %{_bindir}/pg_passwd
%attr(755,root,root) %{_bindir}/pg_version
%attr(755,root,root) %{_bindir}/postgres
%attr(755,root,root) %{_bindir}/postmaster
%attr(755,root,root) %{_bindir}/ipcclean
%attr(755,root,root) %{_bindir}/createlang
%attr(755,root,root) %{_bindir}/droplang

%dir %{_libdir}/pgsql
%dir %{_libdir}/pgsql/modules
%dir %{_libdir}/pgsql/sql
%{_libdir}/pgsql/*.source 
%{_libdir}/pgsql/*.sample
%{_libdir}/pgsql/*.description

%attr(750,postgres,postgres) %dir /var/lib/pgsql
%attr(640,postgres,postgres) %config(noreplace) %verify(not md5 size mtime) /var/log/pgsql

%{_mandir}/man1/createdb.1*
%{_mandir}/man1/createlang.1*
%{_mandir}/man1/createuser.1*
%{_mandir}/man1/dropdb.1*
%{_mandir}/man1/droplang.1*
%{_mandir}/man1/dropuser.1*
%{_mandir}/man1/initdb.1*
%{_mandir}/man1/initlocation.1*
%{_mandir}/man1/pg_passwd.1*
%{_mandir}/man1/postgres.1*
%{_mandir}/man1/postmaster.1*
%{_mandir}/man1/ipcclean.1*

%doc contrib 
%doc doc/FAQ doc/FAQ_Linux doc/README* 
%doc COPYRIGHT README HISTORY doc/bug.template

%files doc
%defattr(644,root,root,755)
%doc doc/unpacked/*
%doc howto

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpq.so.*.*
%attr(755,root,root) %{_libdir}/libecpg.so.*.*
%attr(755,root,root) %{_bindir}/pg_id

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecpg.so
%attr(755,root,root) %{_libdir}/libpq.so
%dir %{_includedir}/pgsql
%{_includedir}/pgsql/c.h
%{_includedir}/pgsql/config.h
%{_includedir}/pgsql/dynloader.h
%{_includedir}/pgsql/ecpgerrno.h
%{_includedir}/pgsql/ecpglib.h
%{_includedir}/pgsql/ecpgtype.h
%{_includedir}/pgsql/fmgr.h
%{_includedir}/pgsql/libpgeasy.h
%{_includedir}/pgsql/libpgtcl.h
%{_includedir}/pgsql/libpq-fe.h
%{_includedir}/pgsql/libpq-int.h
%{_includedir}/pgsql/miscadmin.h
%{_includedir}/pgsql/os.h
%{_includedir}/pgsql/postgres.h
%{_includedir}/pgsql/postgres_ext.h
%{_includedir}/pgsql/pqexpbuffer.h
%{_includedir}/pgsql/rusagestub.h
%{_includedir}/pgsql/sql3types.h
%{_includedir}/pgsql/sqlca.h
%{_includedir}/pgsql/strdup.h
%{_includedir}/pgsql/version.h
%{_includedir}/pgsql/access
%{_includedir}/pgsql/bootstrap
%{_includedir}/pgsql/catalog
%{_includedir}/pgsql/commands
%{_includedir}/pgsql/executor
%{_includedir}/pgsql/iodbc
%{_includedir}/pgsql/lib
%{_includedir}/pgsql/libpq
%{_includedir}/pgsql/mb
%{_includedir}/pgsql/nodes
%{_includedir}/pgsql/optimizer
%{_includedir}/pgsql/parser
%{_includedir}/pgsql/regex
%{_includedir}/pgsql/rewrite
%{_includedir}/pgsql/storage
%{_includedir}/pgsql/tcop
%{_includedir}/pgsql/utils
%attr(755,root,root) %{_bindir}/ecpg
%{_mandir}/man1/ecpg.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libecpg.a
%{_libdir}/libpq.a

%files clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libec*.so.*.*
%attr(755,root,root) %{_libdir}/libpq*.so.*.*
%attr(755,root,root) %{_bindir}/pg_dump
%attr(755,root,root) %{_bindir}/pg_dumpall
%attr(755,root,root) %{_bindir}/pg_upgrade
%attr(755,root,root) %{_bindir}/psql
%attr(755,root,root) %{_bindir}/vacuumdb

%{_mandir}/man1/pg_dump.1*
%{_mandir}/man1/pg_dumpall.1*
%{_mandir}/man1/pg_upgrade.1*
%{_mandir}/man1/psql.1*
%{_mandir}/manl/*.l*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpq++.so.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpq++.so
%{_includedir}/pgsql/libpq++.h
%{_includedir}/pgsql/libpq++

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libpq++.a

%files perl
%defattr(644,root,root,755)
%dir %{perl_sitearch}/auto/Pg
%{perl_sitearch}/auto/Pg/Pg.so
%attr(755,root,root) %{perl_sitearch}/auto/Pg/Pg.bs
%{perl_sitearch}/auto/Pg/autosplit.ix
%{perl_sitearch}/auto/Pg/.packlist
%{perl_sitearch}/Pg.pm
%{_mandir}/man3/*

%files -n pgaccess
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pgaccess
%{_libdir}/pgaccess
%doc src/bin/pgaccess/doc/html/*

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpgtcl.so.*.*
%attr(755,root,root) %{_libdir}/libpgtcl.so
%attr(755,root,root) %{_bindir}/pgtclsh
%attr(755,root,root) %{_bindir}/pgtksh

%files tcl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_includedir}/pgsql/libpgtcl.h

%files tcl-static
%defattr(644,root,root,755)
%{_libdir}/libpgtcl.a

%files odbc
%defattr(644,root,root,755)
%doc src/interfaces/odbc/readme.txt src/interfaces/odbc/notice.txt
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/odbc*
%attr(755,root,root) %{_libdir}/libpsqlodbc.so.*.*

%files odbc-devel
%defattr(644,root,root,755)
%{_includedir}/pgsql/iodbc
%attr(755,root,root) %{_libdir}/libpsqlodbc.so

%files odbc-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpsqlodbc.a

%files module-datetime
%defattr(644,root,root,755)
%attr(755,root,root) %{pgmoduledir}/datetime_functions.so
%attr(644,root,root) %{pgsqldir}/datetime_functions.sql

%files module-plpgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{pgmoduledir}/plpgsql.so

%files module-pltcl
%defattr(644,root,root,755)
%attr(755,root,root) %{pgmoduledir}/pltcl.so
