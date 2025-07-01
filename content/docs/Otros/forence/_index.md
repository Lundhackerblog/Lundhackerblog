---
title: Forense(forensic)
type: docs
prev: docs/Otros/_index.md
next: docs/Otros/programacion/leaf
weight: 6
sidebar:
  open: false
---

## EL PDF ESTA EN LA MISMA CARPETA

{{< cards >}}
  {{< card link="/images/otros/forence/magachaves.pdf" title="PDF ESPAÑOL FORENSING" image="/images/otros/forence/20250125161630.png" subtitle="PDF COMPLETO SOBRE FORENCE EN LINUX" >}}
{{< /cards >}}

## !!!! EL PDF LO ES TODO Y ESTA EN ESPAÑOL

## TOOLS

### 2.3 Descripción de Herramientas

Actualmente existen multitud de aplicaciones destinadas al análisis forense que trabajan sobre distintos aspectos de la máquina a analizar, por ejemplo, sobre las memorias, los discos de almacenamiento, los protocolos de red, las aplicaciones, etc. También existen suites que ofrecen el análisis sobre varios de estos puntos, ofreciendo herramientas verdaderamente potentes y útiles. No obstante, no existe ni la herramienta definitiva ni aquella aprobada y validada por ningún estándar. A continuación, se hará un repaso de las herramientas más populares con una breve descripción y su ámbito de trabajo.

#### Adquisición y Análisis de la Memoria

- **Proccess Dumper**: Convierte un proceso de la memoria a fichero.
- **FTK Imager**: Permite, entre otras cosas, adquirir la memoria.
- **DumpIt**: Realiza volcados de memoria a fichero.
- **Responder CE**: Captura la memoria y permite analizarla.
- **Volatility**: Analiza procesos y extrae información útil para el analista.
- **RedLine**: Captura la memoria y permite analizarla. Dispone de entorno gráfico.
- **Memorize**: Captura la RAM (Windows y OSX).

#### Montaje de Discos

Utilidades para montar imágenes de disco o virtualizar unidades de forma que se tenga acceso al sistema de ficheros para su análisis posterior.

- **ImDisk**: Controlador de disco virtual.
- **OSFMount**: Permite montar imágenes de discos locales en Windows asignando una letra de unidad.
- **raw2vmdk**: Utilidad en Java que permite convertir raw/dd a .vmdk.
- **FTK Imager**: Permite realizar montaje de discos.
- **vhdtool**: Convertidor de formato raw/dd a .vhd, permitiendo el montaje desde el administrador de discos de Windows.
- **LiveView**: Utilidad en Java que crea una máquina virtual de VMware partiendo de una imagen de disco.
- **MountImagePro**: Permite montar imágenes de discos locales en Windows asignando una letra de unidad.

#### Carving y Herramientas de Disco

Recuperación de datos perdidos o borrados, búsqueda de patrones y archivos con contenido determinado (imágenes, vídeos, etc.), recuperación de particiones y tratamiento de estructuras de discos.

- **PhotoRec**: Muy útil para la recuperación de imágenes y vídeos.
- **Scalpel**: Independiente del sistema de archivos, permite personalizar los archivos o directorios a recuperar.
- **RecoverRS**: Recupera URLs de acceso a sitios web y archivos. Realiza carving directamente desde una imagen de disco.
- **NTFS Recovery**: Permite recuperar datos y discos, incluso después de formatearlos.
- **Recuva**: Utilidad para la recuperación de archivos borrados.
- **Raid Reconstructor**: Recupera datos de un RAID roto (RAID 5 o RAID 0) incluso si no se conocen los parámetros RAID.
- **CNWrecovery**: Recupera sectores corruptos e incorpora utilidades de carving.
- **Restoration**: Utilidad para la recuperación de archivos borrados.
- **Rstudio**: Recuperación de datos en sistemas NTFS, FAT, HFS, UFS, Ext, entre otros.
- **Freerecover**: Utilidad para la recuperación de archivos borrados.
- **DMDE**: Compatible con FAT, NTFS y ofrece herramientas de carving.
- **IEF (Internet Evidence Finder)**: Realiza carving en imágenes de disco buscando aplicaciones y datos específicos.
- **Bulk_extractor**: Extrae datos desde una imagen, carpeta o archivo.

#### Utilidades para el Sistema de Ficheros

Conjunto de herramientas para el análisis de datos y archivos esenciales en la búsqueda de un incidente.

- **analyzeMFT**: Utilidad en Python que permite extraer la MFT.
- **MFT Extractor**: Otra utilidad para la extracción de la MFT.
- **INDXParse**: Herramienta para analizar índices y archivos `$I30`.
- **MFT Tools**: Conjunto de utilidades para el acceso a la MFT.
- **MFT_Parser**: Extrae y analiza la MFT.
- **Prefetch Parser**: Extrae y analiza el directorio prefetch.
- **Winprefetchview**: Extrae y analiza el directorio prefetch.
- **Fileassassin**: Desbloquea archivos bloqueados por programas.

#### Herramientas de Red

Herramientas relacionadas con el tráfico de red, útiles para detectar patrones anómalos, malware, conexiones sospechosas, identificación de ataques, etc.

- **WireShark**: Herramienta para la captura y análisis de paquetes de red.
- **NetworkMiner**: Herramienta forense para el descubrimiento de información de red.
- **Netwitness Investigator**: Herramienta forense, la versión gratuita está limitada a 1GB de tráfico.
- **Network Appliance Forensic Toolkit**: Conjunto de utilidades para la adquisición y análisis de la red.
- **Xplico**: Extrae contenido de datos de red (pcap o adquisición en tiempo real) y soporta múltiples protocolos.
- **Snort**: Detector de intrusos que captura y analiza paquetes.
- **Splunk**: Motor para el análisis de datos y logs generados por sistemas e infraestructura de IT.
- **AlientVault**: Similar a Splunk, recolecta datos y logs con inteligencia para la detección de anomalías o intrusiones.

#### Recuperación de Contraseñas

Herramientas para recuperar contraseñas en Windows mediante fuerza bruta, formularios, navegadores, entre otros.

- **Ntpwedit**: Editor de contraseñas para sistemas basados en Windows NT. No válido para Active Directory.
- **Ntpasswd**: Editor de contraseñas para sistemas Windows, se puede iniciar desde un CD-LIVE.
- **pwdump7**: Vuelca los hashes mediante la extracción de binarios SAM.
- **SAMInside / OphCrack / L0phtcrack**: Hacen un volcado de los hashes e incluyen diccionarios para ataques por fuerza bruta.

![imagen error](/images/otros/forence/20250125161630.png)
![imagen error](/images/otros/forence/20250125161647.png)
![imagen error](/images/otros/forence/20250125161718.png)
![imagen error](/images/otros/forence/20250125161803.png)
![imagen error](/images/otros/forence/20250125161816.png)
