---
title: Teoria
type: docs
prev: docs/first-page
next: docs/Red_Team/leaf
weight: 4
sidebar:
  open: false
---

POR EL MOMENTO SOLO TENGO CONTENPALDO ESTOS 4 TIPOS

RESUMEN

- **Técnica 1**: **Shellcode Injection** (NX deshabilitado, ASLR deshabilitado).
- **Técnica 2**: **Shellcode Injection con Bypass de ASLR** (NX deshabilitado, ASLR habilitado).
- **Técnica 3**: **ret2libc** (NX habilitado, ASLR deshabilitado).
- **Técnica 4**: **ret2libc con Bypass de ASLR o ROP** (NX habilitado, ASLR habilitado).
- **EXTRA :Format String Attack**

### Técnica 1: **Shellcode Injection**

- **Condiciones**:

  - **ASLR**: Deshabilitado
  - **NX**: Deshabilitado (esto permite la ejecución en la pila o en cualquier región de memoria de escritura)
  - **Canary**: No
  - **PIE**: No
  - **Fortify**: No
  - **RelRO**: Full (pero en este caso no afecta la explotación)
- **Descripción**: Con **NX** deshabilitado y **ASLR** desactivado, puedes inyectar un shellcode en la pila u otra región de memoria escribible y redirigir la ejecución allí sin preocuparte por protecciones adicionales. Al no haber **canary**, no hay protección para detectar una sobrescritura en el buffer, lo que facilita desbordamientos de pila directos.

- **Ejemplo de Explotación**:

    1. Inyectar shellcode en la pila.
    2. Usar una vulnerabilidad de sobrescritura de buffer para redirigir el flujo de ejecución al shellcode.
- **Posibles Complicaciones**: Ninguna relevante, ya que todas las protecciones clave (NX y ASLR) están deshabilitadas, y **PIE** no está activado, por lo que las direcciones son constantes en cada ejecución.

---

### Técnica 2: **Shellcode Injection con Bypass de ASLR**

- **Condiciones**:

  - **ASLR**: Habilitado
  - **NX**: Deshabilitado
  - **Canary**: No
  - **PIE**: No
  - **Fortify**: No
  - **RelRO**: Full
- **Descripción**: Aquí, puedes seguir utilizando shellcode injection debido a que **NX** está desactivado, pero como **ASLR** está habilitado, la dirección exacta de la pila o del heap será diferente en cada ejecución. Sin embargo, dado que **PIE** está deshabilitado, las direcciones de las funciones en el binario principal son constantes.

- **Ejemplo de Explotación**:

    1. Usar una vulnerabilidad para filtrar una dirección de la pila o del heap (si es posible).
    2. Inyectar el shellcode en la pila y redirigir la ejecución a esa dirección.
- **Posibles Complicaciones**:

  - La **aleatorización de ASLR** requiere una fuga de memoria para predecir la ubicación del shellcode, ya que la dirección de la pila o del heap cambia en cada ejecución.
  - **Canary** deshabilitado facilita desbordamientos sin detección, y **PIE** desactivado ayuda a predecir direcciones en el binario.

---

### Técnica 3: **ret2libc (Return to libc)**

- **Condiciones**:

  - **ASLR**: Deshabilitado
  - **NX**: Habilitado (esto impide la ejecución de código inyectado en la pila o heap)
  - **Canary**: No
  - **PIE**: No
  - **Fortify**: No
  - **RelRO**: Full (la opción de RelRO Full significa que los punteros GOT están protegidos contra escritura, lo que añade seguridad en el acceso a funciones)
- **Descripción**: Dado que **NX** está habilitado, no puedes ejecutar shellcode en la pila. Sin embargo, como **ASLR** está deshabilitado, las direcciones de las funciones en `libc` son constantes, permitiéndote utilizar **ret2libc**. Al redirigir la ejecución a una función `libc` (como `system("/bin/sh")`), puedes ejecutar comandos sin necesidad de shellcode inyectado.

- **Ejemplo de Explotación**:

    1. Usar una sobrescritura de buffer para controlar el puntero de retorno.
    2. Redirigir el flujo de ejecución a `system("/bin/sh")` en `libc` usando direcciones conocidas.
- **Posibles Complicaciones**:

  - **RelRO Full** protege la **GOT** contra escritura, pero como el ataque usa llamadas de retorno a `libc`, no afecta este exploit.
  - La falta de **Canary** facilita los desbordamientos de buffer.
  - **PIE** deshabilitado ayuda a que las direcciones en el binario principal sean constantes.

---

### Técnica 4: **ret2libc con Bypass de ASLR o ROP (Return-Oriented Programming)**

- **Condiciones**:

  - **ASLR**: Habilitado
  - **NX**: Habilitado
  - **Canary**: No
  - **PIE**: No
  - **Fortify**: No
  - **RelRO**: Full
- **Descripción**: Esta es la configuración más segura, ya que tanto **NX** como **ASLR** están habilitados. Con **NX** habilitado, no puedes ejecutar shellcode inyectado, y **ASLR** hace que las direcciones en `libc` varíen en cada ejecución. Sin embargo, dado que **PIE** está deshabilitado, el binario principal tiene direcciones constantes, lo que facilita el uso de gadgets para una cadena **ROP**. Para hacer un **ret2libc** con ASLR habilitado, necesitas una fuga de memoria para determinar la ubicación actual de `libc` en memoria.

- **Ejemplo de Explotación**:

    1. Buscar una vulnerabilidad que permita una **fuga de información** para determinar la dirección de `libc`.
    2. Crear una cadena **ROP** o realizar un **ret2libc** usando las direcciones filtradas.
    3. Llamar a `system("/bin/sh")` o a una secuencia de gadgets para lograr el objetivo del exploit.
- **Posibles Complicaciones**:

  - **ASLR** requiere una fuga de información para determinar las direcciones actuales de `libc`.
  - **RelRO Full** impide sobrescribir punteros GOT directamente, lo cual no afecta la explotación con ROP.
  - La falta de **Canary** y **PIE** facilita la predicción y el uso de gadgets del binario principal.

**Format String Attack**

- Definición: Técnica de explotación que utiliza vulnerabilidades en las funciones de formato (como `printf`) para inyectar y ejecutar código malicioso, así como para leer o escribir en áreas de memoria controladas por el atacante.
