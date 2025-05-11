# TODO:
# - subpackage *_plperl and *_plpython contribs?
# - think about pg_upgrade integration (sysconfig variable to allow upgrade from 8.3+ without dump/restore?)
#   create postgresqlM.N packages with parts of old pgsql required by pg_upgrade
# - test init script (db initialization)
#
# Conditional build:
%bcond_without	tests			# disable testing
%bcond_without	tcl			# disable Tcl support
%bcond_without	kerberos5		# disable kerberos5 support
%bcond_without	llvm			# disable llvm based JIT support
%bcond_without	perl			# disable Perl support
%bcond_without	python			# disable Python support
%bcond_with	bonjour			# Bonjour/DNS_SD support
%bcond_without	ldap			# disable LDAP support
%bcond_without	selinux			# sepgsql contrib module
%bcond_without	systemd			# systemd (notify) support
%bcond_with	systemtap		# systemtap/dtrace probes
%bcond_with	absolute_dbpaths	# enable absolute paths to create database
					# (disabled by default because it is a security risk)
#

%define mver 16

Summary:	PostgreSQL Data Base Management System
Summary(de.UTF-8):	PostgreSQL Datenbankverwaltungssystem
Summary(es.UTF-8):	Gestor de Banco de Datos PostgreSQL
Summary(fr.UTF-8):	Sysème de gestion de base de données PostgreSQL
Summary(pl.UTF-8):	PostgreSQL - system bazodanowy
Summary(pt_BR.UTF-8):	Gerenciador de Banco de Dados PostgreSQL
Summary(ru.UTF-8):	PostgreSQL - система управления базами данных
Summary(tr.UTF-8):	Veri Tabanı Yönetim Sistemi
Summary(uk.UTF-8):	PostgreSQL - система керування базами даних
Summary(zh_CN.UTF-8):	PostgreSQL 客户端程序和库文件
Name:		postgresql
Version:	%{mver}.9
Release:	1
License:	BSD
Group:		Applications/Databases
Source0:	https://ftp.postgresql.org/pub/source/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	04502cd79a9e3964b0e9fb6981ce78b6
Source1:	%{name}.init
Source2:	pgsql-Database-HOWTO-html.tar.gz
# Source2-md5:	5b656ddf1db41965761f85204a14398e
Source3:	%{name}.sysconfig
Source4:	%{name}@.service
Source5:	%{name}.service
Source6:	%{name}.target
Patch0:		%{name}-conf.patch
Patch1:		%{name}-absolute_dbpaths.patch
Patch2:		%{name}-ecpg-includedir.patch
Patch3:		ac.patch
Patch5:		%{name}-heimdal.patch
Patch6:		%{name}-link.patch
URL:		https://www.postgresql.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
%{?with_bonjour:BuildRequires:	avahi-compat-libdns_sd-devel}
# not needed for releases... but fixes something in snapshot
BuildRequires:	bison >= 1.875
%{?with_llvm:BuildRequires:	clang >= 3.9}
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	flex >= 2.5.31
BuildRequires:	gettext-tools
BuildRequires:	gnome-doc-tools
%{?with_kerberos5:BuildRequires:	heimdal-devel >= 8.0}
BuildRequires:	libicu-devel
%{?with_selinux:BuildRequires:	libselinux-devel >= 2.1.10}
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.23
BuildRequires:	libxslt-devel
BuildRequires:	libxslt-progs
%{?with_llvm:BuildRequires: llvm-devel >= 3.9}
BuildRequires:	ncurses-devel >= 5.0
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel >= 1.1.1
BuildRequires:	pam-devel
%if %{with perl}
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-devel
%endif
%if %{with python}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.671
%{?with_systemd:BuildRequires:	systemd-devel >= 1:209}
%{?with_systemtap:BuildRequires:	systemtap-sdt-devel}
%{?with_tcl:BuildRequires:	tcl-devel >= 8.4.3}
%{?with_tests:BuildRequires:	tzdata}
BuildRequires:	zlib-devel
Requires(post):	/bin/id
Requires(post):	/usr/sbin/usermod
Requires(post,preun):	/sbin/chkconfig
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	%{name}-clients >= %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	rc-scripts >= 0.4.3.0
Requires:	systemd-units >= 38
Requires:	tzdata
Provides:	group(postgres)
Provides:	user(postgres)
%if %{with llvm}
Suggests:	%{name}-module-llvmjit = %{version}-%{release}
%endif
Obsoletes:	postgresql-data < 6.5
Obsoletes:	postgresql-ln < 8.3.0
Obsoletes:	postgresql-module-datetime < 7.1
Obsoletes:	postgresql-module-plpgsql < 9.0.0-1
Obsoletes:	postgresql-module-tsearch2 < 8.3.0
Obsoletes:	postgresql-replicate < 8.3.0
Obsoletes:	postgresql-replicate-tools < 8.3.0
Obsoletes:	postgresql-server
Obsoletes:	postgresql-test
Obsoletes:	postgresql-upgrade < 9.2.1-1
Obsoletes:	postgresql-upstart < 9.4.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pgmoduledir	%{_libdir}/postgresql
%define		_pgsqldir	%{_datadir}/postgresql/extension

%define		_ulibdir	/usr/lib

%define          filterout_c     -fvar-tracking-assignments
%define          filterout_cxx   -fvar-tracking-assignments

# omitted contribs:
# spi, test_decoding, worker_spi - examples/tests
# tsearch2 - old module for compatibility only
%define	contrib_modules	adminpack amcheck auth_delay auto_explain bloom btree_gin btree_gist citext cube dblink dict_int dict_xsyn earthdistance file_fdw fuzzystrmatch hstore %{?with_perl:hstore_plperl} %{?with_python:hstore_plpython} intagg intarray isn %{?with_perl:jsonb_plperl} %{?with_python:jsonb_plpython} lo ltree %{?with_python:ltree_plpython} oid2name pageinspect passwordcheck pg_buffercache pg_freespacemap pg_prewarm pg_stat_statements pg_trgm pg_visibility pgcrypto pgrowlocks pgstattuple postgres_fdw seg %{?with_selinux:sepgsql} sslinfo tablefunc tcn tsm_system_rows tsm_system_time unaccent uuid-ossp vacuumlo xml2

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

%description -l de.UTF-8
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

%description -l es.UTF-8
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

%description -l fr.UTF-8
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

%description -l pl.UTF-8
System Zarządzania Bazą Danych PostgreSQL (dawniej znany jako
Postgres, następnie jako Postgres95).

PostgreSQL jest rozszerzeniem systemu zarządzania baz danych POSTGRES,
prototypu DBMS następnej generacji. Co prawda PostgreSQL odziedziczył
model danych oraz bogaty zbiór różnych typów danych, to jednak język
zapytań PostQuel został zastąpiony rozszerzonym SQL-em. PostgreSQL
jest wolnym oprogramowaniem i kody źródłowe tego oprogramowania są w
pełni dostępne.

System PostgreSQL jest tworzony przez zespół ludzi, którzy są zapisani
na listę dyskusyjną dotyczącą PostgreSQL-a. Obecnym koordynatorem jest
Marc G. Fournier (scrappy@postgreSQL.org). Wymieniony wyżej zespół
jest odpowiedzialny za aktualny i przyszły rozwój systemu PostgreSQL.

Autorami PostgreSQL-a 1.01 byli Andrew Yu oraz Jolly Chen. Wielu
innych pomagało przenosząc na różne platformy, testując, analizując i
rozszerzając kod. Oryginalny kod Postgres-a, na podstawie którego
PostgreSQL powstał, był wysiłkiem wielu absolwentów, studentów oraz
zespołu programistów, którzy pracowali pod kierunkiem profesora
Michaela Stonebrakera z Uniwersytetu Kalifornii w Berkeley.

Nazwa oryginalna oprogramowania tworzonego w Berkeley brzmiała
Postgres. W 1995 roku dodano język zapytań SQL i nazwę zmieniono na
Postgres95. W końcu roku 1996 nazwę ostatecznie zmieniono na
PostgreSQL.

PostgreSQL może być uruchomiony pod następującymi systemami: Solaris,
SunOS, HPUX, AIX, Linux, Irix, FreeBSD i innymi systemami uniksowymi.

%description -l pt_BR.UTF-8
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

%description -l ru.UTF-8
PostgreSQL - система управления базами данных (прежде известная как
Postgres, потом как Postgres95).

PostgreSQL - это расширенная версия системы управления базами данных
POSTGRES, исследовательского прототипа DBMS следующей генерации.
Сохраняя мощную модель данных и богатый набор типов данных POSTGRES,
она заменяет язык запросов PostQuel расширенным набором SQL.
PostgreSQL бесплатен и поставляется в виде полного комплекта исходных
текстов.

PostgreSQL разрабатывался командой Internet-разработчиков, подписанных
на список рассылки, посвященный разработке PostgreSQL. В настоящее
время координатором является Marc G. Fournier
(scrappy@postgreSQL.org). Эта команда в настоящее время отвечает за
все текущие и будущие разработки PostgreSQL.

Авторами PostgreSQL 1.01 были Andrew Yu и Jolly Chen. Многие внесли
свой вклад в портирование, тестирование, отладку и улучшение кода.
Оригинальный код Postgres, от которого произошел PostgreSQL, был
создан усилиями студентов, аспирантов и персонала, работающего под
руководством профессора Michael Stonebraker в University of
California, Berkeley.

Оригинальное название ПО в Berkeley было Postgres. Когда в 1995 году
была добавлена функциональность SQL, название изменилось на
Postgres95. В конце 1996 года оно еще раз изменилось и теперь это
PostgreSQL.

PostgreSQL работает на Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD
и большинстве других разновидностей Unix.

%description -l tr.UTF-8
PostgreSQL, POSTGRES'den türemiş bir veri tabanı yönetim sistemidir
(DBMS). Güçlü veri modeli ve zengin POSTGRES veri tiplerini
desteklerken SQL'in genişletilmiş bir altkümesi yerine PostQuel
sorgulama dilini koyar.

%description -l uk.UTF-8
PostgreSQL - система керування базами даних (раніш відома як Postgres,
потім як Postgres95).

PostgreSQL - це розширена версія системи керування базами даних
POSTGRES, дослідницького прототипу DBMS наступної генерації.
Зберігаючи потужну модель даних та багатий набір типів даних POSTGRES,
вона замінює мову запитів PostQuel розширеним набором SQL. PostgreSQL
безкоштовна та поставляється у вигляді повного комплекту вихідних
текстів.

PostgreSQL розробляється командою Internet-програмістів, учасників
списку розсилки, присвяченого розробці PostgreSQL. Наразі
координатором є Marc G. Fournier (scrappy@postgreSQL.org). Ця команда
відповідає за всі поточні та майбутні розробки PostgreSQL.

Авторами PostgreSQL 1.01 були Andrew Yu та Jolly Chen. Багато людей
внесли свій внесок в портування, тестування, відладку та покращення
коду. Оригінальний код Postgres, від якого походить PostgreSQL, був
створений зусиллями студентів, аспірантів та персоналу, який працював
під керівництвом професора Michael Stonebraker в University of
California, Berkeley.

Оригінальна назва програми в Berkeley була Postgres. Коли в 1995 році
було додано функціональність SQL, назва змінилася на Postgres95. В
кінці 1996 року вона ще раз змінилась і зараз це PostgreSQL.

PostgreSQL працює на Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD
та більшості інших різновидів Unix.

%package devel
Summary:	PostgreSQL development header files and libraries
Summary(de.UTF-8):	PostgreSQL-Entwicklungs-Header-Dateien und Libraries
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas PostgreSQL
Summary(fr.UTF-8):	En-têtes et bibliothèques de développement PostgreSQL
Summary(pl.UTF-8):	PostgreSQL - pliki nagłówkowe i biblioteki
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para desenvolvimento com o PostgreSQL
Summary(ru.UTF-8):	PostgreSQL - хедеры и библиотеки разработчика
Summary(tr.UTF-8):	PostgreSQL başlık dosyaları ve kitaplıklar
Summary(uk.UTF-8):	PostgreSQL - хедери та бібліотеки програміста
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains header files and libraries required to compile
applications that are talking directly to the PostgreSQL backend
server.

%description devel -l de.UTF-8
Dieses Paket enthält die Header-Dateien und Libraries, die zum
Kompilieren von Applikationen notwendig sind, die direkt mit dem
PostgreSQL-Backend-Server kommunizieren.

%description devel -l es.UTF-8
Este paquete contiene archivos de inclusión y bibliotecas requeridas
para compilación de aplicativos que se comunican directamente con el
servidor backend PostgreSQL.

%description devel -l fr.UTF-8
Ce package contient les fichiers d'en-tête et les bibliothéques
nécessaires pour compiler des applications ayant des échanges directs
avec le serveur du backend PostgreSQL.

%description devel -l pl.UTF-8
Pakiet zawiera nagłówki oraz biblioteki wymagane do kompilacji
aplikacji łączących się bezpośrednio z serwerem PostgreSQL.

%description devel -l pt_BR.UTF-8
Este pacote contém arquivos de inclusão e bibliotecas requeridas para
compilação de aplicativos que se comunicam diretamente com o servidor
backend PostgreSQL.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры и библиотеки, необходимые для сборки
приложений, непосредственно взаимодействующих с сервером PostgreSQL.

%description devel -l tr.UTF-8
Bu paket, PostgreSQL sunucusuyla konuşacak yazılımlar geliştirmek için
gereken başlık dosyalarını ve kitaplıkları içerir.

%description devel -l uk.UTF-8
Цей пакет містить хедери та бібліотеки, необхідні для розробки
програм, які безпосередньо взаємодіють з сервером PostgreSQL.

%package backend-devel
Summary:	PostgreSQL backend development header files
Summary(pl.UTF-8):	PostgreSQL - pliki nagłówkowe dla backendu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

%description backend-devel
This package contains header files required to compile functions that
could be loaded directly by backend

%description backend-devel -l pl.UTF-8
Pakiet zawiera nagłówki wymagane do kompilacji funkcji ktore moga byc
bezposrednio ladowane przez beckend serwera PostgreSQL.

%package clients
Summary:	Clients needed to access a PostgreSQL server
Summary(es.UTF-8):	Clientes necesarios para acceder al servidor PostgreSQL
Summary(pl.UTF-8):	Klienci wymagani do dostępu do serwera PostgreSQL
Summary(pt_BR.UTF-8):	Clientes necessários para acessar o servidor PostgreSQL
Summary(ru.UTF-8):	Клиентские программы, необходимые для доступа к серверу PostgreSQL
Summary(uk.UTF-8):	Клієнтські програми, необхідні для доступу до сервера PostgreSQL
Group:		Applications/Databases
Requires:	%{name}-libs = %{version}-%{release}

%description clients
This package includes only the clients needed to access an PostgreSQL
server. The server is included in the main package. If all you need is
to connect to another PostgreSQL server, the this is the only package
you need to install. Clients include several command-line utilities
you can use to manage your databases on a remote PostgreSQL server.

%description clients -l es.UTF-8
Este paquete incluye solamente los clientes necesarios para acceder un
servidor PostgreSQL. El servidor está en el paquete principal.

%description clients -l pl.UTF-8
Pakiet zawiera programy klienckie potrzebne dla dostępu do serwera
PostgreSQL oraz narzędzia do zarządzania bazami działające z linii
poleceń. Serwer znajduje się w głównym pakiecie.

%description clients -l pt_BR.UTF-8
Este pacote inclui somente os clientes necessários para acessar um
servidor PostgreSQL. O servidor está no pacote principal.

%description clients -l ru.UTF-8
Этот пакет включает только клиентские программы и библиотеки,
необходимые для доступа к серверу PostgreSQL. Сервер входит в главный
пакет. Если вам надо только работать с другим сервером PostgreSQL, это
единственный пакет, который вам надо установить.

Теперь пакеты с библиотеками для разных языков программирования (C,
C++, Perl и Tcl) разделены. Этот пакет включает только библиотеки для
языка C.

%description clients -l uk.UTF-8
Цей пакет містить тільки клієнтські програми та бібліотеки, необхідні
для доступу до сервера PostgreSQL. Сервер міститься в головному
пакеті. Якщо вам потрібно працювати з іншим сервером PostgreSQL, це
єдиний пакет, який вам треба встановити.

Тепер пакети з бібліотеками для різних мов програмування (C, C++, Perl
і Tcl) розділені. Цей пакет містить тільки бібліотеки для мови C.

%package doc
Summary:	Documentation for PostgreSQL
Summary(pl.UTF-8):	Dodatkowa dokumantacja dla PostgreSQL
Group:		Applications/Databases
BuildArch:	noarch

%description doc
This package includes documentation and HOWTO for programmer, admin
etc., in HTML format.

%description doc -l pl.UTF-8
Pakiet ten zawiera dokumentację oraz HOWTO m.in. dla programistów,
administratorów w formacie HTML.

%package libs
Summary:	PostgreSQL libraries
Summary(es.UTF-8):	Biblioteca compartida del PostgreSQL
Summary(pl.UTF-8):	Biblioteki dzielone programu PostgreSQL
Summary(pt_BR.UTF-8):	Biblioteca compartilhada do PostgreSQL
Summary(zh_CN.UTF-8):	PostgreSQL 客户所需要的共享库
Group:		Libraries
Requires:	openssl%{?_isa} >= 1.1.1

%description libs
PostgreSQL shared libraries.

%description libs -l es.UTF-8
Este paquete contiene la biblioteca compartida para acceso al
PostgreSQL.

%description libs -l pl.UTF-8
Biblioteki dzielone programu PostgreSQL.

%description libs -l pt_BR.UTF-8
Este pacote contém a biblioteca compartilhada para acesso ao
PostgreSQL.

%package ecpg
Summary:	Embedded SQL in C interface
Summary(pl.UTF-8):	Interfejs wbudowanego SQL-a w język C
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description ecpg
Embedded SQL in C interface.

%description ecpg -l pl.UTF-8
Interfejs wbudowanego SQL-a w język C.

%package ecpg-devel
Summary:	Embedded SQL in C interface files
Summary(pl.UTF-8):	Pliki programistyczne interfejsu wbudowanego SQL-a w język C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ecpg = %{version}-%{release}

%description ecpg-devel
Embedded SQL in C interface files.

%description ecpg-devel -l pl.UTF-8
Pliki programistyczne interfejsu wbudowanego SQL-a w język C.

%package static
Summary:	PostgreSQL static libraries
Summary(es.UTF-8):	Bibliotecas estaticas PostgreSQL
Summary(pl.UTF-8):	Biblioteki statyczne programu PostgreSQL
Summary(pt_BR.UTF-8):	Bibliotecas estáticas PostgreSQL
Summary(ru.UTF-8):	Статические библиотеки для программирования с PostgreSQL
Summary(uk.UTF-8):	Статичні бібліотеки для програмування з PostgreSQL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
PostgreSQL static libraries.

%description static -l es.UTF-8
Este paquete contiene bibliotecas estaticas requerida para compilación
de aplicativos que se comunican directamente con el servidor backend
PostgreSQL.

%description static -l pl.UTF-8
Biblioteki statyczne programu PostgreSQL.

%description static -l pt_BR.UTF-8
Este pacote contém as bibliotecas estáticas requeridas para compilação
de aplicativos que se comunicam diretamente com o servidor backend
PostgreSQL.

%description static -l ru.UTF-8
Это отдельный пакет со статическими библиотеками, которые больше не
входят в %{name}-devel.

%description static -l uk.UTF-8
Це окремий пакет зі статичними бібліотеками, які більш не входять в
%{name}-devel.

%package module-llvmjit
Summary:	LLVM JIT module for PostgreSQL
Summary(pl.UTF-8):	Moduł LLVM JIT dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-llvmjit
LLVM JIT module for PostgreSQL.

%description module-llvmjit -l pl.UTF-8
Moduł LLVM JIT dla PostgreSQL-a.

%package module-plperl
Summary:	PL/perl - PostgreSQL procedural language
Summary(pl.UTF-8):	PL/perl - język proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

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

%description module-plperl -l pl.UTF-8
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla języków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurę wyzwalacza lub funkcję w języku
proceduralnym, baza danych nie ma pojęcia jak interpretować tego typu
funkcję. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak ją wykonać. Interpreter jest odpowiednią, specjalną
funkcją, która jest skompilowana w obiekt dzielony i ładowany w razie
potrzeby.

Za pomocą polecenia createlang można dodać obsługę języka
proceduralnego PL/Perl dla swojej bazy danych.

%package module-plpython
Summary:	PL/Python - PostgreSQL procedural language
Summary(pl.UTF-8):	PL/Python - język proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

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

%description module-plpython -l pl.UTF-8
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla języków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurę wyzwalacza lub funkcję w języku
proceduralnym, baza danych nie ma pojęcia jak interpretować tego typu
funkcję. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak ją wykonać. Interpreter jest odpowiednią, specjalną
funkcją, która jest skompilowana w obiekt dzielony i ładowany w razie
potrzeby.

Za pomocą polecenia createlang można dodać obsługę języka
proceduralnego PL/Python dla swojej bazy danych.

%package module-pltcl
Summary:	PL/Tcl - PostgreSQL procedural language
Summary(pl.UTF-8):	PL/Tcl - język proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Requires:	tcl(Pgtcl)

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

%description module-pltcl -l pl.UTF-8
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla języków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurę wyzwalacza lub funkcję w języku
proceduralnym, baza danych nie ma pojęcia jak interpretować tego typu
funkcję. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak ją wykonać. Interpreter jest odpowiednią, specjalną
funkcją, która jest skompilowana w obiekt dzielony i ładowany w razie
potrzeby.

Za pomocą polecenia createlang można dodać obsługę języka
proceduralnego PL/Tcl dla swojej bazy danych.

%package module-dblink
Summary:	dblink module for PostgreSQL
Summary(pl.UTF-8):	Moduł dblink dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-dblink
dblink module for PostgreSQL provides functions returning results from
remote database.

%description module-dblink -l pl.UTF-8
Moduł dblink dla PostgreSQL-a udostępnia funkcje zwracające wyniki ze
zdalnej bazy danych.

%package module-lo
Summary:	Large Objects module for PostgreSQL
Summary(pl.UTF-8):	Moduł Large Objects dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-lo
Large Objects module for PostgreSQL adds a new data type 'lo', some
support functions and a trigger which handles the orphaning problem.

%description module-lo -l pl.UTF-8
Moduł Large Objects dla PostgreSQL-a dodaje nowy typ danych 'lo',
kilka funkcji pomocniczych i wyzwalacz rozwiązujący problem
osieroconych obiektów.

%package module-pg_trgm
Summary:	Trigram matching for PostgreSQL
Summary(pl.UTF-8):	Dopasowanie trigramowe dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-pg_trgm
This module provides functions and index classes for determining the
similarity of text based on trigram matching.

%description module-pg_trgm -l pl.UTF-8
Ten moduł dostarcza funkcje i klasy do rozpoznawania podobnych tekstów
w oparciu o dopasowywanie trigramowe (trigram matching).

%package module-pgcrypto
Summary:	Cryptographic functions for PostgreSQL
Summary(pl.UTF-8):	Funkcje kryptograficzne dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-pgcrypto
Cryptographic functions for PostgreSQL.

%description module-pgcrypto -l pl.UTF-8
Funkcje kryptograficzne dla PostgreSQL.

%package module-sepgsql
Summary:	PostgreSQL external security provider using SELinux
Summary(pl.UTF-8):	Zewnętrzny moduł bezpieczeństwa PostgreSQL-a wykorzystujący SELinuksa
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Requires:	libselinux >= 2.1.10

%description module-sepgsql
PostgreSQL external security provider using SELinux.

%description module-sepgsql -l pl.UTF-8
Zewnętrzny moduł bezpieczeństwa PostgreSQL-a wykorzystujący SELinuksa.

%package module-tablefunc
Summary:	crosstab functions for PostgreSQL
Summary(pl.UTF-8):	Funkcje crosstab dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-tablefunc
crosstab functions for PostgreSQL.

%description module-tablefunc -l pl.UTF-8
Funkcje crosstab dla PostgreSQL-a.

%package module-xml2
Summary:	XML-handling functions for PostgreSQL
Summary(pl.UTF-8):	Funkcje do obsługi XML-a dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2 >= 1:2.6.23

%description module-xml2
Module with XML functions provides both XPath querying and XSLT
functionality. There is also a new table function which allows the
straightforward return of multiple XML results.

%description module-xml2 -l pl.UTF-8
Moduł z funkcjami XML zapewniającymi obsługę zapytań XPath oraz
funkcjonalność XSLT. Jest także nowa funkcja tabelowa pozwalająca na
bezpośrednie zwracanie wielu wyników XML.

%package contrib
Summary:	Miscellaneous PostgreSQL contrib modules
Summary(pl.UTF-8):	Różne moduły dołączone do PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description contrib
Miscellaneous PostgreSQL contrib modules.

%description contrib -l pl.UTF-8
Różne moduły dołączone do PostgreSQL-a.

%prep
%setup -q
%patch -P0 -p1
%{?with_absolute_dbpaths:%patch -P1 -p1}
%patch -P2 -p1
%patch -P3 -p1
%patch -P5 -p1
%patch -P6 -p1

# force rebuild of bison/flex files
find src -name \*.l -o -name \*.y | xargs touch

# Erase all CVS dirs
#find contrib -type d -name CVS -exec rm -rf {} \;

%build
%ifarch x32
march="-mx32"
%endif
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%configure \
	CFLAGS="%{rpmcflags} $march -DNEED_REENTRANT_FUNCS" \
	CPPFLAGS="%{rpmcppflags} $march" \
	CXXFLAGS="%{rpmcxxflags} $march" \
	BITCODE_CFLAGS="%{rpmcflags}" \
	BITCODE_CXXFLAGS="%{rpmcxxflags}" \
	--disable-rpath \
	--enable-depend \
	%{?with_systemtap:--enable-dtrace} \
	--enable-integer-datetimes \
	--enable-nls \
	--enable-thread-safety \
	%{?with_bonjour:--with-bonjour} \
	%{?with_kerberos5:--with-gssapi} \
	%{?with_ldap:--with-ldap} \
	%{?with_llvm:--with-llvm} \
	--with-libxml \
	--with-libxslt \
	--with-openssl \
	--with-pam \
	%{?with_perl:--with-perl} \
	%{?with_python:--with-python} \
	%{?with_selinux:--with-selinux} \
	--with-system-tzdata=%{_datadir}/zoneinfo \
	%{?with_systemd:--with-systemd} \
	%{?with_tcl:--with-tcl --with-tclconfig=%{_ulibdir}} \
	--with-uuid=e2fs

%{__make}

for mod in %{contrib_modules}; do \
	flags="%{rpmcflags} %{rpmcppflags} -DNEED_REENTRANT_FUNCS"
	if [ $mod = "xml2"      ]; then flags="$flags -I/usr/include/libxml2"; fi
	%{__make} -C contrib/$mod CFLAGS="$flags"
done

%{__make} -C src/tutorial \
	NO_PGXS=1

%ifnarch sparc sparcv9 sparc64 alpha
%{?with_tests:%{__make} -j1 check}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{rc.d/init.d,sysconfig}} \
	$RPM_BUILD_ROOT{/var/{lib/pgsql,log},%{_pgsqldir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_mandir} \
	$RPM_BUILD_ROOT{%{systemdunitdir},/etc/systemd/system/%{name}.target.requires} \
	$RPM_BUILD_ROOT/home/services/postgres

install src/tutorial/*.sql $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C doc/src/sgml install-man \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with perl}
%{__make} install -C src/pl/plperl \
	DESTDIR=$RPM_BUILD_ROOT
%endif

for mod in %{contrib_modules}; do \
	%{__make} -C contrib/$mod install \
		DESTDIR=$RPM_BUILD_ROOT
done

touch $RPM_BUILD_ROOT/var/log/pgsql

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/postgresql
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/postgresql

install %{SOURCE4} $RPM_BUILD_ROOT%{systemdunitdir}/%{name}@.service
install %{SOURCE5} $RPM_BUILD_ROOT%{systemdunitdir}/%{name}.service
install %{SOURCE6} $RPM_BUILD_ROOT%{systemdunitdir}/%{name}.target

install -d howto
tar zxf %{SOURCE2} -C howto

# find locales
for f in libpq5 pgscripts postgres psql initdb ecpg ecpglib6 \
	plpgsql %{?with_perl:plperl} %{?with_python:plpython} \
	pg_amcheck pg_archivecleanup pg_basebackup pg_checksums pg_config pg_controldata pg_ctl pg_dump pg_resetwal pg_rewind pg_test_fsync \
	pg_test_timing pg_upgrade pg_waldump pg_verifybackup; do
	%find_lang $f-%{mver}
done
# merge locales
merge_lang() {
	cat $(for f in $@; do echo ${f}-%{mver}.lang ; done)
}
merge_lang pgscripts postgres plpgsql \
	pg_basebackup pg_checksums pg_controldata pg_resetwal pg_rewind pg_upgrade pg_test_fsync pg_test_timing pg_waldump > main.lang
merge_lang psql initdb \
	pg_amcheck pg_archivecleanup pg_ctl pg_dump pg_verifybackup > clients.lang
merge_lang ecpg ecpglib6 > ecpg.lang

%if %{with tcl}
%find_lang pltcl-%{mver}
%endif

%if %{with selinux}
%{__mv} $RPM_BUILD_ROOT{%{_datadir}/postgresql/contrib,%{_pgsqldir}}/sepgsql.sql
%endif

cp -p src/pl/plperl/ppport.h $RPM_BUILD_ROOT%{_includedir}/postgresql/server/

# package it...?  nah, why bother.
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/postgresql/html

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans
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
		if [ $(cat $pgdir/PG_VERSION) != '%{mver}' ]; then
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
	echo "Alternatively you can use pg_upgrade for 8.3+ online upgrade with"
	echo "some restrictions: http://www.postgresql.org/docs/10.0/static/pgupgrade.html"
	echo
	echo "Warning for upgrade from version *before* 7.2."
	echo "Please note, that postgresql module path changed from"
	echo "%{_libdir}/pgsql/module to %{_libdir}/postgresql. Change the path"
	echo "in dump file before restore."
	echo
	echo "Warning for upgrade from version *before* 7.3."
	echo "Reading following webpage is encouraged:"
	echo "http://www.ca.postgresql.org/docs/momjian/upgrade_tips_7.3"
	exit 1
fi

%pre
%groupadd -g 88 -r postgres
%useradd -M -o -r -u 88 -d /home/services/postgres -s /bin/sh -g postgres -c "PostgreSQL Server" postgres

%triggerpostun -- %{name} < 9.3.3-2
#  < 7.2-2
if [ -n "`/bin/id -u postgres 2>/dev/null`" ]; then
	/usr/sbin/usermod -d /home/services/postgres postgres
fi
# < 9.3.3-2
PG_DB_CLUSTERS=""
[ -f /etc/sysconfig/postgresql ] && . /etc/sysconfig/postgresql
for pgdir in $PG_DB_CLUSTERS; do
	instance="$(echo "$pgdir" | sed -e 's/^\///;s/-/\\x2d/g;s/@/\\x40/g;s/\//-/g')"
	/bin/systemctl --quiet enable "postgresql@$instance.service" || :
done
%systemd_trigger postgresql.service

%post
/sbin/chkconfig --add postgresql
%service postgresql restart "postgresql server"
if [ "$1" -eq "1" ]; then
	PG_DB_CLUSTERS=""
	[ -f /etc/sysconfig/postgresql ] && . /etc/sysconfig/postgresql
	export SYSTEMD_LOG_LEVEL=warning SYSTEMD_LOG_TARGET=syslog
	for pgdir in $PG_DB_CLUSTERS; do
		instance="$(echo "$pgdir" | sed -e 's/^\///;s/-/\\x2d/g;s/@/\\x40/g;s/\//-/g')"
		/bin/systemctl --quiet enable "postgresql@$instance.service" || :
	done
fi
%systemd_post postgresql.service

%preun
if [ "$1" = "0" ]; then
	%service postgresql stop
	/sbin/chkconfig --del postgresql

	PG_DB_CLUSTERS=""
	[ -f /etc/sysconfig/postgresql ] && . /etc/sysconfig/postgresql
	export SYSTEMD_LOG_LEVEL=warning SYSTEMD_LOG_TARGET=syslog
	for pgdir in $PG_DB_CLUSTERS; do
		instance="$(echo "$pgdir" | sed -e 's/^\///;s/-/\\x2d/g;s/@/\\x40/g;s/\//-/g')"
		/bin/systemctl --quiet disable "postgresql@$instance.service" || :
	done
fi
%systemd_preun postgresql.service

%postun
%systemd_reload

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	ecpg -p /sbin/ldconfig
%postun	ecpg -p /sbin/ldconfig

%files -f main.lang
%defattr(644,root,root,755)
%doc COPYRIGHT README HISTORY doc/{KNOWN_BUGS,MISSING_FEATURES,TODO}
%attr(754,root,root) /etc/rc.d/init.d/postgresql
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/postgresql
%{systemdunitdir}/%{name}.service
%{systemdunitdir}/%{name}@.service
%{systemdunitdir}/%{name}.target
%dir /etc/systemd/system/%{name}.target.requires

%attr(755,root,root) %{_bindir}/initdb
%attr(755,root,root) %{_bindir}/pg_basebackup
%attr(755,root,root) %{_bindir}/pg_checksums
%attr(755,root,root) %{_bindir}/pg_controldata
%attr(755,root,root) %{_bindir}/pg_ctl
%attr(755,root,root) %{_bindir}/pg_resetwal
%attr(755,root,root) %{_bindir}/pg_receivewal
%attr(755,root,root) %{_bindir}/pg_recvlogical
%attr(755,root,root) %{_bindir}/pg_rewind
%attr(755,root,root) %{_bindir}/pg_test_fsync
%attr(755,root,root) %{_bindir}/pg_test_timing
%attr(755,root,root) %{_bindir}/pg_upgrade
%attr(755,root,root) %{_bindir}/pg_waldump
%attr(755,root,root) %{_bindir}/pgbench
%attr(755,root,root) %{_bindir}/postgres

%attr(755,root,root) %{_pgmoduledir}/cyrillic_and_mic.so
%attr(755,root,root) %{_pgmoduledir}/dict_int.so
%attr(755,root,root) %{_pgmoduledir}/dict_snowball.so
%attr(755,root,root) %{_pgmoduledir}/dict_xsyn.so
%attr(755,root,root) %{_pgmoduledir}/euc*.so
%attr(755,root,root) %{_pgmoduledir}/latin2_and_win1250.so
%attr(755,root,root) %{_pgmoduledir}/latin_and_mic.so
%attr(755,root,root) %{_pgmoduledir}/libpqwalreceiver.so
%attr(755,root,root) %{_pgmoduledir}/pgoutput.so
%attr(755,root,root) %{_pgmoduledir}/plpgsql.so
%attr(755,root,root) %{_pgmoduledir}/utf8_and_*.so
%dir %{_pgsqldir}
%{_pgsqldir}/plpgsql--*.sql
%{_pgsqldir}/plpgsql.control

%dir %{_datadir}/postgresql
%{_datadir}/postgresql/*.bki
%{_datadir}/postgresql/*.sample
%{_datadir}/postgresql/*.sql
%{_datadir}/postgresql/*.txt
%{_datadir}/postgresql/timezonesets
%{_datadir}/postgresql/tsearch_data

%dir %{_datadir}/postgresql/contrib

%attr(700,postgres,postgres) /home/services/postgres
%attr(700,postgres,postgres) %dir /var/lib/pgsql
%attr(640,postgres,postgres) %config(noreplace) %verify(not md5 mtime size) /var/log/pgsql

%{_mandir}/man1/initdb.1*
%{_mandir}/man1/pg_basebackup.1*
%{_mandir}/man1/pg_checksums.1*
%{_mandir}/man1/pg_controldata.1*
%{_mandir}/man1/pg_ctl.1*
%{_mandir}/man1/pg_resetwal.1*
%{_mandir}/man1/pg_receivewal.1*
%{_mandir}/man1/pg_recvlogical.1*
%{_mandir}/man1/pg_rewind.1*
%{_mandir}/man1/pg_waldump.1*
%{_mandir}/man1/pg_test_fsync.1*
%{_mandir}/man1/pg_test_timing.1*
%{_mandir}/man1/pg_upgrade.1*
%{_mandir}/man1/pgbench.1*
%{_mandir}/man1/postgres.1*

%files doc
%defattr(644,root,root,755)
%doc doc/src/sgml/html howto
%{_examplesdir}/%{name}-%{version}

%files libs -f libpq5-%{mver}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpq.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpq.so.5
%dir %{_pgmoduledir}
%if %{with llvm}
%dir %{_pgmoduledir}/bitcode
%endif

%files ecpg -f ecpg.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecpg
%attr(755,root,root) %{_libdir}/libecpg.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libecpg.so.6
%attr(755,root,root) %{_libdir}/libecpg_compat.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libecpg_compat.so.3
%attr(755,root,root) %{_libdir}/libpgtypes.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpgtypes.so.3
%{_mandir}/man1/ecpg.1*

%files ecpg-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecpg.so
%attr(755,root,root) %{_libdir}/libecpg_compat.so
%attr(755,root,root) %{_libdir}/libpgtypes.so
%{_includedir}/ecpg*
%{_pkgconfigdir}/libecpg.pc
%{_pkgconfigdir}/libecpg_compat.pc
%{_pkgconfigdir}/libpgtypes.pc

%files devel -f pg_config-%{mver}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pg_config
%attr(755,root,root) %{_libdir}/libpq.so
%dir %{_includedir}/postgresql
%{_includedir}/libpq-events.h
%{_includedir}/libpq-fe.h
%{_includedir}/pg_config.h
%{_includedir}/pg_config_ext.h
%{_includedir}/pg_config_manual.h
%{_includedir}/pg_config_os.h
%{_includedir}/postgres_ext.h
%dir %{_includedir}/postgresql/internal
%{_includedir}/postgresql/internal/c.h
%{_includedir}/postgresql/internal/fe-auth-sasl.h
%{_includedir}/postgresql/internal/libpq-int.h
%{_includedir}/postgresql/internal/port.h
%{_includedir}/postgresql/internal/postgres_fe.h
%{_includedir}/postgresql/internal/pqexpbuffer.h
%{_includedir}/postgresql/internal/libpq
%{_includedir}/libpq
%{_pkgconfigdir}/libpq.pc
%{_mandir}/man1/pg_config.1*

%files backend-devel
%defattr(644,root,root,755)
%{_includedir}/postgresql/server
%dir %{_pgmoduledir}/pgxs
%attr(755,root,root) %{_pgmoduledir}/pgxs/config
%{_pgmoduledir}/pgxs/src
%{_mandir}/man3/SPI_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libecpg.a
%{_libdir}/libecpg_compat.a
%{_libdir}/libpq.a
%{_libdir}/libpgcommon.a
%{_libdir}/libpgfeutils.a
%{_libdir}/libpgtypes.a
%{_libdir}/libpgport.a
%{_libdir}/libpgcommon_shlib.a
%{_libdir}/libpgport_shlib.a

%files clients -f clients.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/clusterdb
%attr(755,root,root) %{_bindir}/createdb
%attr(755,root,root) %{_bindir}/createuser
%attr(755,root,root) %{_bindir}/dropdb
%attr(755,root,root) %{_bindir}/dropuser
%attr(755,root,root) %{_bindir}/pg_amcheck
%attr(755,root,root) %{_bindir}/pg_archivecleanup
%attr(755,root,root) %{_bindir}/pg_dump
%attr(755,root,root) %{_bindir}/pg_dumpall
%attr(755,root,root) %{_bindir}/pg_isready
%attr(755,root,root) %{_bindir}/pg_restore
%attr(755,root,root) %{_bindir}/pg_verifybackup
%attr(755,root,root) %{_bindir}/psql
%attr(755,root,root) %{_bindir}/reindexdb
%attr(755,root,root) %{_bindir}/vacuumdb

%{_mandir}/man1/clusterdb.1*
%{_mandir}/man1/createdb.1*
%{_mandir}/man1/createuser.1*
%{_mandir}/man1/dropdb.1*
%{_mandir}/man1/dropuser.1*
%{_mandir}/man1/pg_amcheck.1*
%{_mandir}/man1/pg_archivecleanup.1*
%{_mandir}/man1/pg_dump.1*
%{_mandir}/man1/pg_dumpall.1*
%{_mandir}/man1/pg_isready.1*
%{_mandir}/man1/pg_restore.1*
%{_mandir}/man1/pg_verifybackup.1*
%{_mandir}/man1/psql.1*
%{_mandir}/man1/reindexdb.1*
%{_mandir}/man1/vacuumdb.1*
%{_mandir}/man7/*.7*

%if %{with llvm}
%files module-llvmjit
%defattr(644,root,root,755)
%doc src/backend/jit/README
%attr(755,root,root) %{_pgmoduledir}/llvmjit.so
%{_pgmoduledir}/llvmjit_types.bc
# base postgres bitcode
%{_pgmoduledir}/bitcode/postgres
%{_pgmoduledir}/bitcode/postgres.index.bc
# base modules bitcode
%{_pgmoduledir}/bitcode/dict_int
%{_pgmoduledir}/bitcode/dict_int.index.bc
%{_pgmoduledir}/bitcode/dict_xsyn
%{_pgmoduledir}/bitcode/dict_xsyn.index.bc
%endif

%if %{with perl}
%files module-plperl -f plperl-%{mver}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plperl.so
%{_pgsqldir}/plperl--*.sql
%{_pgsqldir}/plperl.control
%{_pgsqldir}/plperlu--*.sql
%{_pgsqldir}/plperlu.control
%endif

%if %{with python}
%files module-plpython -f plpython-%{mver}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plpython3.so
%{_pgsqldir}/plpython*--*.sql
%{_pgsqldir}/plpython*.control
%endif

%if %{with tcl}
%files module-pltcl -f pltcl-%{mver}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/pltcl.so
%{_pgsqldir}/pltcl*--*.sql
%{_pgsqldir}/pltcl*.control
%endif

%files module-dblink
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/dblink.so
%if %{with llvm}
%{_pgmoduledir}/bitcode/dblink
%{_pgmoduledir}/bitcode/dblink.index.bc
%endif
%{_pgsqldir}/dblink--*.sql
%{_pgsqldir}/dblink.control
%{_mandir}/man3/dblink*.3*

%files module-lo
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/lo.so
%if %{with llvm}
%{_pgmoduledir}/bitcode/lo
%{_pgmoduledir}/bitcode/lo.index.bc
%endif
%{_pgsqldir}/lo--*.sql
%{_pgsqldir}/lo.control

%files module-pg_trgm
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/pg_trgm.so
%if %{with llvm}
%{_pgmoduledir}/bitcode/pg_trgm
%{_pgmoduledir}/bitcode/pg_trgm.index.bc
%endif
%{_pgsqldir}/pg_trgm--*.sql
%{_pgsqldir}/pg_trgm.control

%files module-pgcrypto
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/pgcrypto.so
%if %{with llvm}
%{_pgmoduledir}/bitcode/pgcrypto
%{_pgmoduledir}/bitcode/pgcrypto.index.bc
%endif
%{_pgsqldir}/pgcrypto--*.sql
%{_pgsqldir}/pgcrypto.control

%if %{with selinux}
%files module-sepgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/sepgsql.so
%if %{with llvm}
%{_pgmoduledir}/bitcode/sepgsql
%{_pgmoduledir}/bitcode/sepgsql.index.bc
%endif
%{_pgsqldir}/sepgsql.sql
%endif

%files module-tablefunc
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/tablefunc.so
%if %{with llvm}
%{_pgmoduledir}/bitcode/tablefunc
%{_pgmoduledir}/bitcode/tablefunc.index.bc
%endif
%{_pgsqldir}/*tablefunc--*.sql
%{_pgsqldir}/*tablefunc.control

%files module-xml2
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/pgxml.so
%if %{with llvm}
%{_pgmoduledir}/bitcode/pgxml
%{_pgmoduledir}/bitcode/pgxml.index.bc
%endif
%{_pgsqldir}/xml2--*.sql
%{_pgsqldir}/xml2.control

%files contrib
%defattr(644,root,root,755)
%doc contrib/README
%attr(755,root,root) %{_bindir}/oid2name
%attr(755,root,root) %{_bindir}/vacuumlo
%attr(755,root,root) %{_pgmoduledir}/_int.so
%attr(755,root,root) %{_pgmoduledir}/adminpack.so
%attr(755,root,root) %{_pgmoduledir}/amcheck.so
%attr(755,root,root) %{_pgmoduledir}/auth_delay.so
%attr(755,root,root) %{_pgmoduledir}/auto_explain.so
%attr(755,root,root) %{_pgmoduledir}/bloom.so
%attr(755,root,root) %{_pgmoduledir}/btree_gin.so
%attr(755,root,root) %{_pgmoduledir}/btree_gist.so
%attr(755,root,root) %{_pgmoduledir}/citext.so
%attr(755,root,root) %{_pgmoduledir}/cube.so
%attr(755,root,root) %{_pgmoduledir}/earthdistance.so
%attr(755,root,root) %{_pgmoduledir}/file_fdw.so
%attr(755,root,root) %{_pgmoduledir}/fuzzystrmatch.so
%attr(755,root,root) %{_pgmoduledir}/hstore.so
%attr(755,root,root) %{_pgmoduledir}/isn.so
%attr(755,root,root) %{_pgmoduledir}/ltree.so
%attr(755,root,root) %{_pgmoduledir}/pageinspect.so
%attr(755,root,root) %{_pgmoduledir}/passwordcheck.so
%attr(755,root,root) %{_pgmoduledir}/pg_buffercache.so
%attr(755,root,root) %{_pgmoduledir}/pg_freespacemap.so
%attr(755,root,root) %{_pgmoduledir}/pg_prewarm.so
%attr(755,root,root) %{_pgmoduledir}/pg_stat_statements.so
%attr(755,root,root) %{_pgmoduledir}/pg_visibility.so
%attr(755,root,root) %{_pgmoduledir}/pgrowlocks.so
%attr(755,root,root) %{_pgmoduledir}/pgstattuple.so
%attr(755,root,root) %{_pgmoduledir}/postgres_fdw.so
%attr(755,root,root) %{_pgmoduledir}/seg.so
%attr(755,root,root) %{_pgmoduledir}/sslinfo.so
%attr(755,root,root) %{_pgmoduledir}/tcn.so
%attr(755,root,root) %{_pgmoduledir}/tsm_system_rows.so
%attr(755,root,root) %{_pgmoduledir}/tsm_system_time.so
%attr(755,root,root) %{_pgmoduledir}/unaccent.so
%attr(755,root,root) %{_pgmoduledir}/uuid-ossp.so
%if %{with llvm}
%{_pgmoduledir}/bitcode/_int
%{_pgmoduledir}/bitcode/_int.index.bc
%{_pgmoduledir}/bitcode/adminpack
%{_pgmoduledir}/bitcode/adminpack.index.bc
%{_pgmoduledir}/bitcode/amcheck
%{_pgmoduledir}/bitcode/amcheck.index.bc
%{_pgmoduledir}/bitcode/auth_delay
%{_pgmoduledir}/bitcode/auth_delay.index.bc
%{_pgmoduledir}/bitcode/auto_explain
%{_pgmoduledir}/bitcode/auto_explain.index.bc
%{_pgmoduledir}/bitcode/bloom
%{_pgmoduledir}/bitcode/bloom.index.bc
%{_pgmoduledir}/bitcode/btree_gin
%{_pgmoduledir}/bitcode/btree_gin.index.bc
%{_pgmoduledir}/bitcode/btree_gist
%{_pgmoduledir}/bitcode/btree_gist.index.bc
%{_pgmoduledir}/bitcode/citext
%{_pgmoduledir}/bitcode/citext.index.bc
%{_pgmoduledir}/bitcode/cube
%{_pgmoduledir}/bitcode/cube.index.bc
%{_pgmoduledir}/bitcode/earthdistance
%{_pgmoduledir}/bitcode/earthdistance.index.bc
%{_pgmoduledir}/bitcode/file_fdw
%{_pgmoduledir}/bitcode/file_fdw.index.bc
%{_pgmoduledir}/bitcode/fuzzystrmatch
%{_pgmoduledir}/bitcode/fuzzystrmatch.index.bc
%{_pgmoduledir}/bitcode/hstore
%{_pgmoduledir}/bitcode/hstore.index.bc
%{_pgmoduledir}/bitcode/isn
%{_pgmoduledir}/bitcode/isn.index.bc
%{_pgmoduledir}/bitcode/ltree
%{_pgmoduledir}/bitcode/ltree.index.bc
%{_pgmoduledir}/bitcode/pageinspect
%{_pgmoduledir}/bitcode/pageinspect.index.bc
%{_pgmoduledir}/bitcode/passwordcheck
%{_pgmoduledir}/bitcode/passwordcheck.index.bc
%{_pgmoduledir}/bitcode/pg_buffercache
%{_pgmoduledir}/bitcode/pg_buffercache.index.bc
%{_pgmoduledir}/bitcode/pg_freespacemap
%{_pgmoduledir}/bitcode/pg_freespacemap.index.bc
%{_pgmoduledir}/bitcode/pg_prewarm
%{_pgmoduledir}/bitcode/pg_prewarm.index.bc
%{_pgmoduledir}/bitcode/pg_stat_statements
%{_pgmoduledir}/bitcode/pg_stat_statements.index.bc
%{_pgmoduledir}/bitcode/pg_visibility
%{_pgmoduledir}/bitcode/pg_visibility.index.bc
%{_pgmoduledir}/bitcode/pgrowlocks
%{_pgmoduledir}/bitcode/pgrowlocks.index.bc
%{_pgmoduledir}/bitcode/pgstattuple
%{_pgmoduledir}/bitcode/pgstattuple.index.bc
%{_pgmoduledir}/bitcode/postgres_fdw
%{_pgmoduledir}/bitcode/postgres_fdw.index.bc
%{_pgmoduledir}/bitcode/seg
%{_pgmoduledir}/bitcode/seg.index.bc
%{_pgmoduledir}/bitcode/sslinfo
%{_pgmoduledir}/bitcode/sslinfo.index.bc
%{_pgmoduledir}/bitcode/tcn
%{_pgmoduledir}/bitcode/tcn.index.bc
%{_pgmoduledir}/bitcode/tsm_system_rows
%{_pgmoduledir}/bitcode/tsm_system_rows.index.bc
%{_pgmoduledir}/bitcode/tsm_system_time
%{_pgmoduledir}/bitcode/tsm_system_time.index.bc
%{_pgmoduledir}/bitcode/unaccent
%{_pgmoduledir}/bitcode/unaccent.index.bc
%{_pgmoduledir}/bitcode/uuid-ossp
%{_pgmoduledir}/bitcode/uuid-ossp.index.bc
%endif
%{_pgsqldir}/adminpack--*.sql
%{_pgsqldir}/adminpack.control
%{_pgsqldir}/amcheck--*.sql
%{_pgsqldir}/amcheck.control
%{_pgsqldir}/bloom--*.sql
%{_pgsqldir}/bloom.control
%{_pgsqldir}/btree_gin--*.sql
%{_pgsqldir}/btree_gin.control
%{_pgsqldir}/btree_gist--*.sql
%{_pgsqldir}/btree_gist.control
%{_pgsqldir}/citext--*.sql
%{_pgsqldir}/citext.control
%{_pgsqldir}/cube--*.sql
%{_pgsqldir}/cube.control
%{_pgsqldir}/dict_int--*.sql
%{_pgsqldir}/dict_int.control
%{_pgsqldir}/dict_xsyn--*.sql
%{_pgsqldir}/dict_xsyn.control
%{_pgsqldir}/earthdistance--*.sql
%{_pgsqldir}/earthdistance.control
%{_pgsqldir}/file_fdw--*.sql
%{_pgsqldir}/file_fdw.control
%{_pgsqldir}/fuzzystrmatch--*.sql
%{_pgsqldir}/fuzzystrmatch.control
%{_pgsqldir}/hstore--*.sql
%{_pgsqldir}/hstore.control
%{_pgsqldir}/intarray--*.sql
%{_pgsqldir}/intarray.control
%{_pgsqldir}/intagg--*.sql
%{_pgsqldir}/intagg.control
%{_pgsqldir}/isn--*.sql
%{_pgsqldir}/isn.control
%{_pgsqldir}/ltree--*.sql
%{_pgsqldir}/ltree.control
%{_pgsqldir}/pageinspect--*.sql
%{_pgsqldir}/pageinspect.control
%{_pgsqldir}/pg_buffercache--*.sql
%{_pgsqldir}/pg_buffercache.control
%{_pgsqldir}/pg_freespacemap--*.sql
%{_pgsqldir}/pg_freespacemap.control
%{_pgsqldir}/pg_prewarm--*.sql
%{_pgsqldir}/pg_prewarm.control
%{_pgsqldir}/pg_stat_statements--*.sql
%{_pgsqldir}/pg_stat_statements.control
%{_pgsqldir}/pg_visibility--*.sql
%{_pgsqldir}/pg_visibility.control
%{_pgsqldir}/pgrowlocks--*.sql
%{_pgsqldir}/pgrowlocks.control
%{_pgsqldir}/pgstattuple--*.sql
%{_pgsqldir}/pgstattuple.control
%{_pgsqldir}/postgres_fdw--*.sql
%{_pgsqldir}/postgres_fdw.control
%{_pgsqldir}/seg--*.sql
%{_pgsqldir}/seg.control
%{_pgsqldir}/sslinfo--*.sql
%{_pgsqldir}/sslinfo.control
%{_pgsqldir}/tcn--*.sql
%{_pgsqldir}/tcn.control
%{_pgsqldir}/tsm_system_rows--*.sql
%{_pgsqldir}/tsm_system_rows.control
%{_pgsqldir}/tsm_system_time--*.sql
%{_pgsqldir}/tsm_system_time.control
%{_pgsqldir}/unaccent--*.sql
%{_pgsqldir}/unaccent.control
%{_pgsqldir}/uuid-ossp--*.sql
%{_pgsqldir}/uuid-ossp.control
%if %{with perl}
%attr(755,root,root) %{_pgmoduledir}/hstore_plperl.so
%attr(755,root,root) %{_pgmoduledir}/jsonb_plperl.so
%{_pgsqldir}/hstore_plperl--*.sql
%{_pgsqldir}/hstore_plperl.control
%{_pgsqldir}/hstore_plperlu--*.sql
%{_pgsqldir}/hstore_plperlu.control
%{_pgsqldir}/jsonb_plperl--*.sql
%{_pgsqldir}/jsonb_plperl.control
%{_pgsqldir}/jsonb_plperlu--*.sql
%{_pgsqldir}/jsonb_plperlu.control
%if %{with llvm}
%{_pgmoduledir}/bitcode/hstore_plperl
%{_pgmoduledir}/bitcode/hstore_plperl.index.bc
%{_pgmoduledir}/bitcode/jsonb_plperl
%{_pgmoduledir}/bitcode/jsonb_plperl.index.bc
%endif
%endif
%if %{with python}
%attr(755,root,root) %{_pgmoduledir}/hstore_plpython3.so
%attr(755,root,root) %{_pgmoduledir}/jsonb_plpython3.so
%attr(755,root,root) %{_pgmoduledir}/ltree_plpython3.so
%if %{with llvm}
%{_pgmoduledir}/bitcode/hstore_plpython3
%{_pgmoduledir}/bitcode/hstore_plpython3.index.bc
%{_pgmoduledir}/bitcode/jsonb_plpython3
%{_pgmoduledir}/bitcode/jsonb_plpython3.index.bc
%{_pgmoduledir}/bitcode/ltree_plpython3
%{_pgmoduledir}/bitcode/ltree_plpython3.index.bc
%endif
%{_pgsqldir}/hstore_plpython3u--*.sql
%{_pgsqldir}/hstore_plpython3u.control
%{_pgsqldir}/jsonb_plpython3u--*.sql
%{_pgsqldir}/jsonb_plpython3u.control
%{_pgsqldir}/ltree_plpython3u--*.sql
%{_pgsqldir}/ltree_plpython3u.control
%endif
%{_mandir}/man1/oid2name.1*
%{_mandir}/man1/vacuumlo.1*
