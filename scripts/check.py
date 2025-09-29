"""
Funciones de persistencia mínima (CSV).
Se activan si el grupo llega rápido al CP2/CP3.
"""

from typing import List, Dict

# Tipo simple para alumnos de 1°: Usuario = dict con claves fijas.
Usuario = Dict[str, str]

def guardar_usuarios_csv(ruta: str, usuarios: List[Usuario]) -> int:
    """
    Guarda usuarios en CSV con columnas: id,nombre,correo,creado_en
    Devuelve cantidad de filas guardadas.
    """
    # TODO: abrir archivo en modo escritura y guardar encabezados y filas
    raise NotImplementedError("TODO: implementar guardar_usuarios_csv")

def cargar_usuarios_csv(ruta: str) -> List[Usuario]:
    """
    Carga usuarios desde CSV y devuelve una lista de dicts.
    """
    # TODO: abrir archivo en modo lectura y construir lista de dicts
    raise NotImplementedError("TODO: implementar cargar_usuarios_csv")
