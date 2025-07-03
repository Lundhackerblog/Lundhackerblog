---
title: Wireshark
type: docs
prev: docs/Red_Team/
---


## 🧪 **Wireshark para Ciberseguridad – Resumen Profundo y Práctico**

---

## **1. Estructura general de uso**

* Aplicación **gráfica** multiplataforma para análisis de tráfico en profundidad.
* Captura o carga archivos `.pcap` / `.pcapng`.
* Permite inspeccionar paquetes, flujos, protocolos y payloads.

**Flujo básico:**

1. Selecciona interfaz.
2. Aplica filtros.
3. Captura o abre `.pcap`.
4. Analiza.

---

## **2. Opciones avanzadas de captura**

* Desde menú: `Capture > Options` o Ctrl+K
* Puedes configurar:

  * Interfaces múltiples
  * Modo promiscuo
  * Filtros de captura (BPF)
  * Límite de paquetes o tamaño
  * Rotación de archivos por tiempo o tamaño

🔧 **Ejemplo filtro de captura** (no editable luego):

```bash
tcp port 443 or udp port 53
```

---

## **3. Filtros de visualización (Display Filters)**

Aplicables durante y después de la captura. Muy potentes.

| Filtro            | Ejemplo                                     |
| ----------------- | ------------------------------------------- |
| IP origen/destino | `ip.src == 192.168.1.1`                     |
| Puerto            | `tcp.port == 22`                            |
| Protocolo         | `http`, `dns`, `tls`                        |
| Expresiones       | `tcp.flags.syn == 1 and tcp.flags.ack == 0` |
| Contenido         | `frame contains "password"`                 |

---

## **4. Opciones de salida y extracción**

* **Guardar captura:** `.pcapng`, `.pcap`
* **Exportar paquetes seleccionados**
* **Exportar objetos:**
  `File > Export Objects > HTTP/SMB/DICOM...`
* **Follow stream:**
  `Right click > Follow TCP Stream` → para ver sesiones completas.

---

## **5. Análisis estadístico**

`Statistics` > herramientas clave:

* Protocol Hierarchy
* Conversations (IP ↔ IP, TCP ↔ TCP)
* Endpoints (por MAC/IP/port)
* IO Graphs (gráficas de volumen)
* Flow Graph (secuencia tipo diagrama)
* Packet Length, RTT, TCP Stream Graphs

Ideal para detectar:

* Exfiltraciones
* Volúmenes anómalos
* Beaconing

---

## **6. Automatización y scripting**

Wireshark como tal no es para scripting, pero puedes:

* Guardar filtros como perfiles reutilizables.
* Exportar JSON o texto y procesar con scripts.
* Integrar con `dumpcap` para capturas automáticas.
* Usar con logs de red (ej. Zeek, Suricata outputs).

---

## **7. Casos de uso en ciberseguridad**

| Caso                               | Aplicación                                  |
| ---------------------------------- | ------------------------------------------- |
| 🧪 Análisis forense de intrusiones | Revisar tráfico en `.pcap` tras incidentes. |
| 🔎 Ingeniería inversa de malware   | Inspeccionar comunicaciones C2.             |
| 💡 Análisis de protocolo           | Ver estructura de TLS, DNS, HTTP.           |
| 🚨 Validación de reglas IDS        | Comprobación de alertas de Snort/Suricata.  |
| 🕵️‍♂️ Investigaciones internas    | Tráfico sospechoso entre empleados/hosts.   |

---

## **8. Exportar contenido binario**

Desde:

```bash
File > Export Objects > [HTTP, SMB, etc.]
```

Permite extraer:

* Ejecutables, documentos, imágenes
* Descargas vía HTTP o SMB

También desde *Follow Stream* puedes guardar contenido crudo de sesiones (como binario o texto).

---

## **9. Tips finales**

* Usa **profiles personalizados** por tipo de análisis.
* Activa **coloring rules** para identificar patrones.
* Útil para validar capturas hechas con `tcpdump`.
* Compatible con plugins y decodificadores personalizados.
* Utiliza **"Name Resolution"** con cuidado (puede generar más tráfico DNS).
* Guarda capturas pequeñas y filtradas para compartir hallazgos.

---
