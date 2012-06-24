Summary:     PostgreSQL Data Base Management System
Summary(de): PostgreSQL Datenbankverwaltungssystem
Summary(fr): Sys�me de gestion de base de donn�es PostgreSQL.
Summary(pl): PostgreSQL system bazodanowy
Summary(tr): Veri Taban� Y�netim Sistemi
Name:        postgresql
Version:     6.4.2
Release:     5d
Copyright:   BSD
Group:       Applications/Databases
Group(pl):   Aplikacje/Bazy danych
URL:         http://www.postgresql.org/
Source:      ftp://ftp.postgresql.org/pub/%{name}-%{version}.tar.gz
Source1:     postgresql.init
Source2:     pgsql-Database-HOWTO-html.tar.gz
Patch:       postgresql-6.4.2-opt.patch
Buildroot:   /tmp/%{name}-%{version}-root
Prereq:      /sbin/chkconfig /sbin/ldconfig
Requires:    postgresql-clients

%description
PostgreSQL Data Base Management System (formerly known as Postgres, then as
Postgres95). 

PostgreSQL is an enhancement of the POSTGRES database management system, a
next-generation DBMS research prototype.  While PostgreSQL retains the
powerful data model and rich data types of POSTGRES, it replaces the PostQuel
query language with an extended subset of SQL. PostgreSQL is free and the
complete source is available. 

PostgreSQL development is being performed by a team of Internet developers who
all subscribe to the PostgreSQL development mailing list. The current
coordinator is Marc G. Fournier (scrappy@postgreSQL.org). This team is now
responsible for all current and future development of PostgreSQL. 

The authors of PostgreSQL 1.01 were Andrew Yu and Jolly Chen. Many others have
contributed to the porting, testing, debugging and enhancement of the code.
The original Postgres code, from which PostgreSQL is derived, was the effort
of many graduate students, undergraduate students, and staff programmers
working under the direction of Professor Michael Stonebraker at the University
of California, Berkeley. 

The original name of the software at Berkeley was Postgres. When SQL
functionality was added in 1995, its name was changed to Postgres95. The name
was changed at the end of 1996 to PostgreSQL. 

PostgreSQL runs on Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD, and most
flavours of Unix. 

%description -l de
PostgreSQL Datenbank-Managementsystem (fr�her als Postgres, dann als 
Postgres95 bekannt).

PostgreSQL ist eine Verbesserung des POSTGRES-DB-Managementsystems, ein
 DBMS-Forschungsprototyp der n�chsten Generation. W�hrend es das leistungsf�hige
Datenmodell und die reichhaltigen Datentypen von POSTGRES beibeh�lt, ersetzt
es die PostQuel-Abfragesprache durch ein Subset von SQL. PostgreSQL ist gratis,
der gesamte Quellcode ist verf�gbar.

Ein Team von Internet-Entwicklern befa�t sich mit PostgreSQL. Sie alle sind auf
der PostgreSQL-Entwickleradre�liste. Koordinator ist
 Marc G. Fournier (scrappy@postgreSQL.org). Das Team ist verantwortlich f�r alle
aktuellen und k�nftigen Entwicklungen von PostgreSQL.

Die Autoren von PostgreSQL 1.01 waren Andrew Yu und Jolly Chen. Zahlreiche andere
haben zur Portierung, zum Testen, Debugging und zur Verbesserung des Code beigetragen.
Den Original-Postgres-Code, von dem sich PostgreSQL ableitet, verdanken wir der Arbeit
vieler Doktoranden, Studenten und Programmierern unter der Leitung von
Professor Michael Stonebraker an der University of California, Berkeley.

Der urspr�ngliche Name war Postgres. Als 1995 SQL-Funktionalit�t hinzukam,
wurde der Name in Postgres95 ge�ndert. Ende 1996 schlie�lich entschied man sich
f�r PostgreSQL.

PostgreSQL l�uft auf Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD und den meisten
Unix-Systemen.

%description -l fr
Syst�me de gestion de bases de donn�es PostgreSQL (D'abord nomm� Postgres,
puis Postgres95).
PostgreSQL est une am�lioration du syst�me de gestion de bases de donn�es
POSTGRES, un prototype de recherche de la g�n�ration suivant DBMS. Tout
en conservant le puissant mod�le de donn�e de et les types de don�e riches
de Postgres, il remplace le langage de requ�tes de Postgres par un sous
ensemble etendu de commandes SQL. PosrgreSQL est libre, et ses sources
sont disponibles.

Le d�veloppement de PostgreSQL est actuellement r�alis� via internet par\une �quipe de d�veloppeurs inscrits sur la mailing-list de d�veloppement
de PostgreSQL. Le coordinateur actuel est Marc G Fournier
(scrappy@postgreSQL.org). Cette �quipe est responsable du d�veloppemen
actuel et � venir de PostgreSQL.

Les auteurs de PostgreSQL 1.01 �taient Andrew Yu et Jolly Chen. Beaucoup
d'autres ont contribu� au portage, au test, au d�bogage et � l'am�lioration
du code. Le code original de Postgres, duquel PostgreSQL est d�riv�,
a �t� l'oeuvre d'�tudiants de haut niveau, de moins haut niveau, et de
programmeurs travaillant sous la direction du professeur Michael
Stonebraker � l'universit� de Berkeley Californie.

Le nom original du logiciel �tait Postgres. Quand les fonctionnalit�es
SQL furent ajout�es en 1995, son nom est devenu Postgres95. Il a �t� 
rebaptis� PostgreSQL en 1996.

PostgreSQL tourne sur Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD,
et la plupart des Unix.

%description -l pl
PostgreSQL System Zarz�dzania Baz� Danych (dawniej znany jako Postgres,
nast�pnie jako Postgres95). 

PostgreSQL mo�e by� uruchominy pod nast�puj�cymi systemami: Solaris, SunOS, 
HPUX, AIX, Linux, Irix, FreeBSD i innych systemach Unix.

%description -l tr
PostgreSQL, POSTGRES'den t�remi� bir veri taban� y�netim sistemidir (DBMS).
G��l� veri modeli ve zengin POSTGRES veri tiplerini desteklerken SQL'in
geni�letilmi� bir altk�mesi yerine PostQuel sorgulama dilini koyar.

%package devel
Requires:    postgresql-clients
Summary:     PostgreSQL development header files and libraries
Summary(de): PostgreSQL-Entwicklungs-Header-Dateien und Libraries 
Summary(fr): En-t�tes et biblioth�ques de d�veloppement PostgreSQL
Summary(pl): PostgreSQL - nag�owki i biblioteki
Summary(tr): PostgreSQL ba�l�k dosyalar� ve kitapl�klar
Group:       Development/Libraries
Group(pl):   Programowanie/Biblioteki

%description devel
This package contains header files and libraries required to compile
applications that are talking directly to the PostgreSQL backend server. 

%description -l de devel
Dieses Paket enth�lt die Header-Dateien und Libraries, die zum
Kompilieren von Applikationen notwendig sind, die direkt mit dem
PostgreSQL-Backend-Server kommunizieren.

%description -l fr devel
Ce package contient les fichiers d'en-t�te et les biblioth�ques n�cessaires
pour compiler des applications ayant des �changes directs avec le serveur
du backend PostgreSQL.

%description -l pl devel
Pakiet zawiera nag��wki oraz biblioteki wymagane do kompilacji aplikacji 
��cz�cych si� bezpo�rednio z serwerem PostgreSQL.

%description -l tr devel
Bu paket, PostgreSQL sunucusuyla konu�acak yaz�l�mlar geli�tirmek i�in
gereken ba�l�k dosyalar�n� ve kitapl�klar� i�erir.

%package data
Summary:     PostgreSQL initial database structure
Summary(de): PostgreSQL-Ausgangs-Datenbankstruktur 
Summary(fr): Structure initiale de base de donn�es PostgreSQL 
Summary(pl): PostgreSQL - inicjuj�ca struktura bazy danych
Summary(tr): PostgreSQL ba�lang�� veritaban� yap�s�
Group:       Applications/Databases
Group(pl):   Aplikacje/Bazy danych
Requires:    postgresql postgresql-clients
Conflicts:   postgresql-data <= 6.2.1

%description data
This packages includes an initial database structure directory for PostgreSQL.
For a quick startup on PostegreSQL, it is recommended to install this package
with your PostgreSQL backend server (altough it is not required). 

If you choose to not install this package you will have to create the initial
database yourself using 'initdb' command and possibly modify the postgresql
startup script if you choose a directory other than /var/lib/pgsql for
storing your databases.

%description -l de data
Dieses Paket schlie�t ein elementares Strukturverzeichnis f�r 
PostgreSQL ein. F�r einen schnellen Start mit PostegreSQL empfehlen 
wir die Installation dieses Pakets mit Ihrem PostgreSQL-Backend-
Server (obligatorisch ist es nicht).
Sie die anf�ngliche Datenbank selbst mit Hilfe des initdb-Befehls 
erstellen und m�glicherweise das postgresql-Start-Skript modifizieren, 
wenn Sie ein anderes als das /var/lib/pgsql-Verzeichnis zum Speichern 
Ihrer Datenbanken w�hlen. 

%description -l fr data
Ce paquetage contient une structure initiale de base de donn�es pour PostgreSQL.
Pour un d�marrage rapide avec PostgreSQL, il est recommand� d'installer ce
paquetage avec votre serveur PostgreSQL (bien que ce ne soit pas obligatoire).

Si vous n'installez pas ce paquetage, vous devrez cr�er vous-m�me la base de
donn�es initiale avec la commande � initdb � et modifier le script de
d�marrage de PostgreSQL si vous choisissez un autre r�pertoire que
/var/lib/pgsql pour stocker vos bases de donn�es.

%description -l pl data
Pakiet zawiera zainicjowan� struktur� bazodanow� dla PostgreSQL. Dla
szybkiego startu PostgreSQL rekomendowane jest zainstalowanie tego pakietu
razem z pakietem serwera (jednak�e nie jest on wymagany).

Je�eli nie zainstalujesz tego pakietu b�dziesz musia� r�cznie utworzy� 
inicjuj�c� baz� przy pomocy polecenia 'initdb' oraz ewentualnie skrypt
startowy, je�eli nie wybierzesz katalogu /var/lib/pgsql jako katalogu
domy�lnego dla przechowywania baz danych.

%description -l tr data
Bu paket, PostgreSQL i�in bir ba�lang�� veri taban� yap�s� dizinini i�erir.
PostgreSQL'e h�zl� ba�lang�� i�in bu paketin PostgreSQL sunucusuna y�klenmesi
�nerilir. Bu paketi y�klememeyi se�erseniz, ba�lang�� veri taban�n� 'initdb'
komutunu kullanarak kendiniz yaratman�z gerekir.

%package clients
Summary:     clients needed to access a PostgreSQL server
Summary(pl): klienci wymagani do dost�pu do serwera PostgreSQL
Group:       Applications/Databases
Group(pl):   Aplikacje/Bazy danych

%description clients
This package includes only the clients and client libraries needed to access
an PostgreSQL server. The server is included in the main package. If all you
need is to connect to another PostgreSQL server, the  this is the only
package you need to install.

In this package there are client libraries available for C and C++, as
well as several command-line utilities you can use to manage your databases
on a remote PostgreSQL server.

%description -l pl clients
Pakiet zawiera klient�w oraz biblioteki niezb�dne dla dost�pu do serwera 
PostgreSQL. Serwer znajduje si� w g��wnym pakiecie.

%package perl
Summary:     Perl interface to PostgreSQL database
Summary(pl): Interface dla Perl'a umo�liwiaj�cy dost�p do baz PostgreSQL
Group:       Applications/Databases
Group(pl):   Aplikacje/Bazy danych
Requires:    postgresql, perl >= 5.004

%description perl
This package includes only perl modules needed to access an PostgreSQL server.

%description -l pl perl
Pakiet ten zawiera tylko modu�y Perl'a wymagane dla dost�pu do serwera 
PostgreSQL.

%package doc
Summary:     Documentation for PostgreSQL
Summary(pl): Dodatkowa dokumantacja dla PostgreSQL
Group:       Applications/Databases
Group(pl):   Aplikacje/Bazy danych
Requires:    postgresql

%description doc
This package includes documentation and HOWTO for programmer, admin etc., in
HTML format.

%description -l pl doc
Pakiet ten zawiera dokumentacj� oraz HOWTO m.in. dla programist�w,
administrator�w w formacie HTML.

%package odbc
Summary:     ODBC interface to PostgreSQL
Summary(pl): Interface ODBC do PostgreSQL
Group:       Applications/Databases
Group(pl):   Aplikacje/Bazy danych
Requires:    postgresql

%description odbc
This package includes library and header files for interface ODBC.

%description -l pl odbc
Pakiet ten zawiera biblioteki i pliki nag��wkowe dla interface'u ODBC.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch -p1 -b .opt

%build
cd src
autoconf

%ifarch alpha
EXTRA_configure="--with-template=linuxalpha"
%endif
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \
	--enable-hba --enable-locale \
	--with-odbc --with-odbcinst=/etc \
	--without-tcl \
	--with-x \
	--with-perl $EXTRA_configure

gmake OPT_FLAGS="$RPM_OPT_FLAGS"

cd ..
make all PGDOCS=unpacked -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT/usr/{include/pgsql,lib,bin,man}
install -d $RPM_BUILD_ROOT/var/lib/pgsql

( cd src
  gmake POSTGRESDIR=$RPM_BUILD_ROOT/usr install
  gmake POSTGRESDIR=$RPM_BUILD_ROOT/usr install-man
)

# For Perl interface
( cd src/interfaces/perl5
  PERLVER=`ls -d /usr/lib/perl5/${RPM_ARCH}-linux/5.*`
  install -d $RPM_BUILD_ROOT/$PERLVER
  perl Makefile.PL
  make PREFIX=$RPM_BUILD_ROOT/usr install

  PACK="$RPM_BUILD_ROOT/usr/lib/perl5/site_perl/${RPM_ARCH}-linux/auto/Pg/.packlist"
  mv $PACK $PACK.old
  sed -e "s|$RPM_BUILD_ROOT/|/|g" -e "s|./||" < $PACK.old > $PACK
  rm -f $PACK.old
  
  LOCAL="$RPM_BUILD_ROOT/$PERLVER/perllocal.pod"
  mv $LOCAL $LOCAL.old
  sed -e "s|$RPM_BUILD_ROOT/|/|g" < $LOCAL.old > $LOCAL
  rm -f $LOCAL.old
)
find $RPM_BUILD_ROOT/usr/lib/perl5 -type f -print | \
	sed -e "s|$RPM_BUILD_ROOT/|/|g" > perlfiles.list
find $RPM_BUILD_ROOT/usr/lib/perl5 -type d -name Pg -print | \
	sed -e "s|$RPM_BUILD_ROOT/|%dir /|g" >> perlfiles.list

# Move all includes beneath /usr/include/pgsql.
( cd $RPM_BUILD_ROOT/usr/include
  rm -rf include
  for f in *.h access commands executor lib libpq libpq++ port utils
  do
	mv $f pgsql
  done
)

# Move all templates/examples beneath /usr/lib/pgsql
( cd $RPM_BUILD_ROOT/usr/lib
  install -d pgsql
  mv *source *sample pgsql
)

# Move odbc.ini file to etc
mv -f $RPM_BUILD_ROOT/usr/*.ini $RPM_BUILD_ROOT/etc

install -m 755 $RPM_SOURCE_DIR/postgresql.init $RPM_BUILD_ROOT/etc/rc.d/init.d/postgresql

install -d howto
( cd howto
  tar xzf $RPM_SOURCE_DIR/pgsql-Database-HOWTO-html.tar.gz
)

# Strip 'em all
strip -s $RPM_BUILD_ROOT/usr/bin/* || :

# gzip all man pages
gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

# Erase all CVS dir
rm -fR `find contrib/ -type d -name CVS`

%post
/sbin/chkconfig --add postgresql

%post data
# Create sample database
su postgres -c "LD_LIBRARY_PATH=/usr/lib \
    /usr/bin/initdb --pgdata=/var/lib/pgsql \
    --pglib=/usr/lib/pgsql"

%post -p /sbin/ldconfig clients

%post -p /sbin/ldconfig devel

%post -p /sbin/ldconfig odbc

%preun
if [ $1 = 0 ]; then
   if [ -f /var/lock/subsys/postmaster ]; then
       /etc/rc.d/init.d/postgresql stop
   fi
   /sbin/chkconfig --del postgresql
fi

%postun -p /sbin/ldconfig clients

%postun -p /sbin/ldconfig devel

%postun -p /sbin/ldconfig odbc


%clean
rm -rf $RPM_BUILD_ROOT

%files doc
%defattr(644, root, root, 755)
%doc doc/unpacked/*
%doc howto

%files
%defattr(644, root, root, 755)
%doc contrib 
%doc doc/FAQ doc/FAQ_Linux doc/README* 
%doc COPYRIGHT README HISTORY doc/bug.template
%doc doc/*.ps.gz

%attr(755, root, root) /etc/rc.d/init.d/*

%attr(644, postgres, postgres, 755) /usr/lib/pgsql
%attr(755, root, root) /usr/bin/cleardbdir
%attr(755, root, root) /usr/bin/createdb
%attr(755, root, root) /usr/bin/createuser
%attr(755, root, root) /usr/bin/destroydb
%attr(755, root, root) /usr/bin/destroyuser
%attr(755, root, root) /usr/bin/initdb
%attr(755, root, root) /usr/bin/initlocation
%attr(755, root, root) /usr/bin/pg_passwd
%attr(755, root, root) /usr/bin/pg_version
%attr(755, root, root) /usr/bin/postgres
%attr(755, root, root) /usr/bin/postmaster
%attr(644, root,  man) /usr/man/man1/cleardbdir.1.gz
%attr(644, root,  man) /usr/man/man1/createdb.1.gz
%attr(644, root,  man) /usr/man/man1/createuser.1.gz
%attr(644, root,  man) /usr/man/man1/destroydb.1.gz
%attr(644, root,  man) /usr/man/man1/destroyuser.1.gz
%attr(644, root,  man) /usr/man/man1/initdb.1.gz
%attr(644, root,  man) /usr/man/man1/initlocation.1.gz
%attr(644, root,  man) /usr/man/man1/pg_passwd.1.gz
%attr(644, root,  man) /usr/man/man1/postgres.1.gz
%attr(644, root,  man) /usr/man/man1/postmaster.1.gz
%attr(644, root,  man) /usr/man/man5/*.5.gz

%files devel
%defattr(644, root, root, 755)
/usr/lib/libec*.a
/usr/lib/libpq*.a
/usr/lib/libec*.so
/usr/lib/libpq*.so
/usr/include/pgsql
%attr(644, root,  man) /usr/man/man3/*.gz
%attr(755, root, root) /usr/bin/ecpg
%attr(644, root,  man) /usr/man/man1/ecpg.1.gz

%files data
%defattr(-,postgres,postgres)
%attr(-,postgres,postgres) /var/lib/pgsql

%files clients
%defattr(644, root, root, 755)
/usr/lib/libec*.so.*
/usr/lib/libpq*.so.*
%attr(755, root, root) /usr/bin/pg_dump
%attr(755, root, root) /usr/bin/pg_dumpall
%attr(755, root, root) /usr/bin/pg_id
%attr(755, root, root) /usr/bin/pg_upgrade
%attr(755, root, root) /usr/bin/psql
%attr(644, root,  man) /usr/man/man1/pg_dump.1.gz
%attr(644, root,  man) /usr/man/man1/pg_dumpall.1.gz
%attr(644, root,  man) /usr/man/man1/pg_upgrade.1.gz
%attr(644, root,  man) /usr/man/man1/psql.1.gz
%attr(644, root,  man) /usr/man/manl/*.gz

%files -f perlfiles.list perl
%defattr(-, root, root)

%files odbc
%defattr(644, root, root, 755)
%doc src/interfaces/odbc/readme.txt src/interfaces/odbc/notice.txt
%config(noreplace) %verify(not size mtime md5) /etc/odbc*
/usr/lib/libpsqlodbc*
/usr/include/iodbc

%changelog
* Fri Mar  5 1999 Jacek Smyda <smyda@posexperts.com.pl>
- remove adduser (standard user in passwd)
- add polish group names

* Wed Mar  3 1999 Jacek Smyda <smyda@posexperts.com.pl>
- correct group name

* Thu Feb 25 1999 Jacek Smyda <smyda@posexperts.com.pl>
- gzip man pages

* Thu Feb 18 1999 Jacek Smyda <smyda@posexperts.com.pl>
- Remove template database from data package and init after install

* Mon Jan 17 1999 Jacek Smyda <smyda@posexperts.com.pl>
- added translations for pl
- new package: perl, doc, odbc
- finally v6.4.2
- removed tcl interface

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip all binaries
- use defattr in all packages
- updated pgaccess to version 0.90
- /var/lib/pgsql/pg_pwd should not be 666

* Sun Jun 21 1998 Jeff Johnson <jbj@redhat.com>
- create /usr/lib/pgsql (like /usr/include/pgsql)
- resurrect libpq++.so*
- fix name problem in startup-script (problem #533)

* Fri Jun 19 1998 Jeff Johnson <jbj@redhat.com>
- configure had "--prefix=$RPM_BUILD_ROOT/usr"
- move all include files below /usr/include/pgsql.
- resurrect perl client file lists.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
