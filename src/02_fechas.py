from datetime import datetime, timedelta

def dias_faltantes(fecha_texto):
    try:
        dd, mm, aaaa = fecha_texto.split('/')
        dia = int(dd)
        mes = int(mm)
        anio = int(aaaa)
        objetivo = datetime(anio, mes, dia)
    except Exception:
        print('Formato esperado: dd/mm/aaaa (ejemplo: 25/12/2025)')
        return 0
    hoy = datetime.now()
    return (objetivo - hoy).days

def estado_por_dias(fecha_texto):
    resto = dias_faltantes(fecha_texto)
    if resto < 0:
        return 'VENCIDO'
    if resto == 0:
        return 'HOY'
    if resto <= 3:
        return 'PRONTO'
    return 'A TIEMPO'

def formatear_fecha(fecha_texto):
    try:
        dd, mm, aaaa = fecha_texto.split('/')
        return f'{int(dd):02d}/{int(mm):02d}/{int(aaaa):04d}'
    except Exception:
        return fecha_texto
if __name__ == '__main__':
    print('Pruebas fechas:')
    print("dias_faltantes('31/12/2025') ->", dias_faltantes('31/12/2025'))
    print("estado_por_dias('31/12/2025') ->", estado_por_dias('31/12/2025'))
    print("formatear_fecha('7/9/2025') ->", formatear_fecha('7/9/2025'))