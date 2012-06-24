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
Summary(fr):	Sys�me de gestion de base de donn�es PostgreSQL
Summary(pl):	PostgreSQL - system bazodanowy
Summary(pt_BR):	Gerenciador de Banco de Dados PostgreSQL
Summary(ru):	PostgreSQL - ������� ���������� ������ ������
Summary(tr):	Veri Taban� Y�netim Sistemi
Summary(uk):	PostgreSQL - ������� ��������� ������ �����
Summary(zh_CN):	PostgreSQL �ͻ��˳���Ϳ��ļ�
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
PostgreSQL Datenbank-Managementsystem (fr�her als Postgres, dann als
Postgres95 bekannt).

PostgreSQL ist eine Verbesserung des POSTGRES-DB-Managementsystems,
ein DBMS-Forschungsprototyp der n�chsten Generation. W�hrend es das
leistungsf�hige Datenmodell und die reichhaltigen Datentypen von
POSTGRES beibeh�lt, ersetzt es die PostQuel-Abfragesprache durch ein
Subset von SQL. PostgreSQL ist gratis, der gesamte Quellcode ist
verf�gbar.

Ein Team von Internet-Entwicklern befa�t sich mit PostgreSQL. Sie alle
sind auf der PostgreSQL-Entwickleradre�liste. Koordinator ist Marc G.
Fournier (scrappy@postgreSQL.org). Das Team ist verantwortlich f�r
alle aktuellen und k�nftigen Entwicklungen von PostgreSQL.

Die Autoren von PostgreSQL 1.01 waren Andrew Yu und Jolly Chen.
Zahlreiche andere haben zur Portierung, zum Testen, Debugging und zur
Verbesserung des Code beigetragen. Den Original-Postgres-Code, von dem
sich PostgreSQL ableitet, verdanken wir der Arbeit vieler Doktoranden,
Studenten und Programmierern unter der Leitung von Professor Michael
Stonebraker an der University of California, Berkeley.

Der urspr�ngliche Name war Postgres. Als 1995 SQL-Funktionalit�t
hinzukam, wurde der Name in Postgres95 ge�ndert. Ende 1996 schlie�lich
entschied man sich f�r PostgreSQL.

PostgreSQL l�uft auf Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD
und den meisten Unix-Systemen.

%description -l es
Administrador de Banco de Datos PostgreSQL (conocido anteriormente
como Postgres, y despu�s como Postgres95). PostgreSQL es una
continuaci�n mejorada del Sistema Administrador de Banco de Datos
POSTGRES, que era un prototipo de pesquisa para un SGBD de nueva
generaci�n. Mientras PostgreSQL mantiene el potente modelo de datos y
los varios tipos de datos del POSTGRES, substituye el lenguaje de
consulta PostQuel por un subconjunto extendido de la SQL. PostgreSQL
es libre y tiene los fuentes disponibles. El desarrollo del PostgreSQL
se ejecutado por un equipo de estudiosos de Internet, todos suscritos
en la lista de desarrollo del PostgreSQL. El coordinador actual es
Marc G. Fournier (scrappy@postgreSQL.org). Este equipo es ahora
responsable por el desarrollo actual y futuro del PostgreSQL.

%description -l fr
Syst�me de gestion de bases de donn�es PostgreSQL (D'abord nomm�
Postgres, puis Postgres95).

PostgreSQL est une am�lioration du syst�me de gestion de bases de
donn�es POSTGRES, un prototype de recherche de la g�n�ration suivant
DBMS. Tout en conservant le puissant mod�le de donn�e de et les types
de don�e riches de Postgres, il remplace le langage de requ�tes de
Postgres par un sous ensemble etendu de commandes SQL. PosrgreSQL est
libre, et ses sources sont disponibles.

Le d�veloppement de PostgreSQL est actuellement r�alis� via internet
parune �quipe de d�veloppeurs inscrits sur la mailing-list de
d�veloppement de PostgreSQL. Le coordinateur actuel est Marc G
Fournier (scrappy@postgreSQL.org). Cette �quipe est responsable du
d�veloppemen actuel et � venir de PostgreSQL.

Les auteurs de PostgreSQL 1.01 �taient Andrew Yu et Jolly Chen.
Beaucoup d'autres ont contribu� au portage, au test, au d�bogage et �
l'am�lioration du code. Le code original de Postgres, duquel
PostgreSQL est d�riv�, a �t� l'oeuvre d'�tudiants de haut niveau, de
moins haut niveau, et de programmeurs travaillant sous la direction du
professeur Michael Stonebraker � l'universit� de Berkeley Californie.

Le nom original du logiciel �tait Postgres. Quand les fonctionnalit�es
SQL furent ajout�es en 1995, son nom est devenu Postgres95. Il a �t�
rebaptis� PostgreSQL en 1996.

PostgreSQL tourne sur Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD,
et la plupart des Unix.

%description -l pl
System Zarz�dzania Baz� Danych PostgreSQL (dawniej znany jako
Postgres, nast�pnie jako Postgres95).

PostgreSQL jest rozszerzeniem systemu zarz�dzania baz danych POSTGRES,
prototypu DBMS nast�pnej generacji. Co prawda PostgreSQL odziedziczy�
model danych oraz bogaty zbi�r r�nych typ�w danych, to jednak j�zyk
zapyta� PostQuel zosta� zast�piony rozszerzonym SQL-em. PostgreSQL
jest wolnym oprogramowaniem i kody �r�d�owe tego oprogramowania s� w
pe�ni dost�pne.

System PostgreSQL jest tworzony przez zesp� ludzi, kt�rzy s� zapisani
na list� dyskusyjn� dotycz�c� PostgreSQL-a. Obecnym koordynatorem jest
Marc G. Fournier (scrappy@postgreSQL.org). Wymieniony wy�ej zesp�
jest odpowiedzialny za aktualny i przysz�y rozw�j systemu PostgreSQL.

Autorami PostgreSQL-a 1.01 byli Andrew Yu oraz Jolly Chen. Wielu
innych pomaga�o przenosz�c na r�ne platformy, testuj�c, analizuj�c i
rozszerzaj�c kod. Oryginalny kod Postgres-a, na podstawie kt�rego
PostgreSQL powsta�, by� wysi�kiem wielu absolwent�w, student�w oraz
zespo�u programist�w, kt�rzy pracowali pod kierunkiem profesora
Michaela Stonebrakera z Uniwersytetu Kalifornii w Berkeley.

Nazwa oryginalna oprogramowania tworzonego w Berkeley brzmia�a
Postgres. W 1995 roku dodano j�zyk zapyta� SQL i nazw� zmieniono na
Postgres95. W ko�cu roku 1996 nazw� ostatecznie zmieniono na
PostgreSQL.

PostgreSQL mo�e by� uruchomiony pod nast�puj�cymi systemami: Solaris,
SunOS, HPUX, AIX, Linux, Irix, FreeBSD i innymi systemami uniksowymi.

%description -l pt_BR
Gerenciador de Banco de Dados PostgreSQL (conhecido anteriormente como
Postgres, e depois como Postgres95).

O PostgreSQL � uma continua��o melhorada do Sistema Gerenciador de
Banco de Dados POSTGRES, que era um prot�tipo de pesquisa para um SGBD
de nova gera��o. Enquanto o PostgreSQL mant�m o poderoso modelo de
dados e os v�rios tipos de dados do POSTGRES, ele substitui a
linguagem de consulta PostQuel por um subconjunto estendido da SQL. O
PostgreSQL � livre e tem os fontes dispon�veis.

O desenvolvimento do PostgreSQL est� sendo executado por uma equipe de
desenvolvedores da Internet, todos subscritores da lista de
desenvolvimento do PostgreSQL. O coordenador atual � Marc G. Fournier
(scrappy@postgreSQL.org). Esta equipe � agora respons�vel pelo
desenvolvimento atual e futuro do PostgreSQL.

%description -l ru
PostgreSQL - ������� ���������� ������ ������ (������ ��������� ���
Postgres, ����� ��� Postgres95).

PostgreSQL - ��� ����������� ������ ������� ���������� ������ ������
POSTGRES, ������������������ ��������� DBMS ��������� ���������.
�������� ������ ������ ������ � ������� ����� ����� ������ POSTGRES,
��� �������� ���� �������� PostQuel ����������� ������� SQL.
PostgreSQL ��������� � ������������ � ���� ������� ��������� ��������
�������.

PostgreSQL �������������� �������� Internet-�������������, �����������
�� ������ ��������, ����������� ���������� PostgreSQL. � ���������
����� ������������� �������� Marc G. Fournier
(scrappy@postgreSQL.org). ��� ������� � ��������� ����� �������� ��
��� ������� � ������� ���������� PostgreSQL.

�������� PostgreSQL 1.01 ���� Andrew Yu � Jolly Chen. ������ ������
���� ����� � ������������, ������������, ������� � ��������� ����.
������������ ��� Postgres, �� �������� ��������� PostgreSQL, ���
������ �������� ���������, ���������� � ���������, ����������� ���
������������ ���������� Michael Stonebraker � University of
California, Berkeley.

������������ �������� �� � Berkeley ���� Postgres. ����� � 1995 ����
���� ��������� ���������������� SQL, �������� ���������� ��
Postgres95. � ����� 1996 ���� ��� ��� ��� ���������� � ������ ���
PostgreSQL.

PostgreSQL �������� �� Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD
� ����������� ������ �������������� Unix.

%description -l tr
PostgreSQL, POSTGRES'den t�remi� bir veri taban� y�netim sistemidir
(DBMS). G��l� veri modeli ve zengin POSTGRES veri tiplerini
desteklerken SQL'in geni�letilmi� bir altk�mesi yerine PostQuel
sorgulama dilini koyar.

%description -l uk
PostgreSQL - ������� ��������� ������ ����� (��Φ� צ���� �� Postgres,
��Ԧ� �� Postgres95).

PostgreSQL - �� ��������� ���Ӧ� ������� ��������� ������ �����
POSTGRES, ���̦��������� ��������� DBMS �������ϧ ������æ�.
���Ҧ����� ������� ������ ����� �� ������� ��¦� ��Ц� ����� POSTGRES,
���� ��ͦ��� ���� ����Ԧ� PostQuel ���������� ������� SQL. PostgreSQL
����������� �� �������Ѥ���� � �����Ħ ������� ��������� ��Ȧ����
����Ԧ�.

PostgreSQL �������Ѥ���� �������� Internet-������ͦ�Ԧ�, ������˦�
������ ��������, ������������ ������æ PostgreSQL. ����ڦ
������������� � Marc G. Fournier (scrappy@postgreSQL.org). �� �������
צ���צ��� �� �Ӧ �����Φ �� ������Φ �������� PostgreSQL.

�������� PostgreSQL 1.01 ���� Andrew Yu �� Jolly Chen. ������ �����
������ �צ� ������ � ����������, ����������, צ������ �� ����������
����. ���Ǧ������� ��� Postgres, צ� ����� �������� PostgreSQL, ���
��������� ��������� ������Ԧ�, ��Ц���Ԧ� �� ���������, ���� ��������
Ц� ��Ҧ�������� ��������� Michael Stonebraker � University of
California, Berkeley.

���Ǧ������ ����� �������� � Berkeley ���� Postgres. ���� � 1995 ��æ
���� ������ ����æ�����Φ��� SQL, ����� �ͦ������ �� Postgres95. �
˦�æ 1996 ���� ���� �� ��� �ͦ������ � ����� �� PostgreSQL.

PostgreSQL ������ �� Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD
�� ¦�����Ԧ ����� Ҧ�����Ħ� Unix.

%package devel
Summary:	PostgreSQL development header files and libraries
Summary(de):	PostgreSQL-Entwicklungs-Header-Dateien und Libraries
Summary(es):	Archivos de inclusi�n y bibliotecas PostgreSQL
Summary(fr):	En-t�tes et biblioth�ques de d�veloppement PostgreSQL
Summary(pl):	PostgreSQL - pliki nag��wkowe i biblioteki
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para desenvolvimento com o PostgreSQL
Summary(ru):	PostgreSQL - ������ � ���������� ������������
Summary(tr):	PostgreSQL ba�l�k dosyalar� ve kitapl�klar
Summary(uk):	PostgreSQL - ������ �� ¦�̦����� ������ͦ���
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains header files and libraries required to compile
applications that are talking directly to the PostgreSQL backend
server.

%description devel -l de
Dieses Paket enth�lt die Header-Dateien und Libraries, die zum
Kompilieren von Applikationen notwendig sind, die direkt mit dem
PostgreSQL-Backend-Server kommunizieren.

%description devel -l es
Este paquete contiene archivos de inclusi�n y bibliotecas requeridas
para compilaci�n de aplicativos que se comunican directamente con el
servidor backend PostgreSQL.

%description devel -l fr
Ce package contient les fichiers d'en-t�te et les biblioth�ques
n�cessaires pour compiler des applications ayant des �changes directs
avec le serveur du backend PostgreSQL.

%description devel -l pl
Pakiet zawiera nag��wki oraz biblioteki wymagane do kompilacji
aplikacji ��cz�cych si� bezpo�rednio z serwerem PostgreSQL.

%description devel -l pt_BR
Este pacote cont�m arquivos de inclus�o e bibliotecas requeridas para
compila��o de aplicativos que se comunicam diretamente com o servidor
backend PostgreSQL.

%description devel -l ru
���� ����� �������� ������ � ����������, ����������� ��� ������
����������, ��������������� ����������������� � �������� PostgreSQL.

%description devel -l tr
Bu paket, PostgreSQL sunucusuyla konu�acak yaz�l�mlar geli�tirmek i�in
gereken ba�l�k dosyalar�n� ve kitapl�klar� i�erir.

%description devel -l uk
��� ����� ͦ����� ������ �� ¦�̦�����, ����Ȧ�Φ ��� ��������
�������, �˦ ������������� ������Ħ��� � �������� PostgreSQL.

%package backend-devel
Summary:	PostgreSQL backend development header files
Summary(pl):	PostgreSQL - pliki nag��wkowe dla backendu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

%description backend-devel
This package contains header files required to compile functions that
could be loaded directly by backend

%description backend-devel -l pl
Pakiet zawiera nag��wki wymagane do kompilacji funkcji ktore moga byc
bezposrednio ladowane przez beckend serwera PostgreSQL.

%package clients
Summary:	Clients needed to access a PostgreSQL server
Summary(es):	Clientes necesarios para acceder al servidor PostgreSQL
Summary(pl):	Klienci wymagani do dost�pu do serwera PostgreSQL
Summary(pt_BR):	Clientes necess�rios para acessar o servidor PostgreSQL
Summary(ru):	���������� ���������, ����������� ��� ������� � ������� PostgreSQL
Summary(uk):	�̦�����˦ ��������, ����Ȧ�Φ ��� ������� �� ������� PostgreSQL
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
servidor PostgreSQL. El servidor est� en el paquete principal.

%description clients -l pl
Pakiet zawiera programy klienckie potrzebne dla dost�pu do serwera
PostgreSQL oraz narz�dzia do zarz�dzania bazami dzia�aj�ce z linii
polece�. Serwer znajduje si� w g��wnym pakiecie.

%description clients -l pt_BR
Este pacote inclui somente os clientes necess�rios para acessar um
servidor PostgreSQL. O servidor est� no pacote principal.

%description clients -l ru
���� ����� �������� ������ ���������� ��������� � ����������,
����������� ��� ������� � ������� PostgreSQL. ������ ������ � �������
�����. ���� ��� ���� ������ �������� � ������ �������� PostgreSQL, ���
������������ �����, ������� ��� ���� ����������.

������ ������ � ������������ ��� ������ ������ ���������������� (C,
C++, Perl � Tcl) ���������. ���� ����� �������� ������ ���������� ���
����� C.

%description clients -l uk
��� ����� ͦ����� Ԧ���� �̦�����˦ �������� �� ¦�̦�����, ����Ȧ�Φ
��� ������� �� ������� PostgreSQL. ������ ͦ������� � ���������
����Ԧ. ���� ��� ���Ҧ��� ��������� � ����� �������� PostgreSQL, ��
������ �����, ���� ��� ����� ����������.

����� ������ � ¦�̦������� ��� Ҧ���� ��� ������������� (C, C++, Perl
� Tcl) ���Ħ��Φ. ��� ����� ͦ����� Ԧ���� ¦�̦����� ��� ���� C.

%package doc
Summary:	Documentation for PostgreSQL
Summary(pl):	Dodatkowa dokumantacja dla PostgreSQL
Group:		Applications/Databases

%description doc
This package includes documentation and HOWTO for programmer, admin
etc., in HTML format.

%description doc -l pl
Pakiet ten zawiera dokumentacj� oraz HOWTO m.in. dla programist�w,
administrator�w w formacie HTML.

%package libs
Summary:	PostgreSQL libraries
Summary(es):	Biblioteca compartida del PostgreSQL
Summary(pl):	Biblioteki dzielone programu PostgreSQL
Summary(pt_BR):	Biblioteca compartilhada do PostgreSQL
Summary(zh_CN):	PostgreSQL �ͻ�����Ҫ�Ĺ����
Group:		Libraries

%description libs
PostgreSQL shared libraries.

%description libs -l es
Este paquete contiene la biblioteca compartida para acceso al
PostgreSQL.

%description libs -l pl
Biblioteki dzielone programu PostgreSQL.

%description libs -l pt_BR
Este pacote cont�m a biblioteca compartilhada para acesso ao
PostgreSQL.

%package ecpg
Summary:	Embedded SQL in C interface
Summary(pl):	Interfejs wbudowanego SQL-a w j�zyk C
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description ecpg
Embedded SQL in C interface.

%description ecpg -l pl
Interfejs wbudowanego SQL-a w j�zyk C.

%package ecpg-devel
Summary:	Embedded SQL in C interface files
Summary(pl):	Pliki programistyczne interfejsu wbudowanego SQL-a w j�zyk C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ecpg = %{version}-%{release}

%description ecpg-devel
Embedded SQL in C interface files.

%description ecpg-devel -l pl
Pliki programistyczne interfejsu wbudowanego SQL-a w j�zyk C.

%package static
Summary:	PostgreSQL static libraries
Summary(es):	Bibliotecas estaticas PostgreSQL
Summary(pl):	Biblioteki statyczne programu PostgreSQL
Summary(pt_BR):	Bibliotecas est�ticas PostgreSQL
Summary(ru):	����������� ���������� ��� ���������������� � PostgreSQL
Summary(uk):	������Φ ¦�̦����� ��� ������������� � PostgreSQL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
PostgreSQL static libraries.

%description static -l es
Este paquete contiene bibliotecas estaticas requerida para compilaci�n
de aplicativos que se comunican directamente con el servidor backend
PostgreSQL.

%description static -l pl
Biblioteki statyczne programu PostgreSQL.

%description static -l pt_BR
Este pacote cont�m as bibliotecas est�ticas requeridas para compila��o
de aplicativos que se comunicam diretamente com o servidor backend
PostgreSQL.

%description static -l ru
��� ��������� ����� �� ������������ ������������, ������� ������ ��
������ � %{name}-devel.

%description static -l uk
�� ������� ����� ڦ ���������� ¦�̦�������, �˦ ¦��� �� ������� �
%{name}-devel.

%package module-plpgsql
Summary:	PL/pgSQL - PostgreSQL procedural language
Summary(pl):	PL/pgSQL - j�zyk proceduralny bazy danych PostgreSQL
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

Postgres ma wsparcie dla j�zyk�w proceduralnych. W przypadku, kiedy
programista zdefiniuje procedur� wyzwalacza lub funkcj� w j�zyku
proceduralnym, baza danych nie ma poj�cia jak interpretowa� tego typu
funkcj�. Funkcja lub procedura ta jest przekazywana do interpretera,
kt�ry wie jak j� wykona�. Interpreter jest odpowiedni�, specjaln�
funkcj�, kt�ra jest skompilowana w obiekt dzielony i �adowany w razie
potrzeby.

Za pomoc� polecenia createlang mo�na doda� obs�ug� j�zyka
proceduralnego PL/pgSQL dla swojej bazy danych.

%package module-plperl
Summary:	PL/perl - PostgreSQL procedural language
Summary(pl):	PL/perl - j�zyk proceduralny bazy danych PostgreSQL
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

Postgres ma wsparcie dla j�zyk�w proceduralnych. W przypadku, kiedy
programista zdefiniuje procedur� wyzwalacza lub funkcj� w j�zyku
proceduralnym, baza danych nie ma poj�cia jak interpretowa� tego typu
funkcj�. Funkcja lub procedura ta jest przekazywana do interpretera,
kt�ry wie jak j� wykona�. Interpreter jest odpowiedni�, specjaln�
funkcj�, kt�ra jest skompilowana w obiekt dzielony i �adowany w razie
potrzeby.

Za pomoc� polecenia createlang mo�na doda� obs�ug� j�zyka
proceduralnego PL/Perl dla swojej bazy danych.

%package module-plphp
Summary:	PL/PHP - PostgreSQL procedural language
Summary(pl):	PL/PHP - j�zyk proceduralny bazy danych PostgreSQL
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

Postgres ma wsparcie dla j�zyk�w proceduralnych. W przypadku, kiedy
programista zdefiniuje procedur� wyzwalacza lub funkcj� w j�zyku
proceduralnym, baza danych nie ma poj�cia jak interpretowa� tego typu
funkcj�. Funkcja lub procedura ta jest przekazywana do interpretera,
kt�ry wie jak j� wykona�. Interpreter jest odpowiedni�, specjaln�
funkcj�, kt�ra jest skompilowana w obiekt dzielony i �adowany w razie
potrzeby.

Za pomoc� polecenia createlang mo�na doda� obs�ug� j�zyka
proceduralnego PL/PHP dla swojej bazy danych.

%package module-plpython
Summary:	PL/Python - PostgreSQL procedural language
Summary(pl):	PL/Python - j�zyk proceduralny bazy danych PostgreSQL
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

Postgres ma wsparcie dla j�zyk�w proceduralnych. W przypadku, kiedy
programista zdefiniuje procedur� wyzwalacza lub funkcj� w j�zyku
proceduralnym, baza danych nie ma poj�cia jak interpretowa� tego typu
funkcj�. Funkcja lub procedura ta jest przekazywana do interpretera,
kt�ry wie jak j� wykona�. Interpreter jest odpowiedni�, specjaln�
funkcj�, kt�ra jest skompilowana w obiekt dzielony i �adowany w razie
potrzeby.

Za pomoc� polecenia createlang mo�na doda� obs�ug� j�zyka
proceduralnego PL/Python dla swojej bazy danych.

%package module-pltcl
Summary:	PL/Tcl - PostgreSQL procedural language
Summary(pl):	PL/Tcl - j�zyk proceduralny bazy danych PostgreSQL
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

Postgres ma wsparcie dla j�zyk�w proceduralnych. W przypadku, kiedy
programista zdefiniuje procedur� wyzwalacza lub funkcj� w j�zyku
proceduralnym, baza danych nie ma poj�cia jak interpretowa� tego typu
funkcj�. Funkcja lub procedura ta jest przekazywana do interpretera,
kt�ry wie jak j� wykona�. Interpreter jest odpowiedni�, specjaln�
funkcj�, kt�ra jest skompilowana w obiekt dzielony i �adowany w razie
potrzeby.

Za pomoc� polecenia createlang mo�na doda� obs�ug� j�zyka
proceduralnego PL/Tcl dla swojej bazy danych.

%package module-lo
Summary:	Large Objects module for PostgreSQL
Summary(pl):	Modu� Large Objects dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-lo
Large Objects module for PostgreSQL adds a new data type 'lo', some
support functions and a trigger which handles the orphaning problem.

%description module-lo -l pl
Modu� Large Objects dla PostgreSQL-a dodaje nowy typ danych 'lo',
kilka funkcji pomocniczych i wyzwalacz rozwi�zuj�cy problem
osieroconych obiekt�w.

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
Summary(pl):	Rozszerzenie pe�notekstowe dla PostgreSQL-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description module-tsearch2
Implementation of a new data type tsvector - a searchable data type
with indexed access:
http://www.sai.msu.su/~megera/postgres/gist/tsearch/V2/

%description module-tsearch2 -l pl
Implementacja nowego typu danych tsvector - typu danych podlegaj�cego
przeszukiwaniu z dost�pem poprzez indeksy:
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
