#
# - pg_autovacuum init support? look at its readme file, please
# - put pgcrypto docs into docdir
# - put pgcrypto sql files in %{_datadir}/postgresql
# - pg_ctl uses psql again, current patch2 doesn't eliminate this
# - remove postgresql-configure patch and create postgresql-doc patch,
#   which will prevent documentation and manuals installation (the routine
#   is bad and we install docs and mans manually, at all) or create good
#   routine and send it to postgresql team...
#
# Conditional build:
%bcond_without  tests			# disable testing
%bcond_without	tcl				# disables Tcl support
%bcond_without	kerberos5		# disable kerberos5 support
%bcond_with	jdbc				# enable JDBC driver
%bcond_with	absolute_dbpaths	# enable absolute paths to create database
					# (disabled by default because it is a security risk)

%include	/usr/lib/rpm/macros.python
 
Summary:	PostgreSQL Data Base Management System
Summary(de):	PostgreSQL Datenbankverwaltungssystem
Summary(es):	Gestor de Banco de Datos PostgreSQL
Summary(fr):	Sysème de gestion de base de données PostgreSQL
Summary(pl):	PostgreSQL - system bazodanowy
Summary(pt_BR):	Gerenciador de Banco de Dados PostgreSQL
Summary(ru):	PostgreSQL - ÓÉÓÔÅÍÁ ÕÐÒÁ×ÌÅÎÉÑ ÂÁÚÁÍÉ ÄÁÎÎÙÈ
Summary(tr):	Veri Tabaný Yönetim Sistemi
Summary(uk):	PostgreSQL - ÓÉÓÔÅÍÁ ËÅÒÕ×ÁÎÎÑ ÂÁÚÁÍÉ ÄÁÎÉÈ
Summary(zh_CN):	PostgreSQL ¿Í»§¶Ë³ÌÐòºÍ¿âÎÄ¼þ
Name:		postgresql
Version:	7.4
Release:	0.7
License:	BSD
Group:		Applications/Databases
##Source0:	ftp://ftp.postgresql.org/pub/source/v%{version}/%{name}-%{version}.tar.bz2
Source0:	ftp://ftp2.pl.postgresql.org/mirrors/ftp.postgresql.org/source/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	9db7432c431d1570b1f605727daf27bc
Source1:	%{name}.init
Source2:	pgsql-Database-HOWTO-html.tar.gz
# Source2-md5:	5b656ddf1db41965761f85204a14398e
Source3:	%{name}.sysconfig
Patch0:		%{name}-configure.patch
Patch1:		%{name}-pg_ctl-silent.patch
Patch2:		%{name}-pg_ctl-nopsql.patch
Patch3:		%{name}-conf.patch
Patch4:		%{name}-absolute_dbpaths.patch
Patch5:		%{name}-link.patch
Patch6:		%{name}-com_err.patch
Patch7:		%{name}-ecpg_link.patch
Patch8:		%{name}-ecpg-includedir.patch
Icon:		postgresql.xpm
URL:		http://www.postgresql.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison >= 1.875
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	pam-devel
BuildRequires:	perl-devel
BuildRequires:	python-devel >= 2.3
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-pythonprov
%{?with_tcl:BuildRequires:	tcl-devel >= 8.4.3}
%{?with_tcl:BuildRequires:	tk-devel >= 8.4.3}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
PreReq:		rc-scripts
PreReq:		%{name}-clients = %{version}
PreReq:		%{name}-libs = %{version}
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/sbin/usermod
Requires(post,preun):	/sbin/chkconfig
Obsoletes:	postgresql-server
Obsoletes:	postgresql-test

%define		_pgmoduledir	%{_libdir}/postgresql
%define		_pgsqldir	%{_pgmoduledir}/sql

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

%description -l es
Administrador de Banco de Datos PostgreSQL (conocido anteriormente
como Postgres, y después como Postgres95). PostgreSQL es una
continuación mejorada del Sistema Administrador de Banco de Datos
POSTGRES, que era un prototipo de pesquisa para un SGBD de nueva
generación. Mientras PostgreSQL mantiene el potente modelo de datos y
los varios tipos de datos del POSTGRES, substituye el lenguaje de
consulta PostQuel por un subconjunto extendido de la SQL. PostgreSQL
es libre y tiene los fuentes disponibles. El desarrollo del PostgreSQL
se ejecutado por un equipo de estudiosos de Internet, todos suscritos
en la lista de desarrollo del PostgreSQL. El coordinador actual es
Marc G. Fournier (scrappy@postgreSQL.org). Este equipo es ahora
responsable por el desarrollo actual y futuro del PostgreSQL.

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
System Zarz±dzania Baz± Danych PostgreSQL (dawniej znany jako
Postgres, nastêpnie jako Postgres95).

PostgreSQL jest rozszerzeniem systemu zarz±dzania baz danych POSTGRES,
prototypu DBMS nastêpnej generacji. Co prawda PostgreSQL odziedziczy³
model danych oraz bogaty zbiór ró¿nych typów danych, to jednak jêzyk
zapytañ PostQuel zosta³ zast±piony rozszerzonym SQL-em. PostgreSQL
jest wolnym oprogramowaniem i kody ¼ród³owe tego oprogramowania s± w
pe³ni dostêpne.

System PostgreSQL jest tworzony przez zespó³ ludzi, którzy s± zapisani
na listê dyskusyjn± dotycz±c± PostgreSQL-a. Obecnym koordynatorem jest
Marc G. Fournier (scrappy@postgreSQL.org). Wymieniony wy¿ej zespó³
jest odpowiedzialny za aktualny i przysz³y rozwój systemu PostgreSQL.

Autorami PostgreSQL-a 1.01 byli Andrew Yu oraz Jolly Chen. Wielu
innych pomaga³o przenosz±c na ró¿ne platformy, testuj±c, analizuj±c i
rozszerzaj±c kod. Oryginalny kod Postgres-a, na podstawie którego
PostgreSQL powsta³, by³ wysi³kiem wielu absolwentów, studentów oraz
zespo³u programistów, którzy pracowali pod kierunkiem profesora
Michaela Stonebrakera z Uniwersytetu Kalifornii w Berkeley.

Nazwa oryginalna oprogramowania tworzonego w Berkeley brzmia³a
Postgres. W 1995 roku dodano jêzyk zapytañ SQL i nazwê zmieniono na
Postgres95. W koñcu roku 1996 nazwê ostatecznie zmieniono na
PostgreSQL.

PostgreSQL mo¿e byæ uruchominy pod nastêpuj±cymi systemami: Solaris,
SunOS, HPUX, AIX, Linux, Irix, FreeBSD i innych systemach Unix.

%description -l pt_BR
Gerenciador de Banco de Dados PostgreSQL (conhecido anteriormente como
Postgres, e depois como Postgres95).

O PostgreSQL é uma continuação melhorada do Sistema Gerenciador de
Banco de Dados POSTGRES, que era um protótipo de pesquisa para um SGBD
de nova geração. Enquanto o PostgreSQL mantém o poderoso modelo de
dados e os vários tipos de dados do POSTGRES, ele substitui a
linguagem de consulta PostQuel por um subconjunto estendido da SQL. O
PostgreSQL é livre e tem os fontes disponíveis.

O desenvolvimento do PostgreSQL está sendo executado por uma equipe de
desenvolvedores da Internet, todos subscritores da lista de
desenvolvimento do PostgreSQL. O coordenador atual é Marc G. Fournier
(scrappy@postgreSQL.org). Esta equipe é agora responsável pelo
desenvolvimento atual e futuro do PostgreSQL.

%description -l ru
PostgreSQL - ÓÉÓÔÅÍÁ ÕÐÒÁ×ÌÅÎÉÑ ÂÁÚÁÍÉ ÄÁÎÎÙÈ (ÐÒÅÖÄÅ ÉÚ×ÅÓÔÎÁÑ ËÁË
Postgres, ÐÏÔÏÍ ËÁË Postgres95).

PostgreSQL - ÜÔÏ ÒÁÓÛÉÒÅÎÎÁÑ ×ÅÒÓÉÑ ÓÉÓÔÅÍÙ ÕÐÒÁ×ÌÅÎÉÑ ÂÁÚÁÍÉ ÄÁÎÎÙÈ
POSTGRES, ÉÓÓÌÅÄÏ×ÁÔÅÌØÓËÏÇÏ ÐÒÏÔÏÔÉÐÁ DBMS ÓÌÅÄÕÀÝÅÊ ÇÅÎÅÒÁÃÉÉ.
óÏÈÒÁÎÑÑ ÍÏÝÎÕÀ ÍÏÄÅÌØ ÄÁÎÎÙÈ É ÂÏÇÁÔÙÊ ÎÁÂÏÒ ÔÉÐÏ× ÄÁÎÎÙÈ POSTGRES,
ÏÎÁ ÚÁÍÅÎÑÅÔ ÑÚÙË ÚÁÐÒÏÓÏ× PostQuel ÒÁÓÛÉÒÅÎÎÙÍ ÎÁÂÏÒÏÍ SQL.
PostgreSQL ÂÅÓÐÌÁÔÅÎ É ÐÏÓÔÁ×ÌÑÅÔÓÑ × ×ÉÄÅ ÐÏÌÎÏÇÏ ËÏÍÐÌÅËÔÁ ÉÓÈÏÄÎÙÈ
ÔÅËÓÔÏ×.

PostgreSQL ÒÁÚÒÁÂÁÔÙ×ÁÌÓÑ ËÏÍÁÎÄÏÊ Internet-ÒÁÚÒÁÂÏÔÞÉËÏ×, ÐÏÄÐÉÓÁÎÎÙÈ
ÎÁ ÓÐÉÓÏË ÒÁÓÓÙÌËÉ, ÐÏÓ×ÑÝÅÎÎÙÊ ÒÁÚÒÁÂÏÔËÅ PostgreSQL. ÷ ÎÁÓÔÏÑÝÅÅ
×ÒÅÍÑ ËÏÏÒÄÉÎÁÔÏÒÏÍ Ñ×ÌÑÅÔÓÑ Marc G. Fournier
(scrappy@postgreSQL.org). üÔÁ ËÏÍÁÎÄÁ × ÎÁÓÔÏÑÝÅÅ ×ÒÅÍÑ ÏÔ×ÅÞÁÅÔ ÚÁ
×ÓÅ ÔÅËÕÝÉÅ É ÂÕÄÕÝÉÅ ÒÁÚÒÁÂÏÔËÉ PostgreSQL.

á×ÔÏÒÁÍÉ PostgreSQL 1.01 ÂÙÌÉ Andrew Yu É Jolly Chen. íÎÏÇÉÅ ×ÎÅÓÌÉ
Ó×ÏÊ ×ËÌÁÄ × ÐÏÒÔÉÒÏ×ÁÎÉÅ, ÔÅÓÔÉÒÏ×ÁÎÉÅ, ÏÔÌÁÄËÕ É ÕÌÕÞÛÅÎÉÅ ËÏÄÁ.
ïÒÉÇÉÎÁÌØÎÙÊ ËÏÄ Postgres, ÏÔ ËÏÔÏÒÏÇÏ ÐÒÏÉÚÏÛÅÌ PostgreSQL, ÂÙÌ
ÓÏÚÄÁÎ ÕÓÉÌÉÑÍÉ ÓÔÕÄÅÎÔÏ×, ÁÓÐÉÒÁÎÔÏ× É ÐÅÒÓÏÎÁÌÁ, ÒÁÂÏÔÁÀÝÅÇÏ ÐÏÄ
ÒÕËÏ×ÏÄÓÔ×ÏÍ ÐÒÏÆÅÓÓÏÒÁ Michael Stonebraker × University of
California, Berkeley.

ïÒÉÇÉÎÁÌØÎÏÅ ÎÁÚ×ÁÎÉÅ ðï × Berkeley ÂÙÌÏ Postgres. ëÏÇÄÁ × 1995 ÇÏÄÕ
ÂÙÌÁ ÄÏÂÁ×ÌÅÎÁ ÆÕÎËÃÉÏÎÁÌØÎÏÓÔØ SQL, ÎÁÚ×ÁÎÉÅ ÉÚÍÅÎÉÌÏÓØ ÎÁ
Postgres95. ÷ ËÏÎÃÅ 1996 ÇÏÄÁ ÏÎÏ ÅÝÅ ÒÁÚ ÉÚÍÅÎÉÌÏÓØ É ÔÅÐÅÒØ ÜÔÏ
PostgreSQL.

PostgreSQL ÒÁÂÏÔÁÅÔ ÎÁ Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD
É ÂÏÌØÛÉÎÓÔ×Å ÄÒÕÇÉÈ ÒÁÚÎÏ×ÉÄÎÏÓÔÅÊ Unix.

%description -l tr
PostgreSQL, POSTGRES'den türemiþ bir veri tabaný yönetim sistemidir
(DBMS). Güçlü veri modeli ve zengin POSTGRES veri tiplerini
desteklerken SQL'in geniþletilmiþ bir altkümesi yerine PostQuel
sorgulama dilini koyar.

%description -l uk
PostgreSQL - ÓÉÓÔÅÍÁ ËÅÒÕ×ÁÎÎÑ ÂÁÚÁÍÉ ÄÁÎÉÈ (ÒÁÎ¦Û ×¦ÄÏÍÁ ÑË Postgres,
ÐÏÔ¦Í ÑË Postgres95).

PostgreSQL - ÃÅ ÒÏÚÛÉÒÅÎÁ ×ÅÒÓ¦Ñ ÓÉÓÔÅÍÉ ËÅÒÕ×ÁÎÎÑ ÂÁÚÁÍÉ ÄÁÎÉÈ
POSTGRES, ÄÏÓÌ¦ÄÎÉÃØËÏÇÏ ÐÒÏÔÏÔÉÐÕ DBMS ÎÁÓÔÕÐÎÏ§ ÇÅÎÅÒÁÃ¦§.
úÂÅÒ¦ÇÁÀÞÉ ÐÏÔÕÖÎÕ ÍÏÄÅÌØ ÄÁÎÉÈ ÔÁ ÂÁÇÁÔÉÊ ÎÁÂ¦Ò ÔÉÐ¦× ÄÁÎÉÈ POSTGRES,
×ÏÎÁ ÚÁÍ¦ÎÀ¤ ÍÏ×Õ ÚÁÐÉÔ¦× PostQuel ÒÏÚÛÉÒÅÎÉÍ ÎÁÂÏÒÏÍ SQL. PostgreSQL
ÂÅÚËÏÛÔÏ×ÎÁ ÔÁ ÐÏÓÔÁ×ÌÑ¤ÔØÓÑ Õ ×ÉÇÌÑÄ¦ ÐÏ×ÎÏÇÏ ËÏÍÐÌÅËÔÕ ×ÉÈ¦ÄÎÉÈ
ÔÅËÓÔ¦×.

PostgreSQL ÒÏÚÒÏÂÌÑ¤ÔØÓÑ ËÏÍÁÎÄÏÀ Internet-ÐÒÏÇÒÁÍ¦ÓÔ¦×, ÕÞÁÓÎÉË¦×
ÓÐÉÓËÕ ÒÏÚÓÉÌËÉ, ÐÒÉÓ×ÑÞÅÎÏÇÏ ÒÏÚÒÏÂÃ¦ PostgreSQL. îÁÒÁÚ¦
ËÏÏÒÄÉÎÁÔÏÒÏÍ ¤ Marc G. Fournier (scrappy@postgreSQL.org). ãÑ ËÏÍÁÎÄÁ
×¦ÄÐÏ×¦ÄÁ¤ ÚÁ ×Ó¦ ÐÏÔÏÞÎ¦ ÔÁ ÍÁÊÂÕÔÎ¦ ÒÏÚÒÏÂËÉ PostgreSQL.

á×ÔÏÒÁÍÉ PostgreSQL 1.01 ÂÕÌÉ Andrew Yu ÔÁ Jolly Chen. âÁÇÁÔÏ ÌÀÄÅÊ
×ÎÅÓÌÉ Ó×¦Ê ×ÎÅÓÏË × ÐÏÒÔÕ×ÁÎÎÑ, ÔÅÓÔÕ×ÁÎÎÑ, ×¦ÄÌÁÄËÕ ÔÁ ÐÏËÒÁÝÅÎÎÑ
ËÏÄÕ. ïÒÉÇ¦ÎÁÌØÎÉÊ ËÏÄ Postgres, ×¦Ä ÑËÏÇÏ ÐÏÈÏÄÉÔØ PostgreSQL, ÂÕ×
ÓÔ×ÏÒÅÎÉÊ ÚÕÓÉÌÌÑÍÉ ÓÔÕÄÅÎÔ¦×, ÁÓÐ¦ÒÁÎÔ¦× ÔÁ ÐÅÒÓÏÎÁÌÕ, ÑËÉÊ ÐÒÁÃÀ×Á×
Ð¦Ä ËÅÒ¦×ÎÉÃÔ×ÏÍ ÐÒÏÆÅÓÏÒÁ Michael Stonebraker × University of
California, Berkeley.

ïÒÉÇ¦ÎÁÌØÎÁ ÎÁÚ×Á ÐÒÏÇÒÁÍÉ × Berkeley ÂÕÌÁ Postgres. ëÏÌÉ × 1995 ÒÏÃ¦
ÂÕÌÏ ÄÏÄÁÎÏ ÆÕÎËÃ¦ÏÎÁÌØÎ¦ÓÔØ SQL, ÎÁÚ×Á ÚÍ¦ÎÉÌÁÓÑ ÎÁ Postgres95. ÷
Ë¦ÎÃ¦ 1996 ÒÏËÕ ×ÏÎÁ ÝÅ ÒÁÚ ÚÍ¦ÎÉÌÁÓØ ¦ ÚÁÒÁÚ ÃÅ PostgreSQL.

PostgreSQL ÐÒÁÃÀ¤ ÎÁ Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD
ÔÁ Â¦ÌØÛÏÓÔ¦ ¦ÎÛÉÈ Ò¦ÚÎÏ×ÉÄ¦× Unix.

%package devel
Summary:	PostgreSQL development header files and libraries
Summary(de):	PostgreSQL-Entwicklungs-Header-Dateien und Libraries
Summary(es):	Archivos de inclusión y bibliotecas PostgreSQL
Summary(fr):	En-têtes et bibliothèques de développement PostgreSQL
Summary(pl):	PostgreSQL - pliki nag³ówkowe i biblioteki
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para desenvolvimento com o PostgreSQL
Summary(ru):	PostgreSQL - ÈÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔÞÉËÁ
Summary(tr):	PostgreSQL baþlýk dosyalarý ve kitaplýklar
Summary(uk):	PostgreSQL - ÈÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ ÐÒÏÇÒÁÍ¦ÓÔÁ
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}

%description devel
This package contains header files and libraries required to compile
applications that are talking directly to the PostgreSQL backend
server.

%description devel -l de
Dieses Paket enthält die Header-Dateien und Libraries, die zum
Kompilieren von Applikationen notwendig sind, die direkt mit dem
PostgreSQL-Backend-Server kommunizieren.

%description devel -l es
Este paquete contiene archivos de inclusión y bibliotecas requeridas
para compilación de aplicativos que se comunican directamente con el
servidor backend PostgreSQL.

%description devel -l fr
Ce package contient les fichiers d'en-tête et les bibliothéques
nécessaires pour compiler des applications ayant des échanges directs
avec le serveur du backend PostgreSQL.

%description devel -l pl
Pakiet zawiera nag³ówki oraz biblioteki wymagane do kompilacji
aplikacji ³±cz±cych siê bezpo¶rednio z serwerem PostgreSQL.

%description devel -l pt_BR
Este pacote contém arquivos de inclusão e bibliotecas requeridas para
compilação de aplicativos que se comunicam diretamente com o servidor
backend PostgreSQL.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÈÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÓÂÏÒËÉ
ÐÒÉÌÏÖÅÎÉÊ, ÎÅÐÏÓÒÅÄÓÔ×ÅÎÎÏ ×ÚÁÉÍÏÄÅÊÓÔ×ÕÀÝÉÈ Ó ÓÅÒ×ÅÒÏÍ PostgreSQL.

%description devel -l tr
Bu paket, PostgreSQL sunucusuyla konuþacak yazýlýmlar geliþtirmek için
gereken baþlýk dosyalarýný ve kitaplýklarý içerir.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÈÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ
ÐÒÏÇÒÁÍ, ÑË¦ ÂÅÚÐÏÓÅÒÅÄÎØÏ ×ÚÁ¤ÍÏÄ¦ÀÔØ Ú ÓÅÒ×ÅÒÏÍ PostgreSQL.

%package backend-devel
Summary:	PostgreSQL backend development header files
Summary(pl):	PostgreSQL - pliki nag³ówkowe dla backendu
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}

%description backend-devel
This package contains header files required to compile functions that
could be loaded directly by backend

%description backend-devel -l pl
Pakiet zawiera nag³ówki wymagane do kompilacji funkcji ktore moga byc
bezposrednio ladowane przez beckend serwera PostgreSQL.

%package clients
Summary:	Clients needed to access a PostgreSQL server
Summary(es):	Clientes necesarios para acceder al servidor PostgreSQL
Summary(pl):	Klienci wymagani do dostêpu do serwera PostgreSQL
Summary(pt_BR):	Clientes necessários para acessar o servidor PostgreSQL
Summary(ru):	ëÌÉÅÎÔÓËÉÅ ÐÒÏÇÒÁÍÍÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÄÏÓÔÕÐÁ Ë ÓÅÒ×ÅÒÕ PostgreSQL
Summary(uk):	ëÌ¦¤ÎÔÓØË¦ ÐÒÏÇÒÁÍÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÄÏÓÔÕÐÕ ÄÏ ÓÅÒ×ÅÒÁ PostgreSQL
Group:		Applications/Databases
Requires:	%{name}-libs = %{version}

%description clients
This package includes only the clients needed to access an PostgreSQL
server. The server is included in the main package. If all you need is
to connect to another PostgreSQL server, the this is the only package
you need to install. Clients include several command-line utilities
you can use to manage your databases on a remote PostgreSQL server.

%description clients -l es
Este paquete incluye solamente los clientes necesarios para acceder un
servidor PostgreSQL. El servidor está en el paquete principal.

%description clients -l pl
Pakiet zawiera programy klienckie potrzebne dla dostêpu do serwera
PostgreSQL oraz narzêdzia do zarz±dzania bazami dzia³aj±ce z linii
poleceñ. Serwer znajduje siê w g³ównym pakiecie.

%description clients -l pt_BR
Este pacote inclui somente os clientes necessários para acessar um
servidor PostgreSQL. O servidor está no pacote principal.

%description clients -l ru
üÔÏÔ ÐÁËÅÔ ×ËÌÀÞÁÅÔ ÔÏÌØËÏ ËÌÉÅÎÔÓËÉÅ ÐÒÏÇÒÁÍÍÙ É ÂÉÂÌÉÏÔÅËÉ,
ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÄÏÓÔÕÐÁ Ë ÓÅÒ×ÅÒÕ PostgreSQL. óÅÒ×ÅÒ ×ÈÏÄÉÔ × ÇÌÁ×ÎÙÊ
ÐÁËÅÔ. åÓÌÉ ×ÁÍ ÎÁÄÏ ÔÏÌØËÏ ÒÁÂÏÔÁÔØ Ó ÄÒÕÇÉÍ ÓÅÒ×ÅÒÏÍ PostgreSQL, ÜÔÏ
ÅÄÉÎÓÔ×ÅÎÎÙÊ ÐÁËÅÔ, ËÏÔÏÒÙÊ ×ÁÍ ÎÁÄÏ ÕÓÔÁÎÏ×ÉÔØ.

ôÅÐÅÒØ ÐÁËÅÔÙ Ó ÂÉÂÌÉÏÔÅËÁÍÉ ÄÌÑ ÒÁÚÎÙÈ ÑÚÙËÏ× ÐÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ (C,
C++, PERL É TCL) ÒÁÚÄÅÌÅÎÙ. üÔÏÔ ÐÁËÅÔ ×ËÌÀÞÁÅÔ ÔÏÌØËÏ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ
ÑÚÙËÁ C.

%description clients -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ Ô¦ÌØËÉ ËÌ¦¤ÎÔÓØË¦ ÐÒÏÇÒÁÍÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦
ÄÌÑ ÄÏÓÔÕÐÕ ÄÏ ÓÅÒ×ÅÒÁ PostgreSQL. óÅÒ×ÅÒ Í¦ÓÔÉÔØÓÑ × ÇÏÌÏ×ÎÏÍÕ
ÐÁËÅÔ¦. ñËÝÏ ×ÁÍ ÐÏÔÒ¦ÂÎÏ ÐÒÁÃÀ×ÁÔÉ Ú ¦ÎÛÉÍ ÓÅÒ×ÅÒÏÍ PostgreSQL, ÃÅ
¤ÄÉÎÉÊ ÐÁËÅÔ, ÑËÉÊ ×ÁÍ ÔÒÅÂÁ ×ÓÔÁÎÏ×ÉÔÉ.

ôÅÐÅÒ ÐÁËÅÔÉ Ú Â¦ÂÌ¦ÏÔÅËÁÍÉ ÄÌÑ Ò¦ÚÎÉÈ ÍÏ× ÐÒÏÇÒÁÍÕ×ÁÎÎÑ (C, C++, PERL
¦ TCL) ÒÏÚÄ¦ÌÅÎ¦. ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ Ô¦ÌØËÉ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÍÏ×É C.

%package doc
Summary:	Documentation for PostgreSQL
Summary(pl):	Dodatkowa dokumantacja dla PostgreSQL
Group:		Applications/Databases

%description doc
This package includes documentation and HOWTO for programmer, admin
etc., in HTML format.

%description doc -l pl
Pakiet ten zawiera dokumentacjê oraz HOWTO m.in. dla programistów,
administratorów w formacie HTML.

%package libs
Summary:	PostgreSQL libraries
Summary(es):	Biblioteca compartida del PostgreSQL
Summary(pl):	Biblioteki dzielone programu PostgreSQL
Summary(pt_BR):	Biblioteca compartilhada do PostgreSQL
Summary(zh_CN):	PostgreSQL ¿Í»§ËùÐèÒªµÄ¹²Ïí¿â
Group:		Libraries

%description libs
PostgreSQL shared libraries.

%description libs -l es
Este paquete contiene la biblioteca compartida para acceso al
PostgreSQL.

%description libs -l pl
Biblioteki dzielone programu PostgreSQL.

%description libs -l pt_BR
Este pacote contém a biblioteca compartilhada para acesso ao
PostgreSQL.

%package ecpg
Summary:	Embedded SQL in C interface
Summary(pl):	Interfejs wbudowanego SQL-a w jêzyk C
Group:		Libraries

%description ecpg
Embedded SQL in C interface.

%description ecpg -l pl
Interfejs wbudowanego SQL-a w jêzyk C.

%package ecpg-devel
Summary:	Embedded SQL in C interface files
Summary(pl):	Pliki programistyczne interfejsu wbudowanego SQL-a w jêzyk C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description ecpg-devel
Embedded SQL in C interface files.

%description ecpg-devel -l pl
Pliki programistyczne interfejsu wbudowanego SQL-a w jêzyk C.

%package static
Summary:	PostgreSQL static libraries
Summary(es):	Bibliotecas estaticas PostgreSQL
Summary(pl):	Biblioteki statyczne programu PostgreSQL
Summary(pt_BR):	Bibliotecas estáticas PostgreSQL
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÐÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ Ó PostgreSQL
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÐÒÏÇÒÁÍÕ×ÁÎÎÑ Ú PostgreSQL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
PostgreSQL static libraries.

%description static -l es
Este paquete contiene bibliotecas estaticas requerida para compilación
de aplicativos que se comunican directamente con el servidor backend
PostgreSQL.

%description static -l pl
Biblioteki statyczne programu PostgreSQL.

%description static -l pt_BR
Este pacote contém as bibliotecas estáticas requeridas para compilação
de aplicativos que se comunicam diretamente com o servidor backend
PostgreSQL.

%description static -l ru
üÔÏ ÏÔÄÅÌØÎÙÊ ÐÁËÅÔ ÓÏ ÓÔÁÔÉÞÅÓËÉÍÉ ÂÉÂÌÉÏÔÅËÁÍÉ, ËÏÔÏÒÙÅ ÂÏÌØÛÅ ÎÅ
×ÈÏÄÑÔ × %{name}-devel.

%description static -l uk
ãÅ ÏËÒÅÍÉÊ ÐÁËÅÔ Ú¦ ÓÔÁÔÉÞÎÉÍÉ Â¦ÂÌ¦ÏÔÅËÁÍÉ, ÑË¦ Â¦ÌØÛ ÎÅ ×ÈÏÄÑÔØ ×
%{name}-devel.

%package tcl
Summary:	Tcl interface for PostgreSQL
Summary(es):	Bibliotecas y shell Tcl para acceder un servidor PostgreSQL
Summary(pl):	Interfejs Tcl dla PostgreSQL
Summary(pt_BR):	Bibliotecas e shell para programas em Tcl acessarem o servidor PostgreSQL
Summary(ru):	âÉÂÌÉÏÔÅËÉ ÄÌÑ ÄÏÓÔÕÐÁ Ë PostgreSQL ÉÚ Tcl
Summary(uk):	â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÄÏÓÔÕÐÕ ÄÏ PostgreSQL Ú Tcl
Summary(zh_CN):	Ò»¸ö Tcl ¿âºÍ PostgreSQL µÄ PL/Tcl ±à³ÌÓïÑÔ
Group:		Development/Languages/Tcl
Requires:	%{name}-libs = %{version}

%description tcl
Tcl interface for PostgreSQL.

%description tcl -l es
Bibliotecas y shell Tcl para acceder un servidor PostgreSQL

%description tcl -l pl
Interfejs Tcl dla PostgreSQL.

%description tcl -l pt_BR
Bibliotecas e shell para programas em Tcl acessarem o servidor
PostgreSQL.

%description tcl -l ru
libpgtcl - API ÄÌÑ ÄÏÓÔÕÐÁ Ë ÂÁÚÅ ÄÁÎÎÙÈ PostgreSQL ÉÚ ÑÚÙËÁ Tcl.

%description tcl -l uk
libpgtcl - API ÄÌÑ ÄÏÓÔÕÐÕ ÄÏ ÂÁÚÉ ÄÁÎÉÈ PostgreSQL Ú ÍÏ×É Tcl.

%package tcl-devel
Summary:	Development part of Tcl interface for PostgreSQL
Summary(pl):	Czê¶æ dla programistów interfejsu Tcl dla PostgreSQL
Summary(ru):	èÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔÏË Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ libpgtcl (Tcl ÉÎÔÅÒÆÅÊÓ ÄÌÑ PostgreSQL)
Summary(uk):	èÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂÏË Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ libpgtcl (Tcl-¦ÎÔÅÒÆÅÊÓ ÄÌÑ PostgreSQL)
Group:		Development/Languages/Tcl
Requires:	%{name}-tcl = %{version}
Requires:	%{name}-devel = %{version}

%description tcl-devel
Development part of Tcl interface for PostgreSQL.

%description tcl-devel -l pl
Czê¶æ interfejsu Tcl dla PostgreSQL przeznaczona dla programistów.

%description tcl-devel -l ru
üÔÏ ÐÁËÅÔ ÒÁÚÒÁÂÏÔÞÉËÁ ÄÌÑ ÐÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ Ó libpgtcl. ïÎ ×ËÌÀÞÁÅÔ
ÈÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÉÓÐÏÌØÚÏ×ÁÎÉÑ × ÐÒÏÇÒÁÍÍÁÈ, ËÏÔÏÒÙÅ ÉÓÐÏÌØÚÕÀÔ
ËÏÄ ÉÌÉ API libtcl (Tcl ÉÎÔÅÒÆÅÊÓ ÄÌÑ PostgreSQL).

%description tcl-devel -l uk
ãÅ ÐÁËÅÔ ÐÒÏÇÒÁÍ¦ÓÔÁ ÄÌÑ ÐÒÏÇÒÁÍÕ×ÁÎÎÑ Ú libpgtcl. ÷¦Î Í¦ÓÔÉÔØ ÈÅÄÅÒÉ
ÔÁ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ×ÉËÏÒÉÓÔÁÎÎÑ × ÐÒÏÇÒÁÍÁÈ, ÑË¦ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ ËÏÄ ÁÂÏ
API libtcl (Tcl-¦ÎÔÅÒÆÅÊÓÕ ÄÌÑ PostgreSQL).

%package tcl-static
Summary:	Static libraries of Tcl interface for PostgreSQL
Summary(pl):	Biblioteki statyczne interfejsu Tcl dla PostgreSQL
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÐÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ Ó libpgtcl
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÐÒÏÇÒÁÍÕ×ÁÎÎÑ Ú libpgtcl
Group:		Development/Languages/Tcl
Requires:	%{name}-tcl-devel = %{version}

%description tcl-static
Static libraries of Tcl interface for PostgreSQL.

%description tcl-static -l pl
Biblioteki statyczne interfejsu Tcl dla PostgreSQL.

%description tcl-static -l ru
üÔÏ ÏÔÄÅÌØÎÙÊ ÐÁËÅÔ ÓÏ ÓÔÁÔÉÞÅÓËÉÍÉ ÂÉÂÌÉÏÔÅËÁÍÉ, ËÏÔÏÒÙÅ ÂÏÌØÛÅ ÎÅ
×ÈÏÄÑÔ × postgresql-tcl-devel.

%description tcl-static -l uk
ãÅ ÏËÒÅÍÉÊ ÐÁËÅÔ Ú¦ ÓÔÁÔÉÞÎÉÍÉ Â¦ÂÌ¦ÏÔÅËÁÍÉ, ÝÏ Â¦ÌØÛÅ ÎÅ ×ÈÏÄÑÔØ ÄÏ
postgresql-tcl-devel.

%package module-plpgsql
Summary:	PL/pgSQL - PostgreSQL procedural language
Summary(pl):	PL/pgSQL jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
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

%package module-plperl
Summary:	PL/perl - PostgreSQL procedural language
Summary(pl):	PL/perl jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Requires:	%{name} = %{version}
%requires_eq	perl

%description module-plperl
From PostgreSQL documentation.

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/perl procedural language for your database you have to
run createlang command.

%description module-plperl -l pl
Z dokumentacji PostgreSQL.

Postgres ma wsparcie dla jêzyków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurê wyzwalacza lub funkcjê w jêzyku
proceduralnym, baza danych nie ma pojêcia jak interpretowaæ tego typu
funkcjê. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak j± wykonaæ. Interpreter jest odpowiedni±, specjaln±
funkcj±, która jest skompilowana w obiekt dzielony i ³adowany w razie
potrzeby.

Za pomoc± komendy createlang mo¿na dodaæ wsparcie dla jêzyka
proceduralnego PL/perl dla swojej bazy danych.

%package module-plpython
Summary:	PL/python - PostgreSQL procedural language
Summary(pl):	PL/python jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Requires:	%{name} = %{version}
%pyrequires_eq	python

%description module-plpython
From PostgreSQL documentation.

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/python procedural language for your database you have to
run createlang command.

%description module-plpython -l pl
Z dokumentacji PostgreSQL.

Postgres ma wsparcie dla jêzyków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurê wyzwalacza lub funkcjê w jêzyku
proceduralnym, baza danych nie ma pojêcia jak interpretowaæ tego typu
funkcjê. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak j± wykonaæ. Interpreter jest odpowiedni±, specjaln±
funkcj±, która jest skompilowana w obiekt dzielony i ³adowany w razie
potrzeby.

Za pomoc± komendy createlang mo¿na dodaæ wsparcie dla jêzyka
proceduralnego PL/python dla swojej bazy danych.

%package module-pltcl
Summary:	PL/TCL - PostgreSQL procedural language
Summary(pl):	PL/TCL - jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
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

%package module-pgcrypto
Summary:	Cryptographic functions for PostgreSQL
Summary(pl):	Funkcje kryptograficzne dla PostgreSQL
Group:		Applications/Databases
Requires:       %{name} = %{version}

%description module-pgcrypto
Cryptographic functions for PostgreSQL.

%description module-pgcrypto -l pl
Funkcje kryptograficzne dla PostgreSQL.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%{?with_absolute_dbpaths:%patch4 -p1}
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

tar xzf doc/man*.tar.gz

mkdir doc/unpacked
tar zxf doc/postgres.tar.gz -C doc/unpacked

# Erase all CVS dir
find contrib -type d -name CVS -exec rm -rf {} \;

%build
rm -f config/libtool.m4
%{__aclocal} -I config
%{__autoconf}
%configure \
	%{!?_without_pgsql_locale:--enable-locale} \
	%{!?_without_pgsql_multibyte:--enable-multibyte} \
	--disable-rpath \
	--enable-nls \
	--enable-thread-safety \
	--enable-integer-datetimes \
	--enable-depend \
	--enable-recode \
	--enable-syslog \
	--with-pam \
	--enable-unicode-conversion \
	--with-CXX \
	%{?with_tcl:--with-tcl} \
	%{?with_tcl:--with-tk} \
	--with-perl \
	--with-python \
	%{?with_kerberos5:--with-krb5=%{_prefix}} \
	--with-openssl \
	--with-x \
%{?_with_jdbc:	--with-java}

%{__make}
%{__make} -C contrib/pg_autovacuum
%{__make} -C contrib/pgcrypto
%ifnarch sparc sparcv9 sparc64 alpha ppc
%{?with_tests:%{__make} check}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{rc.d/init.d,sysconfig}} \
        $RPM_BUILD_ROOT{/var/{lib/pgsql,log},%{_pgsqldir}} \
	$RPM_BUILD_ROOT{%{_applnkdir}/System,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT/home/services/postgres

%{__make} install install-all-headers \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C src/pl/plperl \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C contrib/pg_autovacuum install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C contrib/pgcrypto install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT/var/log/pgsql

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/postgresql
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/postgresql

cp -a man?	   $RPM_BUILD_ROOT%{_mandir}

# there are html installed, remove them
rm -rf $RPM_BUILD_ROOT%{_infodir}

install -d howto
( cd howto
  tar xzf $RPM_SOURCE_DIR/pgsql-Database-HOWTO-html.tar.gz
)

%py_comp $RPM_BUILD_ROOT%{py_libdir}
%py_ocomp $RPM_BUILD_ROOT%{py_libdir}

# find locales
for f in libpq pg_controldata pg_dump pg_resetxlog pgscripts postgres psql; do
	%find_lang $f
done
# merge locales
cat pgscripts.lang pg_resetxlog.lang postgres.lang pg_controldata.lang > main.lang
cat pg_dump.lang psql.lang > clients.lang

%clean
rm -rf $RPM_BUILD_ROOT

%pre
PG_DB_CLUSTERS=""
if [ -f /etc/sysconfig/postgresql ]; then
	. /etc/sysconfig/postgresql
	if [ -z "$PG_DB_CLUSTERS" -a -n "$POSTGRES_DATA_DIR" ]; then
		PG_DB_CLUSTERS="$POSTGRES_DATA_DIR"
	fi
fi
foundold=0
for pgdir in $PG_DB_CLUSTERS; do
	if [ -f $pgdir/PG_VERSION ]; then
		if [ `cat $pgdir/PG_VERSION` != '7.4' ]; then
			echo "Found database(s) in older, incompatible format in cluster $pgdir."
			foundold=1
		fi
	fi
done
if [ "$foundold" = "1" ]; then
	echo
	echo "Dump all data from clusters mentioned above (using pg_dump or pg_dumpall)"
	echo "and clean (or rename) those directories; then upgrade postgresql and"
	echo "restore all data (using pg_restore or psql)."
	echo "Remember to stop the daemon before upgrading!"
	echo
	echo "Warning for upgrade from version *before* 7.2."
	echo "Please note, that postgresql module path changed from"
	echo "/usr/lib/pgsql/module to /usr/lib/postgresql. Change the path"
	echo "in dump file before restore."
	echo
	echo "Warning for upgrade from version *before* 7.3."
	echo "Reading following webpage is encouraged:"
	echo "http://www.ca.postgresql.org/docs/momjian/upgrade_tips_7.3."
	exit 1
fi

getgid postgres >/dev/null 2>&1 || /usr/sbin/groupadd -g 88 -r -f postgres
if id postgres >/dev/null 2>&1 ; then
	/usr/sbin/usermod -d /home/services/postgres postgres
else
	/usr/sbin/useradd -M -o -r -u 88 \
		-d /home/services/postgres -s /bin/sh -g postgres \
		-c "PostgreSQL Server" postgres
fi

%post
/sbin/chkconfig --add postgresql
if [ -f /var/lock/subsys/postgresql ]; then
	/etc/rc.d/init.d/postgresql restart >&2 || :
else
	echo "Run \"/etc/rc.d/init.d/postgresql start\" to start postgresql server."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/postgresql ]; then
		/etc/rc.d/init.d/postgresql stop
	fi
	/sbin/chkconfig --del postgresql
fi

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post   ecpg -p /sbin/ldconfig
%postun ecpg -p /sbin/ldconfig

%post   tcl -p /sbin/ldconfig
%postun tcl -p /sbin/ldconfig

%files -f main.lang
%defattr(644,root,root,755)
%doc contrib/pg_autovacuum/README*
%attr(754,root,root) /etc/rc.d/init.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/*

%attr(755,root,root) %{_bindir}/clusterdb
%attr(755,root,root) %{_bindir}/createdb
%attr(755,root,root) %{_bindir}/createlang
%attr(755,root,root) %{_bindir}/createuser
%attr(755,root,root) %{_bindir}/dropdb
%attr(755,root,root) %{_bindir}/droplang
%attr(755,root,root) %{_bindir}/dropuser
%attr(755,root,root) %{_bindir}/initdb
%attr(755,root,root) %{_bindir}/initlocation
%attr(755,root,root) %{_bindir}/ipcclean
%attr(755,root,root) %{_bindir}/pg_autovacuum
%attr(755,root,root) %{_bindir}/pg_controldata
%attr(755,root,root) %{_bindir}/pg_ctl
%attr(755,root,root) %{_bindir}/pg_encoding
%attr(755,root,root) %{_bindir}/pg_resetxlog
%attr(755,root,root) %{_bindir}/postgres
%attr(755,root,root) %{_bindir}/postmaster

%attr(755,root,root) %{_pgmoduledir}/ascii*
%attr(755,root,root) %{_pgmoduledir}/cyrillic*
%attr(755,root,root) %{_pgmoduledir}/euc*
%attr(755,root,root) %{_pgmoduledir}/latin*
%attr(755,root,root) %{_pgmoduledir}/utf*

%dir %{_pgsqldir}
%dir %{_pgmoduledir}
%dir %{_datadir}/postgresql
%{_datadir}/postgresql/*.bki
%{_datadir}/postgresql/*.sample
%{_datadir}/postgresql/*.description
%{_datadir}/postgresql/*.sql
%{_datadir}/postgresql/*.txt

%attr(700,postgres,postgres) /home/services/postgres
%attr(700,postgres,postgres) %dir /var/lib/pgsql
%attr(640,postgres,postgres) %config(noreplace) %verify(not md5 size mtime) /var/log/pgsql

%{_mandir}/man1/clusterdb.1*
%{_mandir}/man1/createdb.1*
%{_mandir}/man1/createlang.1*
%{_mandir}/man1/createuser.1*
%{_mandir}/man1/dropdb.1*
%{_mandir}/man1/droplang.1*
%{_mandir}/man1/dropuser.1*
%{_mandir}/man1/initdb.1*
%{_mandir}/man1/initlocation.1*
%{_mandir}/man1/ipcclean.1*
%{_mandir}/man1/pg_controldata.1*
%{_mandir}/man1/pg_ctl.1*
%{_mandir}/man1/pg_resetxlog.1*
%{_mandir}/man1/postgres.1*
%{_mandir}/man1/postmaster.1*

%{_mandir}/man7/*.7*

%doc contrib
%doc doc/FAQ* doc/README*
%doc COPYRIGHT README HISTORY doc/bug.template

%files doc
%defattr(644,root,root,755)
%doc doc/unpacked/*
%doc howto

%files libs -f libpq.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpq.so.*.*
%attr(755,root,root) %{_bindir}/pg_id

%files ecpg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecpg
%attr(755,root,root) %{_libdir}/libecpg.so.*.*
%attr(755,root,root) %{_libdir}/libecpg_compat.so.*.*
%attr(755,root,root) %{_libdir}/libpgtypes.so.*.*
%{_mandir}/man1/ecpg.1*

%files ecpg-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecpg.so
%attr(755,root,root) %{_libdir}/libecpg_compat.so
%attr(755,root,root) %{_libdir}/libpgtypes.so
%{_includedir}/ecpg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pg_config
%attr(755,root,root) %{_libdir}/libpq.so
%dir %{_includedir}/postgresql
%{_includedir}/libpq-fe.h
%{_includedir}/pg_config.h
%{_includedir}/pg_config_os.h
%{_includedir}/postgres_ext.h
%dir %{_includedir}/postgresql/internal
%{_includedir}/postgresql/internal/c.h
%{_includedir}/postgresql/internal/libpq-int.h
%{_includedir}/postgresql/internal/postgres_fe.h
%{_includedir}/postgresql/internal/pqexpbuffer.h
%{_includedir}/postgresql/internal/lib
%{_includedir}/postgresql/internal/libpq
%{_includedir}/libpq
%{_mandir}/man1/pg_config.1*

%files backend-devel
%defattr(644,root,root,755)
%{_includedir}/postgresql/server

%files static
%defattr(644,root,root,755)
%{_libdir}/libecpg.a
%{_libdir}/libecpg_compat.a
%{_libdir}/libpq.a
%{_libdir}/libpgtypes.a

%files clients -f clients.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pg_dump
%attr(755,root,root) %{_bindir}/pg_dumpall
%attr(755,root,root) %{_bindir}/pg_restore
%attr(755,root,root) %{_bindir}/psql
%attr(755,root,root) %{_bindir}/vacuumdb

%{_mandir}/man1/pg_dump.1*
%{_mandir}/man1/pg_dumpall.1*
%{_mandir}/man1/pg_restore.1*
%{_mandir}/man1/psql.1*
%{_mandir}/man1/vacuumdb.1*
%{_mandir}/manl/*.l*

%if %{with tcl}
%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpgtcl.so
%attr(755,root,root) %{_libdir}/libpgtcl.so.*.*
%attr(755,root,root) %{_bindir}/pgtclsh
%attr(755,root,root) %{_bindir}/pgtksh
%{_mandir}/man1/pgtclsh.1*
%{_mandir}/man1/pgtksh.1*

%files tcl-devel
%defattr(644,root,root,755)
%{_includedir}/libpgtcl.h

%files tcl-static
%defattr(644,root,root,755)
%{_libdir}/libpgtcl.a
%endif

%files module-plpgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plpgsql.so

%files module-plperl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plperl.so

%files module-plpython
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plpython.so

%if %{with tcl}
%files module-pltcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pltcl_*
%attr(755,root,root) %{_pgmoduledir}/pltcl.so
%endif

%files module-pgcrypto
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/pgcrypto.so
# Hmm i think two below lines shouldn't be here - but i can be wrong ;)
#%{_datadir}/%{name}/contrib/pgcrypto.sql
#%{_datadir}/info/%{name}/contrib/README.pgcrypto.gz
