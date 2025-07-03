---
title: IPTABLES
type: docs
prev: docs/Red_Team/
---

Vamos a abordar **`iptables`** desde un **enfoque técnico, estructurado y orientado a ciberseguridad**, tocando desde la base hasta usos avanzados. Esta guía sirve tanto para reforzar defensas como para realizar pruebas de hardening o control de tráfico en entornos sensibles.

---

## NIVEL INTERMEDIO

### 🔥 IPTABLES – GUÍA ESTRUCTURADA PARA CIBERSEGURIDAD 🔥

---

### **1. Estructura General y Conceptos Básicos**

`iptables` es una herramienta que interactúa con el **netfilter** del kernel de Linux para controlar el tráfico de red. Funciona con **tablas**, **cadenas (chains)** y **reglas (rules)**.

#### 📌 Elementos principales

* **Tablas**:

  * `filter`: por defecto, maneja filtrado de tráfico.
  * `nat`: para traducción de direcciones (NAT, DNAT, SNAT).
  * `mangle`: modificación avanzada de paquetes.
  * `raw`: configuraciones previas a connection tracking.

* **Cadenas comunes**:

  * `INPUT`: paquetes que entran al sistema.
  * `OUTPUT`: paquetes que salen desde el sistema.
  * `FORWARD`: paquetes que pasan por el sistema (ruteo).
  * `PREROUTING` / `POSTROUTING`: manipulación antes/después del enrutamiento (especialmente NAT/mangle).

* **Acciones (targets)**:

  * `ACCEPT`: permitir.
  * `DROP`: descartar sin respuesta.
  * `REJECT`: descartar con respuesta.
  * `LOG`: registrar sin afectar el flujo.
  * `RETURN`, `DNAT`, `SNAT`, `MASQUERADE`, etc.

---

### **2. Reglas Básicas y Comandos Frecuentes**

| Comando                                           | Descripción                                             |
| ------------------------------------------------- | ------------------------------------------------------- |
| `iptables -L -v`                                  | Lista reglas actuales con contadores.                   |
| `iptables -F`                                     | Borra todas las reglas activas.                         |
| `iptables -P INPUT DROP`                          | Establece política por defecto (en este caso, denegar). |
| `iptables -A INPUT -p tcp --dport 22 -j ACCEPT`   | Acepta conexiones SSH.                                  |
| `iptables -A INPUT -s 192.168.1.10 -j DROP`       | Bloquea IP específica.                                  |
| `iptables -I INPUT 1 -p tcp --dport 80 -j ACCEPT` | Inserta al inicio una regla para HTTP.                  |

---

### **3. Reglas Avanzadas y Filtros Útiles**

#### 🔍 Filtrado por interfaz

```bash
iptables -A INPUT -i eth0 -p tcp --dport 443 -j ACCEPT
```

#### 🧱 Limitar tasa de conexiones (anti-flood)

```bash
iptables -A INPUT -p tcp --dport 22 -m limit --limit 3/min -j ACCEPT
```

#### 🛑 Bloquear escaneos tipo SYN

```bash
iptables -A INPUT -p tcp --syn -j DROP
```

#### 🧨 Bloquear paquetes malformados

```bash
iptables -A INPUT -m state --state INVALID -j DROP
```

#### 🕵️ Detectar y bloquear IPs agresivas (con recent)

```bash
iptables -A INPUT -m recent --name scanner --rcheck --seconds 60 --hitcount 10 -j DROP
iptables -A INPUT -m recent --name scanner --set -j LOG --log-prefix "Scanner Detectado: "
```

---

### **4. Política de Seguridad Recomendada (Modelo Default-Deny)**

```bash
## Limpiar reglas actuales
iptables -F
iptables -X

## Política por defecto
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

## Permitir localhost
iptables -A INPUT -i lo -j ACCEPT

## Permitir tráfico establecido
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

## Permitir SSH (puedes modificar puerto)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

## Permitir ICMP limitado (ping)
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/s -j ACCEPT

## Registrar el resto
iptables -A INPUT -j LOG --log-prefix "DROP: "
```

---

### **5. Casos de Uso en Ciberseguridad**

| Caso                                    | Regla o Estrategia                                          |
| --------------------------------------- | ----------------------------------------------------------- |
| 🚨 Defensa contra escaneos              | Limitar SYNs, bloquear conexiones rápidas, DROP de INVALID. |
| 🧱 Firewall de perímetro                | `iptables` como firewall local en servidores de producción. |
| 💀 Defensa ante ataques de fuerza bruta | Uso de `recent`, `limit`, y detección de patrones.          |
| 📡 Captura selectiva + bloqueo          | Combinar con `tcpdump` y luego generar reglas de bloqueo.   |
| 🧬 NAT y redirección en honeypots       | Usar `DNAT` para redirigir puertos al honeypot.             |

---

### **6. Registro y Auditoría**

Para registrar tráfico:

```bash
iptables -A INPUT -s 10.0.0.0/8 -j LOG --log-prefix "PAQUETE INTERNO: " --log-level 4
```

Visualizar logs:

```bash
cat /var/log/syslog | grep "PAQUETE INTERNO"
```

---

### **7. Scripts de Automatización y Restauración**

#### ✅ Guardar reglas actuales

```bash
iptables-save > /etc/iptables/rules.v4
```

#### ♻️ Restaurar reglas

```bash
iptables-restore < /etc/iptables/rules.v4
```

#### 🔁 Script básico

```bash
#!/bin/bash
iptables -F
iptables -P INPUT DROP
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

---

### **8. Uso de NAT y Redirección (DNAT/SNAT)**

#### 🔁 Redirección de puertos (port forwarding)

```bash
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 192.168.1.100:8080
```

#### 🌍 Habilitar NAT (para compartir internet)

```bash
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

---

### **9. Tips Finales y Buenas Prácticas**

* **Siempre prueba reglas en sesiones con `screen` o `tmux`**.
* Usa `iptables -S` para ver las reglas en formato script.
* Combina con herramientas como `fail2ban` para protección dinámica.
* Valida reglas con `iptables-restore --test`.
* Considera migrar a `nftables` en sistemas modernos (pero `iptables` sigue muy extendido).

---

Buena observación. Lo que te proporcioné de `iptables` está entre **nivel intermedio bajo y medio**, con algunos elementos avanzados, pero aún no entra en terreno **puramente avanzado**, como:

* uso extensivo de módulos (`conntrack`, `multiport`, `string`, `geoip`, etc.),
* integración con **sistemas de detección de intrusos (IDS)**,
* reglas dinámicas,
* defensas contra evasiones específicas,
* y manejo de políticas segmentadas por contexto o contenedor (ej. `docker`, `namespaces`, `VRFs`, etc.).

---

## NIVEL AVANZADO 🔥

Vamos a construir sobre lo anterior, pero **subiendo el nivel técnico**, orientado 100% a **ciberseguridad ofensiva y defensiva**.

---

### 🧱 1. Módulos avanzados de `iptables`

#### 📌 `conntrack`: más potente que `state`

```bash
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

* **`conntrack`** es más preciso que `state`, y permite ver el flujo de conexiones.

---

#### 📌 `string` y `hexstring`: detección por contenido

```bash
iptables -A INPUT -p tcp --dport 80 -m string --algo bm --string "wget " -j DROP
```

```bash
iptables -A INPUT -p tcp -m hexstring --hex-string "|16 03 01|" --algo bm -j LOG --log-prefix "TLS Packet: "
```

* Detectar patrones específicos en payloads. Ideal para:

  * Filtrar malware simple,
  * Detectar escaneos,
  * Analizar ataques en texto plano.

---

#### 📌 `multiport` para puertos múltiples

```bash
iptables -A INPUT -p tcp -m multiport --dports 22,80,443,3306 -j ACCEPT
```

---

### 🚫 2. Protección contra evasión de firewall

#### 🛡 Evitar fragmentación evasiva

```bash
iptables -A INPUT -f -j DROP
```

#### 🛡 Evitar paquetes malformados

```bash
iptables -A INPUT -p tcp ! --syn -m conntrack --ctstate NEW -j DROP
```

#### 🛡 Bloquear paquetes TTL sospechosos

```bash
iptables -A INPUT -m ttl --ttl-lt 10 -j LOG --log-prefix "TTL Bajo: "
iptables -A INPUT -m ttl --ttl-lt 10 -j DROP
```

---

### 📊 3. Trazabilidad y auditoría avanzada

#### 👁️ Registrar todo tráfico hacia puertos sensibles

```bash
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -j LOG --log-prefix "SSH IN: "
```

#### 🧠 Trazar flujo de paquetes salientes

```bash
iptables -A OUTPUT -p tcp -m conntrack --ctstate NEW -j LOG --log-prefix "OUT NEW: "
```

#### 📁 Redirigir logs a archivo separado con `rsyslog`

```bash
:msg, contains, "SSH IN:" /var/log/iptables_ssh.log
& stop
```

---

### 🤖 4. Integración con sistemas de seguridad y respuesta

#### 🧬 Integración con `fail2ban` (ejemplo NGINX)

```ini
[nginx-bad-bots]
enabled = true
filter = nginx-badbots
action = iptables[name=BadBots, port=http, protocol=tcp]
logpath = /var/log/nginx/access.log
```

#### 📡 Integración con Snort/Suricata

* Usar `snort`/`suricata` en modo IDS con salida `NFQUEUE`:

  ```bash
  iptables -I INPUT -j NFQUEUE --queue-num 0
  ```

* El IDS inspecciona y puede descartar tráfico antes de ser procesado por la pila TCP/IP.

---

### 🎯 5. Reglas dinámicas en tiempo real (con `recent`, `hashlimit`)

#### 🔒 Limitación de conexiones concurrentes por IP

```bash
iptables -A INPUT -p tcp --dport 80 -m connlimit --connlimit-above 20 -j REJECT
```

#### 🔂 Anti-DDoS básico por IP

```bash
iptables -A INPUT -p tcp --dport 80 -m hashlimit \
  --hashlimit 25/sec --hashlimit-burst 50 --hashlimit-mode srcip --hashlimit-name web \
  -j ACCEPT
```

---

### 🔥 6. Política segmentada por zonas de red (seguridad en capas)

```bash
## DMZ (web público)
iptables -A INPUT -i eth0 -s 0.0.0.0/0 -p tcp --dport 443 -j ACCEPT

## LAN interna (base de datos)
iptables -A INPUT -i eth1 -s 192.168.1.0/24 -p tcp --dport 3306 -j ACCEPT
```

---

### 🧱 7. Control de tráfico saliente (e.g., exfiltración de datos)

```bash
## Bloquear TOR (puertos conocidos)
iptables -A OUTPUT -p tcp --dport 9001 -j REJECT

## Bloquear DNS dinámico
iptables -A OUTPUT -p udp --dport 53 -m string --string "dyndns" --algo bm -j DROP
```

---

### 🧠 8. Manipulación de paquetes (MANGLE avanzado)

#### 🎯 Marcar tráfico saliente para routing diferenciado

```bash
iptables -t mangle -A OUTPUT -p tcp --dport 443 -j MARK --set-mark 3
```

Usado junto con `ip rule` para políticas de routing avanzadas.

---

### 🛠 9. Herramientas complementarias para hardening

| Herramienta           | Uso                                                  |
| --------------------- | ---------------------------------------------------- |
| `iptables-persistent` | Guardar reglas en Debian/Ubuntu.                     |
| `nftables`            | Evolución moderna de `iptables`.                     |
| `conntrack-tools`     | Monitorizar estado de conexiones.                    |
| `ipset`               | Manejo masivo de IPs (listas negras).                |
| `firewalld`           | API moderna con zonas, más dinámico (Red Hat-based). |

---

### 🧪 10. Ideas para entornos reales (casos avanzados)

* **Firewall para honeypot tipo Cowrie** que solo permite conexiones iniciales pero bloquea reintentos rápidos.
* **Firewall anti-túneles DNS** usando inspección de `string` y volumen.
* **Segmentación por contenedores Docker** usando `iptables` por bridge o `nftables` con `namespace`.

---
