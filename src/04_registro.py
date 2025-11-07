from validaciones import es_correo_valido, es_texto_vacio, es_contrasena_valida
usuarios = []

def crear_usuario(matricula, correo, contrasena):
    if es_texto_vacio(matricula):
        return (False, 'La matrícula no puede estar vacía.')
# TODO 1: Validar correo

# TODO 2: Validar contraseña

# TODO 3: Agregar usuario a la lista
    
    return (True, 'Usuario creado correctamente.')

# TODO 4: Listar usuarios registrados