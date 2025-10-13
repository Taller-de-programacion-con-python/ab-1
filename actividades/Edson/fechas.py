import datetime

def dias_restantes(fecha_texto):
    dd, mm, aaaa = fecha_texto.split("/")
    objetivo = fecha_texto
    dia = int(dd)
    mes = int(mm)
    anio = int(aaaa)
    hoy = datetime.now()
    return (objetivo-hoy)

print(dias_restantes("13/10/2025"))

def estado_tareas(fecha_texto):
    resta = dias_restantes(fecha_texto)
    if resta < 0:
        return "vencido"
    if resta >= 0:
        return "Por completar"
    
