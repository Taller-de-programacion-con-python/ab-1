# CONTRATOS — Sesión 4 (1°)
> Contrato = nombre claro + qué entra + qué sale + qué error + qué mensaje.

## validaciones.validar_correo
- Firma: validar_correo(texto: str) -> tuple[bool, str]
- Entra: texto (correo)
- Sale: (ok, mensaje_clave)
- Error: DatosInvalidos (entrada vacía, con espacios internos o sin '@' / '.')
- Mensajes:
  - ok    -> "validacion.email.ok"
  - error -> "validacion.email.invalido"
- Dependencias: usado por 3° (contratos) y 5° (UI)

## validaciones.validar_texto_no_vacio
- Firma: validar_texto_no_vacio(texto: str) -> tuple[bool, str]
- Entra: texto
- Sale: (ok, mensaje_clave)
- Error: DatosInvalidos (texto vacío o solo espacios)
- Mensajes:
  - ok    -> "validacion.texto.ok"
  - error -> "validacion.texto.vacio"
