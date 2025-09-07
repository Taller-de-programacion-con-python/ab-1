from validaciones import es_correo_valido, es_texto_vacio, es_contrasena_valida
usuarios = []

def crear_usuario(matricula, correo, contrasena):
    if es_texto_vacio(matricula):
        return (False, 'La matrícula no puede estar vacía.')
    if not es_correo_valido(correo):
        return (False, 'El correo no parece válido.')
    if not es_contrasena_valida(contrasena):
        return (False, 'La contraseña debe tener 8+ caracteres, con letras y números.')
    usuarios.append({'matricula': str(matricula).strip(), 'correo': str(correo).strip(), 'contrasena': str(contrasena)})
    return (True, 'Usuario creado correctamente.')

def listar_usuarios():
    return usuarios
if __name__ == '__main__':
    print('Pruebas de registro:')
    print(crear_usuario('A001', 'alguien@ucol.mx', 'abc12345'))
    print(crear_usuario('A002', 'correo@ucol', 'abc12345'))
    print(listar_usuarios())