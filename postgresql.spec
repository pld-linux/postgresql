#
# TODO:
# - plphp has no files section
#
# Conditional build:
%bcond_without	tests			# disable testing
%bcond_without	tcl			# disables Tcl support
%bcond_without	kerberos5		# disable kerberos5 support
%bcond_without	perl			# disable Perl support
%bcond_without	pgsql_locale		# disable PostgreSQL locale
%bcond_without	pgsql_multibyte		# disable PostgreSQL multibyte
%bcond_without	python			# disable Python support
%bcond_with	php			# enable PHP support
%bcond_with	absolute_dbpaths	# enable absolute paths to create database
					# (disabled by default because it is a security risk)

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
Version:	8.1.1
Release:	1
License:	BSD
Group:		Applications/Databases
Source0:	ftp://ftp6.pl.postgresql.org/pub/postgresql/source/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	d22d7bd1d5e5f9aa89d574ff66e2c8bb
##Source0:	ftp://ftp.postgresql.org/pub/source/v%{version}beta/%{name}-%{version}%{beta}.tar.bz2
Source1:	%{name}.init
Source2:	pgsql-Database-HOWTO-html.tar.gz
# Source2-md5:	5b656ddf1db41965761f85204a14398e
Source3:	%{name}.sysconfig
Source8:	http://www.commandprompt.com/files/plphp-8.x.tar.bz2
# Source8-md5:	d307e4ab8cb6900a1c290a5dde1bdeee
Patch0:		%{name}-conf.patch
Patch1:		%{name}-absolute_dbpaths.patch
Patch2:		%{name}-link.patch
Patch3:		%{name}-ecpg_link.patch
Patch4:		%{name}-ecpg-includedir.patch
Patch5:		%{name}-ac.patch
Icon:		postgresql.xpm
URL:		http://www.postgresql.org/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	bison >= 1.875	not needed for releases
BuildRequires:	flex
BuildRequires:	gettext-devel
%{?with_kerberos5:BuildRequires:	heimdal-devel >= 0.7}
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
%{?with_perl:BuildRequires:	perl-devel}
%if %{with php}
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.238
%endif
%if %{with python}
BuildRequires:	python >= 1:2.3
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules >= 1:2.3
%endif
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpmbuild(macros) >= 1.202
BuildRequires:	sed >= 4.0
%{?with_tcl:BuildRequires:	tcl-devel >= 8.4.3}
BuildRequires:	zlib-devel
PreReq:		rc-scripts
PreReq:		%{name}-clients = %{version}-%{release}
PreReq:		%{name}-libs = %{version}-%{release}
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/sbin/usermod
Requires(post,preun):	/sbin/chkconfig
Obsoletes:	postgresql-server
Obsoletes:	postgresql-test
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pgmoduledir	%{_libdir}/postgresql
%define		_pgsqldir	%{_datadir}/postgresql/contrib

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

PostgreSQL mo¿e byæ uruchomiony pod nastêpuj±cymi systemami: Solaris,
SunOS, HPUX, AIX, Linux, Irix, FreeBSD i innymi systemami uniksowymi.

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
Requires:	%{name}-libs = %{version}-%{release}

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
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

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
Requires:	%{name}-libs = %{version}-%{release}

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
C++, Perl É Tcl) ÒÁÚÄÅÌÅÎÙ. üÔÏÔ ÐÁËÅÔ ×ËÌÀÞÁÅÔ ÔÏÌØËÏ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ
ÑÚÙËÁ C.

%description clients -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ Ô¦ÌØËÉ ËÌ¦¤ÎÔÓØË¦ ÐÒÏÇÒÁÍÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦
ÄÌÑ ÄÏÓÔÕÐÕ ÄÏ ÓÅÒ×ÅÒÁ PostgreSQL. óÅÒ×ÅÒ Í¦ÓÔÉÔØÓÑ × ÇÏÌÏ×ÎÏÍÕ
ÐÁËÅÔ¦. ñËÝÏ ×ÁÍ ÐÏÔÒ¦ÂÎÏ ÐÒÁÃÀ×ÁÔÉ Ú ¦ÎÛÉÍ ÓÅÒ×ÅÒÏÍ PostgreSQL, ÃÅ
¤ÄÉÎÉÊ ÐÁËÅÔ, ÑËÉÊ ×ÁÍ ÔÒÅÂÁ ×ÓÔÁÎÏ×ÉÔÉ.

ôÅÐÅÒ ÐÁËÅÔÉ Ú Â¦ÂÌ¦ÏÔÅËÁÍÉ ÄÌÑ Ò¦ÚÎÉÈ ÍÏ× ÐÒÏÇÒÁÍÕ×ÁÎÎÑ (C, C++, Perl
¦ Tcl) ÒÏÚÄ¦ÌÅÎ¦. ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ Ô¦ÌØËÉ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÍÏ×É C.

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
Requires:	%{name}-libs = %{version}-%{release}

%description ecpg
Embedded SQL in C interface.

%description ecpg -l pl
Interfejs wbudowanego SQL-a w jêzyk C.

%package ecpg-devel
Summary:	Embedded SQL in C interface files
Summary(pl):	Pliki programistyczne interfejsu wbudowanego SQL-a w jêzyk C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ecpg = %{version}-%{release}

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
Requires:	%{name}-devel = %{version}-%{release}

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

%package module-plpgsql
Summary:	PL/pgSQL - PostgreSQL procedural language
Summary(pl):	PL/pgSQL - jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-plpgsql
From PostgreSQL documentation:

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
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla jêzyków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurê wyzwalacza lub funkcjê w jêzyku
proceduralnym, baza danych nie ma pojêcia jak interpretowaæ tego typu
funkcjê. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak j± wykonaæ. Interpreter jest odpowiedni±, specjaln±
funkcj±, która jest skompilowana w obiekt dzielony i ³adowany w razie
potrzeby.

Za pomoc± polecenia createlang mo¿na dodaæ obs³ugê jêzyka
proceduralnego PL/pgSQL dla swojej bazy danych.

%package module-plperl
Summary:	PL/perl - PostgreSQL procedural language
Summary(pl):	PL/perl - jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')

%description module-plperl
From PostgreSQL documentation:

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/Perl procedural language for your database you have to
run createlang command.

%description module-plperl -l pl
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla jêzyków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurê wyzwalacza lub funkcjê w jêzyku
proceduralnym, baza danych nie ma pojêcia jak interpretowaæ tego typu
funkcjê. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak j± wykonaæ. Interpreter jest odpowiedni±, specjaln±
funkcj±, która jest skompilowana w obiekt dzielony i ³adowany w razie
potrzeby.

Za pomoc± polecenia createlang mo¿na dodaæ obs³ugê jêzyka
proceduralnego PL/Perl dla swojej bazy danych.

%package module-plphp
Summary:	PL/PHP - PostgreSQL procedural language
Summary(pl):	PL/PHP - jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
%{?requires_php_extension}

%description module-plphp
From PostgreSQL documentation:

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/PHP procedural language for your database you have to
run createlang command.

%description module-plphp -l pl
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla jêzyków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurê wyzwalacza lub funkcjê w jêzyku
proceduralnym, baza danych nie ma pojêcia jak interpretowaæ tego typu
funkcjê. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak j± wykonaæ. Interpreter jest odpowiedni±, specjaln±
funkcj±, która jest skompilowana w obiekt dzielony i ³adowany w razie
potrzeby.

Za pomoc± polecenia createlang mo¿na dodaæ obs³ugê jêzyka
proceduralnego PL/PHP dla swojej bazy danych.

%package module-plpython
Summary:	PL/Python - PostgreSQL procedural language
Summary(pl):	PL/Python - jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python

%description module-plpython
From PostgreSQL documentation:

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/Python procedural language for your database you have to
run createlang command.

%description module-plpython -l pl
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla jêzyków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurê wyzwalacza lub funkcjê w jêzyku
proceduralnym, baza danych nie ma pojêcia jak interpretowaæ tego typu
funkcjê. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak j± wykonaæ. Interpreter jest odpowiedni±, specjaln±
funkcj±, która jest skompilowana w obiekt dzielony i ³adowany w razie
potrzeby.

Za pomoc± polecenia createlang mo¿na dodaæ obs³ugê jêzyka
proceduralnego PL/Python dla swojej bazy danych.

%package module-pltcl
Summary:	PL/Tcl - PostgreSQL procedural language
Summary(pl):	PL/Tcl - jêzyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-pltcl
From PostgreSQL documentation:

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/Tcl procedural language for your database you have to run
createlang command.

%description module-pltcl -l pl
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla jêzyków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurê wyzwalacza lub funkcjê w jêzyku
proceduralnym, baza danych nie ma pojêcia jak interpretowaæ tego typu
funkcjê. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak j± wykonaæ. Interpreter jest odpowiedni±, specjaln±
funkcj±, która jest skompilowana w obiekt dzielony i ³adowany w razie
potrzeby.

Za pomoc± polecenia createlang mo¿na dodaæ obs³ugê jêzyka
proceduralnego PL/Tcl dla swojej bazy danych.

%package module-lo
Summary:	Large Objects module for PostgreSQL
Summary(pl):	Modu³ Large Objects dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-lo
Large Objects module for PostgreSQL adds a new data type 'lo', some
support functions and a trigger which handles the orphaning problem.

%description module-lo -l pl
Modu³ Large Objects dla PostgreSQL-a dodaje nowy typ danych 'lo',
kilka funkcji pomocniczych i wyzwalacz rozwi±zuj±cy problem
osieroconych obiektów.

%package module-pgcrypto
Summary:	Cryptographic functions for PostgreSQL
Summary(pl):	Funkcje kryptograficzne dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-pgcrypto
Cryptographic functions for PostgreSQL.

%description module-pgcrypto -l pl
Funkcje kryptograficzne dla PostgreSQL.

%package module-tsearch2
Summary:	Full text extension for PostgreSQL
Summary(pl):	Rozszerzenie pe³notekstowe dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-tsearch2
Implementation of a new data type tsvector - a searchable data type
with indexed access:
http://www.sai.msu.su/~megera/postgres/gist/tsearch/V2/

%description module-tsearch2 -l pl
Implementacja nowego typu danych tsvector - typu danych podlegaj±cego
przeszukiwaniu z dostêpem poprzez indeksy:
http://www.sai.msu.su/~megera/postgres/gist/tsearch/V2/

%prep
%setup -q -a8
%patch0 -p1
%{?with_absolute_dbpaths:%patch1 -p1}
%patch2 -p1
%patch3 -p1
%patch4 -p1
#patch5 -p1	needed for glibc2.3.4 + gcc4

%if %{with php}
patch -p1 < plphp.patch
%endif

tar xzf doc/man*.tar.gz

mkdir doc/unpacked
tar zxf doc/postgres.tar.gz -C doc/unpacked

# Erase all CVS dirs
#find contrib -type d -name CVS -exec rm -rf {} \;

%build
%{__aclocal} -I config
%{__autoconf}
%configure \
	CFLAGS="%{rpmcflags} -DNEED_REENTRANT_FUNCS" \
	--disable-rpath \
	--enable-depend \
	--enable-integer-datetimes \
	%{?with_pgsql_locale:--enable-locale} \
	%{?with_pgsql_multibyte:--enable-multibyte} \
	--enable-nls \
	--enable-recode \
	--enable-syslog \
	--enable-thread-safety \
	--enable-unicode-conversion \
	--with-CXX \
	%{?with_kerberos5:--with-krb5} \
	--with-openssl \
	--with-pam \
	%{?with_perl:--with-perl} \
	%{?with_php:--with-php=/usr/include/php} \
	%{?with_python:--with-python} \
	%{?with_tcl:--with-tcl} \
	--with-x \
	--without-docdir 

%{__make}
%{__make} -C contrib/lo
%{__make} -C contrib/pgcrypto
%{__sed} -i 's:contrib/::g' contrib/tsearch2/tsearch.sql.in
%{__make} -C contrib/tsearch2
%{__make} -C src/tutorial \
	NO_PGXS=1

%ifnarch sparc sparcv9 sparc64 alpha
%{?with_tests:%{__make} check}
%endif

%if %{with php}
cd src/pl/plphp
%{__make}
cd ../../../
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{rc.d/init.d,sysconfig}} \
	$RPM_BUILD_ROOT{/var/{lib/pgsql,log},%{_pgsqldir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_mandir} \
	$RPM_BUILD_ROOT/home/services/postgres

install src/tutorial/*.sql $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__cc} -shared -Wl,-soname,libpq.so.3 -o $RPM_BUILD_ROOT%{_libdir}/libpq.so.3.0.0 -L$RPM_BUILD_ROOT%{_libdir} -lpq

%if %{with perl}
%{__make} install -C src/pl/plperl \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C contrib/lo install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C contrib/pgcrypto install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C contrib/tsearch2 install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with php}
cd src/pl/plphp
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ../../../
%endif

touch $RPM_BUILD_ROOT/var/log/pgsql

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/postgresql
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/postgresql

install -d howto
tar zxf %{SOURCE2} -C howto

%py_comp $RPM_BUILD_ROOT%{py_libdir}
%py_ocomp $RPM_BUILD_ROOT%{py_libdir}

# find locales
for f in libpq pg_controldata pg_dump pg_resetxlog pgscripts postgres psql initdb pg_ctl pg_config; do
	%find_lang $f
done
# merge locales
cat pgscripts.lang pg_resetxlog.lang postgres.lang pg_controldata.lang > main.lang
cat pg_dump.lang psql.lang initdb.lang pg_ctl.lang > clients.lang

# Remove Contrib documentation. We use macro %doc
rm -rf $RPM_BUILD_ROOT/contrib

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
		if [ `cat $pgdir/PG_VERSION` != '8.1' ]; then
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

%groupadd -g 88 -r postgres
%useradd -M -o -r -u 88 -d /home/services/postgres -s /bin/sh -g postgres -c "PostgreSQL Server" postgres

if [ -n "`/bin/id -u postgres 2>/dev/null`" ]; then
	/usr/sbin/usermod -d /home/services/postgres postgres
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

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	ecpg -p /sbin/ldconfig
%postun	ecpg -p /sbin/ldconfig

%files -f main.lang
%defattr(644,root,root,755)
%doc COPYRIGHT README HISTORY doc/{FAQ*,README*,bug.template}
%attr(754,root,root) /etc/rc.d/init.d/postgresql
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/postgresql

%attr(755,root,root) %{_bindir}/initdb
%attr(755,root,root) %{_bindir}/ipcclean
%attr(755,root,root) %{_bindir}/pg_controldata
%attr(755,root,root) %{_bindir}/pg_ctl
%attr(755,root,root) %{_bindir}/pg_resetxlog
%attr(755,root,root) %{_bindir}/postgres
%attr(755,root,root) %{_bindir}/postmaster

%attr(755,root,root) %{_pgmoduledir}/ascii*
%attr(755,root,root) %{_pgmoduledir}/cyrillic*
%attr(755,root,root) %{_pgmoduledir}/euc*
%attr(755,root,root) %{_pgmoduledir}/latin*
%attr(755,root,root) %{_pgmoduledir}/utf*

%dir %{_pgsqldir}
%dir %{_datadir}/postgresql
%dir %{_datadir}/postgresql/timezone
%{_datadir}/postgresql/*.bki
%{_datadir}/postgresql/*.sample
%{_datadir}/postgresql/*.description
%{_datadir}/postgresql/*.sql
%{_datadir}/postgresql/*.txt
%{_datadir}/postgresql/timezone/*

%attr(700,postgres,postgres) /home/services/postgres
%attr(700,postgres,postgres) %dir /var/lib/pgsql
%attr(640,postgres,postgres) %config(noreplace) %verify(not md5 mtime size) /var/log/pgsql

%{_mandir}/man1/initdb.1*
%{_mandir}/man1/ipcclean.1*
%{_mandir}/man1/pg_controldata.1*
%{_mandir}/man1/pg_ctl.1*
%{_mandir}/man1/pg_resetxlog.1*
%{_mandir}/man1/postgres.1*
%{_mandir}/man1/postmaster.1*

%files doc
%defattr(644,root,root,755)
%doc doc/unpacked/* doc/src/FAQ howto
%{_examplesdir}/%{name}-%{version}

%files libs -f libpq.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpq.so.*
%dir %{_pgmoduledir}

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

%files devel -f pg_config.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pg_config
%attr(755,root,root) %{_libdir}/libpq.so
%dir %{_includedir}/postgresql
%{_includedir}/libpq-fe.h
%{_includedir}/pg_config.h
%{_includedir}/pg_config_manual.h
%{_includedir}/pg_config_os.h
%{_includedir}/postgres_ext.h
%dir %{_includedir}/postgresql/internal
%{_includedir}/postgresql/internal/c.h
%{_includedir}/postgresql/internal/libpq-int.h
%{_includedir}/postgresql/internal/port.h
%{_includedir}/postgresql/internal/postgres_fe.h
%{_includedir}/postgresql/internal/pqexpbuffer.h
%{_includedir}/postgresql/internal/libpq
%{_includedir}/libpq
%{_mandir}/man1/pg_config.1*

%files backend-devel
%defattr(644,root,root,755)
%{_includedir}/postgresql/server
%dir %{_pgmoduledir}/pgxs
%attr(755,root,root) %{_pgmoduledir}/pgxs/config
%{_pgmoduledir}/pgxs/src

%files static
%defattr(644,root,root,755)
%{_libdir}/libecpg.a
%{_libdir}/libecpg_compat.a
%{_libdir}/libpq.a
%{_libdir}/libpgtypes.a
%{_libdir}/libpgport.a

%files clients -f clients.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/clusterdb
%attr(755,root,root) %{_bindir}/createdb
%attr(755,root,root) %{_bindir}/createlang
%attr(755,root,root) %{_bindir}/createuser
%attr(755,root,root) %{_bindir}/dropdb
%attr(755,root,root) %{_bindir}/droplang
%attr(755,root,root) %{_bindir}/dropuser
%attr(755,root,root) %{_bindir}/pg_dump
%attr(755,root,root) %{_bindir}/pg_dumpall
%attr(755,root,root) %{_bindir}/pg_restore
%attr(755,root,root) %{_bindir}/psql
%attr(755,root,root) %{_bindir}/reindexdb
%attr(755,root,root) %{_bindir}/vacuumdb

%{_mandir}/man1/clusterdb.1*
%{_mandir}/man1/createdb.1*
%{_mandir}/man1/createlang.1*
%{_mandir}/man1/createuser.1*
%{_mandir}/man1/dropdb.1*
%{_mandir}/man1/droplang.1*
%{_mandir}/man1/dropuser.1*
%{_mandir}/man1/pg_dump.1*
%{_mandir}/man1/pg_dumpall.1*
%{_mandir}/man1/pg_restore.1*
%{_mandir}/man1/psql.1*
%{_mandir}/man1/reindexdb.1*
%{_mandir}/man1/vacuumdb.1*
%{_mandir}/man7/*.7*

%files module-plpgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plpgsql.so

%if %{with perl}
%files module-plperl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plperl.so
%endif

%if %{with python}
%files module-plpython
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plpython.so
%endif

%if %{with tcl}
%files module-pltcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pltcl_*
%attr(755,root,root) %{_pgmoduledir}/pltcl.so
%endif

%files module-lo
%defattr(644,root,root,755)
%doc contrib/lo/README.lo
%attr(755,root,root) %{_pgmoduledir}/lo.so
%{_pgsqldir}/lo*.sql

%files module-pgcrypto
%defattr(644,root,root,755)
%doc contrib/pgcrypto/README*
%attr(755,root,root) %{_pgmoduledir}/pgcrypto.so
%{_pgsqldir}/pgcrypto.sql

%files module-tsearch2
%defattr(644,root,root,755)
%doc contrib/tsearch2/README*
%attr(755,root,root) %{_pgmoduledir}/tsearch2.so
%{_pgsqldir}/tsearch2.sql
%{_pgsqldir}/untsearch2.sql
%{_pgsqldir}/*.stop
