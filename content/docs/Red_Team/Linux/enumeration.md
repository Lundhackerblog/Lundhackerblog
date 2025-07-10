---
title: Enumeracion Linux
type: docs
prev: docs/first-page
next: docs/Red_Team/leaf
weight: 8
sidebar:
  open: false
---

Buscar archivos con el nombre del usuario que queremos escalar

### BUSCAR INFORMACION DE USUSARIOS

```bash
find / -user pepe 2>/dev/null
find / -type f -user pepe 2>/dev/null
```

 ```bash
grep -R pepe * 2>/dev/null
```

### Tareas cron , ejecución

 ```bash
ps -aux | grep usuario,base datos , lenguaje de programacion ,binario , script
```

 ```bash
/etc/cron.*
/var/spool/cron*
```

## Revisar las conexiones y servicios

 ```bash
systemctl list-units --type=service
```

 ```bash
netstat -tulpn
```

 ```bash
ss -tulpn
```
