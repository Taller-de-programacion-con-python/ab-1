import csv
from pathlib import Path

def guardar_usuarios_csv(ruta, lista_usuarios):
    ruta = Path(ruta)
    with ruta.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['matricula', 'correo', 'contrasena'])
        for u in lista_usuarios:
            w.writerow([u.get('matricula', ''), u.get('correo', ''), u.get('contrasena', '')])
    return True

def cargar_usuarios_csv(ruta):
    ruta = Path(ruta)
    resultado = []
    if not ruta.exists():
        return resultado
    with ruta.open('r', newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            resultado.append({'matricula': row.get('matricula', ''), 'correo': row.get('correo', ''), 'contrasena': row.get('contrasena', '')})
    return resultado
if __name__ == '__main__':
    datos = [{'matricula': 'A001', 'correo': 'a@ucol.mx', 'contrasena': 'abc12345'}, {'matricula': 'A002', 'correo': 'b@ucol.mx', 'contrasena': 'abc12345'}]
    guardar_usuarios_csv('usuarios.csv', datos)
    print('Usuarios guardados. Leyendo...')
    print(cargar_usuarios_csv('usuarios.csv'))