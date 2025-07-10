---
title: 🛜Wifi hacking
type: docs
prev: docs/first-page
weight: 8
sidebar:
  open: false
---

## CURSOS

SAVITAR CURSO WIFI : <https://odysee.com/@s4vitar:f/pentesting_redes_wifi:3>

SAVITAR BLOG ANTIGUO : [Hackear Redes WPA/WPA2 - mundohackers](https://web.archive.org/web/20171003003202/https://mundo-hackers.weebly.com/ataques-wpapsk-contrasentildea.html)

## INFORMACION

**ARTICULO DE INTERES SOBRE HACNIKG WIFI**
[Ataques a WPA2 con Pyrit](https://openaccess.uoc.edu/bitstream/10609/73067/7/danielmartTFG0118memoria.pdf)

{{< cards >}}
  {{< card link="/images/red_team/crack_password/danielmartTFG0118memoria.pdf" title="PYRIT TESIS" image="/images/red_team/crack_password/image.png" subtitle="PDF COMPLETO SOBRE PYRIT" >}}
{{< /cards >}}

## TOOL

### PYRIT

- [GPU - YOUTUBE](https://www.youtube.com/watch?v=Aa03aLFVaJQ&ab_channel=Laguialinux)
- [COMANDOS](https://laguialinux.es/instalar-pyrit-con-soporte-cuda-y-opencl/)
- [MAS INFORMACION](https://laguialinux.es/pyrit-descifrar-clave-wpa-con-gpu/)
- [EJEMPLO DE FILTRACION HANDSHAKE Y EXPLICACION DE USO DE DB](https://laguialinux.es/pyrit-analizando-y-capturando-handshakes/)

## ATAQUE WPS

[Ataques a redes WPS - mundohackers](https://web.archive.org/web/20171003001959/http://mundo-hackers.weebly.com/ataques-a-wps.html)

[getdrive/WPSPIN: WPSPIN.sh for KaliLinux 2](https://github.com/getdrive/WPSPIN)

[raw.githubusercontent.com/getdrive/WPSPIN/refs/heads/master/WPSPIN.sh](https://raw.githubusercontent.com/getdrive/WPSPIN/refs/heads/master/WPSPIN.sh)

- EXTRAS :
[wps-bruteforce · GitHub Topics](https://github.com/topics/wps-bruteforce)

[nikita-yfh/OneShot-C: Run WPS PIN attacks (Pixie Dust, online bruteforce, PIN prediction) without monitor mode with the wpa_supplicant](https://github.com/nikita-yfh/OneShot-C)

HASH WPA DE UN .CAP(captura) :[hashcat hcxpcapngtool - advanced password recovery](https://hashcat.net/cap2hashcat/)

## ATAQUE WPA / WPA2

### IMPORTANTE

Este es la versión mas rápida que podras  crackear de contraseñas a velocidades de millones por segundo , herramientas:

- PYRIT
- GENPMK
- maskprocessor(hastcat)

### INSTALACION EN UN DOCKER (volumen)

DEBE EXISTIR UNA CARPETA LLAMADA APP

- WINDOWS:

```python
docker run -it -v .\app:/app ubuntu:18.04

sed -i 's/\r$//' install.sh #ESTO ES PARA AREGLAR LOS SALTOS DE LINEA
```

- LINUX:

```python
docker run -it -v ./app:/app ubuntu:18.04
```

### BACKUPS TOOLS

- [PYRIT UBUNTU 18 LINK](http://archive.ubuntu.com/ubuntu/pool/universe/p/pyrit/pyrit_0.4.0-7.1build2_amd64.deb)
- COWPATTY - GENPMK
- MASKPROCESSOR - MP64

### BASIC

```bash
#!/bin/bash
echo "Actualizando repositorios e instalando herramientas básicas..."
apt update
apt upgrade -y
apt install -y zsh net-tools build-essential git nano wget curl p7zip-full p7zip-rar
```

### PYRIT ANTIGUO (UBUNTU 18.04)

- INFO [How can I install pyrit, requested by linset?](https://askubuntu.com/questions/1351732/how-can-i-install-pyrit-requested-by-linset)

```bash
apt-get update
apt-cache search python2.7
apt-cache search python-pip

apt-get install -y python2.7 python2.7-dev libssl-dev libpcap-dev libffi-dev libsqlite3-dev

# Instalación de pyrit
echo "INSTALACION DE PYRIT $(apt show pyrit 2>/dev/null | grep -i version)"

apt install  pyrit -y

pyrit | head -n 1
```

- PYRIT V 0.5.0 - GPU-OPEN CL(UBUNTU 18.04 - 20.04 )
INFO :
- [YOUTUBE - Instalar pyrit desde fuentes con soporte para GPU y CUDA o OpenCL](https://www.youtube.com/watch?v=Aa03aLFVaJQ&ab_channel=Laguialinux)
- [Script for Pyrit installation in Ubuntu 22.04](https://gist.github.com/farhatizakaria/48d5a21bb6959842cd3bdfaa7f8795f9)

```bash
apt install -y python3-scapy python2.7 libssl-dev zlib1g-dev libpcap0.8-dev python2.7-dev

wget -c https://github.com/JPaulMora/Pyrit/archive/v0.5.0.tar.gz
echo "INSTALACION DE PYRIT $(ls v0.5.0.tar.gz)"

tar -xf v0.5.0.tar.gz

cd Pyrit-0.5.0
sed -i "s/COMPILE_AESNI/NO_COMPILE_AESNI/" cpyrit/_cpyrit_cpu.c
python2.7 setup.py clean
python2.7 setup.py build
python2.7 setup.py install

pyrit | head -n 1
```

### COWPATTY - GENPMK (UBUNTU 18.04 - 20.04 )

- INFO : [fedora cowpatty-4.6.tgz  backup](https://github.com/lund133369/cowpatty_backup/releases/tag/cowpatty_backup)

```bash
# Descarga y configuración de cowpatty
echo "Descargando y configurando Cowpatty..."
apt-get -y install libpcap-dev libssl-dev

wget http://pkgs.fedoraproject.org/repo/pkgs/cowpatty/cowpatty-4.6.tgz/b90fd36ad987c99e7cc1d2a05a565cbd/cowpatty-4.6.tgz
tar zxfv cowpatty-4.6.tgz
cd cowpatty-4.6/
make

cp cowpatty /usr/bin
cp genpmk /usr/bin
# Verificación de instalación
cowpatty -V
genpmk -V
```

### MASKPROCESSOR 0.73 (UBUNTU 18.04 - 20.04 - WINDOWS BINARI )

- INFO: [maskprocessor [hashcat wiki]](https://hashcat.net/wiki/doku.php?id=maskprocessor)

``` bash
wget https://github.com/hashcat/maskprocessor/releases/download/v0.73/maskprocessor-0.73.7z

7z x maskprocessor-0.73.7z
cd maskprocessor-0.73
cp ./mp64.bin /usr/bin/mp64

echo "MP64 INSTALL $(mp64 -V)"

# EN CASO FALLE USAR ESTA URL DESCARGAR DE IGUAL FORMA CON WGET 
# Release maskprocessor-0.73.7z · lund133369/maskprocessor_fork
#https://github.com/lund133369/maskprocessor_fork/releases/tag/maskprocessor
```

## EXAMPLE - POC WPA2 FALTA

scritp completo LINUX (AREGLAR ESTO)

```bash
docker run -it ubuntu:18.04

apt update && apt upgrade -y

apt install -y zsh net-tools build-essential git nano wget curl  p7zip-full p7zip-rar

zsh

apt-get update
apt-cache search python2.7
apt-cache search python-pip

apt-get install -y python2.7 python2.7-dev python2-pip libssl-dev libpcap-dev libffi-dev libsqlite3-dev

apt install pyrit -y

pyrit

apt-get -y install libpcap-dev libssl-dev

wget http://pkgs.fedoraproject.org/repo/pkgs/cowpatty/cowpatty-4.6.tgz/b90fd36ad987c99e7cc1d2a05a565cbd/cowpatty-4.6.tgz

tar zxfv cowpatty-4.6.tgz
cd cowpatty-4.6/
make
cp cowpatty /usr/bin ; cp genpmk /usr/bin
cowpatty -V ; echo -n ; genpmk -V ; echo -n


6QDWv3_XzUqvK2.
```

FALTA EJEMPLO USANDO TODAS ESTA HERRAMIENTAS

## EXTRA

### 📌 Comandos útiles de `tshark`

| Comando                                                         | ¿Para qué sirve?                                    |
| --------------------------------------------------------------- | --------------------------------------------------- |
| `sudo tshark -D`                                                | Lista interfaces de red disponibles                 |
| `sudo tshark -i wlan0`                                          | Captura tráfico en tiempo real desde `wlan0`        |
| `sudo tshark -i eth0 -w salida.pcap`                            | Guarda la captura en un archivo `.pcap`             |
| `sudo tshark -r archivo.pcap`                                   | Analiza un archivo `.pcap`                          |
| `sudo tshark -f "port 80"`                                      | Aplica filtro de captura (nivel TCP/IP)             |
| `sudo tshark -Y "http.request"`                                 | Aplica filtro de visualización (como Wireshark GUI) |
| `sudo tshark -T fields -e ip.src -e ip.dst -e _ws.col.Protocol` | Muestra solo campos específicos                     |
| `sudo tshark -c 100 -i eth0`                                    | Captura solo 100 paquetes                           |

---
