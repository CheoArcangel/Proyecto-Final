"""
Guarda y carga productos desde el disco local.
"""

import json
import os
from datetime import datetime

ARCHIVO_JSON = "productos.json"
ARCHIVO_ERRORES = "errores.log"

#-------------LOG DE ERRORES EN TXT (.log) ----------------
def registrar_error(mensaje:str) -> None:
    """
    Crea un registro de errores en archivo .log
    """
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #2026-06-17
    linea = f"[{ahora}] {mensaje}\n"

    try:
        with open (ARCHIVO_ERRORES, "a", encoding="utf-8") as archivo:
            archivo.write(linea)
    except Exception as e:
        print(f"No se pudo escribir en el log: {linea}")
        print (f"El error es {e}")

def guardar_json(productos: list) -> bool:
    """
    Sobrescribe el archivo JSON con la lista de productos.
    El archivo queda asi:
    [{}, {}, {}]
    """
    try:
        with open (ARCHIVO_JSON, "w",encoding="utf-8") as archivo:
            json.dump(productos, archivo,indent=4, ensure_ascii=False)
        return True
    except PermissionError:
        msg = f"Sin permisos para escribir '{ARCHIVO_JSON}'"
        print(f" {msg}")
        registrar_error (msg)
        return False

def cargar_json() -> list:
    """
    Lee el archivo json y devuelve la lista de productos
    """

    if not os.path.exists(ARCHIVO_JSON):
        return []
    
    try:
        with open (ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos
    except json.JSONDecodeError as e:
        msg = f"Archivo {ARCHIVO_JSON} corrupto: {e}"
        print(f" {msg}")
        registrar_error(msg)
        return []