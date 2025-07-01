---
title: Stenografia
type: docs
prev: docs/first-page
weight: 8
sidebar:
  open: false
---

## PARTE 1/2: GUIA COMPLETA

[Aperi'Solve (aperisolve.com)](https://www.aperisolve.com/cheatsheet)
[Stego Tricks | HackTricks](https://book.hacktricks.xyz/crypto-and-stego/stego-tricks)

AUDIO-VIDEO : [Cheatsheet - Steganography 101 (pequalsnp-team.github.io)](https://pequalsnp-team.github.io/cheatsheet/steganography-101)

## PARTE 2/2 : TOOLS

## EXIFTOOLS

**Descripción**: Una poderosa utilidad de línea de comandos para leer, escribir y editar metadatos en archivos multimedia. EXIFTools puede manipular datos como la fecha, el modelo de cámara, las coordenadas GPS, entre otros datos.

```bash
 exiftool imagen.jpg
```

## STEGHIDE

- **Descripción**: Herramienta para ocultar datos en archivos multimedia (imágenes, audios). Steghide utiliza un algoritmo de esteganografía para insertar información en archivos sin cambiar su apariencia o tamaño de manera significativa.

INFORMACION

```bash
steghide info imagen.jpg
```

- **OCULTAR DATOS**

```bash
steghide embed -cf imagen.jpg -ef secreto.txt
```

- **EXTRAER DATOS**

```bash
steghide extract -sf imagen.jpg
```

![imagen error](/images/red_team/stenografia/20241012032747.png)

## Binwalk

 **Descripción**: Herramienta para analizar y extraer datos incrustados en binarios, comúnmente usada para el análisis de firmware. Es útil para detectar archivos ocultos o comprimidos en binarios.

```bash
binwalk firmware.bin
```
