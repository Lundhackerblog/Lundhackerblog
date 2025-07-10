---
title: 🔁Revershell Linux
type: docs
prev: docs/first-page
weight: 8
sidebar:
  open: false
---

!! IMPORTANTE !!
SHELL TTY , EN CASO NO FUNCIONE EL :

```bash
script /dev/null -c bash
```

EXISTEN PYTHON PARA REALIZARLO TAMBIEN CON

```python
python -C 'import pty; pty.spawn("/bin/bash")'
```

![imagen error](/images/red_team/revershell/20241019022518.png)

## PWNCAT

[GitHub - calebstewart/pwncat: Fancy reverse and bind shell handler](https://github.com/calebstewart/pwncat)
![imagen error](/images/red_team/revershell/20241015020901.png)
