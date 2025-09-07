def buscar_por_matricula(lista, matricula):
    for u in lista:
        if str(u.get('matricula', '')).strip() == str(matricula).strip():
            return u
    return None

def buscar_por_correo(lista, correo):
    for u in lista:
        if str(u.get('correo', '')).strip().lower() == str(correo).strip().lower():
            return u
    return None
if __name__ == '__main__':
    demo = [{'matricula': 'A001', 'correo': 'a@ucol.mx', 'contrasena': 'abc12345'}, {'matricula': 'A002', 'correo': 'b@ucol.mx', 'contrasena': 'abc12345'}]
    print("buscar_por_matricula(demo, 'A001') ->", buscar_por_matricula(demo, 'A001'))
    print("buscar_por_correo(demo, 'b@ucol.mx') ->", buscar_por_correo(demo, 'b@ucol.mx'))