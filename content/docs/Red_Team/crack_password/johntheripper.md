---
title: John the ripper
type: docs
prev: docs/first-page
weight: 8
sidebar:
  open: false
---
## INSTALACION

## instalacion  - john - gpui

No recuerdo los pasos exactos asisque tendras que apoyarte con las notas de esta carpeta.

Requisitos:

### Toolikt Cuda nvidia + opencl: [CUDA Toolkit 12.2 Update 2 Downloads | NVIDIA Developer](https://developer.nvidia.com/cuda-downloads)

IMPORTANTE: tener la versión 12 de cuda o tratar en lo posible.
![imagen error](/images/red_team/crack_password/20230831213025.png)

Binarios de john(de drive mejor):<https://drive.google.com/file/d/12VfDGLrVDMvvE0T8zvt2sdtsZSvUfDOf/view?usp=sharing>
![imagen error](/images/red_team/crack_password/20230831213438.png)

luego de ello descomprimimos john y entramos a la carpeta RUN:

probamos que funcione ejecutando en CMD , john.exe se supone que todo hasta aqui esta bien.
USO DE GPU:
pasos que debemos seguir :
sacamos información de aquí:([Windows build no opencl devices · Issue #3647 · openwall/john (github.com)](https://github.com/openwall/john/issues/3647))

ejecutamos este comando:

```cmd
john --list=opencl-devices
```

deberia aparecernos lo siguiente:

![imagen error](/images/red_team/crack_password/20230831214446.png)

en caso nos de **ERROR**  o no nos aparezca nada realiza lo siguiente(<https://github.com/openwall/john/issues/3647#issuecomment-464897259>) , en resumidas cuenta el opencl.dll de john que viene no  funciona y reconoce a la gpu por ello se copia el opencl.dll oficial que esta en nuestro computador(c:\windows\system32\) a la ruta JOHN\run con nombre de archivo cygOpenCL.DLL , en mi caso me apareció varios , elegí el que se asemeja mas al tamaño de bytes , probaras varios en caso te aparezcan varios .

![imagen error](/images/red_team/crack_password/20230831214748.png)

luego de de haber podido reconocer la gpu  ahora debemos probar que funciona con lo siguiente :

<https://sleeplessbeastie.eu/2015/11/02/how-to-crack-password-using-nvidia-gpu/#usage>
![imagen error](/images/red_team/crack_password/20230831215026.png)

LEER EL ARTICULO : En este caso solo funcionan los de CUDA , los de opencl no funcionan , tendras que probar con algun hash .

En caso de **ERROR** nos dirigimos al siguiente enlace : [1.9.0-jumbo-1+bleeding-84a4aeb20 - wpapsk-opencl broken after driver/cuda update · Issue #5205 · openwall/john (github.com)](https://github.com/openwall/john/issues/5205)
en resumidas cuentas  , el archivo de configuración de john le falta un parámetro por las versiones de cuda, solo realiza lo que falta (comentario exacto : <https://github.com/openwall/john/issues/5205#issuecomment-1287069933)y> ya deberia estar funcionando .

agregamos el siguiente parámetro:

```c
GlobalBuildOpts = -cl-mad-enable -cl-std=CL1.2
```

volvemos a probar y ay deberia estar funcionando.

EXTRA  , para probar el rendimiento, ejemplos y algunas cosas mas :
[Introducing and Installing John the Ripper - KaliTut](https://kalitut.com/john-the-ripper/)

## USO DE GPU

### john gpu

[How to crack password using Nvidia GPU | sleeplessbeastie's notes](https://sleeplessbeastie.eu/2015/11/02/how-to-crack-password-using-nvidia-gpu/)

![imagen error](/images/red_team/crack_password/20230831211702.png)

---

![imagen error](/images/red_team/crack_password/20230831211755.png)
![imagen error](/images/red_team/crack_password/20230831211855.png)
![imagen error](/images/red_team/crack_password/20230831211912.png)
![imagen error](/images/red_team/crack_password/20230831211942.png)
![imagen error](/images/red_team/crack_password/20230831212012.png)
![imagen error](/images/red_team/crack_password/20230831212032.png)
![imagen error](/images/red_team/crack_password/20230831212100.png)
![imagen error](/images/red_team/crack_password/20230831212125.png)
![imagen error](/images/red_team/crack_password/20230831212146.png)
![imagen error](/images/red_team/crack_password/20230831212203.png)

## COMANDOS

paginas para convertir extraer el hash
[Extraer hashes de archivos encriptados .zip o .rar o .7z](https://hashes.com/es/johntheripper/zip2john)
