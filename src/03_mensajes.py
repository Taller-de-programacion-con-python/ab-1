def mostrar_mensaje_exito(texto):
    return f'✅ {texto}'

def mostrar_mensaje_error(texto):
    return f'❌ {texto}'

def mostrar_mensaje_info(texto):
    return f'ℹ️ {texto}'
if __name__ == '__main__':
    print(mostrar_mensaje_exito('Operación realizada con éxito.'))
    print(mostrar_mensaje_error('Formato de correo no válido.'))
    print(mostrar_mensaje_info('Recuerda guardar tu trabajo.'))
    