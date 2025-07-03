---
title: Tshark y TcpDump
type: docs
prev: docs/Red_Team/
---
## TSHARD VRS TCPDUMP

---

### 🧾 Comparativa: `tcpdump` vs `tshark`

| **Aspecto**                         | **TShark**                                                                               | **Tcpdump**                                                      | **¿Quién lo hace mejor?**                          |
| ----------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------- |
| **1. Decodificación de protocolos** | Analiza protocolos de capa 7 (HTTP, TLS, DNS, etc.) con gran detalle.                    | Se limita a encabezados básicos de red y transporte.             | 🦈 **TShark**                                      |
| **2. Filtros avanzados**            | Usa filtros de visualización avanzados como Wireshark (`-Y http.request.method == GET`). | Solo usa filtros BPF en captura (`port 80`, `host 192.168.1.1`). | 🦈 **TShark**                                      |
| **3. Exportación de datos**         | Exporta a JSON, XML, CSV; permite extraer campos específicos (`-T fields`).              | No permite exportación estructurada; solo salida en texto plano. | 🦈 **TShark**                                      |
| **4. Rendimiento y ligereza**       | Más pesado por la decodificación detallada.                                              | Muy ligero, ideal para sistemas con pocos recursos.              | 🐚 **Tcpdump**                                     |
| **5. Automatización y scripting**   | Altamente integrable en scripts complejos y análisis forense.                            | Se puede usar en scripts, pero limitado en análisis profundo.    | 🦈 **TShark** (pero Tcpdump para entornos mínimos) |

---

## TSHARD

- una **guía avanzada y detallada** de comandos, opciones y usos prácticos de TShark en el contexto de **ciberseguridad**:

### 🧠 **1. Estructura general del comando**

```bash
tshark [opciones de captura] [opciones de filtro] [opciones de salida/visualización]
```

### 🔧 **2. Opciones avanzadas de captura**

| Comando             | Descripción                                                                         |
| ------------------- | ----------------------------------------------------------------------------------- |
| `-i any`            | Captura en todas las interfaces al mismo tiempo. Ideal para auditorías.             |
| `-s <bytes>`        | Define el tamaño del snapshot (por defecto 262144). Ej.: `-s 0` para capturar todo. |
| `-b duration:60`    | Rota archivos de captura cada 60 segundos. Útil en monitoreos largos.               |
| `-b filesize:1024`  | Rota archivo al llegar a 1024 KB. Ideal para logging continuo.                      |
| `-B 32`             | Ajusta el tamaño del buffer a 32 MB (por defecto puede ser insuficiente).           |
| `-n`                | No resuelve nombres DNS ni de puertos (mejora el rendimiento).                      |
| `-f "tcp port 443"` | Filtro de captura (BPF). Muy útil para reducir ruido.                               |

### 🔎 **3. Filtros de visualización (Display Filters)**

| Filtro                                     | Uso                                     |
| ------------------------------------------ | --------------------------------------- |
| `http.request.method == "POST"`            | Filtra solo solicitudes POST.           |
| `ip.addr == 192.168.1.1`                   | Filtra paquetes con IP específica.      |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | Detección de SYN scans.                 |
| `dns.qry.name == "malicious.domain"`       | Filtra consultas DNS maliciosas.        |
| `ftp.request.command == "USER"`            | Extrae posibles nombres de usuario FTP. |

### 🛠️ **4. Opciones de salida y extracción de campos**

| Comando          | Descripción                                                       |
| ---------------- | ----------------------------------------------------------------- |
| `-T fields`      | Modo para extraer campos específicos.                             |
| `-e <campo>`     | Campo a extraer, por ejemplo: `-e ip.src -e ip.dst -e http.host`. |
| `-E separator=,` | Define separador personalizado (CSV, por ejemplo).                |
| `-E header=y`    | Incluye cabecera en la salida.                                    |
| `-t ad`          | Muestra marca de tiempo absoluta (útil en forense).               |

#### 🧪 Ejemplo

```bash
tshark -r captura.pcapng -T fields -e ip.src -e http.host -Y "http.request" -E separator=, -E header=y
```

Extrae IPs de origen y hosts HTTP en formato CSV.

### 📊 **5. Análisis estadístico**

| Comando           | Descripción                                                                        |
| ----------------- | ---------------------------------------------------------------------------------- |
| `-z io,stat,10`   | Estadísticas de tráfico en intervalos de 10 segundos.                              |
| `-z conv,tcp`     | Conversaciones TCP (útil para ver quién habla con quién).                          |
| `-z endpoints,ip` | Lista de endpoints IP únicos.                                                      |
| `-z expert`       | Muestra eventos relevantes o problemas detectados (como retransmisiones, errores). |

### 🧰 **6. Automatización y scripting**

TShark puede integrarse con scripts en **bash, Python, PowerShell, etc.**

#### Ejemplo en Bash

```bash
#!/bin/bash
tshark -i eth0 -Y "http.request" -T fields -e http.host -e http.request.uri >> log_http.csv
```

### 🛡️ **7. Casos de uso en ciberseguridad**

#### 🔐 Extracción de credenciales

```bash
tshark -r captura.pcapng -Y "ftp.request.command == 'PASS'" -T fields -e ftp.request.arg
```

#### 🕵️‍♂️ Detección de escaneos

```bash
tshark -i eth0 -Y "tcp.flags.syn == 1 && tcp.flags.ack == 0" -T fields -e ip.src
```

#### 🧬 Detección de malware por DNS

```bash
tshark -r captura.pcapng -Y "dns.qry.name contains 'xyzmalware.com'" -T fields -e dns.qry.name
```

#### 🧯 Detección de tráfico no cifrado

```bash
tshark -i eth0 -Y "http.request or ftp.request or telnet" -T fields -e ip.src -e frame.protocols
```

### 📁 **8. Exportar contenido binario (archivos de red)**

TShark por sí solo **no exporta archivos**, pero puede ayudarte a identificar contenido con:

```bash
tshark -r captura.pcapng -Y "http.response" -T fields -e http.file_data
```

Para extracción real, se recomienda usar Wireshark o herramientas como `NetworkMiner`.

### 🔚 **9. Tips finales**

- Usa TShark en combinación con `cron` para capturas programadas.
- Perfecto para **entornos sin GUI**, como servidores o contenedores Docker.
- Ideal para pipelines de análisis automático (con ELK, Splunk, etc).

---

## TCPDUMP

Perfecto, vamos a **profundizar de forma profesional y detallada** en el uso de `tcpdump`, **enfocado a ciberseguridad** y alineado con los 9 puntos que has mencionado. Esta guía será muy útil tanto para analistas como para ingenieros de seguridad que buscan aprovechar `tcpdump` a fondo.

---

### 📌 **1. Estructura general del comando**

La sintaxis básica de `tcpdump` es:

```bash
tcpdump [opciones] [expresión de filtro]
```

- **Opciones**: modifican el comportamiento de la captura (interfaz, formato, cantidad de paquetes, etc.)
- **Expresiones**: definen qué tráfico quieres capturar (IP, puerto, protocolo, etc.)

Ejemplo base:

```bash
tcpdump -i eth0 -nn -s 0 -v port 80
```

### ⚙️ **2. Opciones avanzadas de captura**

| Opción          | Descripción                                                             |
| --------------- | ----------------------------------------------------------------------- |
| `-s 0`          | Captura el paquete completo (por defecto captura solo parte).           |
| `-U`            | Modo sin búfer (útil para análisis en tiempo real).                     |
| `-p`            | Desactiva modo promiscuo (no captura todo lo que pasa por la interfaz). |
| `-G <segundos>` | Divide captura en archivos por tiempo. Ej: cada 60 seg.                 |
| `-C <MB>`       | Divide archivos `.pcap` por tamaño. Ej: 100MB.                          |
| `-W <num>`      | Número de archivos rotativos si usas `-C` o `-G`.                       |

**Ejemplo avanzado:**

```bash
tcpdump -i eth0 -w captura_%Y-%m-%d_%H:%M:%S.pcap -G 300 -W 12 -s 0
```

> Captura en archivos de 5 minutos, rotando hasta 12 archivos, grabando paquetes completos.

### 🧩 **3. Filtros de visualización (Display Filters)**

Filtros clásicos (más potentes de lo que parecen):

- **Por protocolo**:

  ```bash
  tcpdump tcp
  tcpdump udp
  tcpdump icmp
  ```

- **Por IP**:

  ```bash
  tcpdump host 192.168.1.10
  tcpdump src 10.0.0.1
  tcpdump dst 8.8.8.8
  ```

- **Por puerto**:

  ```bash
  tcpdump port 22
  tcpdump src port 80 and dst port 1024
  ```

- **Combinaciones lógicas**:

  ```bash
  tcpdump 'tcp and port 443 and src 10.0.0.5'
  ```

- **Redes**:

  ```bash
  tcpdump net 192.168.0.0/24
  ```

- **Expresiones avanzadas**:

  ```bash
  tcpdump 'tcp[tcpflags] & tcp-syn != 0'
  ```

  > Captura sólo paquetes con la bandera SYN activa.

### 📤 **4. Opciones de salida y extracción de campos**

- **Ver tráfico en consola (con detalles):**

  ```bash
  tcpdump -nn -vv -X
  ```

  - `-nn`: sin resolución de nombres.
  - `-vv`: modo verbose.
  - `-X`: muestra payload en HEX + ASCII.

- **Guardar a archivo pcap:**

  ```bash
  tcpdump -w salida.pcap
  ```

- **Leer desde archivo pcap:**

  ```bash
  tcpdump -r salida.pcap
  ```

- **Filtrar al leer archivo:**

  ```bash
  tcpdump -r archivo.pcap 'port 80 and tcp'
  ```

### 📊 **5. Análisis estadístico**

`tcpdump` no tiene estadísticas integradas como `Wireshark` o `tshark`, pero puedes hacer cosas útiles con herramientas Unix:

- **Contar tipos de tráfico:**

  ```bash
  tcpdump -nn -r captura.pcap | awk '{print $5}' | cut -d. -f1 | sort | uniq -c | sort -nr
  ```

- **Contar conexiones por IP origen:**

  ```bash
  tcpdump -nn -r captura.pcap 'tcp[tcpflags] & tcp-syn != 0' | awk '{print $3}' | cut -d. -f1-4 | sort | uniq -c | sort -nr
  ```

### 🤖 **6. Automatización y scripting**

Muy útil en honeypots, sistemas SIEM personalizados o detección basada en firmas:

- **Script básico de captura automática:**

  ```bash
  #!/bin/bash
  TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
  tcpdump -i eth0 -c 1000 -s 0 -w /var/log/capturas/captura_$TIMESTAMP.pcap
  ```

- **Captura por evento (ej. activado desde IDS):**

  ```bash
  tcpdump -i eth0 -c 500 -w alerta_evento_$(date +%s).pcap 'host 192.168.1.20 and port 22'
  ```

### 🛡️ **7. Casos de uso en ciberseguridad**

| Caso                                      | Descripción                                                             |
| ----------------------------------------- | ----------------------------------------------------------------------- |
| 🐍 **Detección de escaneos**              | `tcpdump 'tcp[tcpflags] & tcp-syn != 0'` para detectar SYN scan (nmap). |
| 🧬 **Exfiltración de datos**              | Filtrar tráfico DNS, HTTP con paquetes grandes.                         |
| 🕵️ **Captura en honeypots**              | Captura silenciosa con rotación para análisis posterior.                |
| 📡 **Monitorización de tráfico SSH/SFTP** | `tcpdump port 22`                                                       |
| 🔒 **Análisis de tráfico TLS**            | Extraer handshakes y verificar certificados.                            |
| 🧨 **Detección de malware en red**        | Revisar comportamiento, C2, payloads sospechosos.                       |

### 💾 **8. Exportar contenido binario (archivos de red)**

Aunque `tcpdump` no reconstruye archivos como tal (mejor usar `tcpflow` o `Wireshark` para eso), puedes capturar el payload y luego extraerlo:

```bash
tcpdump -i eth0 -s 0 -X port 80 > dump_http.txt
```

Y luego extraer binarios desde ese volcado con herramientas como:

- `foremost`
- `binwalk`
- `strings`
- `xxd`

### 🧠 **9. Tips finales**

- Usa `screen` o `tmux` para dejar capturas largas corriendo.
- Asegúrate de tener suficiente espacio en disco si usas `-s 0` y `-w`.
- Combina con `cron` para tareas programadas.
- En sistemas críticos, redirige la salida a RAM (`/dev/shm`) para evitar I/O pesado.
- Evita `tcpdump` como root cuando sea posible. Usa `setcap`:

  ```bash
  sudo setcap cap_net_raw,cap_net_admin=eip $(which tcpdump)
  ```

---
