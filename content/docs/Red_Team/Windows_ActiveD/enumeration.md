---
title: Enumeration
type: docs
prev: docs/first-page
weight: 8
sidebar:
  open: false
---

PRINCIPAL
[Active Directory Methodology | HackTricks](https://book.hacktricks.xyz/windows-hardening/active-directory-methodology)

**DNS scan - Enumerating Users - Password Bruteforce-Exploring SMB shares**
[Enumerating AD infrastructure](https://medium.com/@Shorty420/enumerating-ad-98e0821c4c78)

### ACTIVE DIRECTORY ENUMERATION

!!!!   ***IMPACKET-SUIT***   !!!!!!

USERS [Impacket-GetADUsers | WADComs](https://wadcoms.github.io/wadcoms/Impacket-GetADUsers/)
AS-REP NO-AUTH [Impacket-GetNPUsers| WADComs](https://wadcoms.github.io/wadcoms/Impacket-GetNPUsers/)
USER - NTLM KERBEROS [Impacket-getTGT | WADComs](https://wadcoms.github.io/wadcoms/Impacket-getTGT/)

![](/images/red_team/windows/20241012185815.png)

## ENUMERACION

### NMAP

![](/images/red_team/windows/20241004103426.png)
![](/images/red_team/windows/20241004103542.png)

### SMB - 445

VIDEO EXPLICACION FACIL: [Como Usar SMBMAP y SMBCLIENT  (youtube.com)](https://www.youtube.com/watch?v=oXMA1DMjlS4&ab_channel=ElPing%C3%BCinodeMarioLIVE)

==***GUIA COMPLETA AQUI !!!***==  [SMB Enumeration Checklist](https://0xdf.gitlab.io/2018/12/02/pwk-notes-smb-enumeration-checklist-update1.html)
![](/images/red_team/windows/20241012181733.png)

![](/images/red_team/windows/20241012181624.png)
![](/images/red_team/windows/20241012181704.png)

TOOLS:

##### SIN CREDENCIALES

IMPORTANTE!!! -> NULL SESSION =! USER "" =! GUEST

![](/images/red_team/windows/20241004103904.png)NETEXEC [Enumeration | NetExec](https://www.netexec.wiki/smb-protocol/enumeration)
![](/images/red_team/windows/20241004110711.png)
SMBMAP
![](/images/red_team/windows/20241012174004.png)

PODEMOS EJECUTAR TAMBIEN EL

##### CON CREDENCIALES

![](/images/red_team/windows/20241012174019.png)

AQUI SE PUEDE EJECUTAR EL DUMPEAR LAS CONTRASEÑAS DE USUARIOS DEL SISTEMA OPERATIVO WINDOWS APROVECHANDOSE DE SMB Y CREDENCIALES VALIDAS, PARA ESTO PREVIAMENTE EL USUARIO DEBE SER ADMINISTRADOR EN LA PC

```bash
impacket-secretsdump <DOMINIO>/USER:PASSWORD@<IP>
```

![](/images/red_team/windows/20241113215857.png)

## LDAP - 389

GUIA COMPLETA (CON Y SIN CREDENCIALES) [LDAPDOMAINDUMP GUIA COMPLETA)](https://sniferl4bs.com/2020/02/obteniendo-informaci%C3%B3n-del-dominio-con-ldapdomaindump/)
![](/images/red_team/windows/20241004110005.png)

TOOLS :

##### SIN CREDENCIALES

BUSCAR USUARIOS :
![](/images/red_team/windows/20241012182902.png)
![](/images/red_team/windows/20241012182607.png)

##### CON CREDENCIALES

####### LDAPSEARCH

![](/images/red_team/windows/20241012182423.png)
[LDAP NULL - GUEST - "" USERS](https://ivanitlearning.wordpress.com/2019/03/24/root-me-ldap-null-bind/)

![](/images/red_team/windows/20241012185026.png)
![](/images/red_team/windows/20241012185054.png)

####### LDAPDOMAINDUMP

![](/images/red_team/windows/20241004110028.png)

NETEXEC - LDAP : [Authentication | NetExec](https://www.netexec.wiki/ldap-protocol/authentication)
![](/images/red_team/windows/20241012183149.png)

 [Query LDAP | NetExec](https://www.netexec.wiki/ldap-protocol/query-ldap)
![](/images/red_team/windows/20241012183115.png)

## KERBEROS - 88

GUIA COMPLETA DE PENTESTING KERBEROS:
[Kerberos (I): ¿Cómo funciona Kerberos? - Teoría | Tarlogic](https://www.tarlogic.com/es/blog/como-funciona-kerberos/)
[Kerberos (II): ¿Como atacar Kerberos? (tarlogic.com)](https://www.tarlogic.com/es/blog/como-atacar-kerberos/)

GUIA BASICA (KERBEROASTING):
[Enumeración de usuarios Kerberos | Iron Wolf Security Experts (iwolfsec.com)](https://docs.iwolfsec.com/tecnicas-y-ataques/ataques-a-directorio-activo/enumeracion/enumeracion-de-usuarios-kerberos)
[Kerberoasting | Iron Wolf Security Experts (iwolfsec.com)](https://docs.iwolfsec.com/tecnicas-y-ataques/ataques-a-directorio-activo/kerberos/kerberoasting)

![](/images/red_team/windows/20241012180500.png)

WORDLIST NECESARIO - JUGAR CON HEAD -N 10 000 , PARA OBTENER LA CANTIDAD DE USUARIOS QUE DESEES.
[WORDLIST-DICCIONARIOS]

TOOL:

##### SIN CREDENCIALES

###### 1-.PARA OBTENER USUARIOS

![](/images/red_team/windows/20241012190415.png)

![](/images/red_team/windows/20241012180227.png)

![](/images/red_team/windows/20241012180247.png)

###### 2-.PARA OBTENER HASHES DE USUARIOS QUE NO REQUIERAN AUTENTICACION

![](/images/red_team/windows/20241012180207.png)

##### CON CREDENCIALES

BIBLIA KERBEROS
[A cheatsheet with commands that can be used to perform kerberos attacks · GitHub](https://gist.github.com/TarlogicSecurity/2f221924fef8c14a1d8e29f3cb5c5c4a)

ATAQUES
CUANDO TIENENS CREDENCIALES PUEDES APLICAR KERBEROATING
!!! importante alinear la hora !!!

![](/images/red_team/windows/20241113214451.png)

```bash
ntpdate IP-TARGED ## para alinear la hora

impacket-GetUserSPNs <IP-OR-DC>/USERNAME:PASSWORD -request
```

OTROS

## RPC - 135

[Active Directory Enumeration: RPCClient - Hacking Articles](https://www.hackingarticles.in/active-directory-enumeration-rpcclient/)
![](/images/red_team/windows/20241012184713.png)

##### SIN CREDENCIALES

##### CON CREDENCIALES

## NETBIOS - 139

## RDP - 3389-3390

[Password Spraying | NetExec](https://www.netexec.wiki/rdp-protocol/password-spraying)
![](/images/red_team/windows/20241004111214.png)

## RESPONDER

ENVENEDADOR DE TRAFICO , CAPTURA HASH NTLM Y OTRAS COSAS MAS
[RESPONDER GitHub]([GitHub - lgandx/Responder: Responder is a LLMNR, NBT-NS and MDNS poisoner, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication.](https://github.com/lgandx/Responder))

GUIA COMPLETA: [KSEC ARK - Pentesting and redteam knowledge base | Responder - CheatSheet (ivoidwarranties.tech)](https://www.ivoidwarranties.tech/posts/pentesting-tuts/responder/cheatsheet/)
![](/images/red_team/windows/20241004112049.png)
