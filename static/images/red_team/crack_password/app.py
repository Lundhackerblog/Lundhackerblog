import os

# Ruta donde están los archivos
carpeta = "."  # <-- Cámbialo por tu ruta

for archivo in os.listdir(carpeta):
    if archivo.startswith("Pasted image ") and archivo.endswith(".png"):
        nuevo_nombre = archivo.replace("Pasted image ", "")
        ruta_vieja = os.path.join(carpeta, archivo)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)
        os.rename(ruta_vieja, ruta_nueva)
        print(f"Renombrado: {archivo} -> {nuevo_nombre}")
