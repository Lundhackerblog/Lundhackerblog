---
title: Teoria
type: docs
prev: docs/first-page
next: docs/Red_Team/leaf
weight: 4
sidebar:
  open: true
---

## EJEMPLO 1

TUTORIAL GOD Y SIMPLE :
[Buffer Overflow en Windows 32 bits - Desarrollo de un exploit con MiniShare 1.4.1](https://www.youtube.com/watch?v=PQJn4s4E8Os&t=1192s&ab_channel=V%C3%ADctorGarc%C3%ADa)

[(381) Buffer Overflow en Windows 32 bits - Desarrollo de un exploit con MiniShare 1.4.1 - YouTube](https://www.youtube.com/watch?v=PQJn4s4E8Os&t=1192s&ab_channel=V%C3%ADctorGarc%C3%ADa)

[Aprendiendo a EXPLOTAR el BUFFER OVERFLOW desde 0 ☢️ | Laboratorio de Pruebas 🔰 | Hacking Ético 💻](https://www.youtube.com/watch?v=RZecs3YYtKU&t=1052s&ab_channel=BeniB3astt)

[Decompiler Explorer](https://dogbolt.org/)

[Shellcodes database for study cases](https://shell-storm.org/shellcode/index.html)

## EJEMPLO 2

ESTE EJEMPLO ES SIMPLE PUES ES UN BINARIO 32 BIST QUE ACEPTA INPUTS DIRECTAMENTE , AQUI ESTAN LOS PASOS USANDO GDB CON INTERFAZ GEF

BUFFER OVERFLOW
Tipo:

- OS : Linux
- ARQUITECTURA : 32
Protección:
- Canary = False
- NX = False
- PIE = True
- Fortify = False
- RelRo = Full

---

aqui el progrma esta bien
![[/images/red_team/buffer_overflow/20241026033033.png]]

aqui colapsa
![[/images/red_team/buffer_overflow/20241026033106.png]]

abrimos el gdb :
![[/images/red_team/buffer_overflow/20241026033151.png]]

revisamos las protecciones que cuenta para saber que se puede hacer
![[/images/red_team/buffer_overflow/20241026033304.png]]

EXPLICACION CHAT GPT :

### Resumen de Configuraciones de Seguridad

1. **Canary Deshabilitado**:
    - **Descripción**: El mecanismo de **stack canaries** (canarios) es una protección que se utiliza para detectar desbordamientos de buffer en la pila. Si está deshabilitado, significa que no se está utilizando este mecanismo de protección.
    - **Implicaciones**: Aumenta el riesgo de que un atacante pueda sobrescribir el retorno de la pila y ejecutar código malicioso sin ser detectado.
2. **NX Deshabilitado**:
    - **Descripción**: **NX (No-eXecute)** es una protección que impide la ejecución de código en áreas de memoria que deberían ser solo de datos. Si está deshabilitado, el binario permite la ejecución de código en cualquier área de memoria.
    - **Implicaciones**: Facilita ataques como la inyección de código, ya que el atacante puede ejecutar código en la pila o en el heap.
3. **PIE Habilitado**:
    - **Descripción**: **PIE (Position Independent Executable)** permite que el binario se cargue en direcciones de memoria aleatorias, aprovechando ASLR (Address Space Layout Randomization).
    - **Implicaciones**: Mejora la seguridad al dificultar que los atacantes predigan la ubicación de las funciones y variables, haciendo más complicado explotar vulnerabilidades.
4. **Fortify Deshabilitado**:
    - **Descripción**: **Fortify Source** es una técnica que agrega protecciones a las funciones de la biblioteca estándar de C, como `strcpy` y `sprintf`, para ayudar a prevenir vulnerabilidades comunes. Si está deshabilitado, esas protecciones no se aplican.
    - **Implicaciones**: Incrementa la vulnerabilidad del binario a ataques de desbordamiento de buffer y otros tipos de exploit relacionados con la manipulación de cadenas.
5. **RELRO Full Habilitado**:
    - **Descripción**: **RELRO (RELocation Read-Only)** es una protección que hace que las secciones de datos que contienen direcciones de función sean de solo lectura después de que el binario ha sido cargado. **Full RELRO** significa que se utilizan las protecciones completas.
    - **Implicaciones**: Ayuda a proteger contra ataques que intentan modificar la tabla de direcciones de funciones (GOT), aumentando la seguridad del binario.

# CREO UN PATRON PARA IDENTIFICAR EL TMAÑO DEL BUFFER - BASURA

![[/images/red_team/buffer_overflow/20241026034444.png]]

![[/images/red_team/buffer_overflow/20241026034536.png]]

validos nuestra teoria

![[/images/red_team/buffer_overflow/20241026034649.png]]

AÑADIMOS 4 B "BBBB" Y 4 C "CCCC"

![[/images/red_team/buffer_overflow/20241026034750.png]]

![[/images/red_team/buffer_overflow/20241026034855.png]]

COMENSAMOS ON EL ATAQUE

DEBIDO A QUE EL NX ESTA DESHABILITADO PODEMOS CARGAR UN SHELLCODE EN EL MISMO BUFFER PARA LUEGO LLAMARLO :

BUSCAMOS EL SHELL CODE  , SE TIENE QUE PROBAR CON VARIOS POR QUE ALGUNOS PUEDEN FUNCIOANR Y OTROS NO :
![[/images/red_team/buffer_overflow/20241026035831.png]]
![[/images/red_team/buffer_overflow/20241026035847.png]]

EXPLICAMOS EL ATAQUE:
lo que se hara sera escribir en el buffer de relleno el shell code como dice el paso 1 , luego cuando se llege al paso 2 este tiene que apuntar a la direccion del desajuste(explicacion mas abajo) como dice el paso 2 y para terminar este interpretara el shell code como instrucciones a bajo nivel como dice el paso 3

![[/images/red_team/buffer_overflow/20241026042352.png]]

Entonces pensando el eso quedaria dela siguiente forma

![[/images/red_team/buffer_overflow/20241026041753.png]]

donde:
null bytes:  son rellenos que no es nada es vacio
desajuste: esto es importante pues siempre existe un pequeño desajuste y tienes que darle espacio para que el shell code recien se pueda eejcutar bien , y esto suele ser NULL BYTES
shell code: es la instruccion a bajo nivel (solo escritura)
direccion shell code : lo "IDEAL" seria indicar el comienso del shellcode , pero  suelen teneer un desajuste por ende se coloca en el mismo desajuste para que tenga un margen.

entonces costruimos lo siguiente :
primero el tamaño cual debe ser :

![[/images/red_team/buffer_overflow/20241026034750.png]]
EL PATTER NOS DICE QUE  es 508 + 4 bits , que serian 512 para este caso
![[/images/red_team/buffer_overflow/20241026043712.png]]

sabiendo que es 512 debemos restar el shell code que en este caso es 33 BITS , EN LA MISMA DOCUMENTACION LO DICE

dando como resultado 512 - 33 = 479
[Linux/x86 - execve(/bin/bash, [/bin/bash, -p], NULL) - 33 bytes](https://shell-storm.org/shellcode/files/shellcode-606.html)
![[/images/red_team/buffer_overflow/20241026043816.png]]

![[/images/red_team/buffer_overflow/20241026044505.png]]

FALTA!!!!

![[/images/red_team/buffer_overflow/20241026050241.png]]

![[/images/red_team/buffer_overflow/20241026050255.png]]

![[/images/red_team/buffer_overflow/20241026050331.png]]

SHELL CODE COMIENZA POR AQUI

![[/images/red_team/buffer_overflow/20241026050216.png]]
