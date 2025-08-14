from validaciones import es_texto_vacio, es_correo_valido, es_contrasena_valida
from fechas import dias_faltantes, estado_por_dias
from registro import crear_usuario, listar_usuarios
from mensajes import mostrar_mensaje_exito, mostrar_mensaje_error, mostrar_mensaje_info
print('=== Bienvenido/a al primer paso de nuestra app ===')
matricula = input('Matrícula: ').strip()
correo = input('Correo: ').strip()
contrasena = input('Contraseña (8+ con letras y números): ').strip()
ok, msg = crear_usuario(matricula, correo, contrasena)
if ok:
    print(mostrar_mensaje_exito(msg))
else:
    print(mostrar_mensaje_error(msg))
if es_texto_vacio(correo) or not es_correo_valido(correo):
    print(mostrar_mensaje_error('Tu correo no parece válido.'))
else:
    print(mostrar_mensaje_exito('Formato de correo correcto.'))
fecha = input('Fecha de entrega (dd/mm/aaaa): ').strip()
faltan = dias_faltantes(fecha)
estado = estado_por_dias(fecha)
print(mostrar_mensaje_info(f'Faltan {faltan} días para la entrega ({estado}).'))
print('Usuarios en memoria:', listar_usuarios())