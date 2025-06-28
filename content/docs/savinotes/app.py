import os
import re

def generar_front_matter(nombre_archivo):
    titulo = os.path.splitext(nombre_archivo)[0]  # Quita extensión .md
    return f"""---
title: {titulo}
type: docs
prev: docs/savinotes/
---"""

def reemplazar_front_matter(contenido, nuevo_front):
    pattern = re.compile(r'^---\s*$(.*?)^---\s*$', re.DOTALL | re.MULTILINE)
    if pattern.search(contenido):
        return pattern.sub(nuevo_front, contenido)
    else:
        return nuevo_front + "\n\n" + contenido  # Si no tenía front-matter, se añade

def procesar_directorio(ruta_base):
    for root, _, files in os.walk(ruta_base):
        for archivo in files:
            if archivo.endswith('.md'):
                ruta = os.path.join(root, archivo)
                with open(ruta, 'r', encoding='utf-8') as f:
                    contenido = f.read()

                nuevo_front = generar_front_matter(archivo)
                nuevo_contenido = reemplazar_front_matter(contenido, nuevo_front)

                if nuevo_contenido != contenido:
                    with open(ruta, 'w', encoding='utf-8') as f:
                        f.write(nuevo_contenido)
                    print(f'Actualizado: {ruta}')

if __name__ == '__main__':
    procesar_directorio('.')  # Cambia '.' por la ruta de tu carpeta si es necesario
