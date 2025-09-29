"""
Módulo: validaciones
Propósito: ofrecer funciones simples que otros equipos (3° y 5°) puedan usar tal cual.

Contrato público (5 piezas por función):
- Nombre claro
- Qué entra
- Qué sale
- Qué error (si aplica)
- Qué mensaje (clave para UI)

Regla de salida común: devolvemos una tupla (ok: bool, mensaje_clave: str)
"""

from typing import Tuple

def validar_correo(texto: str) -> Tuple[bool, str]:
    """
    validar_correo(texto: str) -> (ok, mensaje_clave)
    Reglas mínimas y comprensibles:
    - Debe ser str
    - No puede estar vacío (ni solo espacios)
    - Debe contener '@' y '.'
    - No debe contener espacios internos
    Mensajes:
    - ok     -> "validacion.email.ok"
    - error  -> "validacion.email.invalido"
    """


    # TODO 1: si 'texto' NO es str -> (False, "validacion.email.invalido")


    # TODO 2: si 'limpio' está vacío -> (False, "validacion.email.invalido")

    # TODO 3: si hay espacios dentro -> (False, "validacion.email.invalido")


def validar_texto_no_vacio(texto: str) -> Tuple[bool, str]:
    """
    validar_texto_no_vacio(texto: str) -> (ok, mensaje_clave)
    Regla:
    - Debe existir al menos un carácter que no sea espacio.
    Mensajes:
    - ok     -> "validacion.texto.ok"
    - error  -> "validacion.texto.vacio"
    """
    
     # TODO 4: si 'texto' NO es str -> (False, "validacion.texto.vacio")

    # TODO 5: si hay al menos un carácter no espacio -> ok

