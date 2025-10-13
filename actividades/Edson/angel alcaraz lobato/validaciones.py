def es_texto_vacio(texto):
    if texto is None:
        return True
    texto = str(texto)
    texto_sin_espacios = texto.strip()
    return texto_sin_espacios == ''

def correo_valido(correo):
    if correo is None:
        return False
    correo = str(texto)
    if '@' not in correo:
        return False
    partes = correo.split('@', 1)
    parte_usuario = partes[0]
    parte_dominio = partes[1]
    if parte_usuario =='':
        return False
    return '.' in parte_dominio