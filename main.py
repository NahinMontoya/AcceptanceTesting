class Tarea:
    def __init__(self, titulo, descripcion, fecha_limite, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.completada = False

    def marcar_completada(self):
        self.completada = True

class AdministradorListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def listar_tareas(self):
        for indice, tarea in enumerate(self.tareas, start=1):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{indice}. [{estado}] {tarea.titulo} - Fecha límite: {tarea.fecha_limite} - Prioridad: {tarea.prioridad}")

    def marcar_tarea_completada(self, indice_tarea):
        if 1 <= indice_tarea <= len(self.tareas):
            tarea = self.tareas[indice_tarea - 1]
            tarea.marcar_completada()
            print(f"Se marcó '{tarea.titulo}' como completada.")
        else:
            print("Índice de tarea no válido.")

    def borrar_tarea(self, indice_tarea):
        if 1 <= indice_tarea <= len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice_tarea - 1)
            print(f"Se eliminó la tarea '{tarea_eliminada.titulo}'.")
        else:
            print("Índice de tarea no válido.")

    def borrar_todas_las_tareas(self):
        self.tareas = []
        print("Se borraron todas las tareas.")

if __name__ == "__main__":
    administrador_tareas = AdministradorListaTareas()

    while True:
        print("                ****** Bienvenidos al sistemas de administracion de tareas ******")
        print("Estas son las opciones disponible")
        print(" 1. Agregar Tarea")
        print(" 2. Listar Tareas")
        print(" 3. Marcar Tarea como Completada")
        print(" 4. Borrar Tarea")
        print(" 5. Borrar Todas las Tareas")
        print(" 6. Salir del sistema")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Ingresa el título de la tarea: ")
            descripcion = input("Ingresa la descripción de la tarea: ")
            fecha_limite = input("Ingresa la fecha límite: ")
            prioridad = input("Ingresa la prioridad (baja/media/alta): ")
            nueva_tarea = Tarea(titulo, descripcion, fecha_limite, prioridad)
            administrador_tareas.agregar_tarea(nueva_tarea)
            print("***** SE HA AGREGADO UNA TAREA *****")

        elif opcion == "2":
            print("Lista de Tareas:")
            administrador_tareas.listar_tareas()

        elif opcion == "3":
            indice_tarea = int(input("Ingresa el número de tarea para marcar como completada: "))
            administrador_tareas.marcar_tarea_completada(indice_tarea)

        elif opcion == "4":
            indice_tarea = int(input("Ingresa el número de tarea para borrar: "))
            administrador_tareas.borrar_tarea(indice_tarea)

        elif opcion == "5":
            administrador_tareas.borrar_todas_las_tareas()
            print("***** SE BORRARON TODAS LAS TAREAS *****")

        elif opcion == "6":
            print("***** SALIENDO DEL SISTEMA *****")
            break

        else:
            print("ERROR por favor ingrese una opción válida del sistema")
