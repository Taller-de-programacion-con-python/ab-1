import datetime

def dias_restantes(fecha_texto):
    dd, mm, aaaa = fecha_texto.split("/")
    objetivo = fecha_texto
    dia = int(dd)
    mes = int(mm)
    anio = int(aaaa)
    hoy = datetime.now()
    return (objetivo-hoy).days


def estado_tareas(fecha_texto):
    resta = dias_restantes(fecha_texto)
    if resta < 0:
        return "Vencido"
    if resta >= 0:
        return "Por completar"
    