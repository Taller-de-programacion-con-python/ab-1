def es_texto_vacio(texto):
    if texto is None:
        return True
    texto = str(texto)
    texto_sin_espacios = texto.strip()
    return texto_sin_espacios == ''

def es_correo_valido(correo):
    if correo is None:
        return False
    correo = str(correo)
    if '@' not in correo:
        return False
    partes = correo.split('@', 1)
    parte_usuario = partes[0]
    parte_dominio = partes[1]
    if parte_usuario == '':
        return False
    return '.' in parte_dominio

def es_contrasena_valida(contrasena):
    if contrasena is None:
        return False
    contrasena = str(contrasena)
    if len(contrasena) < 8:
        return False
    tiene_letra = any((c.isalpha() for c in contrasena))
    tiene_numero = any((c.isdigit() for c in contrasena))
    return tiene_letra and tiene_numero
if __name__ == '__main__':
    print('Pruebas rápidas de validaciones:')
    print("es_texto_vacio('hola') ->", es_texto_vacio('hola'))
    print("es_texto_vacio('   ') ->", es_texto_vacio('   '))
    print("es_correo_valido('alguien@ucol.mx') ->", es_correo_valido('alguien@ucol.mx'))
    print("es_correo_valido('alguien@ucol') ->", es_correo_valido('alguien@ucol'))
    print("es_contrasena_valida('abc12345') ->", es_contrasena_valida('abc12345'))
    print("es_contrasena_valida('1234567') ->", es_contrasena_valida('1234567'))