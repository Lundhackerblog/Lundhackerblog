import os
import re

# Ruta base (puedes cambiarla si quieres apuntar a otra carpeta)
BASE_DIR = "."

# Expresión regular para capturar bloques RMarkdown + include_graphics
BLOCK_REGEX = re.compile(
    r'```{r,.*?fig\.cap="(.*?)",.*?out\.width="(.*?)"}\s+knitr::include_graphics\("([^"]+)"\)\s+```',
    re.DOTALL
)

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = BLOCK_REGEX.subn(
        lambda m: f'![{m.group(1)}]({m.group(3)}){{ style="width:{m.group(2)};" }}',
        content
    )

    if count > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✔ Reemplazado {count} bloque(s) en: {path}")

def walk_and_process(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    walk_and_process(BASE_DIR)
