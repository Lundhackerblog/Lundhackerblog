---
title: Pivoting(Red Team)
type: docs
prev: docs/first-page
weight: 8
sidebar:
  open: true
---

## PARTE 1/3

SOCAT Y CHISEL , USA PROTOCOLO TCP
, POR ELLO PING NO FUNCIONARA PUES ES PROTOCOLO ICMP

## PARTE 2/3

- **`socat`** se encarga de estar en **escucha**, aceptando conexiones en un puerto
    local y redirigiéndolas hacia otro destino (por ejemplo, a través de un túnel).

- **`chisel`** se utiliza para **enviar el tráfico** a través de un túnel, ya sea en modo
    cliente o servidor. En tu caso, `chisel` se está usando para **encapsular el tráfico** y
    **túnelizarlo** entre los hosts intermedios.

### Desglose del comportamiento

1. **`socat` en escucha**:

    - Está configurado para escuchar en un puerto local (por ejemplo, `tcp-l:1111`).
    - Recibe conexiones en ese puerto y luego redirige el tráfico hacia otro destino, que puede ser un túnel establecido por `chisel`.

2. **`chisel` como cliente/servidor**:
    - En la configuración que tienes, `chisel` se usa en modo **cliente** para enviar tráfico
    desde un host a otro, encapsulándolo en un túnel.

    - El **servidor de `chisel`** (en el **Host principal**) recibe este tráfico y lo enruta (en tu
    caso, a través de SOCKS5).

### Resumen de roles

- **socat**: Es el encargado de aceptar conexiones locales en cada uno de los hosts
  intermedios y redirigirlas.

- **chisel**: Envía el tráfico a través de un túnel hacia el siguiente host o servidor, donde
  `socat` puede recibirlo de nuevo o pasarlo al siguiente destino.

  Este enfoque permite que puedas encadenar múltiples túneles entre los hosts, enviando
  el tráfico de forma segura y encapsulada hasta llegar al host destino.

## PARTE 3/3

ANTIGUO:
[PIVOTING EN ENTORNOS CONTROLADOS | Preparación eCPPTv2 (youtube.com)](https://www.youtube.com/watch?v=_7b_GQDfA5M&t=178s&ab_channel=s4vitar)

CURSO SAVITAR :
[PIVOTING DESDE CERO #1 | Preparatoria eCPPTv2 y eCPTXv2 (youtube.com)](https://www.youtube.com/watch?v=L1jSoCcvRY4&t=1401s&ab_channel=S4viOnLive%28BackupDirectosdeTwitch%29)

[PIVOTING DESDE CERO #2 | Preparatoria eCPPTv2 y eCPTXv2 (youtube.com)](https://www.youtube.com/watch?v=E4eUdAd6tAM&ab_channel=S4viOnLive%28BackupDirectosdeTwitch%29)

[PIVOTING DESDE CERO #3 | Preparatoria eCPPTv2 y eCPTXv2 (youtube.com)](https://www.youtube.com/watch?v=sjUgh__Utvs&t=808s&ab_channel=S4viOnLive%28BackupDirectosdeTwitch%29)

[PIVOTING DESDE CERO #4 | Preparatoria eCPPTv2 y eCPTXv2 (youtube.com)](https://www.youtube.com/watch?v=Mc4FuBRyybc&ab_channel=S4viOnLive%28BackupDirectosdeTwitch%29)

EXAMNE DE SIMULACION !!! 6 HORAS !!!

[Simulación de examen eCPPTv2 (youtube.com)](https://www.youtube.com/watch?v=Q7UeWILja-g&t=1s&ab_channel=S4viOnLive%28BackupDirectosdeTwitch%29)

TOOLS:

PRIVOTING CONCEPTOS:
![](/images/red_team/linux/pivontig/20241023135125.png)

![](/images/red_team/linux/pivontig/20241010190059.png)

![](/images/red_team/linux/pivontig/20241010190139.png)

![](/images/red_team/linux/pivontig/20241010190158.png)

![](/images/red_team/linux/pivontig/20241010190218.png)

![](/images/red_team/linux/pivontig/20241010190232.png)

![](/images/red_team/linux/pivontig/20241010190407.png)

![](/images/red_team/linux/pivontig/20241010190504.png)

![](/images/red_team/linux/pivontig/20241010190552.png)
![](/images/red_team/linux/pivontig/20241010190641.png)

![](/images/red_team/linux/pivontig/20241010190709.png)

![](/images/red_team/linux/pivontig/20241010190734.png)
![](/images/red_team/linux/pivontig/20241010190805.png)

NMAP XARGS:
[PROXYCHAINS NMAP XARGS](https://www.youtube.com/watch?v=sjUgh__Utvs&t=6999s&ab_channel=S4viSinFiltro)

![](/images/red_team/linux/pivontig/20241015125229.png)

![](/images/red_team/linux/pivontig/image_0.png)
