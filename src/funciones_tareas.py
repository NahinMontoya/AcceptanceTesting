from src.tarea import Tarea


def agregar_tarea(tareas,titulo):
    nueva_tarea = Tarea(titulo)
    tareas.append(nueva_tarea)


def listar_tareas(tareas):
    lista_tareas = []
    for indice, tarea in enumerate(tareas, start=1):
        lista_tareas.append(f"{indice}. [{tarea.estado}] {tarea.titulo}")
    return lista_tareas

def marcar_tarea_completada(tareas,indice_tarea):
        tarea = tareas[indice_tarea - 1]
        tarea.marcar_completada()

def borrar_tarea(tareas,indice_tarea):
        tarea_eliminada = tareas.pop(indice_tarea - 1)
        return tarea_eliminada

def borrar_todas_las_tareas(tareas):
    tareas.clear()

