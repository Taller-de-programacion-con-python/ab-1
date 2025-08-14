def resumen_horas(tareas):
    total_planeado = 0.0
    total_real = 0.0
    for t in tareas:
        total_planeado += float(t.get('planeado_horas', 0))
        total_real += float(t.get('real_horas', 0))
    diferencia = total_planeado - total_real
    return {'total_planeado': round(total_planeado, 2), 'total_real': round(total_real, 2), 'diferencia': round(diferencia, 2)}
if __name__ == '__main__':
    demo = [{'nombre': 'Tarea 1', 'planeado_horas': 2, 'real_horas': 1.5}, {'nombre': 'Tarea 2', 'planeado_horas': 1, 'real_horas': 2}, {'nombre': 'Tarea 3', 'planeado_horas': 3, 'real_horas': 2.5}]
    print('Resumen horas:', resumen_horas(demo))